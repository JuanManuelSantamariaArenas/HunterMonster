import random
import modules
import pickle

class Monster:

    def __init__(self, symbol, life, movements, jump):
        self.symbol = symbol
        self.life = life
        self.movements = movements
        self.jump = jump

    def __str__(self):
        return f"Monster: SYMBOL: {self.symbol}, LIFE: {self.life}, MOVEMENTS: {self.movements} AND JUMP: {self.jump}"

class CloverMonster(Monster):

    def __init__(self):
        self.symbol = "🦁" # Equivalent: 🍀
        self.life = 100
        self.movements = ["horizontal", "vertical"]
        self.jump = 1

class DiamondMonster(Monster):

    def __init__(self):
        self.symbol = "🐵" # Equivalent: 🔶
        self.life = 75
        self.movements = ["horizontal", "vertical", "diagonal"]
        self.jump = 1

class PicaMonster(Monster):

    def __init__(self):
        self.symbol = "🐼"  # Equivalent: ♠
        self.life = 50
        self.movements = ["diagonal"]
        self.jump = 2


class Tool():

    def __init__(self, symbol, name, decreases_life):
        self.symbol = symbol
        self.name = name
        self.decreases_life = decreases_life

    def __str__(self):
        return f"Tool: SYMBOL: {self.symbol}, NAME: {self.name} AND DECREASES_LIFE: {self.decreases_life}"

class CrossBow(Tool):

    def __init__(self):
        self.symbol = "🏹"   # Equivalent: Cauchera
        self.name = "Crossbow"
        self.decreases_life = 5

class Axe(Tool):

    def __init__(self):
        self.symbol = "🪓"   # Equivalent: Palo con clavos
        self.name = "Axe"
        self.decreases_life = 10

class Sword(Tool):

    def __init__(self):
        self.symbol = "⚔️"  # Equivalent: Molotov
        self.name = "Sword"
        self.decreases_life = 20

class Block(Tool):

    def __init__(self):
        self.symbol = "🛡️"  # Equivalent: Bloqueo
        self.name = "Block"
        self.decreases_life = 0

