"""
JAFG v1.0
Just A Fighting Game
"""

import random
import time

def roll_dice(d4, d6, d8):
    total_roll = 0
    for _ in range(d4):
        total_roll += random.randrange(1,5)
    for _ in range(d6):
        total_roll += random.randrange(1,7)
    for _ in range(d8):
        total_roll += random.randrange(1,9)
    return total_roll

# Constants: Attack Results & Moves
CRIT = "Critical Hit"
HIT = "Hit"
MISS = "Miss"
PUNCH = "Punch"
KICK = "Kick"
BLOCK = "Block"

# Constants: Turn Type: normal, player block or cpu block
PLAYER_TURN = "player_turn"
CPU_TURN = "cpu_turn"
PLAYER_BLOCK = "player_block"
CPU_BLOCK = "cpu_block"
turn_type = PLAYER_TURN

class Fighter:
    def action_punch(self, defender):
        global CRIT, HIT, MISS
        # Attack roll
        attack_roll = roll_dice(0, 1, 0)
        if attack_roll >= self.crit_roll:
            attack_result = CRIT
        elif attack_roll < defender.punch_defence:
            attack_result = MISS
        else:
            attack_result = HIT
        print(f"Attack role: {attack_roll}!")
        time.sleep(0.5)
        # Print move name & calc damage
        if self.punch_lvl == 1:
            print(f"Punch: {attack_result}!")
            damage = roll_dice(2, 0, 0)
        elif self.punch_lvl == 2:
            print(f"Punch+: {attack_result}!")
            damage = roll_dice(4, 0, 0)
        elif self.punch_lvl == 3:
            print(f"Tiger's Bite: {attack_result}!")
            damage = roll_dice(8, 0, 0)
        time.sleep(0.5)
        # Adjust damage depending on attack_result
        if attack_result == CRIT:
            damage *= 2
        elif attack_result == MISS:
            damage = 0
        # Decrease defender's health
        print(f"{self.name} dealt {damage} damage!")
        defender.health -= damage
        time.sleep(1)
        # Return attack result (for use in block_action)
        return attack_result

    def action_kick(self, defender):
        global CRIT, HIT, MISS
        # Attack roll
        attack_roll = roll_dice(0, 1, 0)
        if attack_roll >= self.crit_roll:
            attack_result = CRIT
        elif attack_roll < defender.kick_defence:
            attack_result = MISS
        else:
            attack_result = HIT
        print(f"Attack role: {attack_roll}!")
        time.sleep(0.5)
        # Print move name & calc damage
        if self.kick_lvl == 1:
            print(f"Kick: {attack_result}!")
            damage = roll_dice(0, 0, 2)
        elif self.kick_lvl == 2:
            print(f"Kick+: {attack_result}!")
            damage = roll_dice(0, 0, 3)
        elif self.kick_lvl == 3:
            print(f"Dragon's Wrath: {attack_result}!")
            damage = roll_dice(1, 0, 5)
        time.sleep(0.5)
        # Adjust damage depending on attack_result
        if attack_result == CRIT:
            damage *= 2
        elif attack_result == MISS:
            damage = 0
        # Decrease defender's health
        print(f"{self.name} dealt {damage} damage!")
        defender.health -= damage
        time.sleep(1)
        # Return attack result (for use in block_action)
        return attack_result

    def action_block(self, prev_turn_result):
        # Calculates damage blocked or recovered
        global CRIT, HIT, MISS
        if self.block_lvl == 1:
            recover = roll_dice(2, 0, 0)
        elif self.block_lvl == 2:
            recover = roll_dice(3, 1, 0)
        elif self.block_lvl == 3:
            recover = roll_dice(3, 2, 2)
        if prev_turn_result == CRIT:
            recover = 0
            print(f"{self.name}'s block failed!")
        elif prev_turn_result == MISS:
            print(f"{self.name} recovered {recover} health!")
        elif prev_turn_result == HIT:
            recover //= 2
            print(f"{self.name} recovered {recover} health!")
        else:
            print("Invalid turn result.")
            print(prev_turn_result)
        self.health += recover
    
    def print_stats(self):
        print(f"{self.name}'s current stats:")
        print(f"Health: {self.health}")
        print(f"Punch Defence: {self.punch_defence}")
        print(f"Kick Defence: {self.kick_defence}")
        print(f"Crit Roll: {self.crit_roll}")
        print(f"Punch Level: {self.punch_lvl}")
        print(f"Kick Level: {self.kick_lvl}")
        print(f"Block Level: {self.block_lvl}")
        

