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

@pytest.fixture
def data_good_case_nested():
  res = {'res': '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}''',
'file1': {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
},
'file2': {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": None,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}
}

  return res


@pytest.fixture
def data_good_case_plain():
  res = {'res': '''\
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]''',
'file1': {
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": True,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
},
'file2': {
  "common": {
    "follow": False,
    "setting1": "Value 1",
    "setting3": None,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}
}
  return res