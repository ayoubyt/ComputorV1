#!/usr/bin/python3.7
import re

from collections import deque

s = "123456"

print(re.findall(r"(?=(\d\d))", s))
