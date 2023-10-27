if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.reverse()
    for i in range(n):
        if arr[i] > arr[i+1]:
            print(str(arr[i+1]))
            break
    
