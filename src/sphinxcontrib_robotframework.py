def setup(app):
    app.connect('doctree-resolved',run_robot)


from docutils import nodes

def purge_todos(app, env, docname):
    if not hasattr(env, 'todo_all_todos'):
        return
    env.todo_all_todos = [todo for todo in env.todo_all_todos
                          if todo['docname'] != docname]




def run_robot(app,doctree,docname):
    from robot import run
    from docutils.core import publish_cmdline
    import docutils.core
    import tempfile
    import os
    #run(os.path.join(app.srcdir, docname) + ".rst")
    #doctree = docutils.core.publish_doctree(open('C:/Users/viviverm/Downloads/sphinxcontrib_robotframework/docs/example.rst').read())
    def collect_robot_nodes(node, collected = []):
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
