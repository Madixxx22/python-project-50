from gendiff.difference_calculator.gendiff import generate_diff

#Test for the positive scenario of the generate_diff function
def test_gendiff_good_case():
    res = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true\n}'''
    file1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
    }
    file2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
    }
    assert generate_diff(file1, file2) == res

#test empty case
def test_gendiff_empty_case():
    assert generate_diff({}, {}) == '{}'

#test when there are values in both files
def test_gendiff_full_case():
    file1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
    }
    file2 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
    }
    res = '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50\n}'''

    assert generate_diff(file1, file2) == res

#check if there are different values in both files
def test_gendiff_negative_case():
    file1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
    }
    file2 = {
    "host": "hexlet.com",
    "timeout": 228,
    "proxy": "192.168.13.37",
    "follow": True
    }
    res = '''{
  - follow: false
  + follow: true
  - host: hexlet.io
  + host: hexlet.com
  - proxy: 123.234.53.22
  + proxy: 192.168.13.37
  - timeout: 50
  + timeout: 228\n}'''

    assert generate_diff(file1, file2) == res
