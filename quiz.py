#this is a quiz game to game to guess the capital of certain countries
#we need an object to store the question + answer

quiz={
     'Question1':{
         'question':'What is the capital city of Zimbabwe',
         'Answer':'Harare'
    },
    'Question2': {
        'question': 'What is the capital city of South Africa',
        'Answer': 'Johannesburg'
    },
    'Question3': {
            'question': 'What is the capital city of Botswana',
            'Answer': 'Gaborone'
        },
    'Question4': {
        'question': 'What is the capital city of Britain',
        'Answer': 'London'
    },
    'Question5': {
            'question': 'What is the capital city of Germany',
            'Answer': 'Munich'
        }
}
score_counter=0
for x,value in quiz.items():
    print(value['question'])
    answer=input('enter your answer :')
    if answer.lower()==value['Answer'].lower():
        print('Correct answer')
        score_counter+=1
    else:
        print('Wrong answer')
        print('the answer is : '+value['Answer'])
f'Your score is {score_counter}'

print('You got ' + str(score_counter) + ' '+'out of 5')
percent=f'Your percentage is : {(score_counter *100)/5} %'
print(percent)
