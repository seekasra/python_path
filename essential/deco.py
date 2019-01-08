

def gfather(s):
    def father():
        print("I'm the father after gfather!")
        s()
        print("I'm the father after gfather and son!")
    return father

@gfather
def son():
    print("THISS IS THE SON")


son()
