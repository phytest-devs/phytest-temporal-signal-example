from phytest import Tree
from typing import List


def test_root_to_tip_r_squared(tree: Tree, extra:List):
    tree.assert_root_to_tip(min_r_squared=0.5, extra=extra)


def test_root_to_tip_rate(tree: Tree, extra:List):
    tree.assert_root_to_tip(min_rate=0.002, max_rate=0.005, extra=extra)


def test_root_to_tip_date(tree: Tree, extra:List):
    tree.assert_root_to_tip(min_root_date=1800, max_root_date=1900, extra=extra)

