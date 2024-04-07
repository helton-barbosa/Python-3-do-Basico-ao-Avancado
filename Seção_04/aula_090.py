# Generator expression, Iterables e Iterators em Python

iterable = ['Eu', 'tenho', '__iter__']

# há o __iter__() e __next__()
iterator = iter(iterable)  # .__iter__()


print(next(iterator))
print(f'{iterator.__next__()}')
print(next(iterator))
