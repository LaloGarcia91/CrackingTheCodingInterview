

class URLify:

    def __init__(self, str):
        self.replaceWhiteSpacesInString(str, "%20")

    def replaceWhiteSpacesInString(self, thisStr, replaceWithThis):
        strRebuilt = ""
        for strChar in thisStr.strip():
            if strChar == " ":
                strRebuilt += replaceWithThis
            else:
                strRebuilt += strChar
        print(strRebuilt)


URLify("this is a random sentence           ")
