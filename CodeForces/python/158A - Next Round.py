_, k = map(int, input().split())

participants = list(map(int, input().split()))
selected = participants[k - 1]

counter = 0
for participant in participants:
    if participant >= selected and participant > 0:
        counter += 1
print(counter)
