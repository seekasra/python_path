#Reverse the string word by word

class schange:
    def __init__(self, s=""):
        self.str = s

    def reverse(self):
        words = self.str.rsplit(" ")
        r = []
        for w in reversed(words):
            r.append(w)

        print(r)

def main():

    changer = schange("The test string")
    changer.reverse()



if __name__ == "__main__":
    main()

