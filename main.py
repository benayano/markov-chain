import numpy
from numpy.linalg import matrix_power

markov = [
    [1, 2],
    [3, 4]
]


def markov_det_Step(step, markov_det):
    input_array = numpy.array(markov_det)
    return matrix_power(input_array, step)


def cel_probability(cel, markov_det):
    res = 0
    for row in markov_det:
        res += row[cel]
    return res


if __name__ == '__main__':
    print(markov_det_Step(2, markov))
