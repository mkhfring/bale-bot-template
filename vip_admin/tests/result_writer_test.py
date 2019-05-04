import os
import unittest
from collections import defaultdict

from vip_admin.utils.result_writer import ResultWriter
from vip_admin import MAIN_DIRECTORY


result_path = os.path.join(MAIN_DIRECTORY,'tests/data/practice.xlsx')


class TestResultWriter(unittest.TestCase):

    def test_result_writer(self):

        result_writer = ResultWriter(result_path)

        sample_data = [{'a': 1, 'b': 2}, {'a': 1, 'b': 3}]
        sample_data2 = [{'d': 4, 'f': 5}, {'f': 7, 'd': 8}]
        data_frame = result_writer._create_data_frame(sample_data)

        assert isinstance(data_frame, defaultdict)
        assert len(data_frame['a']) == 2
        assert len(data_frame.keys()) == 2

        with self.assertRaises(RuntimeError):
            result_writer.write_to_excel(
                (sample_data, sample_data2),
                ['sheet1']
            )
        result_writer.write_to_excel(
            (sample_data, sample_data2),
            ['sheet1', 'sheet2']
        )
        assert os.path.exists(result_path)
        sample3 = [{'a': 1, 'b': 2}, {'a': 9}]
        with self.assertRaises(RuntimeError):
            result_writer.write_to_excel((sample3,), ['sheet1'])
