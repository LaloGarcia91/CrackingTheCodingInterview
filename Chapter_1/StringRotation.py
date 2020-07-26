class StringRotation:

    def __init__(self, s1, s2):
        print( self.isRotated(s1, s2) )

    def isRotated(self, s1, s2):
        s2 = list(s2)
        s2_as_str = ""
        for i in range(len(s2)):
            s2.append(s2[0])
            s2.pop(0)
            s2_as_str = "".join(s2)

        s1 = list(s1)
        for i in range(len(s1)):
            s1.append(s1[0])
            s1.pop(0)
            s1_as_str = "".join(s1)

            if s1_as_str == s2_as_str:
                return True
        return False


StringRotation("erbottlewat", "waterbottle")
