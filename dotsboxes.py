import sys
import pygame

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 500, 500
ROWS, COLS = 8,8
total_boxes=(COLS-1)*(COLS-1)
SQUARE_SIZE = WIDTH//COLS

turn=True # first red's turn 
red_score=0
blue_score=0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


lines = []
lines_blue=[]
lines_red=[]

blue_squares=[]
red_squares=[]

# Set up the display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
offset=SQUARE_SIZE/2 #to center the dots in the display

def draw_grid():
    for x in range(0, WIDTH, SQUARE_SIZE):
        for y in range(0, HEIGHT, SQUARE_SIZE):
            pygame.draw.circle(WIN, BLACK, (x+offset, y+offset), 5)

def handle_click(coordinates):
    global turn
    if coordinates in lines:
        return
    lines.append(coordinates)
    if turn==True:
        lines_red.append(coordinates)
        turn= not turn # toggles between true and false
    else:
        lines_blue.append(coordinates)
        turn= not turn
    detect_box(coordinates)
    


def detect_box(coordinates):
    global turn
    global red_score
    global blue_score
    first_box=False
    second_box=False

    pointA=coordinates[0]
    pointB=coordinates[1]
    # print(f"first point: {pointA}")
    # print(f"second point: {pointB}")

    if pointA[0]==pointB[0]:
        # if vertical edge
        vertical=True
        edges_to_check_1=[  #for left box
            [ (pointA[0]-SQUARE_SIZE,pointA[1]) , pointA ],
            [ (pointB[0]-SQUARE_SIZE,pointB[1]) , pointB ],
            [ (pointA[0]-SQUARE_SIZE,pointA[1]) , (pointB[0]-SQUARE_SIZE,pointB[1])]
        ]
        edges_to_check_2=[ # for right box
            [  pointA , (pointA[0]+SQUARE_SIZE,pointA[1]) ],
            [  pointB,(pointB[0]+SQUARE_SIZE,pointB[1]) ],
            [ (pointA[0]+SQUARE_SIZE,pointA[1]) , (pointB[0]+SQUARE_SIZE,pointB[1])]
        ]

    else:
        #if horizontal edge
        vertical=False
        edges_to_check_1=[    # for lower box
            [ pointA ,(pointA[0],pointA[1]+SQUARE_SIZE) ],
            [ pointB ,(pointB[0],pointB[1]+SQUARE_SIZE) ],
            [ (pointA[0],pointA[1]+SQUARE_SIZE) , (pointB[0],pointB[1]+SQUARE_SIZE) ]
        ]
        
        edges_to_check_2=[   # for upper box
            [ (pointA[0],pointA[1]-SQUARE_SIZE) , pointA ],
            [ (pointB[0],pointB[1]-SQUARE_SIZE) , pointB ],
            [ (pointA[0],pointA[1]-SQUARE_SIZE) , (pointB[0],pointB[1]-SQUARE_SIZE) ]
        ]

    if all(edge in lines for edge in edges_to_check_1):
        if vertical==True:
            diagonal=[(pointA[0]-SQUARE_SIZE,pointA[1]),pointB]
            if turn==False:
                red_squares.append(diagonal)
                red_score+=1
            else:
                blue_squares.append(diagonal)
                blue_score+=1
        else:
            diagonal=[pointA,(pointB[0],pointB[1]+SQUARE_SIZE) ]
            if turn==False:
                red_squares.append(diagonal)
                red_score+=1
            else:
                blue_squares.append(diagonal)
                blue_score+=1
        # turn= not turn # if box is deteteced , the player gets the turn again
        first_box=True
        print("first box_detected")


    if all(edge in lines for edge in edges_to_check_2):
        if vertical==True:
            diagonal=[pointA,(pointB[0]+SQUARE_SIZE,pointB[1])]
            if turn==False:
                red_squares.append(diagonal)
                red_score+=1
            else:
                blue_squares.append(diagonal)
                blue_score+=1
        else:
            diagonal=[(pointA[0],pointA[1]-SQUARE_SIZE),pointB]
            if turn==False:
                red_squares.append(diagonal)
                red_score+=1
            else:
                blue_squares.append(diagonal)
                blue_score+=1
     
        # turn= not turn # if box is deteteced , the player gets the turn again
        second_box=True
        print("second box_detetced")

    if first_box or second_box:
        turn= not turn # if box is deteteced , the player gets the turn again
    print(f"red_score: {red_score}")
    print(f"blue_score: {blue_score}")
    return


