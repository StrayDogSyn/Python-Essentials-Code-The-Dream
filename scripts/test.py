
import time


def timeit(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"[time] {fn.__name__} took ~{end-start:.2f}s")
        return result
    return wrapper

@timeit
def compute(a, b):
    return a * b ** 3

print(compute(2, 3))