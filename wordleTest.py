import random
import re

# import all 5 letter Words
# make it so i can touch the screen virtually
# have a knowledge base - green letters - yellow and...
# ...void letters that cannot be used



with open ('wordlewords.txt') as f:
    contents = f.read()
wordsLeft = list(contents.split("\n"))
for word in wordsLeft:
    if len(word) != 5:
        wordsLeft.remove(word)
newList = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



class knowledge():
    def __init__(self):
        self.knowledgeBase = ['-', '-', '-', '-', '-']
        self.kindaCorrect = []
        self.wrong = []
        self.tries = 6
        self.index = 0


    # updates knowledge based on score and word chosen
    def updateKnowledge(self,score,chosen):
        print(len(wordsLeft))
        wordsLeft.remove(chosen)
        for attempt in score:
            if attempt == 'y':
                self.knowledgeBase[self.index] = chosen[self.index]
            elif attempt == 'k':
                self.kindaCorrect.append(chosen[self.index])
            elif attempt == 'n':
                self.wrong.append(chosen[self.index])
            self.index += 1
        self.index = 0
        print(self.knowledgeBase)
        print(self.wrong)
        print(self.kindaCorrect)

    
    def updateCorrect(self,score):
        while self.index < len(score):
            if str(score[self.index]) == 'y':
                for word in wordsLeft:
                    if str(word[self.index]) == str(self.knowledgeBase[self.index]) and word not in newList:
                        newList.append(word)
            self.index += 1
        self.index = 0

        if len(newList) != 0:
            wordsLeft.clear()
            for word in newList:
                wordsLeft.append(word)
            newList.clear()


    # updating word bank based on knowledge base
    def updateWordsWrong(self):
        for ch in self.wrong:
            if ch in alphabet:
                alphabet.remove(ch)
        
        put = True

        for word in wordsLeft:
            for letter in word:
                if letter not in alphabet:
                    put = False
            if put == True and word not in newList:
                newList.append(word)
            put = True


        if len(newList) != 0:
            wordsLeft.clear()
            for word in newList:
                wordsLeft.append(word)
            newList.clear()



    # updates word bank to only words containing kinda letters
    def updateMaybeWords(self, score, chosen):    
        put = True

        for word in wordsLeft:
            for ch in self.kindaCorrect:
                if ch not in word:
                    put = False
            if put == True:
                while self.index < len(score):
                    if score[self.index] == 'k':
                        if word[self.index] == chosen[self.index]:
                            put = False
                    self.index += 1
                self.index = 0

            if put == True and word not in newList:
                    newList.append(word)
            put = True


        if len(newList) != 0:
            wordsLeft.clear()
            for word in newList:
                wordsLeft.append(word)
            newList.clear()
        

    def updateALL(self,score,chosen):
        self.updateCorrect(score)
        self.updateWordsWrong()
        self.updateMaybeWords(score,chosen)

                    

    #  pick a random word if there are many choices
    def randomPick (self):
        print(len(wordsLeft))
        print(random.choice(wordsLeft))



    # checking to see if game is over
    def gameOver(self):
        self.tries -= 1

        if self.tries == 0:
            print ("Game over...")
            return True
        return False

    

    # removing any letters from kinda correct that are in knowledge base
    def dupeCheck(self):
        for ch in self.kindaCorrect:
            if ch in self.knowledgeBase:
                self.kindaCorrect.remove(ch)

    

def main():
    play = knowledge()
    while play.gameOver() == False:
        chose = input('word: ')
        score = input('score: ')
        
        play.updateKnowledge(score,chose)
        play.updateALL(score,chose)
        play.dupeCheck()
        play.randomPick()
        if score == 'yyyyy':
            quit()




main()