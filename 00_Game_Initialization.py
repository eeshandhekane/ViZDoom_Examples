# Dependencies
from vizdoom import DoomGame # The game class, which forms an interface between the game and the agent
from vizdoom import Button # The enumeration for the actions that the agent can 'press'
from vizdoom import GameVariable # The enumeration for the game information, such as the health and the ammo count of the agent
from vizdoom import ScreenFormat # The enumeration for the screen formats
from vizdoom import ScreenResolution # The enumeration for the screen resolutions

import os

####################################################################################################
# Game Loading
####################################################################################################
# Create a game instance
game = DoomGame()
# A game scenario in doom represents how a world looks like and works
# The sample path can be set to the following address or its equivalent, where the "scenarios" directory in ViZDoom resides
scenario_path = '/Users/eeshan/ViZDoom/scenarios'
basic_scenario_path = os.path.join(scenario_path, 'basic.wad')
game.set_doom_scenario_path(basic_scenario_path)
# A scenario might contain multiple maps and we need to set the exact one
doom_map = 'map01'
game.set_doom_map(doom_map)


####################################################################################################
# Screen Rendering Options
####################################################################################################
# Set the screen resolution. There are several options-- check and fill!
game.set_screen_resolution(ScreenResolution.RES_1024X576)
# Set the screen format. There are several options-- check and fill! 
game.set_screen_format(ScreenFormat.RGBA32)
# Whether to render the HUD. (H)eads (U)p (D)isplay is the UI that displays all the vital info of the agent, such as ammo and health
game.set_render_hud(True)
# Whether to render the cross-hair
game.set_render_crosshair(True)
# Whether to render the weapon
game.set_render_weapon(True)
# Whether to render the decals, which are the materials projected on existing surfaces. An example is the bullet impact markers
game.set_render_decals(True)
# Whether to render the particles, which form effects like the muzzle smoke after bullet shots
game.set_render_particles(True)


####################################################################################################
# Add Buttons
####################################################################################################
"""
We can add specific buttons in the following manner--
game.add_available_button(Button.MOVE_LEFT)
However, there are many buttons that are available and a vast amounts of things can be done in the game
For example, move left/move right/duck/drop weapon/select a particular weapon etc.
To see the whole list, we can use the following command--
print(dir(Button))
For now, we will only add buttons for moving and shooting
"""
# Add button to move left
game.add_available_button(Button.MOVE_LEFT)
# Add button to move right
game.add_available_button(Button.MOVE_RIGHT)
# Add button to move front
game.add_available_button(Button.MOVE_FORWARD)
# Add button to move back
game.add_available_button(Button.MOVE_BACKWARD)
# Add button to move up
game.add_available_button(Button.MOVE_UP)
# Add button to move down
game.add_available_button(Button.MOVE_DOWN)
# There is no point to the game if we can not shoot! Add button to shoot
game.add_available_button(Button.ATTACK)


####################################################################################################
# Game Variables
####################################################################################################
"""
We can extract specific game variables, like the ammo and the health of the agent, to be included in the game state
We make this convenient by adding the variables explicitly to the game
Any variable can be acquired anytime in the game, but it is convenient nonetheless to add them to the state
There are a huge number of game variables available, which can be checked with the following command--
print(dir(GameEnvironment))
A specific variable can be included in the following manner--
game.add_available_game_variable(GameVariable.AMMO1)
For now, we will only add the pistol ammo. One needs to check which variable represents what
"""
# Add variable for pistol ammo
game.add_available_game_variable(GameVariable.AMMO2)


####################################################################################################
# Episode Properties
####################################################################################################
# Set episode length
game.set_episode_timeout(200)
# We can also set a start time, which is the number of ticks ommitted by the game, but still run by the engine
game.set_episode_start_time(5)


####################################################################################################
# Window Visibility
####################################################################################################
# Set the window visible
game.set_window_visible(True)


####################################################################################################
# Reward Setting
####################################################################################################
# Set the living reward per tick to be -1, which forces the agent to do something quickly while running an RL algo
game.set_living_reward(0)


####################################################################################################
# Start Game
####################################################################################################
"""
Initialize the game, after which the window should appear (and quickly, disappear)!
This can be just done for checking the correctness of the script, nothing else, as follows--
game.init()
We need to write a game loop for doing something in the game
"""
# Initialize the game
game.init()


####################################################################################################
# Episodes
####################################################################################################
"""
Doom game is run in episodes. Each episode is basically an independent run of the game, carried out sequentially
We need to create a new episode everytime we want to play and then, write a game loop for the episode
The code contains a method to check the termination of the episode, called game.is_episode_finished()
This can be exploited to run the game loop
"""
# Set the number of episodes
num_episodes = 1
# For each episode count ...
for an_episode in range(num_episodes) :
	# Create a new episode
	game.new_episode()
	# Run a simple loop while the episode does not last
	while not game.is_episode_finished() :
		# Get the state from the game state
		current_state = game.get_state()
		# Get the statistics from the state
		number = current_state.number # State number
		game_variables = current_state.game_variables # Game variables
		screen_buffer = current_state.screen_buffer # The screen buffer 
		depth_buffer = current_state.depth_buffer # The depth buffer
		labels_buffer = current_state.labels_buffer # The label buffer
		automap_buffer = current_state.automap_buffer # The automap buffer
		labels = current_state.labels # The labels information
		print('[INFO] number : ', number)		
		print('[INFO] game_variables : ', game_variables)
		print('[INFO] screen_buffer : ', screen_buffer)
		print('[INFO] depth_buffer : ', depth_buffer)
		print('[INFO] labels_buffer : ', labels_buffer)
		print('[INFO] automap_buffer : ', automap_buffer)
		print('[INFO] labels : ', labels)		


####################################################################################################
# Terminate Game
####################################################################################################
# Terminate the game
game.close()