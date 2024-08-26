class demo:
    pass
object = demo()
print(object)

# define the class
class Health:
# define the function init with with all the details    
    def __init__(self,name,age,loc):
#initializing the Health class        
         self.age = age
         self.name = name
         self.loc = loc
# Another method to display health info

def print_info(self):
    print('Health infot Details of individual')
    print('Name :', self.name)
    print('Age :',self.age)
    print('Location :',self.location)  
    
h1 = Health('shikha',23,'kymore')
h1.print_info()           