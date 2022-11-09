import importlib
import json
import unittest

m = importlib.import_module('212WordSearchII-40ms')
# m = importlib.import_module('WordSearchII', './')
# m = __import__('WordSearchII')

fname = '212. WordWearchII.json'
# testcase = eval(open(fname, 'r').read())
data = json.load(open(fname))
testcase = eval(data['code_output'])

output = [expect for _, expect in testcase]
print(output[::-1])

class MyTestCase(unittest.TestCase):

    def test_something(self):
        # self.assertEqual(True, False)  # add assertion here
        soluton = m.Solution()
        for input, expect in testcase:
            output = soluton.findWords(*input)
            self.assertCountEqual(output, expect)
        pass


if __name__ == '__main__':
    unittest.main()
