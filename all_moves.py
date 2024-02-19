COLS=6
all_possible_moves=[]
for i in range (0,COLS):
    for j in range (0,COLS-1):
        horizontal_edge_move=[(i,j),(i,j+1)]
        all_possible_moves.append(horizontal_edge_move)
for i in range (0,COLS):
    for j in range(0,COLS-1):
        vertical_edge_move=[(j,i),(j+1,i)]
        all_possible_moves.append(vertical_edge_move)

print(all_possible_moves)
print(len(all_possible_moves))