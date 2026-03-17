n = int(input())
games = input()

gamesThatWonAnton = 0
gamesThatWonDanik = 0

for x in range(n):
    if games[x] == 'A':
        gamesThatWonAnton += 1
    else:
        gamesThatWonDanik += 1

if gamesThatWonAnton > gamesThatWonDanik:
    print('Anton')
elif gamesThatWonAnton < gamesThatWonDanik:
    print('Danik')
else:
    print('Friendship')
