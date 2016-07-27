#-*-coding:utf-8-*-
#2-3
# import math
# def add(x,y,f):
#     return f(x)+f(y)
#
# print (add(25,9,math.sqrt))


# #2-4
# def format_name(s):
#     return s.capitalize()
#
# print map(format_name, ['adam', 'LISA', 'barT'])


# #2-6
# import math
#
# def is_sqr(x):
#     r = int(math.sqrt(x))
#     return r*r==x
#
# print filter(is_sqr, range(1, 101))


# #2-7
# def cmp_ignore_case(s1,s2):
#     if s1.lower()>s2.lower():
#         return 1
#     if s1.lower()<s2.lower():
#         return -1
#     return 0
#
# print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

# print ('Hi,{name},{message}'.format(name='Tom',message='hihao'))


# def new_counter(n):
#
#     class Counter(object):
#         def __init__(self, num):
#             self.num =num
#
#         def __call__(self):
#             self.num += 1
#             return self.num
#
#     return Counter(n)
#
# c1 = new_counter(10)
# c2 = new_counter(20)
# print c1(), c2(), c1(), c2()


#2-8
def calc_prod(lst):
    def lazy_prod(x,y):
        return x*y
    def prod():
        return reduce(lazy_prod,lst)
    return prod

f = calc_prod([1, 2, 3, 4])
print f()