#!/usr/bin/env python3

import textwrap
import sys


def wrap_text(text, width=79):
    wrapped_text = textwrap.fill(text, width)
    return wrapped_text


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wrap_text.py '<your_long_string>'")
        sys.exit(1)

    long_string = sys.argv[1]
    wrapped_output = wrap_text(long_string)
    print(wrapped_output)
