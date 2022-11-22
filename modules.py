import random

def number_monster_game(rows, columns):
    if 0 < rows <= 10:
        num_monsters = random.randrange(3, 7)   # 3 a 6 Monsters
    elif 10 < rows <= 20:
        num_monsters = random.randrange(4, 11)   # 7 a 10 Monsters
    elif rows > 20:
        num_monsters = random.randrange(12, 15)  # 11 a 14 Monsters
    return num_monsters


def random_coordinates(rows, columns, number_monster):
    random_coordenates_list = []
    for i in range(0, number_monster):
        coordenate_rows = random.randrange(0, rows)
        coordenate_columns = random.randrange(0, columns)
        random_coordenates_list.append((coordenate_rows, coordenate_columns))
    return random_coordenates_list

def coordinates_monster_check(rows, columns, number_monster, random_coordenates_check):
    coordenates = random_coordenates_check
    while True:
        if len(coordenates) == len(set(coordenates)):
            break
        elif len(coordenates) != len(set(coordenates)):
            # print("\nTHE COORDINATES ENTERED ARE INVALID\n")
            coordenates.clear
            coordenates = random_coordinates(rows, columns, number_monster)
    return coordenates


def monsters_released(type_monster_list):
    monster_added = type_monster_list
    clover = 0
    diamond = 0
    pica = 0
    for i in monster_added:
        if i == 0:
            clover += 1
        elif i == 1:
            diamond += 1
        elif i == 2:
            pica += 1
    monster_added.clear()
    monster_added.append(clover)
    monster_added.append(diamond)
    monster_added.append(pica)
    return monster_added

def tool_emoji_used(tool):
    tool_emoji = tool
    if tool_emoji == 1:
        tool_emoji = "🏹"
    elif tool_emoji == 2:
        tool_emoji = "🪓"
    elif tool_emoji == 3:
        tool_emoji = "⚔️"
    elif tool_emoji == 4:
        tool_emoji = "🛡️"
    return tool_emoji
    
def coordinate_attack_correct(rows, columns, coordinate_attack):
    hunter_coordinate_attack = coordinate_attack 
    while True:
        if 0 <= hunter_coordinate_attack[0] < rows and 0 <= hunter_coordinate_attack[1] < columns:
            break
        else:
            print("\nTHE COORDINATES ARE OUTSIDE THE LABYRINTH\n")
            hunter_row_coordinate = int(input("Enter the coordinate of the row you want to attack: "))
            hunter_column_coordinate = int(input("Enter the coordinate of the column you want to attack: "))
            hunter_coordinate_attack = (hunter_row_coordinate, hunter_column_coordinate)
    return hunter_coordinate_attack

def tool_correct(tool):
    while True:
        if 0 < tool <= 4:
            hunter_tool = tool
            break
        else: 
            print("\nTHE DESIRED TOOL DOES NOT EXIST\n")
            tool = int(input("Enter the number of the tool you want to use: "))
    return hunter_tool

def hunter_attack_tool(self, coordinate_attack, tool_used):
    hunter_coordinate_attack = coordinate_attack 
    hunter_tool_used = tool_used
    object_coordinate = self.matrix_hidden[hunter_coordinate_attack[0]][hunter_coordinate_attack[1]]
    if object_coordinate != " ":
        if object_coordinate.symbol == "🛡️":
            print("\nYOU CANNOT ATTACK IN A PLACE THAT IS BLOCKADED\n")
        else:
            monster_coordinate = self.matrix_hidden[hunter_coordinate_attack[0]][hunter_coordinate_attack[1]]
            life_monster = monster_coordinate.life
            # print(life_monster) # -----> Testing
            self.matrix_hidden[hunter_coordinate_attack[0]][hunter_coordinate_attack[1]].life -= hunter_tool_used.decreases_life
            life_monster_current = self.matrix_hidden[hunter_coordinate_attack[0]][hunter_coordinate_attack[1]].life
            # print(f"{self.matrix_hidden[hunter_coordinate_attack[0]][hunter_coordinate_attack[1]].life}") # -----> Testing
            print(f"\nYOU INJURED A {object_coordinate.symbol} WITH A {hunter_tool_used.symbol}, PAST LIFE: {life_monster} AND CURRENT LIFE: {life_monster_current}\n")
            if self.matrix_hidden[hunter_coordinate_attack[0]][hunter_coordinate_attack[1]].life <= 0:
                self.matrix_hidden[hunter_coordinate_attack[0]][hunter_coordinate_attack[1]] = " "
                self.matrix_public[hunter_coordinate_attack[0]][hunter_coordinate_attack[1]] = " "
                print(f"\nYOU MURDERED A {object_coordinate.symbol} WITH A {hunter_tool_used.symbol}\n")
            if hunter_tool_used.name == "Block":
                print("\nIT IS NOT POSSIBLE TO ASSIGN A BLOCK IN A BUSY COORDINATE\n")
    elif object_coordinate == " ":
            if hunter_tool_used.name == "Block":
                self.matrix_hidden[hunter_coordinate_attack[0]][hunter_coordinate_attack[1]] = hunter_tool_used
                self.matrix_public[hunter_coordinate_attack[0]][hunter_coordinate_attack[1]] = hunter_tool_used.symbol
            else:
                print("THERE ARE NO MONSTERS IN THE COORDINATE ENTERED\n")
    return

