def my_func(*p_x):
    print(p_x, type(p_x))

my_func(1,2,3,4,5)


def my_func(**p_x):
    print(p_x, type(p_x))
    print(p_x.keys())
    print(p_x.values())

my_func(x=1,y=2,z=3,w=4,v=5)



def add(x,y):
    return x+y

result=add(10,20)
print(result)

# llambda function
addition = lambda x,y : x+y
result=addition(10,20)
print(result)
