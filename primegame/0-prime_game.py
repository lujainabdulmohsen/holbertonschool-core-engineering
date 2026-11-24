#!/usr/bin/python3
"""Prime Game."""


def isWinner(x, nums):
    """Return the winner of the most rounds."""
    if x <= 0 or not nums:
        return None

    nums = nums[:x]
    limit = max(nums)
    primes = [True] * (limit + 1)
    counts = [0] * (limit + 1)

    for i in range(2, limit + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
        counts[i] = counts[i - 1] + primes[i]

    maria = sum(counts[n] % 2 for n in nums)
    ben = len(nums) - maria

    if maria == ben:
        return None
    return "Maria" if maria > ben else "Ben"
