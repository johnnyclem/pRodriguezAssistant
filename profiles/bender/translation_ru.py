# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# project: pRodriguezAssistant

class AudioAndTTS:
    cloud_tts = None
    offline_tts = 'espeak -p 65 -s 120 -v ru '

    answers = {
        **dict.fromkeys(['reboot', 'shutdown'],
                        (('with_bjah1', 'with_bjah2'), 
                        ('Для Бендера места нет? Ладно, я построю свой лунный модуль с блэкджеком и шлюхами!',
                        'Асталависта мешок мяса!'))),
        'exit': (('lets_get_drunk'), 
                ('Пошли напьёмся.')),
        'confirmation': (('dream_on_skintube'),
                        ('Мечтай кусок мяса!')),
        'confirmed': (('allright'),
                    ('Ладно.')),
        'hey bender': (('bite', 'hello', 'hello_peasants'), 
                    ('Укуси мой блестящий металлический зад!', 'Здорово плебеи!', 'Привет мешок мяса!')),
        'birthplace': (('born_in_tijuana'),
                    ('Я родился в злачном мексиканском городишке, на сборочной линии.')),
        'birthdate': (('birthdate'),
                    ('Четыре года назад.')),
        'who are you': (('im_bender', 'bender_song', 'my_name_is_coilette'),
                    ('Я - Бендер', 'Меня зовут Коллет', 'Я Титаниус Инглсмит!')),
        'animal': (('turtle'),
                ('Черепашка.')),
        'body': (('bodies'),
                ('Тела нужны шлюхам и толстякам.')),
        'bad girl': (('bad_girl'),
                    ('Ты плохая девочка, да?')),
        'sing': (('bender_song'), None),
        'magnet': (('roads_song', 'mountain_song'), None),
        'new sweater': (('new_sweater'),
                    ('Новый?! Какой свитер? Я в нём пришёл! Я вас не знаю люди.')),
        'fall asleep': (('kill_all_humans_1', 'kill_all_humans_2'),
                    ('Убей всех человекоа... Должен убить всех человеков...', 'Эй детка, Хочешь убить всех человеков?')),
        'wake up': (('most_wonderful_dream'),
                ('Мне приснился чудесный сон! И ты там был!')),
        **dict.fromkeys(['enable', 'disable','set', 'configuration', 'player'], 
                        (('can_do', 'yes_sir'),
                        ('Будет сделано!', 'Да сэр!'))),
        'how are you': (('none_of_your_business', 'right_now_i_feel_sorry_for_you', 'so_embarrassed'),
                    ('Не твоё дело!', 'Сейчас я сочувствую тебе.', 'Мне так стыдно, хочу чтоб все умерли.')),
        'electricity': (('plugged_in'), None),
        'unrecognized': (('beat_children', 'compare_your_lives_to_mine'),
                        ('Если хочешь избить детей, сделай это сам.', 'Сравните свои жизни с моей, а затем убейте себя!')),
        'repeated keyphrase': (('im_in_a_hurry'),
                            ('Слушай парень, я тороплюсь')),
        'wait you are serious': (('ow_wait_youre_serious'),
                                ('О, ты серьёзно, тогда я буду смеяться ещё сильнее. Ахахахахаха!')),
        'laugh': (('laugh'),
                ('Хахаха')),
        'no audio': (('silence'), None)
    }

class STTTranslatorRU:

    tr_start_ru_en  = {
        u'бендер': 'bender',
        u'привет бендер': 'hi bender',
        u'эй бендер': 'hi bender',
        u'бендер пауза': 'bender pause',
        u'привет бендер пауза': 'bender pause',
        u'эй бендер пауза': 'bender pause'
    }

    tr_conversation_ru_en =  {
        **tr_start_ru_en,
        u'громче': 'increase volume',
        u'погромче': 'increase volume',
        u'тише': 'decrease volume',
        u'потише': 'decrease volume',
        u'включи плеер': 'start player',
        u'старт плеера': 'start player',
        u'отключи плеер': 'stop player',
        u'стоп плеера': 'stop player',
        u'следующий трек': 'next song',
        u'следующий трэк': 'next song',
        u'следующая песня': 'next song',
        u'спой песню': 'sing a song',
        u'откуда ты': 'where are you from',
        u'где ты родился': 'where are you from',
        u'когда ты родился': 'when were you born',
        u'дата рождения': 'when were you born',
        u'какое твоё любимое животное': 'what is your favorite animal',
        u'какой твой любимый зверь': 'what is your favorite animal',
        u'кто ты': 'who are you',
        u'как ты': 'how are you',
        u'как поживаешь': 'how are you',
        u'как ты живёшь без тела': 'how can you live without a body',
        u'что думаешь об алексе': 'what do you think about alexa',
        u'что ты думаешь об алексе': 'what do you think about alexa',
        u'что думаешь об алисе': 'what do you think about alice',
        u'что ты думаешь об алисе': 'what do you think about alice',
        u'что думаешь о кортане': 'what do you think about cortana',
        u'что ты думаешь о кортане': 'what do you think about cortana',
        u'что думаешь о сири': 'what do you think about siri',
        u'что ты думаешь о сири': 'what do you think about siri',
        u'магнит': 'magnet',
        u'хороший новый свитер': 'a great new sweater',
        u'выключение': 'shutdown',
        u'стоп': 'stop',
        u'пока': 'stop',
        u'включи сон': 'enable sleep',
        u'отключи сон': 'disable sleep',
        u'включи засыпание': 'enable sleep',
        u'отключи засыпание': 'disable sleep',
        u'выход из программы': 'exit the program'
    }
