#!/usr/bin/env python3

alphabet = "abcdefghijklmnopqrstuvwxyz"
print("".join(letter for letter in alphabet if letter not in "qe"))
