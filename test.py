# class A:
#     mod = []
#
#     def __init__(self):
#         self.mod.append("yes")
#
#
# class C:
#     mod = []
#
#     def __init__(self):
#         self.mod.append('maybe')
#
#
# class B(A, C):
#     # mod = ['no']
#
#     def __init__(self):
#         A.__init__(self)
#         C.__init__(self)
#
#
# a = B()
#
# print(a.mod)

print(list(range(10)))