#to draw dotted lines where line can be drawn
def draw_line(mouse_pos):
    box_column=(mouse_pos[0]-offset)//SQUARE_SIZE #  +1
    box_row=(mouse_pos[1]-offset)//SQUARE_SIZE  #  +1


    #now calculate all coordinates of 4 points
    left_x=SQUARE_SIZE * box_column + offset
    right_x=SQUARE_SIZE * (box_column+1) + offset
    
    top_y= SQUARE_SIZE * box_row + offset
    bottom_y= SQUARE_SIZE * (box_row+1) + offset

    points=[[left_x,top_y],[right_x,top_y],[left_x,bottom_y],[right_x,bottom_y]]

    #draw dotted line between points where mouse_position is nearest to 
    center_x=(left_x+right_x) /2
    center_y=(top_y+bottom_y) /2

    nearest_x=left_x if ((center_x-mouse_pos[0])>0) else right_x
    nearest_y=top_y if ((center_y-mouse_pos[1])>0) else  bottom_y

    if abs(mouse_pos[1]-nearest_y)>abs(mouse_pos[0]-nearest_x):
        draw_to=nearest_x
    else:
        draw_to=nearest_y


    # if  mouse_pos[0]<offset or mouse_pos[0]>(offset+(ROWS-1)*SQUARE_SIZE):
    #     drawing_coordinates= 
    # if  mouse_pos[1]<offset or mouse_pos[1]>(offset+(COLS-1)*SQUARE_SIZE):
    #     return
    if draw_to==nearest_x:
        drawing_coordinates = [(nearest_x, top_y), (nearest_x, bottom_y)]
    else:
        drawing_coordinates = [(left_x, nearest_y), (right_x, nearest_y)]


    if turn==True:
        pygame.draw.line(WIN, (255, 200, 200), drawing_coordinates[0], drawing_coordinates[1],3)
    else:
        pygame.draw.line(WIN, (200, 200, 255), drawing_coordinates[0], drawing_coordinates[1],3)

    return drawing_coordinates


def draw_rectangle(points, color):

    x1, y1 = points[0]  # Top-left corner
    x2, y2 = points[1]  # Bottom-right corner
    # Calculate width and height from the endpoints of the diagonal
    x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    pygame.draw.rect(WIN, color, pygame.Rect(x1, y1, width, height))


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)
        # Get the current mouse position
        WIN.fill((240, 240, 240))
        mouse_pos = pygame.mouse.get_pos()

        if  mouse_pos[0]<offset or mouse_pos[0]>(offset+(ROWS-1)*SQUARE_SIZE):
            pass
        elif mouse_pos[1]<offset or mouse_pos[1]>(offset+(COLS-1)*SQUARE_SIZE):
            pass
        else:
            coordinates=draw_line(mouse_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                handle_click(coordinates)
        #draw_grid()

        for line in lines_red:
            pygame.draw.line(WIN, (255, 0, 0), line[0], line[1], 3)
        for line in lines_blue:
            pygame.draw.line(WIN, (0, 0, 255), line[0], line[1], 3)

        for diagonal in red_squares:
            draw_rectangle(diagonal,color=(255,220,220))
        #     pygame.draw.rect(WIN, (255,220,220), pygame.Rect(left, top, width, height))
        for diagonal in blue_squares:
            draw_rectangle(diagonal,color=(200,200,255))
        #     pygame.draw.rect(WIN, (220,220,255), pygame.Rect(left, top, width, height))
            
        draw_grid()

        if len(blue_squares)+len(red_squares)==total_boxes:
            # print("Game OVER")
            pass

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

