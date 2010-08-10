def test_rounding():
  for test, expected_result in ((10, 10.0),
                                # (3, 2),
                                (1.9, 2.0),
                                (4, 4.0)):
    yield _check_rounding, test, expected_result

def _check_rounding(test, expected_result):
  assert(round(test) == expected_result)

class TestRound(object):
  def _check_rounding(self, test, expected):
    assert round(test) == expected

  def test_rounding(self):
    for x, y in [(1, 1),
                 # (3, 2),
                 (1.9, 2)]:
      yield self._check_rounding, x, y
