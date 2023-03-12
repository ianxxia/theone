#
#
#
def test(m):
     if m == 1:
         return 1

     return 2 * test(m -1)

print(test(30))

m = 1 
for i in range(1,5):
    m*=i
    print(m)