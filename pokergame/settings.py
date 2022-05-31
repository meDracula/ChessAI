# Defined color (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)

# Team color Orange:
BLUE = (0, 0, 255)
PLANE_BLUE = (51, 51, 255)

# Team color Orange:
ORANGE = (255, 128, 0)
PLANE_ORANGE = (255, 153, 51)

# game settings
WIDTH = 1024  # 16 * 64 or 32 * 32 or 64 * 16 -> Tile size * map Tiles
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12 -> Tile size * map Tiles
FPS = 30
TITLE = "POKER"
BGCOLOR = DARKGREY
STARTING_TEAM = 'orange'  # orange or blue

# Players
DEFUALT_AMOUNT_PLAYERS = 2 # Maxium amount of players is 4
DEFUALT_PLAYER_NAMES = "Batman", "Joker", "Harley", "Bane"
DEFUALT_BOT = "POKERAI"

# Home dir
DIR = ""

# leaderboard file
LEADERBOARD_SAVE = DIR + "leaderboard_save.data"


# images
BOARD = DIR + 'assets/poker_board.png'
MENU = DIR + 'assets/menu-icon.png'
NUMBER_2 = DIR + 'assets/number_2.png'
NUMBER_3 = DIR + 'assets/number_3.png'
NUMBER_4 = DIR + 'assets/number_4.png'

TILESIZE = 64  # 64, 32, 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
TILESIZE_OFFSET = 10
MENU_TEXT = 'TESTING'
CALL_TEXT = 'CALL'
FOLD_TEXT = 'FOLD'
LEADERBOARD = 'Leaderboards'
EXIT_GAME = 'Exit Game'
NEW_GAME = 'New Game'
NUMBER_OF_PLAYERS = 'Number Of Players'


# cards

CARDWIDHT = 60
CARDHEIGHT = 90
ace_of_clubs = DIR + 'assets/ace of clubs.png'
ace_of_spades = DIR + 'assets/ace of spades.png'
ace_of_hearts = DIR + 'assets/ace of hearts.png'
ace_of_diamonds = DIR + 'assets/ace of diamonds.png'

eight_of_clubs = DIR + 'assets/eight of clubs.png'
eight_of_spades = DIR + 'assets/eight of spades.png'
eight_of_hearts = DIR + 'assets/eight of hearts.png'
eight_of_diamonds = DIR + 'assets/eight of diamonds.png'

five_of_clubs = DIR + 'assets/five of clubs.png'
five_of_spades = DIR + 'assets/five of spades.png'
five_of_hearts = DIR + 'assets/five of hearts.png'
five_of_diamonds = DIR + 'assets/five of diamonds.png'

four_of_clubs = DIR + 'assets/four of clubs.png'
four_of_spades = DIR + 'assets/four of spades.png'
four_of_hearts = DIR + 'assets/four of hearts.png'
four_of_diamonds = DIR + 'assets/four of diamonds.png'

jack_of_clubs = DIR + 'assets/jack of clubs.png'
jack_of_spades = DIR + 'assets/jack of spades.png'
jack_of_hearts = DIR + 'assets/jack of hearts.png'
jack_of_diamonds = DIR + 'assets/jack of diamonds.png'

king_of_clubs = DIR + 'assets/king of clubs.png'
king_of_spades = DIR + 'assets/king of spades.png'
king_of_hearts = DIR + 'assets/king of hearts.png'
king_of_diamonds = DIR + 'assets/king of diamonds.png'

nine_of_clubs = DIR + 'assets/nine_of_clubs.png'
nine_of_spades = DIR + 'assets/nine_of_spades.png'
nine_of_hearts = DIR + 'assets/nine_of_hearts.png'
nine_of_diamonds = DIR + 'assets/nine_of_diamonds.png'

queen_of_clubs = DIR + 'assets/queen_of_clubs.png'
queen_of_spades = DIR + 'assets/queen_of_spades.png'
queen_of_hearts = DIR + 'assets/queen_of_hearts.png'
queen_of_diamonds = DIR + 'assets/queen_of_diamonds.png'

seven_of_clubs = DIR + 'assets/seven_of_clubs.png'
seven_of_spades = DIR + 'assets/seven_of_spades.png'
seven_of_hearts = DIR + 'assets/seven_of_hearts.png'
seven_of_diamonds = DIR + 'assets/seven_of_diamonds.png'

six_of_clubs = DIR + 'assets/six_of_clubs.png'
six_of_spades = DIR + 'assets/six_of_spades.png'
six_of_hearts = DIR + 'assets/six_of_hearts.png'
six_of_diamonds = DIR + 'assets/six_of_diamonds.png'

ten_of_clubs = DIR + 'assets/ten_of_clubs.png'
ten_of_spades = DIR + 'assets/ten_of_spades.png'
ten_of_hearts = DIR + 'assets/ten_of_hearts.png'
ten_of_diamonds = DIR + 'assets/ten_of_diamonds.png'

three_of_clubs = DIR + 'assets/three_of_clubs.png'
three_of_spades = DIR + 'assets/three_of_spades.png'
three_of_hearts = DIR + 'assets/three_of_hearts.png'
three_of_diamonds = DIR + 'assets/three_of_diamonds.png'

two_of_clubs = DIR + 'assets/two_of_clubs.png'
two_of_spades = DIR + 'assets/two_of_spades.png'
two_of_hearts = DIR + 'assets/two_of_hearts.png'
two_of_diamonds = DIR + 'assets/two_of_diamonds.png'


# Directory for player scripts
DIRECTORY = 'scripts'
