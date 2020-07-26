class IsUnique:

    def __init__(self):
        self.loopThisWord("hello")

    def loopThisWord(self, thisWord):
        for letter in thisWord:
            result = self.checkIfLetterRepeatsInString(thisWord, letter)
            if result:
                print("NO Unique characters in the word: " + thisWord)
                return False
        print("ALL Unique characters in the word: " + thisWord)
        return True

    def checkIfLetterRepeatsInString(self, thisWord, letter):
        counter = 0
        for letterInIteration in thisWord:
            if letterInIteration == letter:
                counter += 1
                if counter > 1:
                    return True
        return False


IsUnique()
