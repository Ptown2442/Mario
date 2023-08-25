import pygame

menu_map = [(75, 100), (130, 300), (200, 250), (325, 400)]

level_0 = {
        'boundaries': 'levels/0/level0_boundaries.csv',
        'coins' : 'levels/0/level0_coins.csv',
        'enemies' : 'levels/0/level0_enemies.csv',
        'player' : 'levels/0/level0_player.csv',
        'terrain' : 'levels/0/level0_terrain.csv',
        'trees' : 'levels/0/level0_trees.csv'}

level_1 = {
        'boundaries': 'levels/0/level1_boundaries.csv',
        'coins': 'levels/0/level1_coins.csv',
        'enemies': 'levels/0/level1_enemies.csv',
        'player': 'levels/0/level1_player.csv',
        'terrain': 'levels/0/level1_terrain.csv',
        'trees': 'levels/0/level1_trees.csv'}

level_2 = {
        'boundaries': 'levels/0/level2_boundaries.csv',
        'coins': 'levels/0/level2_coins.csv',
        'enemies': 'levels/0/level2_enemies.csv',
        'player': 'levels/0/level2_player.csv',
        'terrain': 'levels/0/level2_terrain.csv',
        'trees': 'levels/0/level2_trees.csv'}

level_3 = {
        'boundaries': 'levels/0/level3_boundaries.csv',
        'coins': 'levels/0/level3_coins.csv',
        'enemies': 'levels/0/level3_enemies.csv',
        'player': 'levels/0/level3_player.csv',
        'terrain': 'levels/0/level3_terrain.csv',
        'trees': 'levels/0/level3_trees.csv'}

level0 = {'node_pos':(110,400), 'content': level_0, 'unlock':1}
level1 = {'node_pos':(300,220), 'content': level_1, 'unlock':2}
level2 = {'node_pos':(480,610), 'content': level_2, 'unlock':3}
level3 = {'node_pos':(610,350), 'content': level_3, 'unlock':4}
level4 = {'node_pos':(830,210), 'content': level_2, 'unlock':5}
level5 = {'node_pos':(960,400), 'content': level_3, 'unlock':5}

levels = {
        0: level0,
        1: level1,
        2: level2,
        3: level3,
        4: level4,
        5: level5}

current_level = 0
tile_size = 64
screen_width = 1200
screen_height = 704