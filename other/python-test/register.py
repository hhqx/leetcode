
"""
函数f(fa)的装饰器dec(da), 核心是:
dec = dec(da) # init
f = dec(f) # call



@decorator(darg)
def f(farg):
    return

等价于:
def f(farg):
    return
f = decorator(darg)(f)



"""


class CONFIG_Class(object):

    def __init__(self, tag=None):
        # self._func = func
        self.config = dict()
        self.tag = tag



        # self._func = decorator
        return


    def __call__(self, func):
        # print ('class decorator runing')
        # self._func(*self.args, **self.kwargs)
        # print ('class decorator ending')
        def wrapper(*args, **kwargs):
            print(f'[tag: {self.tag}]. Add {func.__name__}:{func} to CONFIG')
            self.config[self.tag] = func
            return func(*args, **kwargs)

        return wrapper

    def register(self, tag):
        def decorator(func):
            print(f'[tag: {tag}]. Add {func.__name__}:{func} to CONFIG')
            self.config[tag] = func
            def wrapper(*args, **kwargs):
                # 装饰点什么
                return func(*args, **kwargs)

            return wrapper
        return decorator

    def __repr__(self):

        return f'{self.config}'


CONFIG = CONFIG_Class()

# @CONFIG_Class
# def bar():
#     print('bar')
#
# bar()
