import inspect


class Solution:
    def minimumTotal(self, triangle) -> int:
        L = len(triangle)
        for i in range(L - 2, -1, -1):
            now, prev = triangle[i + 1], triangle[i]
            for j in range(0, i + 1):
                prev[j] += min(now[j], now[j + 1])

        return triangle[0][0]
    def hello(self, triansdf):
        pass

    def ahello(self, triansdf):
        pass


class ClassTest(Solution):
    def __init__(self):
        pass

# 利用inspect包，筛选Solution 中的 class
for (name, obj) in inspect.getmembers(Solution):
    # print(name)
    pass

# 利用inspect包，筛选Solution 中的 function
for (name, obj) in inspect.getmembers(Solution, inspect.isfunction):
    print(name)
    pass
    # 注册该model到amin界面
    # if str(model).find(__package__+".models") >= 0:
    #     admin.site.register(model, )

# .__code__.co_varnames


class TestClass:

    def __init__(self, ):
        self.solution_class = Solution

        # 利用inspect包，筛选 Solution 中的 function
        for (func_name, func_obj) in inspect.getmembers(self.solution_class, inspect.isfunction):
            print(func_name)
            print(inspect.getfullargspec(func_obj))
            # get function args
            full_args = inspect.getfullargspec(func_obj)
            args = full_args.args
            print(f'Test function name: Solution.{func_name}, args: {args}')
            pass
        pass

TestClass()