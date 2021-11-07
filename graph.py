class Graph:
    def __init__(self, action_tree):
        self.action_tree = action_tree

    def get_neighbors(self, v):
        return self.action_tree[v]


    # assigns all nodes the same weight
    def transform(self, n):
        t_graph = action_tree
        t_graph = {x: 1 for x in t_graph}
        return t_graph[n]

    def a_star_algorithm(self, start, stop):
        # In this open_lst is a list of nodes which have been visited, but who's
        # neighbours haven't all been always inspected, It starts off with the start
        # node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected

        # open is a list of nodes which have been visited without all neighbors inspected. begins with start node
        # close is a list of nodes which have been visited and all neighbors have been inspected
        open_list = set([start])
        closed = set([])

        # present_distance has present distances from start to all other nodes
        # the default value is +infinity
        present_distance = {start: 0}

        # contains mapping of all nodes
        node_map = {start: start}

        while len(open_list) > 0:
            n = None

            # it will find a node with the lowest value of f() -
            for v in open_list:
                if n is None or present_distance[v] + self.transform(v) < present_distance[n] + self.transform(n):
                    n = v;

            if n is None:
                print('Path does not exist!')
                return None

            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []

                while node_map[n] != n:
                    reconst_path.append(n)
                    n = node_map[n]

                reconst_path.append(start)

                reconst_path.reverse()

                # present_distance[v] is the distance of the optimized path
                print('Path found: {}'.format(reconst_path), present_distance[v])
                return reconst_path

            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_list and m not in closed:
                    open_list.add(m)
                    node_map[m] = n
                    present_distance[m] = present_distance[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and present_distance data
                # and if the node was in closed, move it to open_list
                else:
                    if present_distance[m] > present_distance[n] + weight:
                        present_distance[m] = present_distance[n] + weight
                        node_map[m] = n

                        if m in closed:
                            closed.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed
            # because all of its neighbors were inspected
            open_list.remove(n)
            closed.add(n)

        print('Path does not exist!')
        return None


action_tree = {
    'get_Mug': [('leave_Mug', 1), ('enter_Room', 1)],
    'leave_Mug': [('have_Coffee', 2)],
    'enter_Room': [('have_Coffee', 2)],
    'have_Coffee': [('enter_Room', 3)]
}

# action_tree = {
#     'enter_Room' : [('get_Mug', 1)],
#     'get_Mug' : ['have_Coffee', 1],
#     'have_Coffee' : [('')]
# }
graph1 = Graph(action_tree)
graph1.a_star_algorithm('get_Mug', 'have_Coffee')
