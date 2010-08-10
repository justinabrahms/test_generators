import unittest2
from unittest2.plugins.moduleloading import testGenerator

class RoundTests(unittest2.TestCase):
  def _foo(self,a,b):
    assert round(a) == b

  @testGenerator
  def test_rounding(self):
    for x in [(1,1),
              (1.9, 2),
              # (9, 8),
              (1.6, 2),
              (1.4, 1)]:
      yield self._foo, x
