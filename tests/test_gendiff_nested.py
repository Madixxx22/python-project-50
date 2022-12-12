import pytest
from tests.fixtures import *
from gendiff.difference_calculator.gendiff import generate_diff

def test_gendiff_nested_json_good_case(data_good_case_nested):
  assert generate_diff(data_good_case_nested['file1'], data_good_case_nested['file2'], format = 'stylish') == data_good_case_nested['res']

def test_gendiff_nested_yml_good_case(data_good_case_nested):
  assert generate_diff(data_good_case_nested['file1'], data_good_case_nested['file2'], format = 'stylish') == data_good_case_nested['res']