class Labyrinth:
    def __init__(self):
        self.matrix_hidden = []
        self.matrix_public = []
        self.added_monsters_list = {}
        self.rows_and_columns = []
    
    def fill_array(self, rows, columns):
        for i in range(0, rows):
            self.matrix_hidden.append([0]*columns)
            self.matrix_public.append([0]*columns)
        for i in range(0, rows):
            for j in range(0, columns):
                self.matrix_hidden[i][j] = " "
                self.matrix_public[i][j] = " "
        self.rows_and_columns = [rows, columns]
        return self.matrix_hidden, self.matrix_public, self.rows_and_columns
    
    def show_matrix_hidden(self):
        for i in self.matrix_hidden:
            print(i)

    def show_matrix_public(self):
        for i in self.matrix_public:
            print(i)
    
    def show_added_monsters_list(self):
        for key, values in self.added_monsters_list.items():
            print(f"{key} : {values}")

    def __str__(self) -> str:
        return f"{self.matrix_hidden}"

    def monster_add_labyrinth(self, type_monster):
        monster_add = CloverMonster()
        if type_monster == 0:
            monster_add = CloverMonster()
        elif type_monster == 1:
            monster_add = DiamondMonster()
        elif type_monster == 2:
            monster_add = PicaMonster()
        return monster_add

    def spawn_monsters(self, rows, columns):
        # list_monster = [CloverMonster(), DiamondMonster(), PicaMonster()]
        number_monster = modules.number_monster_game(rows, columns)
        print(f"\n{number_monster} MONSTERS WERE GENERATED")
        random_coordinates = modules.random_coordinates(rows, columns, number_monster)
        coordinates_monster = modules.coordinates_monster_check(rows, columns, number_monster, random_coordinates)
        monster_type_number = []
        for i in range(0, number_monster):
            type_monster = random.randrange(0, 3)
            monster_type_number.append(type_monster)
            # monster_add = list_monster[type_monster]
            monster_add = self.monster_add_labyrinth(type_monster)
            position_rows = coordinates_monster[i][0]
            position_columns = coordinates_monster[i][1]
            self.matrix_hidden[position_rows][position_columns] = monster_add # ----> monster_add.symbol
            self.matrix_public[position_rows][position_columns] = monster_add.symbol
            self.added_monsters_list[i] = monster_add
        monster_type_number = modules.monsters_released(monster_type_number)
        print(f"\n🦁 = {monster_type_number[0]}, 🐵 = {monster_type_number[1]} AND 🐼 = {monster_type_number[2]}\n")
        # print("\n🦁 = {}, 🐵 = {} AND 🐼 = {}\n".format(monster_type_number[0], monster_type_number[1], monster_type_number[2]))
        return self.matrix_hidden, self.matrix_public, self.added_monsters_list
    
    def hunter_attack(self, rows, columns):
        print("\n THE TOOLS YOU CAN USE ARE:\n 1. CROSSBOW (DECREASES 5 LIFE): 🏹\n 2. AXE (DECREASES 10 LIFE): 🪓\n 3. SWORD (DECREASES 20 LIFE): ⚔️\n 4. BLOCK (RESTRICTS MOVEMENT OF MONSTERS): 🛡️\n")
        tool = int(input("Enter the number of the tool you want to use: "))
        tool = modules.tool_correct(tool)
        tool_emoji = modules.tool_emoji_used(tool)
        list_tool = [CrossBow(), Axe(), Sword(), Block()]
        hunter_row_coordinate = int(input("Enter the coordinate of the row you want to attack: "))
        hunter_column_coordinate = int(input("Enter the coordinate of the column you want to attack: "))
        coordinate_attack = (hunter_row_coordinate, hunter_column_coordinate)  
        coordinate_attack =  modules.coordinate_attack_correct(rows, columns, coordinate_attack)
        print(f"\nTHE HUNTER USED THE TOOL {tool} ( {tool_emoji}  ), AT THE COORDINATE {coordinate_attack} OF THE LABYRINTH")
        modules.hunter_attack_labyrinth(self, list_tool, tool, coordinate_attack)
        return self.matrix_hidden, self.matrix_public

    def move_monsters(self, rows, columns):
        list_monster_movement = [] 
        immobilized_monsters = ["","",""]
        for i in range(0, rows):
            for j in range(0, columns):
                if self.matrix_hidden[i][j] != " " and self.matrix_hidden[i][j].symbol != "🛡️":
                    monster_check = self.matrix_hidden[i][j]
                    list_monster_movement.append(monster_check)
                    check_monster = modules.list_monster_movement_check(list_monster_movement, monster_check)
                    # print(check_monster)
                    if check_monster == False:
                        if self.matrix_hidden[i][j].symbol == "🦁":
                            # print(f"Exist monster lion: ({i}, {j})")
                            jump_monster = self.matrix_hidden[i][j].jump
                            coordinates_horizontal_movement = modules.coordinates_horizontal_movement(i, j, jump_monster)
                            coordinates_vertical_movement = modules.coordinates_vertical_movement(i, j, jump_monster)
                            coordinates_horizontal_movement = modules.coordinates_movement_labyrinth(rows, columns, coordinates_horizontal_movement)
                            coordinates_vertical_movement = modules.coordinates_movement_labyrinth(rows, columns, coordinates_vertical_movement)
                            coordinates_horizontal_movement = modules.free_coordinates_movement_labyrinth(self, coordinates_horizontal_movement)
                            coordinates_vertical_movement = modules.free_coordinates_movement_labyrinth(self, coordinates_vertical_movement)
                            monster_movement_coordinates = coordinates_horizontal_movement + coordinates_vertical_movement
                            if len(monster_movement_coordinates) > 0:
                                new_coordinates_monster = random.choice(monster_movement_coordinates)
                                # print(f"Movement: " + str(new_coordinates_monster)) # ----> Testing
                                current_coordinates_monster = (i, j)
                                monster_movement_labyrinth = self.matrix_hidden[i][j]
                                modules.monster_movement(self, monster_movement_labyrinth, current_coordinates_monster, new_coordinates_monster)
                                immobilized_monsters[0] = False
                            else:
                                immobilized_monsters[0] = True
                        elif self.matrix_hidden[i][j].symbol == "🐵":
                            # print(f"Exist monster monkey: ({i}, {j})")
                            jump_monster = self.matrix_hidden[i][j].jump
                            coordinates_horizontal_movement = modules.coordinates_horizontal_movement(i, j, jump_monster)
                            coordinates_vertical_movement = modules.coordinates_vertical_movement(i, j, jump_monster)
                            coordinates_diagonal_movement = modules.coordinates_diagonal_movement(i, j, jump_monster)
                            coordinates_horizontal_movement = modules.coordinates_movement_labyrinth(rows, columns, coordinates_horizontal_movement)
                            coordinates_vertical_movement = modules.coordinates_movement_labyrinth(rows, columns, coordinates_vertical_movement)
                            coordinates_diagonal_movement = modules.coordinates_movement_labyrinth(rows, columns, coordinates_diagonal_movement)
                            coordinates_horizontal_movement = modules.free_coordinates_movement_labyrinth(self, coordinates_horizontal_movement)
                            coordinates_vertical_movement = modules.free_coordinates_movement_labyrinth(self, coordinates_vertical_movement)
                            coordinates_diagonal_movement = modules.free_coordinates_movement_labyrinth(self, coordinates_diagonal_movement)
                            monster_movement_coordinates = coordinates_horizontal_movement + coordinates_vertical_movement + coordinates_diagonal_movement
                            if len(monster_movement_coordinates) > 0:
                                new_coordinates_monster = random.choice(monster_movement_coordinates)
                                # print(f"Movement: " + str(new_coordinates_monster))
                                current_coordinates_monster = (i, j)
                                monster_movement_labyrinth = self.matrix_hidden[i][j]
                                modules.monster_movement(self, monster_movement_labyrinth, current_coordinates_monster, new_coordinates_monster)
                                immobilized_monsters[1] = False
                            else:
                                immobilized_monsters[1] = True
                        elif self.matrix_hidden[i][j].symbol == "🐼":
                            # print(f"Exist monster panda: ({i}, {j})")
                            jump_monster = self.matrix_hidden[i][j].jump
                            coordinates_diagonal_movement = modules.coordinates_diagonal_movement(i, j, jump_monster)
                            coordinates_diagonal_movement = modules.coordinates_movement_labyrinth(rows, columns, coordinates_diagonal_movement)
                            coordinates_diagonal_movement = modules.free_coordinates_movement_labyrinth(self, coordinates_diagonal_movement)
                            monster_movement_coordinates = coordinates_diagonal_movement
                            if len(monster_movement_coordinates) > 0:
                                new_coordinates_monster = random.choice(monster_movement_coordinates)
                                # print(f"Movement: " + str(new_coordinates_monster))
                                current_coordinates_monster = (i, j)
                                monster_movement_labyrinth = self.matrix_hidden[i][j]
                                modules.monster_movement(self, monster_movement_labyrinth, current_coordinates_monster, new_coordinates_monster)
                                immobilized_monsters[2] = False  
                            else:
                                immobilized_monsters[2] = True
                else:
                    # print(f"There is no monster: ({i}, {j})")
                    pass
        return self.matrix_hidden, self.matrix_public, immobilized_monsters

    def hunted_monsters(self, rows, columns):
        monster = 0
        for i in range(0, rows):
            for j in range(0, columns):
                if self.matrix_hidden[i][j] != " " and self.matrix_hidden[i][j].symbol != "🛡️":
                    monster += 1
        if monster == 0:
            return True
        elif monster > 0:
            return False

    def save_game(self):
        with open("record.txt", "wb") as file:
            pickle.dump(self, file)
    
    def load_game(self):
        with open("record.txt", "rb") as file:
            past_labyrinth = pickle.load(file)
            self.matrix_hidden = past_labyrinth.matrix_hidden
            self.matrix_public = past_labyrinth.matrix_public
            rows_and_colomns = past_labyrinth.rows_and_columns
        return rows_and_colomns

