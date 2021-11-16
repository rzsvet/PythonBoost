matrix: List[List[number]] = []
rows = 0
columns = 0
deltaX = 0
deltaZ = 0


def on_on_chat():
    blocks.fill(AIR, pos(-25, 0, -25), pos(25, 3, 25), FillOperation.REPLACE)
    blocks.fill(GRASS,
                pos(-25, -1, -25),
                pos(25, -1, 25),
                FillOperation.REPLACE)
    can_exit()


player.on_chat("game_start", on_on_chat)


def find_path(i_row, i_column):
    global matrix, rows, columns, deltaX, deltaZ
    agent.teleport(pos(rows + 1 - i_row, 0, columns + 1 - i_column), WEST)
    weight = matrix[i_row][i_column]
    if i_row - 1 >= 0:
        if matrix[i_row - 1][i_column] == 0:
            matrix[i_row - 1][i_column] += weight + 1
            find_path(i_row - 1, i_column)
    if i_row + 1 < rows:
        if matrix[i_row + 1][i_column] == 0:
            matrix[i_row + 1][i_column] += weight + 1
            find_path(i_row + 1, i_column)
    if i_column - 1 >= 0:
        if matrix[i_row][i_column - 1] == 0:
            matrix[i_row][i_column - 1] += weight + 1
            find_path(i_row, i_column - 1)
    if i_column + 1 < columns:
        if matrix[i_row][i_column + 1] == 0:
            matrix[i_row][i_column + 1] += weight + 1
            find_path(i_row, i_column + 1)


def can_exit():
    global matrix, rows, columns, deltaX, deltaZ
    matrix = [
        [0, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0]
    ]
    rows = len(matrix)
    columns = len(matrix[0])
    deltaX = rows + 2
    deltaZ = columns + 2
    blocks.fill(GRASS,
                pos(1, 0, 1),
                pos(deltaX, 0, deltaZ),
                FillOperation.REPLACE)
    for i_row in range(rows):
        for i_column in range(columns):
            if matrix[i_row][i_column] == 0:
                blocks.fill(AIR,
                            pos(deltaX - i_row - 1, 0, deltaZ - i_column - 1),
                            pos(deltaX - i_row - 1, 1, deltaZ - i_column - 1),
                            FillOperation.REPLACE)
    matrix[0][0] = 1
    find_path(0, 0)

    if matrix[rows - 1][columns - 1] == 0:
        player.say("False")
    else:
        player.say("True")