#!/usr/bin/env python
"""Formats data based on parens, brackets, and braces.  Splits on commas."""
from __future__ import print_function

import string
import sys

WRAPPERS = {
    "{": "}",
    "(": ")",
    "[": "]",
}

SPLITTERS = [","]


def _is_start_of_line(text):
  for last_char in reversed(text):
    if last_char == "\n":
      return True
    if last_char not in string.whitespace:
      return False
  return True


def indent(to_indent, wrappers=None, splitters=None, indent_by="  "):
  """Indents and dedents given wrappers and indent_by."""
  if wrappers is None:
    wrappers = WRAPPERS
  if splitters is None:
    splitters = SPLITTERS
  formatted_data = ""
  indent_level = 0
  for char in to_indent:
    if char in wrappers.values():
      if indent_level > 0:
        indent_level -= 1
      formatted_data += ("\n{}{}\n".format(indent_by * indent_level, char))
    else:
      if not _is_start_of_line(formatted_data) or char not in string.whitespace:
        formatted_data += char
    if char in splitters:
      formatted_data += ("\n")
    if char in wrappers:
      formatted_data += ("\n")
      indent_level += 1
    if formatted_data[-1] == "\n":
      formatted_data += indent_by * indent_level
  return formatted_data


if __name__ == "__main__":
  data = sys.stdin.read()
  print(indent(data))
