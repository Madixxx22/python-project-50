from tests.fixtures import *
from gendiff.difference_calculator.gendiff import generate_diff_yml

#Test for the positive scenario of the generate_diff function
def test_gendiff_yml_good_case(data_good_case):
  print(generate_diff_yml(data_good_case['file1'], data_good_case['file2']))
  assert generate_diff_yml(data_good_case['file1'], data_good_case['file2']) == data_good_case['res']

#test empty case
def test_gendiff_yml_empty_case():
  assert generate_diff_yml({}, {}) == '{}'

#test when there are values in both files
def test_gendiff_yml_full_case(data_full_case):
  assert generate_diff_yml(data_full_case['file1'], data_full_case['file2']) == data_full_case['res']

#check if there are different values in both files
def test_gendiff_yml_negative_case(data_negative_case):
  assert generate_diff_yml(data_negative_case['file1'], data_negative_case['file2']) == data_negative_case['res']