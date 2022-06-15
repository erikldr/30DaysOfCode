import sys

N = int(input().strip())

phoneBook = dict()

for i in range(N):
    friends = input().strip().lower().split(" ")
    phoneBook[friends[0]] = friends[1]

query = sys.stdin.readline().strip()

while query:
    num_cel = phoneBook.get(query)

    if num_cel:
        print(query + "=" + num_cel)
    else:
        print("Not found")
    query = sys.stdin.readline().strip()

print(query)
