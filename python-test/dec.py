import logging

def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

def decorator(func):
    def wrapper(*args, **kwargs):
        # if level == "warn":
        #     logging.warning("%s is running" % func.__name__)
        # elif level == "info":
        logging.info("%s is running" % func.__name__)
        return func(*args)
    return wrapper


@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

f = use_logging(level="warn")
@f
def foo2(name='foo2'):
    print("i am %s" % name)


@decorator
def boo(name='boo'):
    print("i am %s" % name)

class class1:

    def __call__(self, *args, **kwargs):
        print ('class decorator runing')

        return

foo()
foo2()
boo()
