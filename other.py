import random
"""
    def spawn_monsters(self, rows, columns):
        clover_monster = Monster("🍀", 100, 1, 1)
        diamond_monster = Monster("🔶", 75, 2, 1)
        pica_monster = Monster("♠", 50, 3, 2)
        position_rows = [random.randrange(0, rows) for i in range(0, 3)]
        position_columns = [random.randrange(0, columns) for i in range(0, 3)]
        while True:
            if position_rows[0] == position_rows[1] and position_columns[0] == position_columns[1]:
                position_rows[0] = random.randrange(0, rows) 
                position_columns[0] = random.randrange(0, columns)
            elif position_rows[0] == position_rows[2] and position_columns[0] == position_columns[2]:
                position_rows[0] = random.randrange(0, rows) 
                position_columns[0] = random.randrange(0, columns)
            elif position_rows[1] == position_rows[2] and position_columns[1] == position_columns[2]:
                position_rows[1] = random.randrange(0, rows) 
                position_columns[1] = random.randrange(0, columns)
            else:
                break
        print(position_rows)
        print(position_columns)
        for i in range(0, 3):
            if i == 0:
                self.matrix[position_rows[i]][position_columns[i]] = clover_monster.simbolo
            elif i == 1:
                self.matrix[position_rows[i]][position_columns[i]] = diamond_monster.simbolo
            elif i == 2:
                self.matrix[position_rows[i]][position_columns[i]] = pica_monster.simbolo
        return self.matrix
"""  

"""
import random

def random_coordinates(rows, columns, number_monster):
    print("Entre aqui")
    random_coordenates = []
    for i in range(0, number_monster):
        coordenate_rows = random.randrange(0, rows)
        coordenate_columns = random.randrange(0, columns)
        random_coordenates.append((coordenate_rows, coordenate_columns))
    print(random_coordenates)
    return random_coordenates


def coordinates_monster(rows, columns, number_monster, coor):
    coordenates = coor
    print(coordenates)
    while True:
        if len(coordenates) == len(set(coordenates)):
            print("No hay repetidos")
            break
        elif len(coordenates) != len(set(coordenates)):
            coordenates.clear
            coordenates = random_coordinates(rows, columns, number_monster)
    return coordenates

coorde_igu = [(1, 0), (2, 9), (1, 0), (3, 5), (6, 2)]
coorde_dif = [(1, 0), (2, 9), (1, 3), (3, 5), (6, 2)]
uno = coordinates_monster(5, 8, 5, coorde_igu)
print(uno)
"""

"""
import random

def random_coordinates(rows, columns, number_monster):
    random_coordenates_list = []
    for i in range(0, number_monster):
        coordenate_rows = random.randrange(0, rows)
        coordenate_columns = random.randrange(0, columns)
        random_coordenates_list.append((coordenate_rows, coordenate_columns))
    return random_coordenates_list

def coordinates_monster(rows, columns, number_monster, random_coordenates_check):
    coordenates = random_coordenates_check
    while True:
        if len(coordenates) == len(set(coordenates)):
            break
        elif len(coordenates) != len(set(coordenates)):
            coordenates.clear
            coordenates = random_coordinates(rows, columns, number_monster)
    return coordenates
"""

"""
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))

print("="*10)
labyrinth_one = Labyrinth()
print(labyrinth_one) 
print("="*10)
mon1 = CloverMonster()
mon2 = DiamondMonster()
mon3 = PicaMonster()
print(mon1)
print(mon2)
print(mon3)
print("="*10)
labyrinth_one.fill_array(rows, columns)
print(labyrinth_one)
print("="*10)
labyrinth_one.show_matrix()
print("="*10)
labyrinth_one.spawn_monsters(rows, columns)
labyrinth_one.show_matrix()
"""

"""
    position_rows = [random.randrange(0, rows) for i in range(0, number_monster)]
    position_columns = [random.randrange(0, columns) for i in range(0, number_monster)]
    coordinates = []
    for i in range(0, len(position_rows)):
        coordinates.append((position_rows[i], position_columns[i]))
    print(coordinates)
    print(position_rows)
    print(position_columns)
    return coordinates
"""

