STYLISH_BASIC = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

STYLISH_NESTED = '''\
{
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
}'''

PLAIN_NESTED = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''

JSON_NESTED = '''[{"key": "common", "action": "nested", "children": \
[{"key": "follow", "action": "added", "val": false}, \
{"key": "setting1", "action": "unchanged", "val": "Value 1"}, \
{"key": "setting2", "action": "deleted", "val": 200}, \
{"key": "setting3", "action": "changed", "old": true, "new": null}, \
{"key": "setting4", "action": "added", "val": "blah blah"}, \
{"key": "setting5", "action": "added", "val": {"key5": "value5"}}, \
{"key": "setting6", "action": "nested", "children": \
[{"key": "doge", "action": "nested", "children": \
[{"key": "wow", "action": "changed", "old": "", "new": "so much"}]}, \
{"key": "key", "action": "unchanged", "val": "value"}, \
{"key": "ops", "action": "added", "val": "vops"}]}]}, \
{"key": "group1", "action": "nested", "children": \
[{"key": "baz", "action": "changed", "old": "bas", "new": "bars"}, \
{"key": "foo", "action": "unchanged", "val": "bar"}, \
{"key": "nest", "action": "changed", "old": {"key": "value"}, "new": "str"}]}, \
{"key": "group2", "action": "deleted", "val": {"abc": 12345, "deep": {"id": 45}}}, \
{"key": "group3", "action": "added", "val": \
{"deep": {"id": {"number": 45}}, "fee": 100500}}]'''