class PlayerFighter(Fighter):
    def __init__(self):
        self.name = "Player"
        self.health = 50
        self.punch_defence = 2
        self.kick_defence = 2
        self.crit_roll = 6
        self.punch_lvl = 1
        self.kick_lvl = 1
        self.block_lvl = 1
    
    # Player's turn: calls action_punch/kick/block & changes value of turn_type depending on user input
    def player_turn(self, other_fighter, allow_block):
        global turn_type
        # Prompts user for a move choice, excluding block if necessary
        print("Choose an action:")
        print(f"PUNCH: lvl {self.punch_lvl}")
        print(f"KICK: lvl {self.kick_lvl}")
        if turn_type == PLAYER_TURN:
            print(f"BLOCK: lvl {self.block_lvl}")
        player_action = input(">")
        action_list = [PUNCH, KICK]
        if allow_block == True:
            action_list.append(BLOCK)
        while player_action.capitalize() not in action_list:
            player_action = input("Invalid input, try again. >")
        # Calls a function for the chosen move and changes the turn type for next turn
        if player_action.capitalize() == PUNCH:
            if turn_type == PLAYER_TURN:
                turn_type = CPU_TURN
            return self.action_punch(other_fighter)
        elif player_action.capitalize() == KICK:
            if turn_type == PLAYER_TURN:
                turn_type = CPU_TURN
            return self.action_kick(other_fighter)
        elif player_action.capitalize() == BLOCK:
            if allow_block == True:
                if turn_type == PLAYER_TURN:
                    turn_type = PLAYER_BLOCK
            else:
                print("Block disabled this turn.")
        else:
            print("Invalid input.")

    # Player Upgrade functions
    def increase_health(self, increase):
        self.health += increase
    def increase_defence(self, punch_increase, kick_increase):
        self.punch_defence += punch_increase
        self.kick_defence += kick_increase
    def decrease_crit(self, decrease):
        self.crit_roll -= decrease
    def lvl_up(self, punch_increase, kick_increase, block_increase):
        self.punch_lvl += punch_increase
        self.kick_lvl += kick_increase
        self.block_lvl += block_increase
    

class CpuFighter(Fighter):
    def __init__(self, name, difficulty, health, punch_defence, kick_defence, crit_roll, punch_lvl, 
        kick_lvl, block_lvl, move_weights, tagline):
        self.name = name
        self.difficulty = difficulty
        self.health = health
        self.punch_defence = punch_defence
        self.kick_defence = kick_defence
        self.crit_roll = crit_roll
        self.punch_lvl = punch_lvl
        self.kick_lvl = kick_lvl
        self.block_lvl = block_lvl
        self.move_weights = move_weights
        self.tagline = tagline
    
    # CPU's turn: calls action_punch/kick/block & changes value of turn_type depending on random choice
    def cpu_turn(self, other_fighter, allow_block):
        global turn_type
        # Selects a move randomly using the fighter's move weights
        cpu_action = random.choices([PUNCH, KICK, BLOCK], self.move_weights)[0]
        if allow_block == False:
            while cpu_action == BLOCK:
                cpu_action = random.choices([PUNCH, KICK, BLOCK], self.move_weights)[0]
        print(f"{self.name} chose {cpu_action}!")
        # Calls a function for the chosen move and changes the turn type for next turn
        if cpu_action.capitalize() == PUNCH:
            if turn_type == CPU_TURN:
                turn_type = PLAYER_TURN
            return self.action_punch(other_fighter)
        elif cpu_action.capitalize() == KICK:
            if turn_type == CPU_TURN:
                turn_type = PLAYER_TURN
            return self.action_kick(other_fighter)
        elif cpu_action.capitalize() == BLOCK:
            if allow_block == True:
                if turn_type == CPU_TURN:
                    turn_type = CPU_BLOCK
            else:
                print("Block disabled this turn.")
        else:
            print("Invalid input.")

# List of CPU Fighters
cpu_test_dummy = CpuFighter("Test Dummy", "Test", 20, 2, 2, 6, 1, 1, 1, [0.3, 0.3, 0.4],
                            "Good for practice, but not much else.")
