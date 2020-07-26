class StringCompression:

    def __init__(self, word):
        self.CompressThisWord(word)

    def CompressThisWord(self, word):
        arrayOfLetters = self.BuildArrayOfDifferentLetters(word)

        if self.CheckIfStringCanBeCompressed( arrayOfLetters ):
            compressesString = ""
            for i in range(len(arrayOfLetters)):
                elementLetter = arrayOfLetters[i][0]
                lettersCount = len(arrayOfLetters[i])
                compressesString += elementLetter + str(lettersCount) + " "
            print(compressesString)
        else:
            print("Can't compresses the string: "+word)

    def BuildArrayOfDifferentLetters(self, word):

        acumulate = ""
        for i in range(len(word)):
            currentLetterInWord = word[i]
            if len(acumulate) == 0:
                acumulate += currentLetterInWord
                continue
            lastLetterAcumulated = acumulate[len(acumulate) - 1]
            if currentLetterInWord == lastLetterAcumulated:
                acumulate += currentLetterInWord
            else:
                acumulate += ","
                acumulate += currentLetterInWord
        return acumulate.split(",")

    def CheckIfStringCanBeCompressed(self, arrayOfLetters):
        for i in range(len(arrayOfLetters)):
            if len(arrayOfLetters[i]) > 1:
                return True # string CAN be compressed
        return False # string CAN'T be compressed


StringCompression("hello")
