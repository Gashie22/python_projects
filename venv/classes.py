
class Beginner:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def name(self):
        print('Gashie')

    def age(self):
        print('25')


Beg=Beginner(25,38) #creating an object
Beg.age()
Beg.name()
print(Beg.x)