cpu_easy_1 = CpuFighter("Lethargic Steve", "Easy", 30, 2, 2, 6, 1, 1, 1, [0.6, 0.3, 0.1],
                            "He's so lethargic, go easy on him.")
cpu_easy_2 = CpuFighter("Weak Besty", "Easy", 30, 2, 2, 6, 1, 1, 1, [0.3, 0.6, 0.1],
                            "She's so weak, go easy on her.")
cpu_medium_1 = CpuFighter("Monty McMedium", "Medium", 50, 3, 3, 6, 1, 1, 1, [0.6, 0.3, 0.1],
                            "Likes his steak done medium. Part of the McMedium family.")
cpu_medium_2 = CpuFighter("Marcus McMedium", "Medium", 50, 2, 2, 6, 2, 1, 2, [0.6, 0.1, 0.3],
                            "Claims to be a pyschic medium. Part of the McMedium family.")
cpu_medium_3 = CpuFighter("Maude McMedium", "Medium", 50, 2, 2, 6, 2, 2, 1, [0.4, 0.4, 0.2],
                            "Medium height & build. Wears size medium. Part of the McMedium family.")
cpu_medium_4 = CpuFighter("Matilda McMedium", "Medium", 40, 2, 2, 5, 1, 1, 1, [0.5, 0.4, 0.1],
                            "Youngest & arguably most medium of the McMedium family.")
cpu_hard_1 = CpuFighter("The Brawler", "Hard", 70, 4, 2, 6, 1, 1, 3, [0.5, 0.1, 0.4],
                            "Built like a brick lavatory. You'll have to wear him down.")
cpu_hard_2 = CpuFighter("The Monk", "Hard", 70, 2, 4, 6, 2, 2, 2, [0.4, 0.4, 0.3],
                            "A mysterious, balanced & unpredictable fighter. Be prepared for anything.")
cpu_hard_3 = CpuFighter("The Tiger", "Hard", 70, 3, 3, 6, 3, 1, 2, [0.8, 0.1, 0.1],
                            "Not an actual tiger. Those punches are no joke though.")
cpu_hard_4 = CpuFighter("The Dragon", "Hard", 70, 3, 3, 6, 1, 3, 2, [0.1, 0.8, 0.1],
                            "Not an actual dragon. Those kicks are no joke though.")
cpu_deadly_1 = CpuFighter("The Immovable Object", "Deadly", 100, 4, 3, 6, 2, 1, 3, [0.5, 0.0, 0.5],
                            "Arch-nemesis of The Unstoppable Force.")
cpu_deadly_2 = CpuFighter("The Unstoppable Force", "Deadly", 50, 3, 3, 5, 3, 3, 1, [0.0, 0.9, 0.1],
                            "Arch-nemesis of The Immovable Object.")

# Dictionary containing CPU secret codes for use in secret() function
cpu_secret_codes = {cpu_hard_1: 'B', cpu_hard_2: 'A', cpu_hard_3: 'N', cpu_hard_4: 'A', cpu_deadly_1: 'N', cpu_deadly_2: 'A'}

# Win Text & Death Text functions
def generate_cpu_death_text():
    death_text_list = ["collapses!", "crumples!", "disintegrates!", "is vaporised!", "is cut in half!", "is floored!",
                        "is very dead. No coming back from that one.", "explodes! It's a disgusting sight.",
                        "turns into a pool of chunky goop on the ground! A little bit gets on your shoes. Gross.",
                        "is incinerated! It smells like burnt hair now. Great."]
    return random.choices(death_text_list)[0]

def generate_player_death_text():
    death_text_list = ["You collapse to the ground.", "Your vision fades out.", "You lose consciousness.",
                        "As the final hit connects you know you've lost. Bollocks.",
                        "You look down to see your blood covering the floor. It's definitely supposed to stay inside your body.",
                        "You don't even see the final hit coming. Before you know it it's all over."]
    return random.choices(death_text_list)[0]

def player_win_text(player, opponent):
    # Prints end-of-fight text if player wins
    print()
    time.sleep(2)
    print(opponent.name, generate_cpu_death_text())
    time.sleep(2)
    print(f"{player.name} wins!\n")
    time.sleep(2)
    if opponent.difficulty == "Hard" or opponent.difficulty == "Deadly":
        print(f"{opponent.name}'s secret code: {cpu_secret_codes[opponent]}")
    print("Well fought!")
    print("However, more fights await you!")
    time.sleep(2)
    print("Returning to Main Menu...")
    time.sleep(2)