def start_game():
    # print("🪓🏹")
    print("🏹"*5 + "🪓"*5 + "⚔️"*5 + "🛡️"*5)
    print("WELCOME TO HUNTER MONSTERS\n")
    labyrinth_one = Labyrinth() 
    question_load_game = input("DO YOU WANT TO LOAD THE LAST GAME?, (y/n): ")
    if question_load_game == "y" or question_load_game == "Y":
        load_labyrinth = labyrinth_one.load_game()
        rows = load_labyrinth[0]
        columns = load_labyrinth[1]
        print("\nTHE GAME WAS LOADED SUCCESSFULLY\n")
    elif question_load_game == "n" or question_load_game == "N":
        print("\nWE START THE GAME, DO YOUR BEST!\n")
        # rows = int(input("Enter the # of rows: "))
        # columns = int(input("Enter the # of columns: "))
        rows = random.randrange(5, 21)
        columns = random.randrange(5, 11)
        print("="*10)
        labyrinth_one.fill_array(rows, columns)
    print(f"\nTHE LABYRINTH OF THE GAME ({rows} x {columns})\n")
    labyrinth_one.show_matrix_hidden()
    print("-"*10) # ----> Testing
    labyrinth_one.show_matrix_public() # ----> Testing
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
    if question_load_game != "y" or question_load_game != "Y":
        labyrinth_one.spawn_monsters(rows, columns)
    labyrinth_one.show_matrix_hidden() # ----> Testing
    print("-"*5) # ----> Testing
    labyrinth_one.show_matrix_public() # ----> Testing
    print("="*10)
    Attempts = random.randrange(8, 13)
    print(f"\nTHE HUNTER HAS {Attempts} ATTEMPTS")
    while Attempts > 0:
        labyrinth_one.hunter_attack(rows, columns)
        labyrinth_one.move_monsters(rows, columns)
        labyrinth_one.show_matrix_hidden()
        print("-"*5) # ----> Testing
        labyrinth_one.show_matrix_public()
        win = labyrinth_one.hunted_monsters(rows, columns)
        if win:
            print("\nCONGRATULATIONS YOU HAVE HUNTED ALL THE MONSTERS\n")
            break
        else:
            # for i in immobilized_monsters:
            Attempts -= 1
            print(f"\nTHE HUNTER HAS {Attempts} ATTEMPTS\n")
        if Attempts == 0:
            print("\nGAME OVER YOU'RE OUT OF TRIES\n")
        else: 
            if Attempts == 3:                
                question_save_game = input("\nDO YOU WANT TO SAVE THE CURRENT GAME?, (y/n): ")
                if question_save_game == "y" or question_save_game == "Y":
                    labyrinth_one.save_game()
                    print("\nTHE GAME WAS SAVED SUCCESSFULLY\n")
                    break
                elif question_save_game == "n" or question_save_game == "N":
                    print("\nBE ALERT YOU HAVE 3 ATTEMPTS LEFT\n")
    return
start_game()