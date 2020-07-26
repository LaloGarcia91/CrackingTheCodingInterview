class CheckPermutation:

    def __init__(self, str1, str2):
        self.checkIfIsPermutation(str1, str2)

    def checkIfIsPermutation(self, str1, str2):
        str1_len = len(str1)
        str2_len = len(str2)

        if str1_len == str2_len:
            counterIfEqualLetters = 0
            for str1_letter in str1:
                if str1_letter in str2:
                    counterIfEqualLetters += 1
                else:
                    print("It is NOT a permutation")
                    return False
                if counterIfEqualLetters == str1_len:
                    print("It IS a permutation")
                    return True
        else:
            print("Words are not even the same length")


# run exercise
CheckPermutation("HELLO", "HLLEO")
