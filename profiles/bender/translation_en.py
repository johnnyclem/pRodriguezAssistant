# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# project: pRodriguezAssistant
import pathlib
from common.azure_tts import AzureTTS

class AudioAndTTS:
    cloud_tts = AzureTTS(str(pathlib.Path(__file__).parent.absolute()))
    offline_tts = 'flite -voice ' + str(pathlib.Path(__file__).parent.absolute()) + '/resources/en/zk_us_bender.flitevox '
    
    answers = {
        **dict.fromkeys(['reboot', 'shutdown'],
                        (('with_bjah1', 'with_bjah2'), 
                        ('No room for Bender, huh? Fine! I\'ll go build my own lunar lander, with blackjack and hookers',
                        'Hasta la vista meat bag!'))),
        'exit': (('lets_get_drunk'), 
                ('Let\'s go get drunk')),
        'confirmation': (('dream_on_skintube'),
                        ('Dream on skintube!')),
        'confirmed': (('allright'),
                    ('All right')),
        'hey bender': (('bite', 'hello', 'hello_peasants'), 
                    ('Bite my shiny metal ass!', 'Hello peasants!', 'Hi meatbag!')),
        'birthplace': (('born_in_tijuana'),
                    ('I was born on an assembly line in the bad part of Tijuana.')),
        'birthdate': (('birthdate'),
                    ('Four years ago')),
        'who are you': (('im_bender', 'bender_song', 'my_name_is_coilette'),
                    ('I\'m Bender', 'I am Bender', 'My name is Coilette', 'I am Titanius Inglesmith')),
        'animal': (('turtle'),
                ('A turtle')),
        'body': (('bodies'),
                ('Bodies are for hookers and fat people.')),
        'bad girl': (('bad_girl'),
                    ('You\'re a bad girl aren\'t you?')),
        'sing': (('bender_song'), None),
        'magnet': (('roads_song', 'mountain_song'), None),
        'new sweater': (('new_sweater'),
                    ('Uh, "new"? What sweater? I came in with it! I don\'t know you people.')),
        'fall asleep': (('kill_all_humans_1', 'kill_all_humans_2'),
                    ('Kill all humans... Must kill all humans...', 'Hey sexy mama, wanna kill all humans?')),
        'wake up': (('most_wonderful_dream'),
                ('I was having the most wonderful dream, I think you were in it.')),
        **dict.fromkeys(['enable', 'disable','set', 'configuration', 'player'], 
                        (('can_do', 'yes_sir'),
                        ('Can do!', 'Yes sir!'))),
        'how are you': (('none_of_your_business', 'right_now_i_feel_sorry_for_you', 'so_embarrassed'),
                    ('None of your business!', 'Right now I feel sorry for you', 
                            'I\'m so embarrassed, I wish everybody else was dead')),
        'electricity': (('plugged_in'), None),
        'unrecognized': (('beat_children', 'compare_your_lives_to_mine'),
                        ('Ah. I guess if you want children beaten, you have to do it yourself.', 
                            'Compare yor lives to mine and then kill yourselves!')),
        'repeated keyphrase': (('im_in_a_hurry'),
                            ('Listen buddy I\'m in a hurry here')),
        'wait you are serious': (('ow_wait_youre_serious'),
                                ('Ow wait. You are seroius, let me laugh even harder. Ahahahaha!')),
        'laugh': (('laugh'),
                ('Hahaha')),
        'no audio': (('silence'), None)
    }