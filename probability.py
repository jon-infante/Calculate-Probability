import math
from random import choices


def calc_probability(prob_heads, num_flips):
    """Calculates the amount of times Heads and Tails gets flipped,
    looking for 2 Heads 1 Tails.

    prob_heads: float
    flips: int
    """
    answers = [[['H'], ['H'], ['T']], [['H'], ['T'], ['H']], [['T'], ['H'], ['H']]]
    total = 0
    head_tails = ['H', 'T']
    weights = [prob_heads, 1 - prob_heads]

    for _ in range(num_flips):
        flips = []
        for _ in range(0, 3):
            flip = choices(head_tails, weights)
            flips.append(flip)
        if flips in answers:
            total += 1
    return total / num_flips

def test_probability(prob_heads, num_flips):
    two_heads = 0
    for _ in range(num_flips):
        two_heads += 3 * prob_heads**2 * (1 - prob_heads)
    return two_heads / num_flips


if __name__ == '__main__':
    print(calc_probability(0.5, 1000))
    print(test_probability(0.5, 1000))
