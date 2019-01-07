
def main():
    for i in inclusive_range(1,25):
        print(i, end =' ')
    print()


def inclusive_range(*args):
    num_args = len(args)
    stop = 1
    start = 0
    step = 1

    if num_args == 0:
        print("Error - too few arguments are passed")
    elif num_args == 1:
        stop = args[0]
    elif num_args == 2: 
        start = args[0]
        stop = args[1]
    else:
        start = args[0]
        stop = args[1]
        step = args[1]


    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == "__main__": main()
