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

    stack.append([starting_node])

    while len(stack) > 0:
        current_path = stack.pop()
        paths.append(current_path)
        last_node = current_path[-1]
        if last_node not in visited:
            neighbors = get_neighbors(adj_list, current_path[-1])
            if neighbors is not None:
                for n in neighbors:
                    stack.append(current_path + [n])

    for path in paths:
        if longest_path == None:
            longest_path = path
        else:
            if len(path) > len(longest_path):
                longest_path = path
            if len(path) == len(longest_path):
                if path[-1] < longest_path[-1]:
                    longest_path = path

    if len(longest_path) == 1:
        return -1

    return longest_path[-1]