def cpu_win_text(opponent):
    # Prints end-of-fight text if player wins
    print()
    time.sleep(2)
    print(generate_player_death_text())
    print(f"{opponent.name} wins!\n")
    time.sleep(2)
    print("Better luck next time!")
    print("Thankfully, you live to fight another day!")
    time.sleep(2)
    print("Returning to Main Menu...")
    time.sleep(2)

# Fight function, including opponent choice & player upgrades
def fight():
    global turn_type
    # Prompts user to choose difficulty of their opponent
    print()
    time.sleep(1)
    print("Choose the difficulty of your opponent.")
    print("(Harder opponents mean more upgrades for you before the fight starts.)\n")
    print("EASY: Shouldn't be a problem! (1 upgrade)")
    print("MEDIUM: A decent challenge! (3 upgrades)")
    print("HARD: Good luck! (5 upgrades)")
    print("DEADLY: The name says it all! (5 upgrades)")
    diff_input = input(">")
    while diff_input.lower() not in ("easy", "medium", "hard", "deadly"):
        diff_input = input("Invalid input, try again. >")
    # Chooses a random opponent of the chosen difficulty
    if diff_input.lower() == "easy":
        opponent = random.choices([cpu_easy_1, cpu_easy_2])[0]
        upgrade_counter = 1
    elif diff_input.lower() == "medium":
        opponent = random.choices([cpu_medium_1, cpu_medium_2, cpu_medium_3, cpu_medium_4])[0]
        upgrade_counter = 3
    elif diff_input.lower() == "hard":
        opponent = random.choices([cpu_hard_1, cpu_hard_2, cpu_hard_3, cpu_hard_4])[0]
        upgrade_counter = 5
    elif diff_input.lower() == "deadly":
        opponent = random.choices([cpu_deadly_1, cpu_deadly_2])[0]
        upgrade_counter = 5
    print()
    time.sleep(2)
    print(f"Your opponent is {opponent.name}, difficulty: {opponent.difficulty}.")
    print(opponent.tagline)
    print()
    time.sleep(2)
    # Prompts user to upgrade their fighter a number of times depending on the chosen difficulty
    player = PlayerFighter()
    print("Time to upgrade your fighter!")
    while upgrade_counter > 0:
        print(f"You have {upgrade_counter} upgrade(s) to choose.\n")
        time.sleep(1)
        player.print_stats()
        print()
        time.sleep(1)
        # Creates list of current possible upgrades i.e. excluding those already maxed out
        upgrade_list = ["health"]
        if player.punch_defence < 4:
            upgrade_list.append("punchdef")
        if player.kick_defence < 4:
            upgrade_list.append("kickdef")
        if player.crit_roll == 6:
            upgrade_list.append("crit")
        if player.punch_lvl < 3:
            upgrade_list.append("punchlvl")
        if player.kick_lvl < 3:
            upgrade_list.append("kicklvl")
        if player.block_lvl < 3:
            upgrade_list.append("blocklvl")
        # Printing the list of current possible upgrades
        print("Choose an upgrade.")
        print("HEALTH: Increase health by 15 (no max)")
        if "punchdef" in upgrade_list:
            print("PUNCHDEF: Increase Punch Defence by 1 (max 4)")
        if "kickdef" in upgrade_list:
            print("KICKDEF: Increase Kick Defence by 1 (max 4)")
        if "crit" in upgrade_list:
            print("CRIT: Decrease Crit Roll by 1 (min 5)")
        if "punchlvl" in upgrade_list:
            print("PUNCHLVL: Increase Punch Level by 1 (max 3)")
        if "kicklvl" in upgrade_list:
            print("KICKLVL: Increase Kick Level by 1 (max 3)")
        if "blocklvl" in upgrade_list:
            print("BLOCKLVL: Increase Block Level by 1 (max 3)")
        upgrade_input = input(">")
        while upgrade_input.lower() not in upgrade_list:
            upgrade_input = input("Invalid input, try again. >")
        # Changes fighter's stats according to chosen upgrade
        if upgrade_input.lower() == "health":
            player.increase_health(15)
            print(f"\nHealth increased to {player.health}.")
            upgrade_counter -= 1
        if upgrade_input.lower() == "punchdef":
            player.increase_defence(1, 0)
            print(f"\nPunch Defence increased to {player.punch_defence}.")
            upgrade_counter -= 1
        if upgrade_input.lower() == "kickdef":
            player.increase_defence(0, 1)
            print(f"\nKick Defence increased to {player.kick_defence}.")
            upgrade_counter -= 1
        if upgrade_input.lower() == "crit":
            player.decrease_crit(1)
            print(f"\nCrit Roll decreased to {player.crit_roll}.")
            upgrade_counter -= 1
        if upgrade_input.lower() == "punchlvl":
            player.lvl_up(1, 0, 0)
            print(f"\nPunch Level increased to {player.punch_lvl}.")
            upgrade_counter -= 1
        if upgrade_input.lower() == "kicklvl":
            player.lvl_up(0, 1, 0)
            print(f"\nKick Level increased to {player.kick_lvl}.")
            upgrade_counter -= 1
        if upgrade_input.lower() == "blocklvl":
            player.lvl_up(0, 0, 1)
            print(f"\nBlock Level increased to {player.block_lvl}.")
            upgrade_counter -= 1
        time.sleep(1)
    print("\nUpgrades finished!\n")
    time.sleep(1)
    player.print_stats()
    time.sleep(1)
    # Introduction to the fight
    print("\nLet's get the fight started!")
    print(random.choices(["Good luck!", "I hope you lose!"], [0.95, 0.05])[0])
    time.sleep(2)
    print("Ready!")
    time.sleep(1)
    print(random.choices(["Set!", "Steady!"])[0])
    time.sleep(1)
    print(random.choices(["Fight!", "FIGHT!", "FIIIIIIGHT!", "Banana."], [0.35, 0.3, 0.3, 0.05])[0])
    time.sleep(1)
    print()
    
    # Initialise turn_type
    # The player takes their turn first, unless the opponent is difficulty Deadly, in which case they go first
    if opponent.difficulty == "Deadly":
        turn_type = CPU_TURN
    else:
        turn_type = PLAYER_TURN
    
    # Fight Turn structure is different depending on the turn type
    while True:
        if turn_type == PLAYER_TURN:
            # Prints fighters' health
            print()
            time.sleep(1)
            print(f"{player.name}'s turn.")
            time.sleep(0.5)
            print(f"{player.name}'s health: {player.health}, {opponent.name}'s health {opponent.health}")
            time.sleep(0.5)
            # Player takes their turn
            player.player_turn(opponent, True)
            # Check for Player victory
            if opponent.health <= 0:
                player_win_text(player, opponent)
                break
        elif turn_type == CPU_TURN:
            # Prints fighters' health
            print()
            time.sleep(1)
            print(f"{opponent.name}'s turn.")
            time.sleep(0.5)
            print(f"{player.name}'s health: {player.health}, {opponent.name}'s health {opponent.health}")
            # CPU takes its turn
            opponent.cpu_turn(player, True)
            time.sleep(0.5)
            # Check for CPU victory
            if player.health <= 0:
                cpu_win_text(opponent)
                break
        elif turn_type == PLAYER_BLOCK:
            # Increase player defence
            player.punch_defence += 1
            player.kick_defence += 1
            if player.block_lvl == 3:
                player.punch_defence += 1
                player.kick_defence += 1
            # CPU turn w/ block disabled
            print()
            time.sleep(1)
            print(f"{opponent.name}'s turn.")
            time.sleep(0.5)
            print(f"{player.name}'s health: {player.health}, {opponent.name}'s health {opponent.health}")
            time.sleep(0.5)
            cpu_turn_result = opponent.cpu_turn(player, False)
            # Recover player health based on result of CPU's turn
            player.action_block(cpu_turn_result)
            if player.health <= 0:
                cpu_win_text(opponent)
                break
            # Decrease player defence
            player.punch_defence -= 1
            player.kick_defence -= 1
            if player.block_lvl == 3:
                player.punch_defence -= 1
                player.kick_defence -= 1
            # Passes to player's turn
            turn_type = PLAYER_TURN
        elif turn_type == CPU_BLOCK:
            # Increase CPU defence
            opponent.punch_defence += 1
            opponent.kick_defence += 1
            if opponent.block_lvl == 3:
                opponent.punch_defence += 1
                opponent.kick_defence += 1
            # Player turn w/ block disabled
            print()
            time.sleep(1)
            print(f"{player.name}'s turn.")
            time.sleep(0.5)
            print(f"{player.name}'s health: {player.health}, {opponent.name}'s health {opponent.health}")
            time.sleep(0.5)
            player_turn_result = player.player_turn(opponent, False)
            # Recover CPU health based on result of CPU's turn
            opponent.action_block(player_turn_result)
            if opponent.health <= 0:
                player_win_text(player, opponent)
                break
            # Decrease CPU defence
            opponent.punch_defence -= 1
            opponent.kick_defence -= 1
            if opponent.block_lvl == 3:
                opponent.punch_defence -= 1
                opponent.kick_defence -= 1
            # Passes to CPU's turn
            turn_type = CPU_TURN
        else:
            print("Unknown turn type.")
        time.sleep(2)
        

