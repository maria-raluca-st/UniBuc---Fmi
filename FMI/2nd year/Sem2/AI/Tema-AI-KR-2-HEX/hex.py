import pygame as pg
from math import sin, cos, ceil, pi
from queue import Queue
from heapq import heapify, heappush, heappop
# from fibheap import *
from copy import deepcopy
from time import time
from random import randint
import os
from math import pi, cos, sin, sqrt, floor



#------------------------------CONSTANTE----------------------------


# GUI 
WIDTH, HEIGHT = 1280, 720
#WIDTH, HEIGHT = 1200, 600
BUTTON_WIDTH, BUTTON_HEIGHT = 90, 35
TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT = 100, 35

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (235, 133, 133)
GREEN = (177, 226, 180)
BLUE = (119, 182, 238)
LIGHT_BLUE = (185, 233, 233)
YELLOW = (247, 250, 161)
ORANGE = (250, 206, 161)
PINK = (246, 205, 205)
LIGHT_GRAY = (224, 224, 224)
DARK_GRAY = (192, 192, 192)
DARKER_GRAY = (96, 96, 96)
I_TO_C = {'R': RED, 'G': GREEN, 'B': BLUE, 'Y': YELLOW, 'O': ORANGE, 'P': PINK, 'LB' : LIGHT_BLUE}


# Game related data
INITIAL_RADIUS = 80
INITIAL_CENTER = (WIDTH, HEIGHT)
DEPTHS = {"Incepator": 1, "Mediu": 2, "Avansat": 3}
GAME_MODE = {0: "pvp", 1: "pvc", 2: "pvc", 3: "cvc"}

#Values
INF = float('inf')
NODES = 0
FPS = 60

show_once = 1


# Optional
TIMES_TAKEN = []
TOTAL_NODES = []
START_TIME = 0
PROGRAM_TIME = 0
MUTARI = [0, 0]


# initializare all imported pygame modules
pg.init()
pg.font.init()


BUTTON_FONT = pg.font.SysFont('homerun', 20)
TEXT_FONT = pg.font.SysFont('homerun', 40)



#-------------------------------------------UI(Butoane,Textbox)-------------------------------------

