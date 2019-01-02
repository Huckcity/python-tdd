def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in(collection, item):
    assert item not in collection, "{0} should not contain {1}".format(collection, item)
    
def test_between(value, lower, upper):
    assert lower<=value<=upper, "{0} is not in the range of {1} and {2}".format(value, lower, upper)
    
    