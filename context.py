# with
# 上下文管理器协议包含 __enter__ 和 __exit__ 两个方法
# with语句开始运行时, 会在上下文管理器对象上调用 __enter__ 方法
# with语句将会绑定这个方法的返回值到 as 子句中指定的目标, 如果有的话
# with语句运行结束后, 会在上下文管理器对象上调用 __exit__ 方法, 以此扮演 finally 子句的角色

# 执行 with 后面的表达式得到的结果是上下文管理器对象
# 把值绑定到目标变量上(as 子句)是在上下文管理器对象上调用 __enter__ 方法的结果
with open('main.py') as f:
    src = f.read(100)
print(len(src))  # 18
print(f.closed)  # True


class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'abc'  # 通过return绑定as子句变量

    def reverse_write(self, text):
        self.original_write(text[::-1])

    # exc_type 异常类
    # exc_val 异常实例
    # exc_tb traceback对象
    # 如果__exit__方法返回None或者True之外的值, with块中的任何异常都会向上冒泡
    def __exit__(self, exc_type, exc_val, exc_tb):
        import sys  # 重复导入模块不会消耗很多资源, 因为 Python 会缓存导入的模块
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True


with LookingGlass() as w:
    print('abcdefg')  # gfedcba
    print(w == 'abc')  # eurT

print('abcdefg')  # abcdefg

# contextlib
import contextlib


# @contextmanager
# 这个函数是一个 decorator, 它可以定义一个支持 with 语句上下文管理器的工厂函数
# 而不需要创建一个类或 __enter__() 与 __exit__() 方法
# 被装饰的函数在被调用时, 必须返回一个 generator 迭代器
# __enter__执行时, 调用生成器函数, 保存生成器对象gen
# 调用next(gen), 产出yield值
# __exit__执行时, 检查有没有把异常传给exc_type; 如果有, 调用gen.throw(exception)
# 没有异常就继续next(gen), 执行yield之后的代码
@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    try:
        yield 'abc'  # 产出一个值绑定到as子句变量
    # 如果with块中出现异常会捕获并在yield表达式抛出
    except ZeroDivisionError as e:
        print(f'ZeroDivisionError! {e}')  # orez yb noisivid !rorrEnoisiviDoreZ
    finally:
        sys.stdout.write = original_write


with looking_glass() as w:
    print(123 / 0)  # 321
    print(w == 'abc')  # eurT
print('abcdefg')  # abcdefg

# contextlib.suppress(Exception) 忽略指定异常
with contextlib.suppress(ZeroDivisionError):
    print(1 / 0)
