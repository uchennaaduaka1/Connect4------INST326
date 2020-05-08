def next_cell(cell, offset):
    return [cell[0] + offset[0], cell[1] + offset[1]]

def piece_is_in_grid(grid_height, grid_width, cell):
    return (cell[0] >= 0 and cell[0] < grid_height and cell[1] >= 0 and cell[1] < grid_width)

def count_diagonal_win(grid, last_played_cell, offset1, offset2):
    cell = last_played_cell
    grid_height = len(grid)
    grid_width = len(grid[0])
    counter = 1
    
    while piece_is_in_grid(grid_height, grid_width, next_cell(cell, [offset1[0], offset1[1]])):
        counter += 1
        cell = next_cell(cell, [offset1[0],offset1[1]])
        cell = last_played_cell
    
    while piece_is_in_grid(grid_height, grid_width, next_cell(cell, [offset2[0], offset2[1]])):
        counter += 1
        cell = next_cell(cell, [offset2[0], offset2[1]])
    
    return counter

def win_is_horizontal(grid, player, last_played_cell, winning_score):
    player_score = 0
    for cell in grid[last_played_cell[0]]:
        if cell == player:
            player_score += 1
            if player_score >= winning_score:
                return True
        else:
            player_score = 0
    return False

def win_is_vertical(grid, player, last_played_cell, winning_score):
    player_score = 0
    for row in range(0, len(grid)):
        if grid[row][last_played_cell[1]] == player:
            player_score += 1
            if player_score >= winning_score:
                return True
            else:
                player_score = 0
    return False

def win_is_diagonal(grid, player, last_played_cell, winning_score, offset1, offset2):
    if count_diagonal_win(grid, last_played_cell, offset1, offset2) < winning_score:
        return False
    
    game_cell = last_played_cell
    while piece_is_in_grid(len(grid), len(grid[0]), next_cell(game_cell, offset1)):
        game_cell = next_cell(game_cell,offset1)
    
    player_score = 0
    for i in range(0, count_diagonal_win(grid, last_played_cell, offset1, offset2)):
        if grid[game_cell[0]][game_cell[1]] == player:
            player_score += 1
            if player_score >= winning_score:
                return True
        else:
            player_score = 0
        game_cell = next_cell(game_cell, offset2)
    return False

def game_is_win(grid, player, last_played_cell, winning_score):
    if win_is_horizontal(grid, player, last_played_cell, winning_score):
        return True
    if win_is_vertical(grid, player, last_played_cell, winning_score):
        return True
    #A descending diagonal win
    if win_is_diagonal(grid, player, last_played_cell, winning_score, [-1,-1], [1,1]):
        return True
    #A ascending diagonal win
    else:
        return win_is_diagonal(grid, player, last_played_cell, winning_score, [-1,1],[1,-1])