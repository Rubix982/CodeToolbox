#!/usr/bin/env python3

import re
import sys

if len(sys.argv) != 2:
    print("Usage: clean_ansi.py '<string>'")
    sys.exit(1)

print("----")
clean_v1 = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]').sub('', sys.argv[1])
clean_v2 = re.compile(r'\\27\[[0-?]*[ -/]*[@-~]').sub('', clean_v1)
print(clean_v2)
