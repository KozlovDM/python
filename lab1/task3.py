dictionary = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
dictionary = dict(map(reversed, dictionary.items()))
print(dictionary)
