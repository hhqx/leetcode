import itertools

arr = [1, 2, 2]
for sub in itertools.permutations(arr, 2):
    print(sub)
print('\n', end='')

# from itertools import permutations
#
# perm = permutations(arr, 2)
# for i in set(perm):
#     print(i)
# print(' ')


from more_itertools import distinct_permutations
for p in distinct_permutations(arr, 2):
    print(p)
print('')