# Stats function: displays fighter stats for the user
def fighter_stats():
    while True:
        # Prints list of fighters for user to choose from
        time.sleep(1)
        print("\nChoose a fighter to see their stats.")
        print(f"EASY1: Stats for {cpu_easy_1.name}, difficulty {cpu_easy_1.difficulty}.")
        print(f"EASY2: Stats for {cpu_easy_2.name}, difficulty {cpu_easy_2.difficulty}.")
        print(f"MED1: Stats for {cpu_medium_1.name}, difficulty {cpu_medium_1.difficulty}.")
        print(f"MED2: Stats for {cpu_medium_2.name}, difficulty {cpu_medium_2.difficulty}.")
        print(f"MED3: Stats for {cpu_medium_3.name}, difficulty {cpu_medium_3.difficulty}.")
        print(f"MED4: Stats for {cpu_medium_4.name}, difficulty {cpu_medium_4.difficulty}.")
        print(f"HARD1: Stats for {cpu_hard_1.name}, difficulty {cpu_hard_1.difficulty}.")
        print(f"HARD2: Stats for {cpu_hard_2.name}, difficulty {cpu_hard_2.difficulty}.")
        print(f"HARD3: Stats for {cpu_hard_3.name}, difficulty {cpu_hard_3.difficulty}.")
        print(f"HARD4: Stats for {cpu_hard_4.name}, difficulty {cpu_hard_4.difficulty}.")
        print(f"DEAD1: Stats for {cpu_deadly_1.name}, difficulty {cpu_deadly_1.difficulty}.")
        print(f"DEAD2: Stats for {cpu_deadly_2.name}, difficulty {cpu_deadly_2.difficulty}.")
        print("PLAYER: Base stats for Player Fighter.")
        print("MENU: Return to the Main Menu")
        # Checks that user input is valid
        option_list = ["easy1", "easy2", "easy3", "easy4", "med1", "med2", "med3", "med4", "hard1", "hard2", "hard3", "hard4", "dead1", "dead2", "player", "menu"]
        stat_input = input(">")
        while stat_input.lower() not in option_list:
            stat_input = input("Invalid input, try again. >")
        print()
        time.sleep(1)
        # Prints fighter stats or goes back to the main menu depending on user input
        if stat_input.lower() == "menu":
            print("Returning to the Main Menu...\n")
            time.sleep(2)
            break
        elif stat_input.lower() == "player":
            player = PlayerFighter()
            player.print_stats()
            input("Press Enter >")
            time.sleep(1)
        elif stat_input.lower() == "easy1":
            cpu_easy_1.print_stats()
            input("Press Enter >")
            time.sleep(1)
        elif stat_input.lower() == "easy2":
            cpu_easy_2.print_stats()
            input("Press Enter >")
            time.sleep(1)
        elif stat_input.lower() == "med1":
            cpu_medium_1.print_stats()
            input("Press Enter >")
            time.sleep(1)
        elif stat_input.lower() == "med2":
            cpu_medium_2.print_stats()
            input("Press Enter >")
            time.sleep(1)
        elif stat_input.lower() == "med3":
            cpu_medium_3.print_stats()
            input("Press Enter >")
            time.sleep(1)
        elif stat_input.lower() == "med4":
            cpu_medium_4.print_stats()
            input("Press Enter >")
            time.sleep(1)
        elif stat_input.lower() == "hard1":
            cpu_hard_1.print_stats()
            input("Press Enter >")
            time.sleep(1)
        elif stat_input.lower() == "hard2":
            cpu_hard_2.print_stats()
            input("Press Enter >")
            time.sleep(1)
        elif stat_input.lower() == "hard3":
            cpu_hard_3.print_stats()
            input("Press Enter >")
            time.sleep(1)
        elif stat_input.lower() == "hard4":
            cpu_hard_4.print_stats()
            input("Press Enter >")
            time.sleep(1)
        elif stat_input.lower() == "dead1":
            cpu_deadly_1.print_stats()
            input("Press Enter >")
            time.sleep(1)
        elif stat_input.lower() == "dead2":
            cpu_deadly_2.print_stats()
            input("Press Enter >")
            time.sleep(1)

