import json
import unittest

import networkx as nx
import matplotlib.pyplot as plt
import json_tree


class NetworkxTests(unittest.TestCase):
    def _get_data_from_file(self, file_name):
        with open(file_name) as js_reader:
            j = js_reader.read()

        return json.loads(j)
    def test_product_data(self):
        jsonl = self._get_data_from_file("product_data.json")
        edges = json_tree.bfs(jsonl, "product")
        G = nx.Graph()
        G.add_edges_from(list(edges))
        print(list(nx.connected_components(G)))

        subax1 = plt.subplot(121)
        nx.draw(G, with_labels=True, font_weight='bold')
        subax2 = plt.subplot(122)
        nx.draw_shell(G, nlist=[range(5, 10), range(5)],
                      with_labels=True, font_weight='bold')
        plt.show()
if __name__ == '__main__':
    unittest.main()
