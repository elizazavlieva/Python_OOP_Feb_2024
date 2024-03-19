import itertools


def possible_permutations(lst):
    for perm in itertools.permutations(lst):
        yield list(perm)


# def possible_permutations(numbers: list):
#     if len(numbers) == 1:
#         yield numbers
#     else:
#         for i in range(len(numbers)):
#             for perm in possible_permutations(numbers[:i] + numbers[i + 1:]):
#                 yield [numbers[i]] + perm


""" TESTS """

[print(n) for n in possible_permutations([1, 2, 3])]
[print(n) for n in possible_permutations([1])]
