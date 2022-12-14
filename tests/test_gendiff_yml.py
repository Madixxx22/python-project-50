from tests.fixtures import * # noqa: F811 F401 E261 E501 F403 pylint: disable=unused-variable
from gendiff.difference_calculator.gendiff import generate_diff


# Test for the positive scenario of the generate_diff function
def test_gendiff_yml_good_case(data_good_case):
    assert generate_diff(data_good_case['file1'],
                         data_good_case['file2'],
                         format='stylish') == data_good_case['res']


# Test empty case
def test_gendiff_yml_empty_case():
    assert generate_diff({}, {}, format='stylish') == '{\n}'


# Test when there are values in both files
def test_gendiff_yml_full_case(data_full_case):
    assert generate_diff(data_full_case['file1'],
                         data_full_case['file2'],
                         format='stylish') == data_full_case['res']


# Check if there are different values in both files
def test_gendiff_yml_negative_case(data_negative_case):
    assert generate_diff(data_negative_case['file1'],
                         data_negative_case['file2'],
                         format='stylish') == data_negative_case['res']
