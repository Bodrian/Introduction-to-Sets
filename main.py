def average(array):
    f = sum(set(array))/len(set(array))
    return f

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
