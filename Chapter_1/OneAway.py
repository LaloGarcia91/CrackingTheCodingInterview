class OneAway:

    def __init__(self, str1, str2):
        self.CheckIfWordsAre1CharAway(str1, str2)

    def CheckIfWordsAre1CharAway(self, str1, str2):
        check_1 = self.LoopThe2Words(str1, str2)
        check_2 = self.LoopThe2Words(str2, str1)

        if check_1 or check_2:
            print("One Away was found!")
            return True
        if not check_1 and not check_2:
            print("None 'One Away' found.")
            return False


    def LoopThe2Words(self, str1, str2):
        if str1 == str2:
            return False

        if (len(str1) == (len(str2) + 1)) or len(str1) == len(str2):
            counterForLettersNotShared = 0  # if this counter remains in 1... means that strings are "One Away".
            lettersSharedSoFar = ""  # if this string is always 1 char away from the longest string passed, strings are "One Away"

            i = 0
            while i < len(str1):
                if i < len(str2) and str1[i] == str2[i]:
                    lettersSharedSoFar += str1[i]
                else:
                    counterForLettersNotShared += 1
                if len(lettersSharedSoFar) == len(str2) or len(lettersSharedSoFar)+1 == len(str2):
                    return True
                i += 1
        return False


OneAway("hello", "hell")
