from phytest import Alignment, Sequence, Tree


def test_sequence(sequence: Sequence):
    sequence.assert_valid_alphabet()


def test_alignment(alignment: Alignment):
    alignment.assert_width(462)


def test_root_to_tip(tree: Tree, alignment: Alignment):
    tree.assert_root_to_tip(min_r_squared=0.5, min_rate=0.001, max_rate=0.009, min_root_date=1800, max_root_date=1900)
    tree.plot_root_to_tip("root-to-tip.pdf", covariation=True, sequence_length=alignment.get_alignment_length())
