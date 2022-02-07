"""
A file for creating unit tests

Run in spyder with
 !python -m pytest test.py
"""

from djset import MyDisjointSet


def test_trivial():
    assert(True)
    
def test_site_example():
    """
    Test the example from the web site
    """
    s = MyDisjointSet(10)
    s.union(0, 2)
    s.union(1, 8)
    s.union(8, 7)
    
    assert(not s.find(0, 3))
    assert(s.find(1, 7))
    s.union(1, 6)
    s.union(0, 1)
    assert(s.find(0, 7))
    assert(not s.find(1, 9))

def test_my():
    # TODO: Fill this in with your own test
    assert(True)