if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    ans_key= student_marks.get(query_name)
    avg=0
    for i in range(len(ans_key)):
        avg+=ans_key[i]
               
    answer = avg/len(ans_key)
    print(format(answer,".2f"))
