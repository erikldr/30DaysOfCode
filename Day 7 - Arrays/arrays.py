n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

arr.reverse()
print(" ".join(str(x) for x in arr))

