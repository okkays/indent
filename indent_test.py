# Lint as: python3
"""Tests for indent."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest

import indent


class IndentTest(unittest.TestCase):

  def test_indents_simple(self):
    data = "{}"
    result = indent.indent(data)
    print("====\n", result, "\n====")
    self.assertEqual(result, "{\n  \n}\n")

  def test_indents_multiple(self):
    data = "{([hello])}"
    result = indent.indent(data)
    print("====\n", result, "\n====")
    self.assertEqual(result,
                     "{\n  (\n    [\n      hello\n    ]\n    \n  )\n  \n}\n")

  def test_breaks_splitters(self):
    data = "[fish, waffles, cake]"
    result = indent.indent(data)
    print("====\n", result, "\n====")
    self.assertEqual(result, "[\n  fish,\n  waffles,\n  cake\n]\n")


if __name__ == "__main__":
  unittest.main()
