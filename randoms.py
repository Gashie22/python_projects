import random
for i in range(3):
    x=random.random()
    print(x)
y=random.randint(5,8)
print(y)


nums=[3,4,5]
z=random.choice(nums)
print(z)
class Dice :
    def roll(self,nam):
        e=random.randint(1,6)
        f=random.randint(1,6)

        return e,f

    nam=(1,2,3,4,5,6)

Dice1=Dice()
result=Dice1.roll(nam=2)
print(result)

