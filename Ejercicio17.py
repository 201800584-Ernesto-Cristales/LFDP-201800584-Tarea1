def count_substring(string, sub_string):
    contador = 0
    i = string.find(sub_string)
    while i != -1:
        contador += 1
        i = string.find(sub_string, i+1)
    return contador

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
#Find a String