# import random

# # Set up some constants
# WIDTH, HEIGHT = 600, 600
# ROWS, COLS = 6,6
# total_boxes=(COLS-1)*(COLS-1)
# SQUARE_SIZE = WIDTH//COLS
# offset=SQUARE_SIZE/2 

# class RandomBot:
#     def __init__(self,grid_size,edges):
#         # self.board_state=board_state
#         self.grid_size=grid_size
#         self.edges=edges
#     def update_board(self,edge_list):
#         self.edges=edge_list
#     def get_move(self):
#         while True:
#             x = random.randint(0, self.grid_size-1)
#             y = random.randint(0, self.grid_size-1)
#             point1=(x,y)
            
#             # Generate point2
#             rand_num = random.choice([-1, 1])
#             if random.choice([True, False]):
#                 point2 = (x + rand_num, y)
#             else:
#                 point2 = (x, y + rand_num)

#             # Convert grid points to actual coordinate on window
#             point1 = (offset+point1[0]*SQUARE_SIZE, offset+point1[1]*SQUARE_SIZE)
#             point2 = (offset+point2[0]*SQUARE_SIZE, offset+point2[1]*SQUARE_SIZE)

#             if [point1,point2] not in self.edges : # if new edges found 
#                 break
#         return [point1,point2]



import random

# Set up some constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 6,6
total_boxes=(COLS-1)*(COLS-1)
SQUARE_SIZE = WIDTH//COLS
offset=SQUARE_SIZE/2 

class RandomBot:
    def __init__(self,grid_size,edges):
        # self.board_state=board_state
        self.grid_size=grid_size
        self.edges=edges
    def update_board(self,edge_list):
        self.edges=edge_list
    def get_move(self):
        while True:
            x = random.randint(0, self.grid_size-1)
            y = random.randint(0, self.grid_size-1)
            point1=(x,y)
            
            # Generate point2
            rand_num = random.choice([-1, 1])
            if random.choice([True, False]):
                point2 = (x + rand_num, y)
            else:
                point2 = (x, y + rand_num)

            # Convert grid points to actual coordinate on window
            point1 = (offset+point1[0]*SQUARE_SIZE, offset+point1[1]*SQUARE_SIZE)
            point2 = (offset+point2[0]*SQUARE_SIZE, offset+point2[1]*SQUARE_SIZE)

            # Check if points are within the grid
            if (offset <= point1[0] <= (self.grid_size-1)*SQUARE_SIZE and 
                offset <= point1[1] <= (self.grid_size-1)*SQUARE_SIZE and
                offset <= point2[0] <= (self.grid_size-1)*SQUARE_SIZE and
                offset <= point2[1] <= (self.grid_size-1)*SQUARE_SIZE and
                [point1,point2] not in self.edges): # if new edges found 
                break
        return [point1,point2]
