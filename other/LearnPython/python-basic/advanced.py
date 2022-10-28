def decorator_info(func, *dargs, **dkwargs):
    def inner(*args, **kwargs):
        if dargs:
            print('Something args in decorator: {}'.format(args))
        if dkwargs:
            print('Something kwargs in decorator: {}'.format(args))
        print("Executing {} function".format(func.__name__))
        func(*args, **kwargs)
        print("Finished {} execution".format(func.__name__))
    return inner


@decorator_info
def printer(msg):
    # msg = "hello default"
    print(msg)

printer('hello')



