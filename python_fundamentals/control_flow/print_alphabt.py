#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"
result = "".join(c for c in alphabet if c not in "qe")
print("{}".format(result), end="")
