# 类装饰器的使用



class Check(object):
    def __init__(self,fn):    # 因此需要提供一个init方法，并且需要增加一个fn参数用于接收被装饰的函数名称
        self.__fn = fn


    def __call__(self, *args, **kwargs):
        # 添加装饰功能
        print('请先登录....')
        self.__fn()   # self.__fn等于fn,而fn又等于comment,所以说self.__fn()等价于comment()

@Check         # @Check 等价于  comment = Check(comment)
def comment():
    print('发表评论')


comment()