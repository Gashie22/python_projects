import modules
modules.find_max()

from  modules import find_max

def first_one (name,surname):
    print(f'{name},{surname}')
  #  print('hello Gashie')

    print('how are you today?')


print('start')
first_one('Alexa','Maso')
first_one('courage','maso')
print('stop')
try:
    def cube(num):
        answer = num * num * num
        return answer


    num = int(input('enter your number : '))
    result=cube(num)
    print(result)

except NameError :
    print('invalid operations')

except ValueError :
    print("enter an integer")


