import Actions
import queue

q1 = queue.Queue()
root = Actions.create_making_breakfast_tree()

q1.put(root)

while not q1.empty():
    node = q1.get()
    print(node.name)
    for child in node.children_actions:
        q1.put(child)
