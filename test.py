import pytest
from tree import Tree

@pytest.fixture
def my_tree():
    tree = Tree()
    tree.add(100)
    tree.add(10)
    tree.add(5)
    tree.add(1)
    tree.add(2)
    tree.add(3)
 
    return tree

def test_find_existing(my_tree):
    """ Test finding existing nodes """
    assert my_tree.find(100) != None
    assert my_tree.find(10)!= None
    assert my_tree.find(5) != None
    assert my_tree.find(1) != None

def test_find_nonexisting(my_tree):
    """ Test finding non-existing nodes """
    assert my_tree.find(25) == None
    assert my_tree.find(111) == None
    assert my_tree.find(0) == None
    assert my_tree.find(1000) == None
