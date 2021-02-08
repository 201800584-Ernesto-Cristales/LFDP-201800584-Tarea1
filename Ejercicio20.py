if __name__ == '__main__':
    N = int(input())
    array = []
    for i in range(1,N+1):
        procedimiento = input().split()
        if(procedimiento[0] == 'insert'):
            array.insert(int(procedimiento[1]),int(procedimiento[2]))
        elif(procedimiento[0] == 'remove'):
            array.remove(int(procedimiento[1]))
        elif(procedimiento[0] == 'print'):
            print(array)
        elif(procedimiento[0] == 'pop'):
            array.pop()
        elif(procedimiento[0] == 'sort'):
            array.sort()
        elif(procedimiento[0] == 'append'):
            array.append(int(procedimiento[1]))
        elif(procedimiento[0] == 'reverse'):
            array.reverse()
#Lists