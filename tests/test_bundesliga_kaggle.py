#!/usr/bin/env python

"""Tests for `bundesliga_kaggle` package."""


import unittest
from click.testing import CliRunner

from bundesliga_kaggle import bundesliga_kaggle
from bundesliga_kaggle import cli


class TestBundesliga_kaggle(unittest.TestCase):
    """Tests for `bundesliga_kaggle` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'bundesliga_kaggle.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
