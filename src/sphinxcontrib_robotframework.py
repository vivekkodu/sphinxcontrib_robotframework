# -*- coding: utf-8 -*-

import os
import robot


def setup(app):
    app.add_config_value('sphinxcontrib_robotframework_enabled', True, True)
    app.connect('doctree-resolved', run_robot)


def run_robot(app, doctree, docname):
    if not app.config.sphinxcontrib_robotframework_enabled:
        return

    robot.run(os.path.join(app.srcdir, docname) + ".rst")

    return

    # XXX: The approach after this is not required, if we can execute
    # the above robot.run-call without error...

    def collect_robot_nodes(node, collected=[]):
        robot_tagname = 'literal_block'
        robot_classes = ['code', 'robotframework']
        is_robot_node = (
            node.tagname == robot_tagname
            and node.attributes.get('classes') == robot_classes
        )
        if is_robot_node:
            collected.append(node)
        else:
            for node in node.children:
                collected = collect_robot_nodes(node, collected)
        return collected

    robot_nodes = collect_robot_nodes(doctree)

    if robot_nodes:
        robot_data = "\n\n".join([node.rawsource for node in robot_nodes])
        print(robot_data)
        txtfile = open("C:/Users/viviverm/Downloads/sphinxcontrib_robotframework/docs/temp.robot","wb")
        txtfile.write(robot_data)
        txtfile.seek(0)
        #run(txtfile)

    if os.path.getsize('C:/Users/viviverm/Downloads/sphinxcontrib_robotframework/docs/temp.robot')>0:
        run('C:/Users/viviverm/Downloads/sphinxcontrib_robotframework/docs/temp.robot')

    #need to delete content of temp.robot or crete named temporary file
