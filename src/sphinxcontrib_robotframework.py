# -*- coding: utf-8 -*-

import os
import robot
import tempfile
import StringIO


def setup(app):
    app.add_config_value('sphinxcontrib_robotframework_enabled', True, True)
    app.connect('doctree-resolved', run_robot)


def run_robot(app, doctree, docname):
    if not app.config.sphinxcontrib_robotframework_enabled:
        return

    # XXX: This does not work, because it would run Docutils within Docutils
    # with unexpected consequences like: AttributeError: Values instance has no
    # attribute 'env'

    # import os
    # robot.run(os.path.join(app.srcdir, docname) + ".rst")

    def collect_robot_nodes(node, collected=[]):
        robot_tagname = 'literal_block'
        robot_classes = frozenset(['code', 'robotframework'])
        is_robot_node = (
            node.tagname == robot_tagname
            and robot_classes <= frozenset(
                node.attributes.get('classes'))
        )
        if is_robot_node:
            collected.append(node)
        else:
            for node in node.children:
                collected = collect_robot_nodes(node, collected)
        return collected
    robot_nodes = collect_robot_nodes(doctree)

    if not robot_nodes:
        return

    robot_data = "\n\n".join([node.rawsource for node in robot_nodes])

    robot_file = tempfile.NamedTemporaryFile(suffix='.robot')
    robot_file.write(robot_data.encode('utf-8'))
    robot_file.flush()  # flush buffer into file

    # Change the current working directory to app.srcdir:
    cwd = os.getcwd()
    os.chdir(app.srcdir)
    stdout = StringIO.StringIO()

    options = {
        'outputdir': app.srcdir,
        'stdout': stdout,
        'output': 'NONE',
        'log': 'NONE',
        'report': 'NONE'
    }
    robot.run(robot_file.name, **options)

    # Change the current working directory back:
    os.chdir(cwd)

    # TODO: Print the output only, if there were errors
    stdout.seek(0)
    print stdout.read()

    robot_file.close()  # close file (and delete it, because it is a tempfile)
