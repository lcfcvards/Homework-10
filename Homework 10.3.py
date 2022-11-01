game = [
    ["X", "X", "O"],
    ["O", "X", "O"],
    ["X", "O", "O"],
]

winner = None

for i in range(3):
    if game[i][0] == game[i][1] == game[i][2]:
        winner = game[i][0]
    if game[0][i] == game[1][i] == game[2][i]:
        winner = game[0][i]
if game[0][0] == game[1][1] == game[2][2]:
    winner = game[0][0]
if game[0][2] == game[1][1] == game[2][0]:
    winner = game[0][2]

if winner:
    print(f"Победитель - {winner}")
else:
    print("Ничья")
