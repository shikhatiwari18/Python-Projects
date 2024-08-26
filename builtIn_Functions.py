print(dir(__builtins__))
temp = [22.0,32,36,42.5,19]
for T in temp:
    f = ((9/5) * T) + 32
    print('{:5.1f} in degree C is equivalent to {:6.1f} in degree F.'.format (T,f))
    
def Farenhite(T):
    return round(((9/5)*T) + 32, 1)
print(Farenhite(22))

temp = [22.1,12,33,56,88]
results = list(map(Farenhite,temp))
print('Temp in deg C',temp)
print('Temp in degree F', results)

num = [32,45,16,55,1,50,101]
odd_num =[]
for n in num:
    if n % 2 :
        odd_num.append(n)
print(odd_num)        

num = [1,2,3,4,5,6,7,8,9,10]
odd_num = list(filter(lambda n: n %2,num))
print(odd_num)

num = [2,4,6,8,10,22]
tot = 0
for n in num:
    tot += n
print('Total :',tot)    

from functools import reduce
num = [2,4,6,8,10]
result = reduce(lambda x,y:x+y,num)
print('Total is',result)


        