#!/usr/bin/env python3

import difflib
import argparse


def show_diff(str1, str2):
    # Use difflib to compare strings
    diff = difflib.ndiff(str1.split(), str2.split())
    return "\n".join(diff)


def main():
    # Create an argument parser for the CLI
    parser = argparse.ArgumentParser(
        description="Show the diff between two argument strings."
    )

    # Add arguments for the two strings
    parser.add_argument("string1", help="First argument string to compare")
    parser.add_argument("string2", help="Second argument string to compare")

    # Parse the arguments
    args = parser.parse_args()

    # Show the difference between the two strings
    diff_result = show_diff(args.string1, args.string2)
    print(diff_result)


if __name__ == "__main__":
    main()

