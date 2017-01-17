if __name__ == '__main__':
    N = int(input())    # 12
    commands = []
    list = []
    
    for i in range(0, N):
        j = input()
        commands.append(j)  # creates array of commands
                            
    for line in commands:
        if 'insert' in line:
            i, e = int(line.split()[1]), int(line.split()[2])
            list.insert(i, e)
        elif 'print' in line:
            print(list)
        elif 'remove' in line:
            e = int(line.split()[1])
            list.remove(e)
        elif 'append' in line:
            e = int(line.split()[1])
            list.append(e)
        elif 'sort' in line:
            list.sort()
        elif 'pop' in line:
            del list[-1]
        elif 'reverse' in line:
            list = list[::-1]