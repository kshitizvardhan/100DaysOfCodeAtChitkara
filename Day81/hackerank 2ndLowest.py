students={}

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.update({name:score})
        scores=sorted(students.values())
    nd2lowest= scores[1]
    
    for names,scores in sorted(students.items()):
        if scores == nd2lowest:
            print(names)
