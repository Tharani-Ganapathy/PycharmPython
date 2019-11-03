from PyDictionary import PyDictionary
from random_word import RandomWords
r = RandomWords()
pd = PyDictionary()
# Return a single random word
word_of_the_game = r.get_random_word(minLength=3, maxLength=12, hasDictionaryDef="true")
print(word_of_the_game)
today_word = word_of_the_game
print(pd.meaning(word_of_the_game))
# creating a blank space
blank_word = []
length = int(len(word_of_the_game))

for i in range(0, length):
    blank_word.append("_")
print(blank_word)
counter = 0
while counter < 7:
        x = input("Enter the letter : ")
        flag = word_of_the_game.find(x)
        if flag < 0:
            counter = counter+1
        else:
            while flag >= 0:
                word_of_the_game = word_of_the_game.replace(x, '_', 1)
                blank_word[flag] = x
                flag = word_of_the_game.find(x)
            print(blank_word)

        if word_of_the_game.count('_') == len(today_word):
            print("You win!!!")
            break

if counter == 7:
    print("Better Luck Next Time!!!")