#!/usr/bin/env python3.7
import re

from collections import deque

import math

import computer_v.glob as g

g.varname = "yes"

print(re.search(r"[a-zA-Z]+", "(x + 1)(x + 2)").group(0))