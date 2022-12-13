import functools


def coroutine(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        inter = func(*args, **kwargs)
        next(inter)
        return inter
    return new_func


@coroutine
def storage():
    values = set()
    was_there = False
    while True+
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


if __name__ == '__main__':
    st = storage()
    # next(st)
    print(st.send(42))  # False
    print(st.send(42))  # True
