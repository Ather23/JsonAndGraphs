
def is_dict(content):
    return isinstance(content, dict)


def is_array_of_dict(content):
    return isinstance(content, list) \
           and len(content) > 0 \
           and isinstance(content[0], dict)


def extract_content(content):
    if is_dict(content):
        return content
    elif is_array_of_dict(content):
        return content[0]
    else:
        raise Exception("Unknown content type {}".format(type(content)))


def bfs(json, start_node_key=None):
    queue = []

    if start_node_key is None:
        start_node_key = "default_root"
        queue.append((start_node_key, json))
    else:
        queue.append((start_node_key,
                      extract_content(json[start_node_key])))
    edges = set()

    while queue:
        parent, data = queue.pop(0)
        for k in data.keys():
            content = data[k]
            if is_dict(content):
                queue.append((k, content))
            elif is_array_of_dict(content):
                queue.append((k, content[0]))
            edges.add((parent, k))
    return edges
