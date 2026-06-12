import time
def decorator(func):
    def warpper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f'time: {end - start}')
        return res
    return warpper

@decorator
def test(a, b):
    print('test function')
    return a + b

print(test(1, 2))