def hunter_attack_labyrinth(self, list_tool, tool, coordinate_attack):
    list_tool_game = list_tool
    hunter_tool = tool
    hunter_coordinate_attack = coordinate_attack
    # print(f"{hunter_tool} and {hunter_coordinate_attack}") # -----> Testing
    if hunter_tool == 1:
        # hunter_tool = "🏹"
        tool_used = list_tool_game[(hunter_tool - 1)]
        hunter_attack_tool(self, hunter_coordinate_attack, tool_used)
    elif hunter_tool == 2:
        # hunter_tool = "🪓"
        tool_used = list_tool_game[(hunter_tool - 1)]
        hunter_attack_tool(self, hunter_coordinate_attack, tool_used)
    elif hunter_tool == 3:
        # hunter_tool = "⚔️"
        tool_used = list_tool_game[(hunter_tool - 1)]
        hunter_attack_tool(self, hunter_coordinate_attack, tool_used)
    elif hunter_tool == 4:
        # hunter_tool = "🛡️"
        tool_used = list_tool_game[(hunter_tool - 1)]
        hunter_attack_tool(self, hunter_coordinate_attack, tool_used)
    return

def coordinates_horizontal_movement(row, column, jump):
    coordinates_horizontal_movement = []
    # print(f"({row}, {column})") # ----> Testing
    movement_one = ( row, column - jump)
    movement_two = (row, column + jump)
    coordinates_horizontal_movement.append(movement_one)
    coordinates_horizontal_movement.append(movement_two)
    # print(coordinates_horizontal_movement) # ----> Testing
    return coordinates_horizontal_movement

def coordinates_vertical_movement(row, column, jump):
    coordinates_vertical_movement = []
    # print(f"({row}, {column})") # ----> Testing
    movement_one = ( row - jump, column)
    movement_two = (row + jump, column)
    coordinates_vertical_movement.append(movement_one)
    coordinates_vertical_movement.append(movement_two)
    # print(coordinates_vertical_movement)  # ----> Testing
    return coordinates_vertical_movement

def coordinates_diagonal_movement(row, column, jump):
    coordinates_diagonal_movement = []
    # print(f"({row}, {column})") # ----> Testing
    movement_one = ( row - jump, column - jump)
    movement_two = (row - jump, column + jump)
    movement_three = (row + jump , column - jump)
    movement_four = (row + jump, column + jump)
    coordinates_diagonal_movement.append(movement_one)
    coordinates_diagonal_movement.append(movement_two)
    coordinates_diagonal_movement.append(movement_three)
    coordinates_diagonal_movement.append(movement_four)
    # print(coordinates_diagonal_movement)  # ----> Testing
    return coordinates_diagonal_movement
    
def coordinates_movement_labyrinth(rows, columns, coordinates_movement):
    monster_movement_coordinates = coordinates_movement
    monster_movement_coordinates_need = []
    # print(f"{monster_movement_coordinates} -------------xxxxxx") # ----> Testing
    correct_coodinates_number = None
    for coordinates in monster_movement_coordinates:
        if 0 <= coordinates[0] < rows and 0 <= coordinates[1] < columns:
            correct_coodinates_number = True
            # print(correct_coodinates_number) # ----> Testing
            monster_movement_coordinates_need.append(coordinates)
        else:
            correct_coodinates_number = False # ----> Testing
            # print(correct_coodinates_number)
    # print(monster_movement_coordinates) # ----> Testing
    # print(monster_movement_coordinates_need)
    return monster_movement_coordinates_need

def free_coordinates_movement_labyrinth(self, coordinates_movement):
    monster_movement_coordinates = coordinates_movement
    monster_movement_coordinates_need = []
    if len(monster_movement_coordinates) > 0:
        for coordinates in monster_movement_coordinates:
            if self.matrix_hidden[coordinates[0]][coordinates[1]] == " ":
                monster_movement_coordinates_need.append(coordinates)
                # print(f"Free: ({coordinates[0]}, {coordinates[1]})") # ----> Testing      
            else:
                # print(f"Busy: ({coordinates[0]}, {coordinates[1]})") # ----> Testing
                pass
    return monster_movement_coordinates_need

def monster_movement(self, monster_movement_labyrinth, current_coordinates_monster, new_coordinates_monster):
    current_coordinates_monster_need = current_coordinates_monster
    new_coordinates_monster_need = new_coordinates_monster
    self.matrix_hidden[new_coordinates_monster_need[0]][new_coordinates_monster_need[1]] = monster_movement_labyrinth
    self.matrix_hidden[current_coordinates_monster_need[0]][current_coordinates_monster_need[1]] = " "
    self.matrix_public[new_coordinates_monster_need[0]][new_coordinates_monster_need[1]] = monster_movement_labyrinth.symbol
    self.matrix_public[current_coordinates_monster_need[0]][current_coordinates_monster_need[1]] = " "
    return

def list_monster_movement_check(list_monster_movement, monster):
    list_monster_movement_need = list_monster_movement
    contador = 0 
    if len(list_monster_movement_need) > 0:
        for monsters in list_monster_movement_need:
            if monster == monsters:
                contador += 1
        if contador > 1:
            return True    
        else: 
            return False
    else:
        return