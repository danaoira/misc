if __name__ == '__main__':
    def set_lows(val, low, sec):
        if val is low or val is sec:
            pass
        elif (val < low):
            sec = low
            low = val
        elif (low < val) and (val < sec):
            sec = val
        return low, sec
    
    def get_sec(students, second):
        sec_students = []
                
        for _ in students:
            if _[1] == second:
                sec_students.append(_[0])
                
        if len(sec_students) is 1:
            print(sec_students[0])
        else:
            for i in sorted(sec_students):
                print(i)
    
    students = []
    lowest = 1000
    second = 999
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
        lowest, second = set_lows(score, lowest, second)
        
    get_sec(students, second)