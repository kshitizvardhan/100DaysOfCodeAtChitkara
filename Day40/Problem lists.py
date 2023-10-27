if __name__ == '__main__':
    N = int(input())
    li=[]
    for i in range(N):
        n=input().split()
        if n[0]=="insert":
            i, e=int(n[1]), int(n[2])
            li.insert(i, e)
        elif n[0]=="remove":
            e=int(n[1])
            li.remove(e)
        elif n[0]=="append":
            e=int(n[1])
            li.append(e)
        elif n[0]=="sort":
            li.sort()
        elif n[0]=="pop":
            li.pop()
        elif n[0]=="reverse":
            li.reverse()
        elif n[0]=="print":
            print(li)
        