"""
    print(f"Monster: {self.matrix_hidden[hunter_coordinate_attack[0]][hunter_coordinate_attack[1]]}") # ----> Add
    monster = self.matrix_hidden[hunter_coordinate_attack[0]][hunter_coordinate_attack[1]].life
    # print(f"Monster: {monster.symbol}")
    print(f"Monster: {monster}")
"""
"""
       for i in range(0, rows):
            for j in range(0, columns):
                if self.matrix_hidden[i][j] != " " and self.matrix_hidden[i][j].symbol != "🛡️":
                    print(f"Exist monster: ({i}, {j})")
                else: 
                    print(f"There is no monster: ({i}, {j})")
        return self.matrix_hidden, self.matrix_public
"""

"""
rows = 5
columns = 4
row = int(input("Enter row: "))
colum = int(input("Enter column: "))
while True:
    if 0 <= row < rows and 0 <= colum < columns:
        print("Sí")
        break
    elif 0 > row >= rows and 0 > colum >= columns:
        print("No")
        row = int(input("Enter row: "))
        colum = int(input("Enter column: "))
    else:
        print("Si/No")
        row = int(input("Enter row: "))
        colum = int(input("Enter column: "))
"""
lista = [10, 20, 30, 40, 30, 20, 10]

indice = lista.index(30)

print(indice)
"""
def coordinates_movement_labyrinth(rows, columns, coordinates_movement):
    monster_movement_coordinates = coordinates_movement
    print(f"{monster_movement_coordinates} -------------xxxxxx") # ----> Testing
    correct_coodinates_number = None 
    for coordinates in monster_movement_coordinates:
        if 0 <= coordinates[0] < rows and 0 <= coordinates[1] < columns:
            correct_coodinates_number = True
            print(correct_coodinates_number) # ----> Testing
        else:
            correct_coodinates_number = False # ----> Testing
            print(correct_coodinates_number)
        if correct_coodinates_number == False:
            position_coordinate_list = monster_movement_coordinates.index(coordinates)
            monster_movement_coordinates.pop(position_coordinate_list)
        print(monster_movement_coordinates) # ----> Testing
    return monster_movement_coordinates
"""
"""
def coordinates_movement_labyrinth(rows, columns, coordinates_movement):
    monster_movement_coordinates = coordinates_movement
    print(f"{monster_movement_coordinates} -------------xxxxxx") # ----> Testing
    correct_coodinates_number = None 
    position_coordinate_list = []
    for coordinates in monster_movement_coordinates:
        if 0 <= coordinates[0] < rows and 0 <= coordinates[1] < columns:
            correct_coodinates_number = True
            print(correct_coodinates_number) # ----> Testing
        else:
            correct_coodinates_number = False # ----> Testing
            print(correct_coodinates_number)
        if correct_coodinates_number == False:
            position_coordinate = monster_movement_coordinates.index(coordinates)
            position_coordinate_list.append(position_coordinate)
    print(f"{position_coordinate_list} ---- POSI") 
    if len(position_coordinate_list) > 0:
        for index in position_coordinate_list:
            monster_movement_coordinates.pop(index)
    print(monster_movement_coordinates) # ----> Testing
    return monster_movement_coordinates
"""
"""
def coordinates_movement_labyrinth(rows, columns, coordinates_movement):
    monster_movement_coordinates = coordinates_movement
    print(f"{monster_movement_coordinates} -------------xxxxxx") # ----> Testing
    correct_coodinates_number = None
    for coordinates in monster_movement_coordinates:
        if 0 <= coordinates[0] < rows and 0 <= coordinates[1] < columns:
            correct_coodinates_number = True
            print(correct_coodinates_number) # ----> Testing
        else:
            correct_coodinates_number = False # ----> Testing
            print(correct_coodinates_number)
        if correct_coodinates_number == False:
            monster_movement_coordinates.remove(coordinates)
    print(monster_movement_coordinates) # ----> Testing
    return monster_movement_coordinates
"""

