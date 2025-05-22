#!/usr/bin/env python
"""
Test script for the precommit-hooks CLI.

This script imports and runs the CLI directly to test its functionality.
"""

from precommit_hooks.cli import cli

if __name__ == "__main__":
    # Test the CLI by running it with the --help option
    import sys
    sys.argv = ["precommit-hooks", "--help"]
    cli()