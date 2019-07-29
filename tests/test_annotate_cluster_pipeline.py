import unittest
import os

import scCloud.commands


class TestAnnotateClusterPipeline(unittest.TestCase):

    def tearDown(self):
        os.remove('test_annotate.txt')

    def test_annotate(self):
        cmd = scCloud.commands.annotate_cluster(
            ['annotate_cluster', os.path.join('tests', 'output', 'test_de.h5ad'), 'test_annotate.txt',
             '--json-file', os.path.join('tests', 'data', 'markers.json')])
        cmd.execute()
        with open(os.path.join('tests', 'output', 'test_annotate.txt')) as f:
            data = f.readlines()
        with open('test_annotate.txt') as f:
            test_data = f.readlines()
        self.assertEqual(data, test_data)


if __name__ == '__main__':
    unittest.main()
