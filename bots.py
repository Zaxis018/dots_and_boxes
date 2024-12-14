import random
import copy


# Set up some constants
WIDTH, HEIGHT = 600, 600

class RandomBot:
    def __init__(self,grid_size,edges):
        # self.board_state=board_state
        self.grid_size=grid_size
        global gridSize
        gridSize=self.grid_size

        ROWS, COLS = gridSize,gridSize
        total_boxes=(COLS-1)*(COLS-1)

        global all_possible_moves
        all_possible_moves=[]
        for i in range (0,COLS):
            for j in range (0,COLS-1):
                horizontal_edge_move=[(i,j),(i,j+1)]
                all_possible_moves.append(horizontal_edge_move)
        for i in range (0,COLS):
            for j in range(0,COLS-1):
                vertical_edge_move=[(j,i),(j+1,i)]
                all_possible_moves.append(vertical_edge_move)

        self.SQUARE_SIZE = WIDTH//self.grid_size
        self.offset=self.SQUARE_SIZE/2 
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
            move_copy[0] = (self.offset+move_copy[0][0]*self.SQUARE_SIZE, self.offset+move_copy[0][1]*self.SQUARE_SIZE)
            move_copy[1] = (self.offset+move_copy[1][0]*self.SQUARE_SIZE, self.offset+move_copy[1][1]*self.SQUARE_SIZE)

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

class MinimaxBot:
    def __init__(self, grid_size, edges):
        self.grid_size = grid_size
        self.edges = edges
        self.SQUARE_SIZE = WIDTH // self.grid_size
        self.offset = self.SQUARE_SIZE / 2

        # Precompute all possible moves (similar to RandomBot)
        self.all_possible_moves = []
        for i in range(0, grid_size):
            for j in range(0, grid_size - 1):
                horizontal_edge = [(i, j), (i, j + 1)]
                vertical_edge = [(j, i), (j + 1, i)]
                self.all_possible_moves.append(horizontal_edge)
                self.all_possible_moves.append(vertical_edge)

    def update_board(self, edge_list):
        self.edges = list(edge_list)

    def evaluate_board(self, edges):
        """
        Evaluation function to score the current board state.
        Higher values are better for the bot, and lower values favor the opponent.
        """
        score = 0
        for i in range(self.grid_size - 1):
            for j in range(self.grid_size - 1):
                top = [(i, j), (i, j + 1)]
                bottom = [(i + 1, j), (i + 1, j + 1)]
                left = [(i, j), (i + 1, j)]
                right = [(i, j + 1), (i + 1, j + 1)]

                box_edges = [top, bottom, left, right]
                count = sum(edge in edges for edge in box_edges)

                # Adjust the score based on how close the box is to being completed
                if count == 3:
                    score += 10  # Favor moves that complete a box
                elif count == 2:
                    score += 1  # Favor moves that set up a box

        return score

    def minimax(self, edges, depth, is_maximizing):
        """
        Minimax algorithm to determine the best move.
        """
        if depth == 0 or len(edges) == len(self.all_possible_moves):
            return self.evaluate_board(edges)

        if is_maximizing:
            max_eval = float('-inf')
            for move in self.all_possible_moves:
                if move not in edges:
                    new_edges = edges + [move]
                    eval = self.minimax(new_edges, depth - 1, False)
                    max_eval = max(max_eval, eval)
            return max_eval

        else:
            min_eval = float('inf')
            for move in self.all_possible_moves:
                if move not in edges:
                    new_edges = edges + [move]
                    eval = self.minimax(new_edges, depth - 1, True)
                    min_eval = min(min_eval, eval)
            return min_eval

    def get_move(self):
        """
        Select the best move using the Minimax algorithm.
        """
        best_move = None
        best_value = float('-inf')

        for move in self.all_possible_moves:
            if move not in self.edges:
                new_edges = self.edges + [move]
                move_value = self.minimax(new_edges, depth=3, is_maximizing=False)

                if move_value > best_value:
                    best_value = move_value
                    best_move = move

        if best_move is not None:
            move_copy = [list(best_move[0]), list(best_move[1])]
            move_copy[0] = (self.offset + move_copy[0][0] * self.SQUARE_SIZE, self.offset + move_copy[0][1] * self.SQUARE_SIZE)
            move_copy[1] = (self.offset + move_copy[1][0] * self.SQUARE_SIZE, self.offset + move_copy[1][1] * self.SQUARE_SIZE)
            return move_copy

        return None

