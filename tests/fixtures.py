import pytest

@pytest.fixture
def data_good_case():
  res = {'res': '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true\n}''',
  'file1': {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
    },
    'file2': {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
    } 
  }
  return res
  

@pytest.fixture
def data_full_case():
  res = {'file1': {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
    },
    'file2': {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
    },
    'res': '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50\n}'''}
  return res

@pytest.fixture
def data_negative_case():
  res = {'file1': {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
    },
    'file2': {
    "host": "hexlet.com",
    "timeout": 228,
    "proxy": "192.168.13.37",
    "follow": True
    },
    'res': '''{
  - follow: false
  + follow: true
  - host: hexlet.io
  + host: hexlet.com
  - proxy: 123.234.53.22
  + proxy: 192.168.13.37
  - timeout: 50
  + timeout: 228\n}'''
  }
  return res