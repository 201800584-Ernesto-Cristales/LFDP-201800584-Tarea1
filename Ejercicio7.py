if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print ([[A,B,C] for A in range(x+1) for B in range(y+1) for C in range(z+1) if A + B + C != n ])