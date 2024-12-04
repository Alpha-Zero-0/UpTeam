################
# Player Setup #
################
class Player:
    def __init__(self):
        self.name = ''
        self.confidence = 0
        self.problem_solving = 0
        self.networking = 0
        self.energy_tokens = 10
        self.position = 'ground'
        self.won = False
        self.solves = 0

player1 = Player()

#############
# Game Setup #
#############
def start_game():
    print("#############################################")
    print("# Welcome to upTeam's Social Mobility RPG!  #")
    print("#############################################")
    create_character()

def create_character():
    print("Character Creation:")
    player1.name = input("Enter your character's name: ")
    allocate_points()
    print(f"Welcome, {player1.name}! Your journey begins now.")
    # Proceed to the first level
    level_1()

def allocate_points():
    points = 10
    while points > 0:
        print(f"You have {points} points to allocate.")
        player1.confidence += int(input("Allocate points to Confidence: "))
        player1.problem_solving += int(input("Allocate points to Problem-Solving: "))
        player1.networking += int(input("Allocate points to Networking: "))
        points -= (player1.confidence + player1.problem_solving + player1.networking)
        if points < 0:
            print("You have allocated too many points. Try again.")
            points += (player1.confidence + player1.problem_solving + player1.networking)
            player1.confidence = 0
            player1.problem_solving = 0
            player1.networking = 0

def level_1():
    print("Level 1: Insight Day – The Gate of Knowledge")
    print("You’ve entered Insight Day Isle, where the fog of ignorance looms.")
    # Implement sub-bosses and main boss encounters here
    # Example:
    encounter_kpmgrasp()

def encounter_kpmgrasp():
    print("Encounter: KPMGrasp – A shadowy figure hoarding knowledge.")
    while True:
        action = input("Choose your action (Attack/Defend/Special): ").lower()
        if action == "attack":
            print("You use Problem-Solving to present clear evidence.")
            # Implement attack logic
        elif action == "defend":
            print("You defend against KPMGrasp's attack.")
            # Implement defend logic
        elif action == "special":
            print("You use a special skill.")
            # Implement special skill logic
        else:
            print("Invalid action. Try again.")
        # Check for win/lose conditions

# Start the game
start_game()
		time.sleep(0.05)
	for character in speech6:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.2)
	time.sleep(1)

	os.system('clear')
	print("################################")
	print("# Here begins the adventure... #")
	print("################################\n")
	print("You find yourself in the center of a strange place.\nSeems like you are trapped in a little box.\n")
	print("Every inside face of the box seems to have a different theme.\nHow can you get out of this...\n")
	print("You notice objects standing sideways on the walls.\nDoes gravity not apply? There are clouds though...")
	main_game_loop()


title_screen()
