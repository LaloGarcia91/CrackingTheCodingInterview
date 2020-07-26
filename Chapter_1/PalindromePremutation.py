class PalindromePremutation:
    differentLettersInString = {}
    evenNumbersCounter = 0
    oddNumbersCounter = 0

    def __init__(self, word):
        self.CheckIfPalindromePermutation(word)

    def CheckIfPalindromePermutation(self, word):
        word = word.replace(" ", "")
        self.AcumulateTheDifferentLettersFromThisString(word)
        self.GetEvenOrOddLettersCount()

        if self.evenNumbersCounter > 0 and self.oddNumbersCounter <= 1:
            print("TRUE - It is a permutation of a palindrome.")
        else:
            print("FALSE - It is not a permutation of a palindrome.")

    def AcumulateTheDifferentLettersFromThisString(self, word):
        for letter in word:
            if not letter in self.differentLettersInString:
                self.differentLettersInString[letter] = 1
            else:
                self.differentLettersInString[letter] += 1

    def GetEvenOrOddLettersCount(self):
        for letterKey in self.differentLettersInString:
            thisLetterCount = self.differentLettersInString[letterKey]
            if thisLetterCount % 2 == 0:  # is even number
                self.evenNumbersCounter += 1
            else:  # is odd number
                self.oddNumbersCounter += 1


PalindromePremutation("tact coa")
