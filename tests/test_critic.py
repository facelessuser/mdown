"""Test critic lib."""
from __future__ import unicode_literals
import unittest
from . import common
from pymdown import critic_dump


class TestCritic(unittest.TestCase):
    """TestCritic."""

    text = common.dedent(
        '''
        # This is a {~~test~>Unit Test~~}
        This is a {++CritcMarkup ++}{--test to --}test{-- CriticMarkup--}.

        {==This is a good test.==}{>>This probably isn't needed.<<}
        '''
    )

    def test_accept(self):
        """Test accepting critic marks."""

        cd = critic_dump.CriticDump()
        result = cd.dump(self.text, True)

        expected = common.dedent(
            '''
            # This is a Unit Test
            This is a CritcMarkup test.

            This is a good test.
            '''
        )

        self.assertEqual(result, expected)

    def test_reject(self):
        """Test rejecting critic marks."""

        cd = critic_dump.CriticDump()
        result = cd.dump(self.text, False)

        expected = common.dedent(
            '''
            # This is a test
            This is a test to test CriticMarkup.

            This is a good test.
            '''
        )

        self.assertEqual(result, expected)
