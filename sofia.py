# MODULE: SOFIA / Main program
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2020 		(http://www.kateliev.com)
#------------------------------------------------------------
# https://kateliev.github.io/sofia/

# No warranties. By using this you agree
# that you use it at your own risk!

# - Dependencies ------------------------
from __future__ import print_function

import os, sys, json
from lib.io import *

# - Init --------------------------------
__version__ = '0.0.1'

basePath = os.getcwd()
run_args = sys.argv[1:]

clear_screen = '\033[H\033[J'

# - Main --------------------------------
if '--play' in run_args:
	play_path = run_args[run_args.index('--play') + 1]
	play_game = json.load(open(play_path, 'r'), cls=io_json_decoder)
	
	game_setting = play_game.game_setting
	game_ego = game_setting.actors.ego

	print(clear_screen)
	print('{}\n{}'.format(play_game.game_name, play_game.game_version))
	raw_input('Press ENTER to continue...')
	
	print(clear_screen)
	print(game_setting.rooms[game_ego.location])