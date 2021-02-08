if __name__ == '__main__':
    n = int(input())
    if n > 1 and n < 150:
        b = range(n)
        for m in b:
            print (m+1, end="")
    else:
        print("")
#Print Function