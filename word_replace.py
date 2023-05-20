def word_replace():
    str = f'hie there my name is {name},and i am a boy'
    print(str)
    replace=input('enter the word to replace: ').lower()
    new_word=input('enter the new word: ').lower()
    new_sentence=str.replace(replace,new_word)
    print(new_sentence)

name='Gashie'
word_replace()