#!/usr/bin/python3
"""Prime game module."""


def isWinner(x, nums):
    """Determine the winner of a prime game session with `x` rounds.

    Args:
        x (int): The number of rounds.
        nums (list): A list of n for each round.

    Returns:
        str or None: Name of the winner or None if it's a tie.
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = generate_prime_sieve(max_num)

    maria_wins = sum(1 for n in nums if count_primes(primes, n) % 2 == 1)
    ben_wins = x - maria_wins

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'


def generate_prime_sieve(n):
    """Generate a prime sieve up to n.

    Args:
        n (int): The upper limit for the sieve.

    Returns:
        list: A boolean list where True indicates a prime number.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return sieve


def count_primes(sieve, n):
    """Count the number of primes less than or equal to n.

    Args:
        sieve (list): A pre-computed prime sieve.
        n (int): The upper limit for counting primes.

    Returns:
        int: The count of primes up to n.
    """
    return sum(sieve[:n+1])
