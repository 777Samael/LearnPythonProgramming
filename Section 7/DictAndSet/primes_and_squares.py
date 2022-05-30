from typing import Generator


def squares_generator(n: int) -> Generator[int, None, None]:
    """Generator to return the perfect squares less than `n`."""
    if n > 0:
        i = next_square = 1
        while next_square < n:
            yield next_square
            i += 1
            next_square = i * i


def primes_generator(n: int) -> Generator[int, None, None]:
    """
    Very naive implementation of the Sieve of Eratosthenes to generate prime numbers.

    This is *not* suitable for production use.
    For an optimised algorithm, check out the work by Tim Peters et al @ActiveState, and Will Ness.
    https://stackoverflow.com/questions/2211990/how-to-implement-an-efficient-infinite-generator-of-prime-numbers-in-python/19391111#19391111

    :param n: The number to generate primes up to.
    :return: A generator of all positive prime numbers less than or equal to `n`.
    """
    if n >= 2:
        # start with the set of positive odd integers from 3 to `n`, inclusive.
        integers = set(range(3, n + 1, 2))
        # There's no point removing multiples of 2 from odd numbers.
        yield 2
        next_prime = 3
        while integers:
            yield next_prime
            # Remove all multiples of `next_prime`.
            integers.difference_update(range(next_prime, n + 1, 2 * next_prime))
            next_prime = min(integers, default=None)  # None if set is empty.


if __name__ == '__main__':
    print("Squares less than 1000:")
    squares = list(squares_generator(1000))
    print(squares)
    print("Generated {} squares.".format(len(squares)))

    print("Primes up to 1000")
    primes = set(primes_generator(1000))
    print(sorted(primes))
    print("Generated {} primes.".format(len(primes)))

    check = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
             31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
             73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
             127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
             179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
             233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
             283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
             353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
             419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
             467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
             547, 557, 563, 569, 571, 577, 587, 593, 599, 601,
             607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
             661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
             739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
             811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
             877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
             947, 953, 967, 971, 977, 983, 991, 997}
    print(primes == check)