"""
                        if self.matrix_hidden[i][j].symbol == "🐵":
                            print(f"Exist monster lion: ({i}, {j})")
                            jump_monster = self.matrix_hidden[i][j].jump
                            coordinates_horizontal_movement = modules.coordinates_horizontal_movement(i, j, jump_monster)
                            coordinates_vertical_movement = modules.coordinates_vertical_movement(i, j, jump_monster)
                            coordinates_diagonal_movement = modules.coordinates_diagonal_movement(i, j, jump_monster) # ----> Testing 
                            coordinates_horizontal_movement = modules.coordinates_movement_labyrinth(rows, columns, coordinates_horizontal_movement)
                            coordinates_vertical_movement = modules.coordinates_movement_labyrinth(rows, columns, coordinates_vertical_movement)
                            coordinates_diagonal_movement = modules.coordinates_movement_labyrinth(rows, columns, coordinates_diagonal_movement) # ----> Testing
                            coordinates_horizontal_movement = modules.free_coordinates_movement_labyrinth(self, coordinates_horizontal_movement)
                            coordinates_vertical_movement = modules.free_coordinates_movement_labyrinth(self, coordinates_vertical_movement)
                            coordinates_diagonal_movement = modules.free_coordinates_movement_labyrinth(self, coordinates_diagonal_movement) # ----> Testing
                            monster_movement_coordinates = coordinates_horizontal_movement + coordinates_vertical_movement + coordinates_diagonal_movement
                            if len(monster_movement_coordinates) > 0:
                                new_coordinates_monster = random.choice(monster_movement_coordinates)
                                print(f"Movement: " + str(new_coordinates_monster)) # ----> Testing
                                current_coordinates_monster = (i, j)
                                monster_movement_labyrinth = self.matrix_hidden[i][j]
                                modules.monster_movement(self, monster_movement_labyrinth, current_coordinates_monster, new_coordinates_monster)
"""

"""
def start_game():
    # print("🪓🏹")
    print("🏹"*5 + "🪓"*5 + "⚔️"*5 + "🛡️"*5)
    print("WELCOME TO HUNTER MONSTERS\n")
    labyrinth_one = Labyrinth() 
    # rows = int(input("Enter the # of rows: "))
    # columns = int(input("Enter the # of columns: "))
    rows = random.randrange(5, 21)
    columns = random.randrange(5, 11)
    print("="*10)
    labyrinth_one.fill_array(rows, columns)
    print(f"\nTHE LABYRINTH OF THE GAME ({rows} x {columns})\n")
    labyrinth_one.show_matrix_hidden()
    # labyrinth_one.show_matrix_public() # ----> Add
    print("")
    print("="*10)
    m_clover = CloverMonster()
    m_diamond = DiamondMonster()
    m_pica = PicaMonster()
    print("\nTHERE ARE THREE KINDS OF MONSTERS\n")
    print(m_clover)
    print(m_diamond)
    print(m_pica)
    t_crossbow = CrossBow()
    t_axe = Axe()
    t_sword = Sword() 
    t_block = Block()
    print("\nTHERE ARE FOUR KINDS OF TOOLS\n")
    print(t_crossbow)
    print(t_axe)
    print(t_sword)
    print(t_block)
    print("")
    print("="*10)
    labyrinth_one.spawn_monsters(rows, columns)
    
    labyrinth_one.show_added_monsters_list()    # ------> Show added monsters list
    print("="*10)
    print("")
    
    
    labyrinth_one.show_matrix_hidden()  # ----> Hidden and Testing  # ------> Hunter Attack
    print("-"*20) # -----> Testing
    labyrinth_one.show_matrix_public()  # ----> Public and Testing
    print("="*10)
    labyrinth_one.hunter_attack(rows, columns)
    labyrinth_one.show_matrix_hidden() # ----> Hidden and Testing
    print("-"*20)
    labyrinth_one.show_matrix_public() # ----> Public and Testing
    print("="*10)
    labyrinth_one.hunter_attack(rows, columns) # ----> Testing
    labyrinth_one.show_matrix_hidden() # ----> Hidden and Testing
    print("-"*20)
    labyrinth_one.show_matrix_public() # ----> Public and Testing
    
    
    labyrinth_one.show_matrix_hidden()  # ----> Hidden and Testing # ------> Move monsters
    print("-"*20) # -----> Testing
    labyrinth_one.show_matrix_public()  # ----> Public and Testing
    print("="*10)
    labyrinth_one.move_monsters(rows, columns)
    labyrinth_one.show_matrix_hidden()  # ----> Hidden and Testing
    print("-"*20) # -----> Testing
    labyrinth_one.show_matrix_public()  # ----> Public and Testing
    print("="*10)
    
    return
start_game()
"""