class Button:
    def __init__(self, x, y, width, height, color, text, font_color):
        '''
        Initializare buton
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.font_color = font_color
        self.selected = False
        self.rect = pg.Rect(x, y, width, height)

    def draw(self, window):
        '''
        Draw buton on surface
        '''
        # text - negru la selectie buton
        text_font = BUTTON_FONT.render(self.text, True, self.font_color if not self.selected else BLACK)
        # buton - gri la selectie
        pg.draw.rect(window, self.color if not self.selected else DARK_GRAY, self.rect)
        # blit = block transfer -> copy contents of one surface onto another surface
        window.blit(text_font, (self.x + (self.width - text_font.get_width()) // 2, self.y + self.height // 2 - text_font.get_height() // 2))

    def select_button(self, coord):
        '''
        Selectare buton
        '''
        # collidepoint -> returns true if the point is within the bounds of the rectangle 
        if self.rect.collidepoint(coord):
            self.selected = True
            return True
        return False


class ButtonGroup:
    '''
    Clasa ButtonGoup pt toate butoanele care sunt grupate
    '''
    ROW_SPACE = 15
    COL_SPACE = 15

    @classmethod
    def create_buttons(self, x, y, width, height, lista, per_row):
        res = []
        next_x, next_y = x, y
        for (i, (text, col_but, col_font)) in enumerate(lista):
            res.append(Button(next_x, next_y, width, height, col_but, text, col_font))
            if i % per_row == per_row - 1 :
                next_x, next_y = x, next_y + height + ButtonGroup.COL_SPACE
            else:
                next_x += width + ButtonGroup.ROW_SPACE
        return res

    def __init__(self, x, y, width, height, text, lista_texte, per_row=3):
        self.selected = None
        self.total_width = min( per_row, len(lista_texte)) * (width + ButtonGroup.ROW_SPACE) - ButtonGroup.ROW_SPACE
        self.total_height = ceil(len(lista_texte) / per_row) *(height + ButtonGroup.COL_SPACE) - ButtonGroup.COL_SPACE
        self.x = x - self.total_width // 2
        self.y = y
        self.text = text
        self.per_row = per_row
        self.button_list = ButtonGroup.create_buttons(self.x, self.y, width, height, lista_texte, per_row)
        self.selected_button = None

    def select_button(self, coord):
        for idx, buttton in enumerate(self.button_list):
            if buttton.select_button(coord):
                if self.selected_button is not None:
                    self.button_list[self.selected_button].selected = False
                self.selected_button = idx
                return True
        return False

    def draw(self, window, other_selected=None):
        text_font = TEXT_FONT.render(self.text, True, BLACK)
        window.blit(text_font, (self.x + self.total_width // 2 - text_font.get_width() // 2, self.y - 2 * ButtonGroup.COL_SPACE - text_font.get_height() // 2))
        for idx, button in enumerate(self.button_list):
            if idx != other_selected:
                button.draw(window)



class TextBox:
    '''
    Clasa pentru TextBox(Pt Custom dimension game) 
    '''

    def __init__(self, x, y):
        self.font = TEXT_FONT
        self.input_box = pg.Rect(x, y, 100, 35)
        self.color_inactive = BLACK
        self.color_active = LIGHT_BLUE
        self.color = BLACK
        self.text = ''
        self.active = False

    def handle_event(self, event):

        # event MOUSEBUTTONDOWN -> click
        if event.type == pg.MOUSEBUTTONDOWN:
            self.active = self.input_box.collidepoint(event.pos)
            self.color = self.color_active if self.active else self.color_inactive
        
        # event KEYDOWN -> keyboard button pressed -> se verifica corectitudinea si return dimensiune daca e ok    
        if event.type == pg.KEYDOWN:
            if self.active:
                # event K_RETURN -> enter pressed 
                if event.key == pg.K_RETURN:
                    try:
                        dim = int(self.text)
                        if 3 <= dim <= 11:
                            return dim
                        raise Exception()

                    except ValueError:
                        self.text = ''
                        print("Dimensiunea trebuie sa fie numar")
                    except Exception:
                        self.text = ''
                        print("Dimensiunea trebuie sa fie intre 3 si 11")

                # event K_BACKSPACE -> delete last character
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.font.render(self.text + event.unicode, True, BLACK).get_width() + 10 < self.input_box.width:
                        self.text += event.unicode

    def draw(self, window, text_box_width=100):
        text_input = self.font.render(self.text, True, BLACK)
        # Fix width
        self.input_box.width = text_box_width
        window.blit(text_input, (self.input_box.x + 5, self.input_box.y + 5))
        pg.draw.rect(window, self.color, self.input_box, 2)


#----------------------------------------------------------GEOMETRIC + UI- JOC----------------------------------------------------------- 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y


class Hexagon:
    # Nr de laturi/puncte
    n = 6

    @classmethod
    def compute_points(self, center, radius):     # Puncte hexagon
        return [Point(center.x + radius * sin(2 * pi * i / Hexagon.n), center.y + radius * cos(2 * pi * i / Hexagon.n)) for i in range(Hexagon.n)]

    @classmethod
    def compute_edges(self, points):              
        lines = list(zip(points, points[1:] + points[:1]))
        return [Line(line[0], line[1]) for line in lines]

    def __init__(self, center, radius):
        '''
        Initializare hexagon
        '''
        self.x = center.x
        self.y = center.y
        self.radius = radius
        self.points = Hexagon.compute_points(center, radius)
        self.edges = Hexagon.compute_edges(self.points)
        self.selected = None

    def draw_laturi(self, window, pos, border_width=5):
        '''
        Culoarea laturilor hexagoanelor (margini - culoarea corespunz. jucatorului care castiga atigand marginea respectiva , selectat- margini negre)
        '''

        # Hexagon selectat - laturi negre - pt ca a fost ales si nu poate fi reales
        if self.selected:
            pg.draw.lines(window, BLACK, True, [(p.x, p.y) for p in self.points], border_width)
            return

        # Colorare tabla -> margini - culoare player , altfel - negru
        #   
        #    STANGA SUS ->  /   \   <- DREAPTA SUS
        #    STANGA ->      |   | <- DREAPTA
        #    STANGA JOS ->  \   /  <- DREAPTA JOS
        #
        points = [(p.x, p.y) for p in self.points]
        row, col = pos
        min_color, max_color = I_TO_C[Game.MIN_PLAYER], I_TO_C[Game.MAX_PLAYER]

        # Laturile din dreapta - jucator 1 -daca e margine , altfel negru
        color = min_color if col == Game.COLS - 1 else BLACK
        pg.draw.line(window, color, points[1], points[2], border_width)

        # Latura din dreapta-sus - prima linie toate jucator 2 , mai putin ultima col - jucator 1
        color = min_color if col == Game.COLS - 1 else (max_color if row == 0 else BLACK)
        pg.draw.line(window, color, points[2], points[3], border_width)

        # Laturile din stanga-sus - jucator 1 primul rand , altfel negru
        color = max_color if row == 0 else BLACK
        pg.draw.line(window, color, points[3], points[4], border_width)

        # Latura din stanga - toate jucator 2 prima col , altfel negru
        color = min_color if col == 0 else BLACK
        pg.draw.line(window, color, points[4], points[5], border_width)

        # Latura din stanga-jos - toate jucator 2 prima coloana cu ultimul rand jucator 1
        color = min_color if col == 0 else (max_color if row == Game.ROWS - 1 else BLACK)
        pg.draw.line(window, color, points[5], points[0], border_width)

        # Latura din dreapta_jos - toate jucator 1 ultimul rand , altfel negru
        color = max_color if row == Game.ROWS - 1 else BLACK
        pg.draw.line(window, color, points[0], points[1], border_width)


    def draw(self, window, pos, color=LIGHT_GRAY):
        pg.draw.polygon(window, color, [(point.x, point.y) for point in self.points])
        self.draw_laturi(window, pos)

    def check_inside(self, point):
        """
        Verif. daca un punct este inauntru unui hexagon.
        Extindem punctul prin o semidreapra
        Numim nr de intersectari = n .
        n = par   => punctul nu e in hexagon
        n = impar => punctul e in haxagon
        """
        intersections = 0
        for line in self.edges:
            # Daca punctul e mai sus sau mai jos de orice muchie a hexagonului , e clar ca nu e in el
            if not (min(line.y1, line.y2) <= point.y <= max(line.y1, line.y2)):
                continue
            # Daca muchia este verticala , verif punct inainte de latura
            if line.x1 == line.x2:
                if point.x <= line.x1:
                    intersections += 1
                continue
            
            # ecuatia muchiei
            m = (line.y2 - line.y1) / (line.x2 - line.x1)  # panta
            n = line.y1 - m * line.x1

            # Calculam x-ul punctului corespunzator lui punct.y pe linie.
            x_line = (point.y - n) / m
            if point.x <= x_line:
                intersections += 1
        return intersections % 2 == 1


class HexGame:
    """
    Clasa pt joc  - contine hexagoanele 
    """

    def __init__(self, game, hexagons):
        '''
        Initializarea jocului
        '''
        self.game = game
        self.hexagons = hexagons

    def new_hexagon(self):
        for i in range(Game.ROWS):
            for j in range(Game.COLS):
                if self.game.game_state[i][j] != Game.EMPTY and self.game.game_state[i][j] != self.hexagons[i][j].selected:
                    return i, j

    def select_hexagon(self, selected, player):
        i, j = selected
        if self.hexagons[i][j].selected is None:
            self.hexagons[i][j].selected = player
            return True
        return False

    def draw(self, window, hovered, path=[]):
        for i in range(Game.ROWS):
            for j in range(Game.COLS):
                if self.hexagons[i][j].selected != None:
                    # se deseaneaza hexagonul selectat cu culoarea jucatorului care l-a selectat
                    self.hexagons[i][j].draw(window, (i, j), I_TO_C[self.hexagons[i][j].selected])
                    if (i, j) in path:
                        # se marcheaza pathul castigator
                        pg.draw.circle(window, BLACK, (self.hexagons[i][j].x, self.hexagons[i][j].y), self.hexagons[i][j].radius - 30)
                elif hovered != None and i == hovered[0] and j == hovered[1]:
                    self.hexagons[i][j].draw(window, (i, j), hovered[2])
                else:
                    self.hexagons[i][j].draw(window, (i, j))



# ALGORITHM COMPONENTS
class Game:
    """
    Clasa pt tabla jocului curent
    """
    ROWS = None
    COLS = None
    MIN_PLAYER = None
    MAX_PLAYER = None
    EMPTY = '#'

    @classmethod
    def initialize_game(self, rows, cols, min_player, max_player):
        Game.ROWS = rows
        Game.COLS = cols
        Game.MIN_PLAYER = min_player
        Game.MAX_PLAYER = max_player


    def __init__(self, game_state):
        self.game_state = game_state

    
    def console_show(self):
        '''
          Starea curenta a jocului in consola
        '''
        #4.
        space = 0
        for i in range(Game.ROWS):
            print(" " * space, end="")
            for j in range(Game.COLS):
                print(self.game_state[i][j], end=" ")
            space += 1
            print()

    def is_valid(self, i, j):
        '''
        verif. daca e valida pozitia sau nu
        '''
        return (0 <= i < Game.ROWS and 0 <= j < Game.COLS)

    # 7. stare finala verificare
    def final(self):
        '''
        Verificare daca am ajuns in stare finala(BFS)
        '''

        q = Queue()

        # Directie
        dx = [0, 0, -1, 1, -1, 1]
        dy = [-1, 1, 0, 0, 1, -1]

        # verificarea pt jucator 1 - daca ajunge de pe prima coloana pe ultima

        marked = [[False] * Game.COLS for _ in range(Game.ROWS)]
        for i in range(Game.ROWS):
            if self.game_state[i][0] == Game.MIN_PLAYER:
                q.put((i, 0))
                marked[i][0] = True
        while not q.empty():
            i, j = q.get()

            # Daca am ajuns pe partea dreapta a tablei:
            if j == Game.COLS - 1:
                return Game.MIN_PLAYER

            for k in range(6):
                if self.is_valid(i + dx[k], j + dy[k]) and self.game_state[i + dx[k]][j + dy[k]] == Game.MIN_PLAYER and not marked[i + dx[k]][j + dy[k]]:
                    q.put((i + dx[k], j + dy[k]))
                    marked[i + dx[k]][j + dy[k]] = True

        # verificarea pt jucator 2 - daca ajunge de pe primul rand pe ultimul

        marked = [[False] * Game.COLS for _ in range(Game.ROWS)]
        for i in range(Game.COLS):
            if self.game_state[0][i] == Game.MAX_PLAYER:
                q.put((0, i))
                marked[0][i] = True
        while not q.empty():
            i, j = q.get()

            # Daca am ajuns jos in tabla:
            if i == Game.ROWS - 1:
                return Game.MAX_PLAYER

            for k in range(6):
                if self.is_valid(i + dx[k], j + dy[k]) and self.game_state[i + dx[k]][j + dy[k]] == Game.MAX_PLAYER and not marked[i + dx[k]][j + dy[k]]:
                    q.put((i + dx[k], j + dy[k]))
                    marked[i + dx[k]][j + dy[k]] = True

        # return false -> starea nu e finala (nu se face verif. pt remiza pt ca nu putem avea remiza)
        return False

    def final_path(self, player):
        path = []
        parent = [[None] * Game.COLS for _ in range(Game.ROWS)]
        q = Queue()

        dx = [0, 0, -1, 1, -1, 1]
        dy = [-1, 1, 0, 0, 1, -1]

        if player == Game.MIN_PLAYER:
            for i in range(Game.ROWS):
                if self.game_state[i][0] == Game.MIN_PLAYER:
                    q.put((i, 0))
                    parent[i][0] = -1
        else:
            for i in range(Game.COLS):
                if self.game_state[0][i] == Game.MAX_PLAYER:
                    q.put((0, i))
                    parent[0][i] = -1

        while not q.empty():
            i, j = q.get()

            # Daca MIN a ajuns in dreapta / MAX jos(stare finala)
            if (j == Game.COLS - 1 and player == Game.MIN_PLAYER) or (i == Game.ROWS - 1 and player == Game.MAX_PLAYER):
                path.append((i, j))
                break

            for k in range(6):
                if self.is_valid(i + dx[k], j + dy[k]) and self.game_state[i + dx[k]][j + dy[k]] == player and not parent[i + dx[k]][j + dy[k]]:
                    q.put((i + dx[k], j + dy[k]))
                    parent[i + dx[k]][j + dy[k]] = (i, j)

        cur_pos = path[0]
        while parent[cur_pos[0]][cur_pos[1]] != -1:
            cur_pos = parent[cur_pos[0]][cur_pos[1]]
            path.append(cur_pos)

        return path

    def select_position(self, pos, player):
        i, j = pos
        if self.game_state[i][j] == Game.EMPTY:
            self.game_state[i][j] = player

    def next_hexagons(self, pos):
        '''
        Hexagoanele din jurul unui hexagon
        '''
        i, j = pos
        dx = [0, 0, -1, 1, -1, 1]
        dy = [-1, 1, 0, 0, 1, -1]

        next_to = []
        for k in range(6):
            if self.is_valid(i + dx[k], j + dy[k]):
                next_to.append((i + dx[k], j + dy[k]))
        return next_to

    def bridges(self, pos):
        '''
        Puntile de pe tabla
        '''
        i, j = pos

        # Locurile unde sunt puntile potentiale
        dx = [-1, 1, 2, 1, -1, -2]
        dy = [-1, -2, -1, 1, 2, 1]

        # Locurile dintre ele
        bdx = [-1, 0, 1, 1, 0, -1]
        bdy = [0, -1, -1, 0, 1, 1]

        bridges = []
        # Between bridge
        b_bridge = []
        for k in range(6):
            if self.is_valid(i + dx[k], j + dy[k]):
                bridges.append((i + dx[k], j + dy[k]))
                b_bridge.append([(i + bdx[k], j + bdy[k]), (i + bdx[(k + 1) % 6], j + bdy[(k + 1) % 6])])
        return bridges, b_bridge


    def bridges_with_edge(self, pos):
        '''
        Determina puntile dintre latura si celula curenta
        '''
        i, j = pos

        bridge_to_edges = []

        if self.game_state[i][j] == Game.MIN_PLAYER:
            if j == 1:
                bridge_to_edges = [(i, 0), (min(Game.ROWS - 1, i + 1), 0)]

            elif j == Game.COLS - 2:
                bridge_to_edges = [(i, j + 1), (max(0, i - 1), j + 1)]


        elif self.game_state[i][j] == Game.MAX_PLAYER:
            if i == 1:
                bridge_to_edges = [(0, j), (0, min(Game.COLS - 1, j + 1))]

            elif i == Game.ROWS - 2:
                bridge_to_edges = [(i + 1, j), (i + 1, max(0, j - 1))]

        return bridge_to_edges

    #5.Functia de generare a muatrilor
    def mutari(self, player):
        '''
        Toate mutarile posibile din stare    
        '''
        lista_mutari = []
        for i in range(Game.ROWS):
            for j in range(Game.COLS):
                if self.game_state[i][j] == '#':
                    # Daca pozitia e goala , se poate alege hexagonul repsectiv
                    new_game = Game(deepcopy(self.game_state))
                    new_game.select_position((i, j), player)
                    lista_mutari.append(new_game)
        return lista_mutari


    def mutari_logice(self, player):
        '''
        Toate mutarile logice care ne intereseaza - aproape de hexagoanele alese de jucatorul curent/celalalt jucator/punti
        Returns : lista mutari cu toate mutarile convenabile
        '''

        lista_mutari = []
        marked = [[False] * Game.COLS for _ in range(Game.ROWS)]

        for i in range(Game.ROWS):
            for j in range(Game.COLS):
                if self.game_state[i][j] != Game.EMPTY:
                    if marked[i][j]:
                        continue

                    next_nodes = self.next_hexagons((i, j))
                    bridges, intre = self.bridges((i, j))
                    edges = self.bridges_with_edge((i, j))
                    next_nodes.extend(bridges)
                    next_nodes.extend(edges)
                    for x, y in next_nodes:
                        if not marked[x][y] and self.game_state[x][y] == Game.EMPTY:
                            marked[x][y] = True
                            new_game = Game(deepcopy(self.game_state))
                            new_game.select_position((x, y), player)
                            lista_mutari.append(new_game)
        return lista_mutari

    def oponent(self, player):
        return Game.MAX_PLAYER if player == Game.MIN_PLAYER else Game.MIN_PLAYER


    
    def euristica_1(self, player, turn):
        '''
        Prima euristica
        '''

        marked = [[False] * Game.COLS for _ in range(Game.ROWS)]
        next_to_score = 0
        opponent_score = 0
        block_score = 0
        bridge_score = 0
        destroy_bridge_score = 0
        connect_bridge = 0
        edge_score = 0   
        destroy_edge_score = 0
        connect_edge = 0

        for i in range(Game.ROWS):
            for j in range(Game.COLS):
                if self.game_state[i][j] == player:
                    marked[i][j] = True
                    # Verifica langa
                    for x, y in self.next_hexagons((i, j)):
                        if self.game_state[x][y] == player:
                            next_to_score += 1
                        elif self.game_state[x][y] == self.oponent(player):
                            opponent_score += 1

                    if next_to_score > 3:
                        next_to_score = -4 if next_to_score == 4 else (-8 if next_to_score == 5 else -11)

                    # Verificare daca e blocant MAX_PLAYER pt opnonent
                    if player == Game.MAX_PLAYER and ((j == 0 and (self.game_state[i][1] == self.oponent(player) or self.game_state[max(0, i - 1)][1] == self.oponent(player))) or (j == Game.COLS - 1 and (self.game_state[i][j - 1] == self.oponent(player) or self.game_state[min(Game.ROWS - 1, i + 1)][j - 1] == self.oponent(player)))):
                        block_score += 1
                    

                    # Gasim puntile
                    bridges, intre_bridges = self.bridges((i, j))

                    for idx, pos in enumerate(bridges):
                        bi, bj = pos

                        if marked[bi][bj]:
                            continue

                        intre = intre_bridges[idx]

                        # oponent e pe bridge
                        if self.game_state[bi][bj] == self.oponent(player):
                            destroy_bridge_score += 1
                        
                        # player e pe bridge
                        elif self.game_state[bi][bj] == self.game_state[i][j]:
                            pos1, pos2 = intre
                            hex_intre = [self.game_state[pos1[0]][pos1[1]], self.game_state[pos2[0]][pos2[1]]]

                            # sau in hex intre
                            if hex_intre == [Game.EMPTY, Game.EMPTY]:
                                bridge_score = min(bridge_score + 1, 5)

                            elif sorted(hex_intre) == sorted([player, self.oponent(player)]):
                                connect_bridge = min(connect_bridge + 1, 5)

                    # Verificare langa edge
                    edges = self.bridges_with_edge((i, j))
                    if edges != []:
                        pos1, pos2 = edges
                        hex_edge = [self.game_state[pos1[0]][pos1[1]], self.game_state[pos2[0]][pos2[1]]]

                        if sorted(hex_edge) == sorted([player, self.oponent(player)]):
                            connect_edge = min(3, connect_edge + 1)

                        elif hex_edge == [self.oponent(player), self.oponent(player)]:
                            destroy_edge_score -= 1
                        elif edges == [Game.EMPTY, Game.EMPTY] or player in edges:
                            edge_score = min(edge_score + 1, 3)
        
        return ((1 if turn == player else 0) + 50 * block_score + 15 * opponent_score + 10 * next_to_score + 10 * connect_bridge + 10 * destroy_bridge_score + 7 * connect_edge + 5 * bridge_score + 5 * destroy_edge_score + 3 * edge_score)

    def euristica_2(self, player, turn):

        scor_eur1 = self.euristica_1(player, turn)

        marked = [[None] * Game.COLS for _ in range(Game.ROWS)]
        de_examinat = []

        # gasim nodurile disjuncte si gasim din ce noduri calc distantele
        for i in range(Game.ROWS):
            for j in range(Game.COLS):
                if self.game_state[i][j] == player and not marked[i][j]:
                    de_examinat.append((i, j))
                    q = Queue()
                    q.put((i, j))
                    marked[i][j] = True
                    while not q.empty():
                        pos = q.get()

                        vecini = self.next_hexagons(pos)
                        for x, y in vecini:
                            if self.game_state[x][y] == player and not marked[x][y]:
                                marked[x][y] = True
                                q.put((x, y))


        # shortest path din fiecare clasa de hexagoane
        goal = INF
        for hex in de_examinat:

            heap = []
            heappush(heap, (0, hex))
            distance = [[INF] * Game.COLS for _ in range(Game.ROWS)]
            distance[hex[0]][hex[1]] = 0

            while len(heap) > 0:
                dist, pos = heappop(heap)
                i, j = pos
                if distance[i][j] < dist:
                    continue
                for x, y in self.next_hexagons(pos):
                    if self.game_state[x][y] == Game.EMPTY and distance[x][y] > distance[i][j] + 1:
                        distance[x][y] = distance[i][j] + 1
                        heappush(heap, (distance[x][y], (x, y)))
                    elif self.game_state[x][y] == player and distance[x][y] > distance[i][j]:
                        distance[x][y] = distance[i][j]
                        heappush(heap, (distance[x][y], (x, y)))

            # Verificam dist minime pe sides:
            min_1, min_2 = INF, INF

            if player == Game.MAX_PLAYER:
                for i in range(Game.COLS):
                    min_1 = min(min_1, distance[0][i])
                    min_2 = min(min_2, distance[Game.ROWS - 1][i])
            else:
                for i in range(Game.ROWS):
                    min_1 = min(min_1, distance[i][0])
                    min_2 = min(min_2, distance[i][Game.COLS - 1])
            
            goal = min(goal, min_1 + min_2)

        return 10 * scor_eur1 + 50 * (10 - goal) 

    def estimeaza_scor(self, depth, final_state, player_turn, heuristic=1):

        if final_state == Game.MIN_PLAYER:
            return -500000 - depth
        elif final_state == Game.MAX_PLAYER:
            return 500000 + depth

    
        if heuristic == 1:
            return self.euristica_1(Game.MAX_PLAYER, player_turn) - self.euristica_1(Game.MIN_PLAYER, player_turn)

        return self.euristica_2(Game.MAX_PLAYER, player_turn) - self.euristica_2(Game.MIN_PLAYER, player_turn)


class State:
    """
    Clasa pt. Minimax si ALfa-Beta
    """

    def __init__(self, game, current_player, depth, parinte=None, scor=None):

        self.game = game
        self.current_player = current_player

        # Adancime in arborele de stari
        self.depth = depth

        # Scor stare (daca e finala) sau pt cea mai buna stare-urm. (pt jucator curent)
        self.scor = scor

        # Lista mutari posibile din starea curenta
        self.mutari_posibile = []

        # Cea mai buna mutare din lista de mutari posibile pt jucatorul curent
        self.next_state = None


    def jucator_opus(self):
        if self.current_player == Game.MIN_PLAYER:
            return Game.MAX_PLAYER
        else:
            return Game.MIN_PLAYER

    def mutari(self):
        l_mutari = self.game.mutari_logice(self.current_player)
        juc_opus = self.jucator_opus()
        l_stari_mutari = [State(mutare, juc_opus, self.depth - 1, parinte=self) for mutare in l_mutari]

        return l_stari_mutari


    def __str__(self):
        sir = str(self.next_state) + "(Joc curent:" + self.current_player + ")\n"
        return sir

#------------------------------------ALGORITMII--------------------------------------
    
NODES_A = 0    

def min_max(stare: State, heuristic: int):
    global NODES_A
    NODES_A += 1
   
    if stare.depth == 0 or stare.game.final():
        stare.scor = stare.game.estimeaza_scor(stare.depth, stare.game.final(), stare.current_player, heuristic)
        return stare

    # toate mutarile posibile din starea curenta
    stare.mutari_posibile = stare.mutari()

    # minimax pe toate mutarile posibile 
    mutari_scor = [min_max(x, heuristic) for x in stare.mutari_posibile] 

    if stare.current_player == Game.MAX_PLAYER:
        # JMAX -> starea urm = cea cu scorul maxim
        stare.next_state = max(mutari_scor, key=lambda x: x.scor)
    else:
        # JMIN -> starea urm = cea cu scorul minim
        stare.next_state = min(mutari_scor, key=lambda x: x.scor)

    stare.scor = stare.next_state.scor
    return stare


def alpha_beta(alpha: int, beta: int, stare: State, heuristic: int):
    global NODES_A
    NODES_A += 1

   
    if stare.depth == 0 or stare.game.final():
        stare.scor = stare.game.estimeaza_scor( stare.depth, stare.game.final(), stare.current_player, heuristic)
        return stare

    if alpha > beta:
        return stare  # Este intr-un interval invalid deci nu o mai procesez

    stare.mutari_posibile = stare.mutari()

    if stare.current_player == Game.MAX_PLAYER:
        scor_curent = float('-inf')
        for mutare in stare.mutari_posibile:
            # Calculeaza scorul
            # Aici construim subarborele pentru stare_noua
            stare_noua = alpha_beta(alpha, beta, mutare, heuristic)

            if (scor_curent < stare_noua.scor):
                stare.next_state = stare_noua
                scor_curent = stare_noua.scor
            if (alpha < stare_noua.scor):
                alpha = stare_noua.scor
                if alpha >= beta:
                    break
    elif stare.current_player == Game.MIN_PLAYER:
        scor_curent = float('inf')
        for mutare in stare.mutari_posibile:
            # Calculeaza scorul
            # Aici construim subarborele pentru stare_noua
            stare_noua = alpha_beta(alpha, beta, mutare, heuristic)

            if (scor_curent > stare_noua.scor):
                stare.next_state = stare_noua
                scor_curent = stare_noua.scor
            if (beta > stare_noua.scor):
                beta = stare_noua.scor
                if alpha >= beta:
                    break

    stare.scor = stare.next_state.scor
    return stare


#create new user event cu ID 25
EXIT_AND_STATS = pg.USEREVENT + 1
EXIT_BUTTON = Button(WIDTH - 105, 15, 90, 35, RED, "EXIT", WHITE)

#new user event for restart game - ID 26
RESTART_GAME = pg.USEREVENT + 2
RESTART_BUTTON = Button(WIDTH - 105, 200, 90, 35, GREEN, "RESTART", WHITE)



#---------------------------------UTILITY(functii)-------------------------------------------


def create_hexagons(n, m, INITIAL_POINT):
    HEXAGONS = [[] for _ in range(n)]
    GAME_STATE = [[] for _ in range(n)]
    RADIUS = INITIAL_RADIUS - 4 * max(n, m)
    HEX_HEIGHT = floor(RADIUS * sqrt(3) / 2)
    grid_width = ((n - 1) + 2 * (m - 1)) * HEX_HEIGHT
    grid_height = (n - 1) * 3 * RADIUS // 2

    cur_x, cur_y = INITIAL_POINT[0] // 2 - grid_width // 2, INITIAL_POINT[1] // 2 - grid_height // 2
    HEXAGONS = [[] for _ in range(n)]
    
    for i in range(n):
        if i > 0:
            cur_x = HEXAGONS[i - 1][0].x + HEX_HEIGHT

        for j in range(m):
            HEXAGONS[i].append(Hexagon(Point(cur_x, cur_y), RADIUS))
            GAME_STATE[i].append(Game.EMPTY)
            cur_x += 2 * HEX_HEIGHT
        cur_y += 3 * RADIUS / 2
    return HEXAGONS, GAME_STATE


def get_player_name(game_mode, turn, minplayer, maxplayer):
    '''
    Returns player name for each type of game
    '''
    if game_mode == "pvp":
        return "Player 1" if turn == minplayer else "Player 2"
    elif game_mode == "pvc":
        return "Player" if turn == minplayer else "Computer"
    elif game_mode == "cvc": 
        return "Computer 1" if turn == minplayer else "Computer 2"


def show_computer_stats(name, time, nodes, score):
    print( f"{name}'s Stats:\nTime taken: {round(time, 3)} sec\nNoduri calculate: {nodes}\nEstimarea avantajului pentru {name}: {score}\n")


def show_user_stats(name, time):
    print(f"{name}'s Stats:\nTime taken: {round(time, 3)}\n")


def show_stats(game_mode, prog_time, times, nodes, moves):
    global show_once
    if not show_once:
        return
    show_once -= 1

    print(f"Statistica jocului:\nRegimul jocului: " + "Player vs Player" if game_mode == "pvp" else ("Player vs Computer" if game_mode == "pvc" else "Computer vs Computer"))
    
    if times != []:
        print(f"Timpul total de rulare a programului: {round(prog_time, 3)}")
        print(
            f"Timpul maxim de gandire al calculatorului: {round(max(times), 3)}\nTimpul minim de gandire al calculatorului: {round(min(times), 3)}")
        print(
            f"Timpul mediu de gandire: {round(mean(times), 3)}\nMediana timpului: {round(median(times), 3)}")
    
    if nodes != []:
        print(f"Numarul de noduri generate: {sum(nodes)}")
        print(f"Numarul maxim de noduri generate: {max(nodes)}\nNumarul minim de noduri generate: {min(nodes)}")
        print(f"Numarul mediu de noduri: {round(mean(nodes))}\nMediana numarului de noduri: {round(median(nodes))}")
    
    players = ["Player 1" if game_mode == "pvp" else("Player" if game_mode != "cvc" else "Computer 1"), "Player 2" if game_mode == "pvp" else( "Computer" if game_mode != "cvc" else "Computer 2")]
    print(f"Numarul de mutari al {players[0]}: {moves[0]}\nNumarul de mutari al {players[1]}: {moves[1]}")


def mean(array):
    return sum(array) / len(array)


def median(array):
    if len(array) % 2 == 1:
        return array[len(array) // 2]
    return (array[len(array) // 2] + array[(len(array) + 1) // 2]) / 2
    

#--------------------------------------GUI--------------------------------------------



WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Stanescu Raluca, Hex Game")
BACKGROUND = pg.transform.scale(pg.image.load(os.path.join('assets', '4.jpg')), (WIDTH, HEIGHT))
TITLE_FONT = pg.font.SysFont('homerun', 90)
WIN_FONT = pg.font.SysFont('homerun', 60)
NORMAL_FONT = pg.font.SysFont('homerun', 40)
SMALL_FONT = pg.font.SysFont('homerun', 30)


# DATELE JOCULUI
SIZE = [None, None]
NEXT_MENU = False
GAME = None
PLAYER_TURN = None
PLAY_GAME = False
WINNER = None


def update_game_window(hovered, mouse_click, game_mode):
    global PLAYER_TURN
    WIN.blit(BACKGROUND, (0, 0))

    GAME.draw(WIN, hovered)

    # Player 1/2/Computer turn: -1.4
    player_name = get_player_name(game_mode, PLAYER_TURN, Game.MIN_PLAYER, Game.MAX_PLAYER)
    next_move_text = NORMAL_FONT.render(player_name + " Turn", True, BLACK)
    WIN.blit(next_move_text, (900, HEIGHT - next_move_text.get_height() - 600))
    

    # Exit button:
    EXIT_BUTTON.draw(WIN)
    if mouse_click != None and EXIT_BUTTON.select_button(mouse_click):
        pg.event.post(pg.event.Event(EXIT_AND_STATS))
    
    #RESTART Button:  -- testare cu  funtia de exit -- merge
    RESTART_BUTTON.draw(WIN)
    if mouse_click != None and RESTART_BUTTON.select_button(mouse_click):
        pg.event.post(pg.event.Event(RESTART_GAME))

    pg.display.update()


def update_final_window(winner, mouse_click, game_mode):

    WIN.blit(BACKGROUND, (0, 0))

    path = GAME.game.final_path(winner)
    GAME.draw(WIN, None, path)

    # Winner name
    player_name = get_player_name(game_mode, winner, Game.MIN_PLAYER, Game.MAX_PLAYER).upper()

    # 1.5 . Castigaotrul
    next_move_text = WIN_FONT.render(player_name + " WINS", True, BLACK)
    WIN.blit(next_move_text, (840, HEIGHT - next_move_text.get_height() - 600))

    # Exit button:
    EXIT_BUTTON.draw(WIN)
    if mouse_click != None and EXIT_BUTTON.select_button(mouse_click):
        pg.event.post(pg.event.Event(EXIT_AND_STATS))
    
    #RESTART Button: 
    RESTART_BUTTON.draw(WIN)
    if mouse_click != None and RESTART_BUTTON.select_button(mouse_click):
        pg.event.post(pg.event.Event(RESTART_GAME))

    pg.display.update()




def update_first_menu_window(size_buttons, size_text_boxes, mode_buttons, next_button, mouse_click):
    global SIZE, NEXT_MENU

    WIN.blit(BACKGROUND, (0, 0))
    
    title_text = TITLE_FONT.render("THE GAME OF HEX", True, BLACK)
    WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 70))

    if mouse_click != None:
        size_buttons.select_button(mouse_click)
        mode_buttons.select_button(mouse_click)

    size_buttons.draw(WIN)
    mode_buttons.draw(WIN)

    if size_buttons.selected_button != None:
        dim = size_buttons.selected_button + 3
        SIZE = [dim, dim] if dim < 12 else SIZE

    # Bool ca sa stim ca avem custom dim
    CUSTOM_SIZE_SEL = size_buttons.selected_button == len(size_buttons.button_list) - 1
    
    if CUSTOM_SIZE_SEL:
        for sztb in size_text_boxes:
            sztb.draw(WIN)
        aux_text = NORMAL_FONT.render("x", True, BLACK)
        WIN.blit(aux_text, (WIDTH // 2 - aux_text.get_width() // 2, 305))
        help_text = SMALL_FONT.render("Dimensiunile tablei pot varia intre 3 si 11 pentru randuri si coloane.", True, BLACK)
        WIN.blit(help_text, (WIDTH // 2 - help_text.get_width() // 2, 345))
        

    # Verificare daca corespund size-urile cu cele din textbox-uri
    GOOD_CUSTOM = CUSTOM_SIZE_SEL and ([str(SIZE[0]), str(SIZE[1])] == [size_text_boxes[0].text, size_text_boxes[1].text])
    if None not in SIZE and (CUSTOM_SIZE_SEL == GOOD_CUSTOM) and size_buttons.selected_button != None and mode_buttons.selected_button != None:
        next_button.draw(WIN)
        if mouse_click != None and next_button.select_button(mouse_click):
            NEXT_MENU = True
    pg.display.update()


def update_second_menu_window(algorithm_buttons, difficulty_buttons, game_mode, player1_buttons, player2_buttons, next_button, mouse_click):
    global PLAY_GAME
    WIN.blit(BACKGROUND, (0, 0))
    title_text = TITLE_FONT.render("THE GAME OF HEX", True, BLACK)
    WIN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 70))

    if mouse_click != None:
        # pvp -> nu mai avem algoritm + dificultate
        if game_mode != "pvp":
            algorithm_buttons.select_button(mouse_click)
            difficulty_buttons.select_button(mouse_click)      
        
        player1_buttons.select_button(mouse_click)
        player2_buttons.select_button(mouse_click)
          

    if game_mode != "pvp":
        algorithm_buttons.draw(WIN)
        difficulty_buttons.draw(WIN)

    nu_afisa = player2_buttons.selected_button
    player1_buttons.draw(WIN, nu_afisa)
    nu_afisa = player1_buttons.selected_button
    player2_buttons.draw(WIN, nu_afisa)

    # daca s au apasat toate butoanele , se afiseaza butonul de next
    if ((game_mode != "pvp" and algorithm_buttons.selected_button != None and difficulty_buttons.selected_button != None) or game_mode == "pvp") and player1_buttons.selected_button != None and player2_buttons.selected_button != None:
        next_button.draw(WIN)
        if mouse_click != None and next_button.select_button(mouse_click):
            PLAY_GAME = True
    pg.display.update()


def menu_gui():
    global GAME, PLAY_GAME, NEXT_MENU
    run = True
    mouse_click = None

    # PRIMUL MENIU DE SELECTII
    # Pt alegerea dimensiuniii - grup de butoane de la 3 la 11 + dimensiune custom
    size_buttons = ButtonGroup( WIDTH // 2, 200, BUTTON_WIDTH, BUTTON_HEIGHT, "Selectati dimensiunea tablei", [(f"{i}x{i}", BLACK, WHITE) for i in range(3, 12)] + [("Custom", BLACK, WHITE)], 5)
    size_text_boxes = [TextBox(WIDTH // 2 - TEXT_BOX_WIDTH - 15, 300), TextBox(WIDTH // 2 + 15, 300)]
    
    #Tip joc
    mode_buttons = ButtonGroup(WIDTH // 2, 460, 180, BUTTON_HEIGHT, "Selectati tipul de joc", [("Player vs Player", RED, WHITE), ( "Player vs Computer (Easy)", ORANGE, BLACK), ("Player vs Computer (Hard)", YELLOW, BLACK), ("Computer vs Computer", BLUE, WHITE)], 4)
    
    #Buton NEXT window
    next_button = Button(WIDTH // 2 - BUTTON_WIDTH // 2, 650, BUTTON_WIDTH,BUTTON_HEIGHT, BLACK, "NEXT", WHITE)
    
    clock = pg.time.Clock()
    while run:
        clock.tick(FPS)
        if NEXT_MENU:
            run = False
            break
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_click = pg.mouse.get_pos()

            for idx, sztb in enumerate(size_text_boxes):
                val = sztb.handle_event(event)
                if val != None:
                    SIZE[idx] = val
        update_first_menu_window(size_buttons, size_text_boxes, mode_buttons, next_button, mouse_click)
        mouse_click = None

    if NEXT_MENU:
        game_mode = GAME_MODE[mode_buttons.selected_button]
        heuristic = 1 if mode_buttons.selected_button == 1 else (2 if mode_buttons.selected_button == 2 else None)
        n, m = SIZE
    else:
        pg.quit()
        return

    # AL DOILEA MENIU DE SELECTII
    run = True
    algorithm_buttons = ButtonGroup(WIDTH // 2, 220, BUTTON_WIDTH, BUTTON_HEIGHT, "Selectati algoritmul", [("Minimax", BLUE, WHITE), ("Alpha-Beta", RED, WHITE)])
    #2. dificultate
    difficulty_buttons = ButtonGroup(WIDTH // 2, 360, BUTTON_WIDTH, BUTTON_HEIGHT, "Selectati dificultatea", [("Incepator", RED, WHITE), ("Mediu", YELLOW, BLACK), ("Avansat", BLUE, WHITE)])
    #1.2- simbolurile cu care se joaca
    player1_buttons = ButtonGroup(WIDTH // 3, 500 if game_mode != "pvp" else 350, BUTTON_WIDTH, BUTTON_HEIGHT, "Player 1" if game_mode == "pvp" else("Player" if game_mode != "cvc" else "Computer 1"), [("BLUE", BLUE, WHITE),( "GREEN",GREEN, WHITE), ( "RED",RED, WHITE)])
    player2_buttons = ButtonGroup(2 * WIDTH // 3, 500 if game_mode != "pvp" else 350, BUTTON_WIDTH, BUTTON_HEIGHT, "Player 2" if game_mode == "pvp" else ("Computer" if game_mode == "pvc" else "Computer 2"), [("BLUE", BLUE, WHITE),( "GREEN",GREEN, WHITE), ( "RED",RED, WHITE)])
    next_button = Button(WIDTH // 2 - BUTTON_WIDTH // 2, 650, BUTTON_WIDTH, BUTTON_HEIGHT, BLACK, "PLAY", WHITE)
    
    clock = pg.time.Clock()
    while run:
        clock.tick(FPS)
        if PLAY_GAME:
            run = False
            break
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                # get mouse cursor position
                mouse_click = pg.mouse.get_pos()
        update_second_menu_window(algorithm_buttons, difficulty_buttons, game_mode, player1_buttons,player2_buttons, next_button, mouse_click)
        mouse_click = None
    if PLAY_GAME:
        selected_algo, difficulty = None, None
        if game_mode != "pvp":
            #1.ce algoritm se foloseste
            selected_algo = "minimax" if algorithm_buttons.selected_button == 0 else "alphabeta"
            difficulty = difficulty_buttons.button_list[difficulty_buttons.selected_button].text
        
        # Initiala culorii jucatorului 1
        min_player = player1_buttons.button_list[player1_buttons.selected_button].text[0]
        # Initiala culorii jucatorului 2
        max_player = player2_buttons.button_list[player2_buttons.selected_button].text[0]
        game_gui(n, m, min_player, max_player, game_mode, heuristic, selected_algo, difficulty)
    else:
        pg.QUIT


def game_gui(n, m, min_player, max_player, game_mode, heuristic, algo, difficulty):
    # 3.aici se genereaza starea initiala
    global GAME, PLAYER_TURN, WINNER, START_TIME, PROGRAM_TIME, MUTARI, TIMES_TAKEN, TOTAL_NODES,NODES_A
    run = True
    mouse_click = None
    mouse_hover = None
    selected = None
    hovered = None
    if game_mode != "pvp":
        depth = DEPTHS[difficulty]
    clock = pg.time.Clock()

    HEXAGONS, GAME_STATE = create_hexagons(n, m, INITIAL_CENTER)
    Game.initialize_game(n, m, min_player, max_player)
    GAME = HexGame(Game(GAME_STATE), HEXAGONS)
    PLAYER_TURN = Game.MIN_PLAYER
    GAME.game.console_show()
    PROGRAM_TIME = time()
    START_TIME = time()
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
            if event.type == EXIT_AND_STATS:
                show_stats(game_mode, time() - START_TIME,TIMES_TAKEN, TOTAL_NODES, MUTARI)
                run = False
                break
            if event.type == RESTART_GAME:
                TIMES_TAKEN = []
                TOTAL_NODES = []
                MUTARI = [0, 0]

                PROGRAM_TIME = time()
                START_TIME = time()

                game_gui(n, m, min_player, max_player, game_mode, heuristic, algo, difficulty)

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_click = pg.mouse.get_pos()
            if event.type == pg.MOUSEMOTION:
                mouse_hover = pg.mouse.get_pos()

        # PLAYER VERSUS COMPUTER
        if game_mode == "pvc" and not WINNER and run:
            if PLAYER_TURN == Game.MIN_PLAYER:
                is_hover = False
                for i in range(Game.ROWS):
                    for j in range(Game.COLS):
                        # selectia hexagonului
                        if mouse_click != None and GAME.hexagons[i][j].check_inside(Point(mouse_click[0], mouse_click[1])):
                            selected = i, j, RED
                        # hover pe hexagon - arata unde e pozitie valida
                        elif mouse_hover != None and GAME.hexagons[i][j].check_inside(Point(mouse_hover[0], mouse_hover[1])):
                            hovered = i, j, DARK_GRAY
                            is_hover = True
                if not is_hover or (selected != None and hovered != None and selected[:2] == hovered[:2]):
                    hovered = None

                # Selectam, daca a fost ales un hexagon de catre utilizator
                if selected != None:
                    i, j = selected[:2]
                    if GAME.select_hexagon((i, j), PLAYER_TURN):
                        GAME.game.select_position((i, j), PLAYER_TURN)
                        print("Good choice")
                        GAME.game.console_show()
                        show_user_stats("Player", time() - START_TIME)
                        MUTARI[0] += 1
                        PLAYER_TURN = Game.MIN_PLAYER if PLAYER_TURN == Game.MAX_PLAYER else Game.MAX_PLAYER
                    else:
                        print("Already selected")
            else:
                START_TIME = time()
                if algo == "minimax":
                    next_table = min_max(State(deepcopy(GAME.game), Game.MAX_PLAYER, depth), heuristic)
                else:
                    next_table = alpha_beta(-INF, INF,State(deepcopy(GAME.game), Game.MAX_PLAYER, depth), heuristic)
                time_taken = time() - START_TIME
                GAME.game = next_table.next_state.game

               
                GAME.select_hexagon(GAME.new_hexagon(), PLAYER_TURN)
                print("Computer has played move:")
                GAME.game.console_show()

                TOTAL_NODES.append(NODES_A)
                TIMES_TAKEN.append(time_taken)
                MUTARI[1] += 1
                show_computer_stats("Computer", time_taken, NODES_A, next_table.scor)
                N = 0
                PLAYER_TURN = Game.MIN_PLAYER
                START_TIME = time()

        # PLAYER VERSUS PLAYER
        elif game_mode == "pvp" and not WINNER and run:
            if WINNER:
                continue
            is_hover = False
            for i in range(Game.ROWS):
                for j in range(Game.COLS):
                    if mouse_click != None and GAME.hexagons[i][j].check_inside(Point(mouse_click[0], mouse_click[1])):
                        selected = i, j, RED
                    elif mouse_hover != None and GAME.hexagons[i][j].check_inside(Point(mouse_hover[0], mouse_hover[1])):
                        hovered = i, j, DARK_GRAY
                        is_hover = True
            if not is_hover or (selected != None and hovered != None and selected[:2] == hovered[:2]):
                hovered = None

            # Selectam, daca a fost ales un hexagon de catre utilizator
            if selected != None:
                i, j = selected[:2]
                if GAME.select_hexagon((i, j), PLAYER_TURN):
                    GAME.game.select_position((i, j), PLAYER_TURN)
                    print("Good choice")
                    GAME.game.console_show()
                    show_user_stats(f"Player {1 if PLAYER_TURN == Game.MIN_PLAYER else 2}", time() - START_TIME)
                    MUTARI[0 if Game.MIN_PLAYER == PLAYER_TURN else 1] += 1
                    PLAYER_TURN = Game.MIN_PLAYER if PLAYER_TURN == Game.MAX_PLAYER else Game.MAX_PLAYER
                else:
                    print("Already selected")

        # COMPUTER VS COMPUTER
        elif game_mode == "cvc" and not WINNER and run:
            START_TIME = time()
            heuristic = 1 if PLAYER_TURN == Game.MIN_PLAYER else 2

            if sum(MUTARI) == 0:  # Prima mutare -> random
                i, j = randint(0, Game.ROWS - 1), randint(0, Game.COLS - 1)
                GAME.game.select_position((i, j), PLAYER_TURN)
            else:
                if algo == "minimax":
                    next_table = min_max(State(deepcopy(GAME.game), PLAYER_TURN, depth), heuristic)
                else:
                    next_table = alpha_beta(-INF, INF, State(deepcopy(GAME.game), PLAYER_TURN, depth), heuristic)
                GAME.game = next_table.next_state.game

            time_taken = time() - START_TIME
            GAME.select_hexagon(GAME.new_hexagon(), PLAYER_TURN)
            print(f"Computer {heuristic} has played move:")
            GAME.game.console_show()
            TOTAL_NODES.append(NODES_A)
            TIMES_TAKEN.append(time_taken)
            player_name = f"Computer {heuristic}"
            if sum(MUTARI) != 0:
                show_computer_stats(player_name, time_taken, NODES_A, next_table.scor)
            MUTARI[heuristic - 1] += 1
            NODES_A = 0
            PLAYER_TURN = GAME.game.oponent(PLAYER_TURN)

        # Daca am castigat, afisam asta
        WINNER = GAME.game.final() if not WINNER else WINNER
        if not WINNER:
            update_game_window(hovered, mouse_click, game_mode)
        else:
            program_time_taken = time() - PROGRAM_TIME
            show_stats(game_mode, program_time_taken,TIMES_TAKEN, TOTAL_NODES, MUTARI)
            #game_mode = "pvc"
            PLAYER_TURN = Game.MIN_PLAYER  # Sa avem acces la mouse
            update_final_window(WINNER, mouse_click, game_mode)

        # Anulam selectia anterioara
        selected = None
        mouse_click = None
    pg.QUIT


if __name__ == "__main__":
    menu_gui() 