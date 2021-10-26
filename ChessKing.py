PosCol = int(input())
PosRow = int(input())
CellCol = int(input())
CellRow = int(input())
if CellCol == PosCol + 1 or CellCol == PosCol - 1 or CellCol == PosCol:
    if CellRow == PosRow + 1 or CellRow == PosRow - 1 or CellRow == PosRow:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
