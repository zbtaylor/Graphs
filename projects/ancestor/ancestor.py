def adjacency_list(nodes):
    adj_list = {}
    for connection in nodes:
        parent = connection[0]
        child = connection[1]
        if child not in adj_list.keys():
            adj_list[child] = [parent]
        else:
            adj_list[child].append(parent)
    return adj_list


def get_neighbors(adj_list, node):
    if node in adj_list.keys():
        return adj_list[node]


def earliest_ancestor(ancestors, starting_node):
    stack = []
    visited = set()
    paths = []
    longest_path = None
    adj_list = adjacency_list(ancestors)

    # initial path
    stack.append([starting_node])

    # while the stack is not empty
    while len(stack) > 0:
        # grab current path
        current_path = stack.pop()
        # add to list of possible paths
        paths.append(current_path)
        # grab last node
        last_node = current_path[-1]
        # if it hasn't been visited
        if last_node not in visited:
            neighbors = get_neighbors(adj_list, current_path[-1])
            # and the node has neighbors
            if neighbors is not None:
                # create new paths for current path + each neighbor
                for n in neighbors:
                    stack.append(current_path + [n])

    # iterate paths looking for the longest
    for path in paths:
        if longest_path == None:
            longest_path = path
        else:
            if len(path) > len(longest_path):
                longest_path = path
            # if the lengths match, keep the one with the lower id final ancestor
            if len(path) == len(longest_path):
                if path[-1] < longest_path[-1]:
                    longest_path = path

    # if the path length is only one, it had no ancestors
    if len(longest_path) == 1:
        return -1

    # return the final ancestor in our longest path
    return longest_path[-1]
