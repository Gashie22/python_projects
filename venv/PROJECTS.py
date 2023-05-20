weight = int(input("enter your weight in lbs or kgs:  "))
mass= input("enter k for kgs and lb for pounds: ")

if mass.upper()=='K' :
 weight=weight*0.45
 print(f"weight is : {weight}")
elif mass.upper()=='L':
 weight=weight/0.45
 print(f'weight is : {weight}')
else:print('enter valid unit')

input('Type help to start')
instr=input()

while instr.lower()=='help':


 print('enter start-to start the car')
 print("enter stop-to stop the car")
 print("quit - to exit")





 if start.lower()=='start':
  start = input()
  print('engine started')
 elif stop.lower()=='stop':
  stop = input()
  print('stop')
 elif quits.lower()=='quit':
  quits = input()
  break

else: print("invalid option")

