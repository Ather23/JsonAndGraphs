import unittest
import json_tree
import json


class JsonTreeTests(unittest.TestCase):

    def _get_data_from_file(self, file_name):
        with open(file_name) as js_reader:
            j = js_reader.read()

        return json.loads(j)

    def test_product_data(self):
        jsonl = self._get_data_from_file("product_data.json")
        edges = json_tree.bfs(jsonl, "product")
        product_keys = set([("product", x) for x in jsonl["product"].keys()])
        product_neighbours = set()
        for p, c in edges:
            if p == 'product':
                product_neighbours.add((p, c))

        assert product_keys == product_neighbours

    def test_variant_data(self):
        jsonl = self._get_data_from_file("variant_data.json")
        edges = json_tree.bfs(jsonl, "variants")

        keys = set([("variants", x) for x in jsonl["variants"][0].keys()])

        neighbours = set()
        for p, c in edges:
            if p == 'variants':
                neighbours.add((p, c))

        assert keys == neighbours

    def test_no_root_key_data(self):
        jsonl = self._get_data_from_file("no_root_key.json")
        edges = json_tree.bfs(jsonl)

        keys = set([("default_root", x) for x in jsonl.keys()])

        neighbours = set()
        for p, c in edges:
            if p == 'default_root':
                neighbours.add((p, c))
        assert len(keys) == len(neighbours)
        assert keys == neighbours


if __name__ == '__main__':
    unittest.main()
