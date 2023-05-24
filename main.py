import pickle

with open('num.pickle', 'rb') as num:
    l = list(filter(lambda x: not x % 3, list(pickle.load(num))))
print(sum(l) / len(l))
###############################################################
colors= {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
print('dict_2 =', {i: len(i) for i in colors.values()})
###############################################################
dict1 = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
print({i: list(filter(lambda x: x % 2 != 0, j)) for i, j in dict1.items()})