def average(array):
    # your code goes here
    array=set(array)
    summed=sum(array)
    avg=summed/len(array)
    return format(avg, ".3f")
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
