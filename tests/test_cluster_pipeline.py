import unittest
import os
import scCloud.commands
from .test_util import assert_adata_equal


class TestClusterPipeline(unittest.TestCase):
    def tearDown(self):
        os.remove('test_cluster.h5ad')

    def test_cluster(self):
        cmd = scCloud.commands.cluster(
            ['cluster', os.path.join('tests', 'data', '3k_pbmc'),
             'test_cluster', '--run-leiden',
             '--run-approximated-leiden', '--run-tsne', '--run-umap',
             '--run-net-tsne', '--run-net-fitsne', '--run-net-umap', '--run-fitsne'])
        cmd.execute()
        assert_adata_equal(self, os.path.join('tests', 'output', 'test_cluster.h5ad'), 'test_cluster.h5ad')


# '--run-approximated-louvain',
# '--run-louvain',
# '--run-fle',
# '--run-net-fle'
# '--plot-hvg',


if __name__ == '__main__':
    unittest.main()
