# -*- coding: utf-8 -*-

import robot
import tempfile

from sphinx.directives import CodeBlock


class RobotAwareCodeBlock(CodeBlock):

    def run(self):
        if u"robotframework" in self.arguments:
            document = self.state_machine.document
            robot_source = u"\n".join(self.content)
            if not hasattr(document, '_robot_source'):
                document._robot_source = robot_source
            else:
                document._robot_source += u"\n" + robot_source
        return super(RobotAwareCodeBlock, self).run()


def run_robot(app, doctree, docname):

    if not app.config.sphinxcontrib_robotframework_enabled:
        return

    # XXX: This does not work, because it would run Docutils within Docutils
    # with unexpected consequences like: AttributeError: Values instance has no
    # attribute 'env'

    # import os
    # robot.run(os.path.join(app.srcdir, docname) + ".rst")

    if not hasattr(doctree, '_robot_source'):
        return

    robot_file = tempfile.NamedTemporaryFile(dir=app.srcdir, suffix='.robot')
    robot_file.write(doctree._robot_source.encode('utf-8'))
    robot_file.flush()  # flush buffer into file

    options = {
        'outputdir': app.srcdir,
        'output': 'NONE',
        'log': 'NONE',
        'report': 'NONE'
    }
    robot.run(robot_file.name, **options)
    app.env.process_images(docname, doctree)

    robot_file.close()  # close file (and delete it, because it is a tempfile)


def setup(app):
    app.add_config_value('sphinxcontrib_robotframework_enabled', True, True)
    app.add_directive('code', RobotAwareCodeBlock)
    app.connect('doctree-resolved', run_robot)
