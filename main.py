import numpy
from numpy.linalg import matrix_power

markov = [
    [0.5, 0.5, 0],
    [0.25, 0.5, 0.25],
    [0, 0.5, 0.5],
]


def markov_det_Step(step, markov_det):
    input_array = numpy.array(markov_det)
    return matrix_power(input_array, step)


def cell_probability(cell, markov_det, wait=3):
    wait = len(markov_det)
    res = 0
    for row in markov_det:
        res += row[cell]
    return res/wait


def probability_after_step(step, cell, markov_det):
    deter = markov_det_Step(step, markov_det)
    print(f"after {step} steps the probability to get cell{cell} is {cell_probability(cell, deter)}")
    print(markov_det_Step(step, deter))


if __name__ == '__main__':
    probability_after_step(1, 2, markov)
