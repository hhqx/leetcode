
from register import CONFIG


@CONFIG.register('test')
def yolo5(*args):
    print('input in yolo5: ', *args)

@CONFIG.register('yolo6')
class yolo6:
    def __init__(self):

        return
    def __call__(self, *args, **kwargs):

        return