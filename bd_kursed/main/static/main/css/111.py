# lst = list(range(1,6))
# d = {str(element) + '!': element  for element in lst if element %2 == 0}
# print(''.join(d.keys()))

# data = {el for lst in [[1,2,2],[2,4]] for el in lst if sum(lst)  !=6}
# r =  sum(data)
#
# print(r)

# lst = [1,2,3,5,7,9,13,15,24,38,44,56,64,128,256,512,1024]
# lst.extend([312,218,511,333,614,221])
# lst = list(filter(lambda x: x%3 ==2 and x <8, lst))
# print(sum(lst))

# lst = [1,2,3,9,8,6,5,3,1,8,5,2,4,3, sum([255,12,244, -13])]
# lst = list(map(lambda x: x*2, lst[:4]))
# print(lst[-1])

def dec(f):
    def n (*args,**kwargs):
        return f(*args,**kwargs)+ sum(args) + max(kwargs.values())
    return n

@dec
def my_func(a,b,c=1,**kwargs):
    return a+b-c

print(my_func(3,2,d=2,e=3))