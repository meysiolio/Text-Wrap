def wrap(string, max_width):
    n = 0
    l = []
    while (n+1) * max_width <= len(string):
        l.append(string[n*max_width:(n+1)*max_width])
        n += 1
        
    l.append(string[n*max_width:])    
    string = '\n'.join(l)
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
