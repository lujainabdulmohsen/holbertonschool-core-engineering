#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"
print("{}".format("".join(letter for letter in alphabet if letter not in "qe")))
