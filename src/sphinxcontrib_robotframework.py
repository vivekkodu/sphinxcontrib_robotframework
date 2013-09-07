# -*- coding: utf-8 -*-

import robot
import tempfile


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

    robot_file = tempfile.NamedTemporaryFile(dir=app.srcdir, suffix='.robot')
    robot_file.write(robot_data.encode('utf-8'))
    robot_file.flush()  # flush buffer into file

    options = {
        'outputdir': app.srcdir,
        'output': 'NONE',
        'log': 'NONE',
        'report': 'NONE'
    }
    robot.run(robot_file.name, **options)

    robot_file.close()  # close file (and delete it, because it is a tempfile)
