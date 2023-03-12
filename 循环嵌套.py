
#9*9
# list=[]
# for i in range(1,10):
#     for n in range(1,10):
#
#         a='{}*{}={}'.format(n,i,i*n)
#
#         list.append(a)
#         if n==i:
#             break
#
#         # list.append(' ')
#     print(list)
#     list=[]


for a in range(1,10):
    m = a + 1
    for n in range(1,m):

        print('{}*{}={}'.format(n,a,a*n),end='\t')

    print(' ')