# A small reward for players who defeat all Hard & Deadly opponents
def secret():
    print(f"Enter the secret code obtained by defeating {cpu_hard_1.name}.")
    secret_input = input(">")
    if secret_input.upper() != cpu_secret_codes[cpu_hard_1]:
        time.sleep(2)
        print("Incorrect. Returning to Main Menu...")
        time.sleep(2)
        return
    print(f"Enter the secret code obtained by defeating {cpu_hard_2.name}.")
    secret_input = input(">")
    if secret_input.upper() != cpu_secret_codes[cpu_hard_2]:
        time.sleep(2)
        print("Incorrect. Returning to Main Menu...")
        time.sleep(2)
        return
    print(f"Enter the secret code obtained by defeating {cpu_hard_3.name}.")
    secret_input = input(">")
    if secret_input.upper() != cpu_secret_codes[cpu_hard_3]:
        time.sleep(2)
        print("Incorrect. Returning to Main Menu...")
        time.sleep(2)
        return
    print(f"Enter the secret code obtained by defeating {cpu_hard_4.name}.")
    secret_input = input(">")
    if secret_input.upper() != cpu_secret_codes[cpu_hard_4]:
        time.sleep(2)
        print("Incorrect. Returning to Main Menu...")
        time.sleep(2)
        return
    print(f"Enter the secret code obtained by defeating {cpu_deadly_1.name}.")
    secret_input = input(">")
    if secret_input.upper() != cpu_secret_codes[cpu_deadly_1]:
        time.sleep(2)
        print("Incorrect. Returning to Main Menu...")
        time.sleep(2)
        return
    print(f"Enter the secret code obtained by defeating {cpu_deadly_2.name}.")
    secret_input = input(">")
    if secret_input.upper() != cpu_secret_codes[cpu_deadly_2]:
        time.sleep(2)
        print("Incorrect. Returning to Main Menu...")
        time.sleep(2)
        return
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("Congratulations! Have a banana!")
    time.sleep(2)
    print(" _")
    print("//\\")
    print("V  \\")
    print(" \  \_")
    print("  \,'.`-.")
    print("  |\ `. `.   ")    
    print("  ( \  `. `-.                        _,.-:\\")
    print("   \ \   `.  `-._             __..--' ,-';/")
    print("    \ `.   `-.   `-..___..---'   _.--' ,'/")
    print("     `. `.    `-._        __..--'    ,' /")
    print("       `. `-_     ``--..''       _.-' ,'")
    print("         `-_ `-.___        __,--'   ,'")
    print("            `-.__  `----\"\"\"    __.-'")
    print("                  `--..____..--'")
    time.sleep(1)
    print("\nThanks for playing Just A Fighting Game! :)")
    input("Press Enter >")


# Main Script

# Introduction
print("\n\nWelcome to Just A Fighting Game!")
print("For information on how the game works, see the Game Manual text file.")
input("Press Enter >")
time.sleep(1)
print("\nAvailable inputs will be in caps & are case insensitive.")
print("Input prompts will be indicated by the > symbol.")
print("MENU: Proceed to the main menu")
misc_input = ""
while misc_input.lower() != "menu":
    misc_input = input(">")

# Main Menu Loop
while True:
    time.sleep(0.5)
    print("\nMain Menu:")
    print("FIGHT: Start the fight already!")
    print("STATS: The lowdown on all the fighters.")
    print("SECRET: Let's be honest, this isn't very secret.")
    print("EXIT: Get me out of here!")
    menu_input = input(">")
    if menu_input.lower() == "fight":
        turn_type = PLAYER_TURN
        fight()
    elif menu_input.lower() == "stats":
        fighter_stats()
    elif menu_input.lower() == "secret":
        secret()
    elif menu_input.lower() == "exit":
        break

