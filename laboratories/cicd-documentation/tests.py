from node import Node
from node import Tree

def test_find_existing_node():
    tree = Tree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    node = tree._find(5, tree.getRoot())
    assert node is not None
    assert node.data == 5


def test_find_non_existing_node():
    tree = Tree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    node = tree._find(20, tree.getRoot())
    assert node is None
