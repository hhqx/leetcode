

class any_func:
    """ any() """
    # 0 is False
    d = {0: 'False'}
    print(any(d))

    # 1 is True
    d = {0: 'False', 1: 'True'}
    print(any(d))

    # 0 and False are false
    d = {0: 'False', False: 0}
    print(any(d))

    # iterable is empty
    d = {}
    print(any(d))

    # 0 is False
    # '0' is True
    d = {'0': 'False'}
    print(any(d))

class all_func:
    """ all() """
    s = {0: 'False', 1: 'False'}
    print(all(s))

    s = {1: 'True', 2: 'True'}
    print(all(s))

    s = {1: 'True', False: 0}
    print(all(s))

    s = {}
    print(all(s))

    # 0 is False
    # '0' is True
    s = {'0': 'True'}
    print(all(s))




d = 'decorators'.__import__()
print(d)



