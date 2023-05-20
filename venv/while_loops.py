secret_num=9


i=1
while i <=3 :
    guess_num=int(input('enter the secret number : '))
    if guess_num==secret_num:
        print(f'congrats , you won ')
        break
    else:print('try again')
    i+=1

else:print('you failed')
