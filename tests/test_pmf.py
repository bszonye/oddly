"""Unit tests for bones.pmf.PMF class."""

__author__ = "Bradd Szonye <bszonye@gmail.com>"

from bones.pmf import PMF


class TestPMFInit:
    """Test the PMF constructor."""

    def test_pmf_simple(self) -> None:
        """Test with default arguments."""
        pmf = PMF()
        assert len(pmf) == 0

    def test_pmf_int(self) -> None:
        """Test with default arguments."""
        items = (0,)
        pmf = PMF(items)
        assert len(pmf) == 1
        assert pmf[0] == 1

    def test_pmf_copy(self) -> None:
        """Test copying another AttackPMF."""
        items = (0,)
        pmf1 = PMF(items)
        pmf2 = PMF(pmf1)
        assert pmf1.pairs is pmf2.pairs
        assert pmf1.denominator is pmf2.denominator
