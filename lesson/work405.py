class CodeA:

    @staticmethod
    def foo():
        print("调用静态方法 foo()")

class CodeB:
    @classmethod
    def foo(cls):
        print("调用类方法 foo()")
