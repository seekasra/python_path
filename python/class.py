#
# Example file for working with classes
#


class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString )
        


class anotherClass(myClass):
    def method1(self):
        myClass.method2(self, "hi")
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherClass method2 ")
        




def main():
    c = myClass()
    c.method1()
    c.method2("LOL")
 
    c2 = anotherClass()
    c2.method1()
    #c2.method2()

if __name__ == "__main__":
  main()

