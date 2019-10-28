from time import *


def time_calls(f):
    def new_f(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        print(f"Time to call {f}: {time() - start}")
    return new_f
