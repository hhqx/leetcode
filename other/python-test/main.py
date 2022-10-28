# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



from register import CONFIG

# @CONFIG.register('test')
# def yolo5(*args):
#     print('input in yolo5: ', *args)

# @CONFIG('test')
# @CONFIG_Class('yolo5')
@CONFIG.register('yolo5')
def yolo5(*args, **kwargs):
    # print('input in yolo5: ', *args)
    print('yolo5', args, kwargs)


# @CONFIG.register('yolo5')
# def yolo5(*args, **kwargs):
#     print('input in yolo5: ', *args)


@CONFIG.register('yolo6')
class yolo6:
    def __init__(self,  *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return

    def __call__(self, *args, **kwargs):
        print('yolo6', self.args, self.kwargs)
        return

# yolo6 = CONFIG.register('yolo6')(yolo6)

# yolo6()

print(CONFIG)

CONFIG.config['yolo5'](1,2,3)
CONFIG.config['yolo6'](1,2,3)()

print(CONFIG.config['yolo5'],  yolo5)

# for name, f in CONFIG.config.items():
#     f(1, 2, 3, 4)
    # print(name, f(1,2,3,4))
    # print(name, )

# yolo5('input1', 'input2')
