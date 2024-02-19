import random

# Set up some constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 6,6
total_boxes=(COLS-1)*(COLS-1)
SQUARE_SIZE = WIDTH//COLS
offset=SQUARE_SIZE/2 


all_possible_moves=[]
for i in range (0,COLS):
    for j in range (0,COLS-1):
        horizontal_edge_move=[(i,j),(i,j+1)]
        all_possible_moves.append(horizontal_edge_move)
for i in range (0,COLS):
    for j in range(0,COLS-1):
        vertical_edge_move=[(j,i),(j+1,i)]
        all_possible_moves.append(vertical_edge_move)


class RandomBot:
    def __init__(self,grid_size,edges):
        # self.board_state=board_state
        self.grid_size=grid_size
        self.edges=edges

    def update_board(self,edge_list):
        self.edges=list(edge_list)

    def get_move(self):
        while True:
            # x = random.randint(0, self.grid_size)
            # y = random.randint(0, self.grid_size)
            # point1=(x,y)
            
            # # Generate point2
            # rand_num = random.choice([-1, 1])
            # if random.choice([True, False]):
            #     point2 = (x + rand_num, y)
            # else:
            #     point2 = (x, y + rand_num)

            random_number = random.randint(0, len(all_possible_moves)-1)
            move=all_possible_moves[random_number]
            
            #create a move_copy so that in next run of while loop previous move value isnt altered
            move_copy = [list(move[0]), list(move[1])]

            # Convert grid points to actual coordinate on window
            move_copy[0] = (offset+move_copy[0][0]*SQUARE_SIZE, offset+move_copy[0][1]*SQUARE_SIZE)
            move_copy[1] = (offset+move_copy[1][0]*SQUARE_SIZE, offset+move_copy[1][1]*SQUARE_SIZE)


            # # Convert grid points to actual coordinate on window
            # point1 = (offset+point1[0]*SQUARE_SIZE, offset+point1[1]*SQUARE_SIZE)
            # point2 = (offset+point2[0]*SQUARE_SIZE, offset+point2[1]*SQUARE_SIZE)

            # # Check if points are within the grid
            # if (offset <= point1[0] <= (self.grid_size)*SQUARE_SIZE and 
            #     offset <= point1[1] <= (self.grid_size)*SQUARE_SIZE and
            #     offset <= point2[0] <= (self.grid_size)*SQUARE_SIZE and
            #     offset <= point2[1] <= (self.grid_size)*SQUARE_SIZE and
            #     [point1,point2] not in self.edges): # if new edges found 
            #     break
            if move_copy not in self.edges:
                break

        # Order the points such that point1 always has lesser x or y coordinate
        # if point1[0] == point2[0]:  # Vertical edge
        #     if point1[1] > point2[1]:
        #         point1, point2 = point2, point1
        # else:  # Horizontal edge
        #     if point1[0] > point2[0]:
        #         point1, point2 = point2, point1
            
        # if move[0][0] == move[1][0]:  # Vertical edge
        #     if move[0][1] > move[1][1]:
        #         move[0], move[1] = move[1], move[0]
        # else:  # Horizontal edge
        #     if move[0][0] > move[1][0]:
        #         move[0], move[1] = move[1], move[0]


        #return [point1,point2]
        return move_copy
        

