from tree import Tree


def test_find_existing_node():
    tree = Tree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    node = tree.find(5)
    assert node is not None
    assert node.data == 5


def test_find_non_existing_node():
    tree = Tree()
    tree.add(10)
    tree.add(5)
    tree.add(15)

    node = tree.find(100)
    assert node is None
