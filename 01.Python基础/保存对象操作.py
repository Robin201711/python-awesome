# encoding=utf-8

import pickle


class A(object):
    pass

a = A()
a.name = 'robin'

# 保存对象
a = pickle.dumps(a)
print type(a)

# 还原对象
b = pickle.loads(a)
print type(b)
print b.name
