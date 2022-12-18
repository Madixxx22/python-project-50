from tests.fixtures import * # noqa: F811 F401 E261 E501 F403 pylint: disable=unused-variable
from gendiff.difference_calculator.gendiff import generate_diff


def test_gendiff_nested_json_good_case(data_good_case_plain):
    assert generate_diff(data_good_case_plain['file1'],
                         data_good_case_plain['file2'],
                         format='plain') == data_good_case_plain['res']


def test_gendiff_nested_yml_good_case(data_good_case_plain):
    assert generate_diff(data_good_case_plain['file1'],
                         data_good_case_plain['file2'],
                         format='plain') == data_good_case_plain['res']
