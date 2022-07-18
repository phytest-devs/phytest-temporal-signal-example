from phytest import Tree


def test_root_to_tip_r_squared(tree: Tree):
    tree.assert_root_to_tip(min_r_squared=0.5)


def test_root_to_tip_rate(tree: Tree):
    tree.assert_root_to_tip(min_rate=0.002, max_rate=0.005)


def test_root_to_tip_date(tree: Tree):
    tree.assert_root_to_tip(min_root_date=1800, max_root_date=1900)
