import unittest
import os
import shutil
import scCloud.commands
from .test_util import assert_excel_equal, assert_adata_files_equal


class TestDePipeline(unittest.TestCase):

    def tearDown(self):
        os.remove('test_de.xlsx')
        os.remove('test_de.h5ad')

    def test_de_analysis(self):
        # de_analysis modifies h5ad file
        shutil.copy(os.path.join('tests', 'output', 'test_cluster.h5ad'), 'test_de.h5ad')
        cmd = scCloud.commands.de_analysis(
            ['de_analysis', 'test_de.h5ad', 'test_de.xlsx', '--fisher',
             '--mwu', '--roc', '--labels', 'leiden_labels'])
        cmd.execute()
        assert_excel_equal(self, os.path.join('tests', 'output', 'test_de.xlsx'), 'test_de.xlsx')
        assert_adata_files_equal(self, os.path.join('tests', 'output', 'test_de.h5ad'), 'test_de.h5ad')


if __name__ == '__main__':
    unittest.main()
