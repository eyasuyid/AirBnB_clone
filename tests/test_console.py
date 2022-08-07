#!/usr/bin/python3
"""Console unittests"""
import sys
import unittest
from unittest.mock import create_autospec
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """class TestConsole"""

    def setUp(self):
        """set up stdin and stdout"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        """create HBNBCommand"""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def _last_write(self, nr=None):
        """:return: last `n` output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(
            lambda c: c[0][0], self.mock_stdout.write.call_args_list[-nr:]))

    def test_quit(self):
        """Tesing `quit` command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))

if __name__ == '__main__':
    unittest.main()
