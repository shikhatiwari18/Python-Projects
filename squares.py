l = [1,2,3,4]
def squares(x):
    return x*x
updated_list = []
for i in l:
    updated_list.append(squares(i))
print(updated_list) 

print(type(map(squares,l)))   