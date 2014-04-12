# Variables used throughout
# Think of them as "Global-ish"

"""Settings"""
settingList = []

SFX = 0
MUSIC = 1
PARTICLES = 2
WORLD_UNLOCKED = 3
SENSITIVITY = 4
SETTING_FULLSCREEN = 5

"""MUSIC"""
MENU_MUSIC = 0
WORLD_ONE = 1
WORLD_TWO = 2
WORLD_THREE = 3
BOSS_MUSIC = 4

"""Screen resolution stuff here"""
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FULLSCREEN = True
ANTI_ALIAS = True
MOUSE_DEFAULT_POSITION = (512, 384)

FRAMES_PER_SECOND = 30.0

"""Sound Channel Constants"""
MUSIC_CHANNEL = 0
PLAYER_CHANNEL = 1
OW_CHANNEL = 2
BAAKE_CHANNEL = 3
BOSS_CHANNEL = 4
PICKUP_CHANNEL = 5
"""Boundary Stuff here"""
LEFT = 0
TOP = 1
RIGHT = 2
BOTTOM = 3

BOUND_STYLE_NONE = 0
BOUND_STYLE_CLAMP = 1
BOUND_STYLE_WRAP = 2
BOUND_STYLE_REFLECT = 3
BOUND_STYLE_KILL = 4
BOUND_STYLE_CUSTOM = 5

"""Bullet constants"""
COLLIDE_STYLE_HURT = 0
COLLIDE_STYLE_REFLECT = 1
COLLIDE_STYLE_NOVA = 2
COLLIDE_STYLE_NONE = 3

BULLET_SPEED = 30

"""Actor types, for use in spawning"""
ACTOR_PLAYER = 0
ACTOR_BULLET = 1

ACTOR_MOONO = 2

ACTOR_BAAKE = 3
ACTOR_ROKUBI = 4
ACTOR_BATTO = 5
ACTOR_HAOYA = 6

ACTOR_BOKKO = 7
ACTOR_HAKTA = 8
ACTOR_RAAYU = 9
ACTOR_PAAJO = 10

ACTOR_YUREI = 11

ACTOR_BOSS_TUT = 12
ACTOR_BAAKE_BOSS = 13
ACTOR_MOONO_BOSS = 14

"""Actor types, for use in collision"""
#ACTOR_PLAYER = 0
#ACTOR_BULLET = 1
ACTOR_TYPE_ENEMY = 2
ACTOR_TYPE_BAAKE = 3
ACTOR_TYPE_PICKUP = 4
ACTOR_TYPE_BOSS = 5

"""Menu Constants"""
START_GAME = True
EXIT_GAME = False

"""Font alignment enumerations"""
TOP_LEFT = 0
TOP_MIDDLE = 1
TOP_RIGHT = 2
CENTER_LEFT = 3
CENTER_MIDDLE = 4
CENTER_RIGHT = 5
BOTTOM_LEFT = 6
BOTTOM_MIDDLE = 7
BOTTOM_RIGHT = 8

"""Menu Enumberations"""
START_GAME = 1
WORLD_MENU = 2
OPTION_MENU = 3
CREDIT_MENU = 4
EXIT_GAME = 9
RESUME_GAME = 1

WORLD1 = 2
WORLD2 = 3
WORLD3 = 4
TUTORIAL = 1

SOUND_MENU = 2
DISPLAY_MENU = 1

TOGGLE_SFX = 1
TOGGLE_MUSIC = 2
TOGGLE_PARTICLES = 1
TOGGLE_FULLSCREEN = 2
CHANGE_SENSITIVITY = 4
EXIT_OPTIONS = 9

ENABLE_JOYSTICK = 1
ENABLE_MOUSE = 2
ENABLE_KEYBOARD = 3

NEXT_WORLD = 2
HIGH_SCORE = 1

"""Define font path"""
FONT_PATH = "data/fonts/SF Espresso Shack Bold.ttf"

"""Define a fill color RGB"""
FILL_COLOR = 233,234,187
FONT_COLOR = 43,37,22
FONT_INACTIVE_COLOR = 125,108,65

"""World Constants"""
DEFEAT_STAGE = 15 * FRAMES_PER_SECOND

"""Group enumerations"""
POWERUP_GROUP = 0
ENEMY_GROUP = 1
BOSS_GROUP = 2
TEXT_GROUP = 3
EFFECTS_GROUP = 4

"""Temporary Enumerations for how many stages/levels are in the game"""
MAX_STAGE = 3 #+1 for a total of four stages
MAX_LEVEL = 4 #+1 for a total of four levels
MAX_WORLD = 3 #+1 for a total of four worlds

""" Enumerations for actor_list """
STAGE_SPAWNED = 0
ACTOR_TYPE = 1
SPAWN_RATE = 2
DEFAULT_SPAWN = 3

""" Enumerations for enemy_list """
TIME_TO_SPAWN = 0
#ACTOR_TYPE = 1
#MAX_SPAWN_RATE = 2
NUMBER_SPAWNED = 3