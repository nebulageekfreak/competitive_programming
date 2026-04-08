problems, minutes = map(int, input().split())
counter = 0
time = 240

for i in range(1, problems + 1):
    if i * 5 + minutes <= time:
        counter += 1
        minutes += i * 5
    

print(counter)
