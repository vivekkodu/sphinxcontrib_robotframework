def setup(app):
    app.add_config_value('todo_include_todos', False, False)

    app.add_node(todolist)
    app.add_node(todo,
                 html=(visit_todo_node, depart_todo_node),
                 latex=(visit_todo_node, depart_todo_node),
                 text=(visit_todo_node, depart_todo_node))

    app.add_directive('todo', TodoDirective)
    app.add_directive('todolist', TodolistDirective)
    app.connect('doctree-resolved', process_todo_nodes)
    app.connect('env-purge-doc', purge_todos)
    app.connect('source-read',run_robot)


from docutils import nodes

class todo(nodes.Admonition, nodes.Element):
    pass

class todolist(nodes.General, nodes.Element):
    pass

def visit_todo_node(self, node):
    self.visit_admonition(node)

def depart_todo_node(self, node):
    self.depart_admonition(node)


from sphinx.util.compat import Directive

class TodolistDirective(Directive):

    def run(self):
        return [todolist('')]


from sphinx.util.compat import make_admonition

class TodoDirective(Directive):

    # this enables content in the directive
    has_content = True

    def run(self):
        env = self.state.document.settings.env

        targetid = "todo-%d" % env.new_serialno('todo')
        targetnode = nodes.target('', '', ids=[targetid])

        ad = make_admonition(todo, self.name, [('Todo')], self.options,
                             self.content, self.lineno, self.content_offset,
                             self.block_text, self.state, self.state_machine)

        if not hasattr(env, 'todo_all_todos'):
            env.todo_all_todos = []
        env.todo_all_todos.append({
            'docname': env.docname,
            'lineno': self.lineno,
            'todo': ad[0].deepcopy(),
            'target': targetnode,
        })

        return [targetnode] + ad

def purge_todos(app, env, docname):
    if not hasattr(env, 'todo_all_todos'):
        return
    env.todo_all_todos = [todo for todo in env.todo_all_todos
                          if todo['docname'] != docname]


def process_todo_nodes(app, doctree, fromdocname):
    if not app.config.todo_include_todos:
        for node in doctree.traverse(todo):
            node.parent.remove(node)

    # Replace all todolist nodes with a list of the collected todos.
    # Augment each todo with a backlink to the original location.
    env = app.builder.env

    for node in doctree.traverse(todolist):
        if not app.config.todo_include_todos:
            node.replace_self([])
            continue

        content = []

        for todo_info in env.todo_all_todos:
            para = nodes.paragraph()
            filename = env.doc2path(todo_info['docname'], base=None)
            description = (
                ('(The original entry is located in %s, line %d and can be found ') %
                (filename, todo_info['lineno']))
            para += nodes.Text(description, description)

            # Create a reference
            newnode = nodes.reference('', '')
            innernode = nodes.emphasis(('here'),('here'))
            newnode['refdocname'] = todo_info['docname']
            newnode['refuri'] = app.builder.get_relative_uri(
                fromdocname, todo_info['docname'])
            newnode['refuri'] += '#' + todo_info['target']['refid']
            newnode.append(innernode)
            para += newnode
            para += nodes.Text('.)', '.)')

            # Insert into the todolist
            content.append(todo_info['todo'])
            content.append(para)

        node.replace_self(content)

def run_robot(app,docname,source):
    from robot import run
    from docutils.core import publish_cmdline
    import docutils.core
    import tempfile
    import os
    #run(os.path.join(app.srcdir, docname) + ".rst")
    doctree = docutils.core.publish_doctree(open('C:/Users/viviverm/Downloads/sphinxcontrib_robotframework/docs/example.rst').read())
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


    #need to delete content of temp.robot
    #don't know why extensions has to be changed in conf.py for each subsequent run
