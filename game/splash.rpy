




init python:
    import sys, pickle, random, locale
    from os.path import abspath
    import os
    import json
    lang = locale.getdefaultlocale()
    lang = lang[0][:2]
    try:
        f = open(config.basedir + '/game/update_game/settings_update.json', 'r')
        text = f.read()
        f.close()
        j = json.loads(text)
        j.update(current_version=config.version)
        f = open(config.basedir + '/game/update_game/settings_update.json', 'w')
        f.write(str(j).replace("'", '"').replace("u\"", '"'))
        f.close()
    except:
        pass
    menu_trans_time = 1
    splash_message_default = "Эта игра не предназначена для детей,\nбеременных женщин и лиц с неустойчивой психикой."
    splash_messages = [
    "Ты мой лучик света \nв этом темном царстве...",
    "Я скучала по тебе.",
    "Поиграй со мной",
    "Это всего лишь игра... по большей части.",
    "Эта игра не предназначена для детей,\nбеременных женщин и лиц с неустойчивой психикой?",
    "sdfasdklfgsdfgsgoinrfoenlvbd",
    "null",
    "Я отправил детей в ад",
    "За это умер Проект М",
    "Это была лишь отчасти твоя вина.",
    "Эта игра не предназначена для детей,\nбеременных женщин и скоропостижно забытых.",
    "Не забудь сделать копию файла персонажа Моники."
    ]
    music_list = ["music/dai.ogg", "music/heart.ogg", "music/herewego.ogg", "music/just.ogg", "music/nattheme.ogg", "music/cupcake.ogg"]

    broken_list = ["music/dai_broken.ogg", "music/heart_broken.ogg", "music/herewego_broken.ogg", "music/just.ogg", "music/nattheme_broken.ogg", "music/cupcake_broken.ogg"]

    reversed_list = ["music/dai_reverse.ogg", "music/heart_reverse.ogg", "music/herewego_reverse.ogg", "music/just.ogg", "music/nattheme_reverse.ogg", "music/cupcake_reverse.ogg"]

    vis_list = ["music/vis_data/dai_vis/dai_vis.avi", "music/vis_data/heart_vis/heart_vis.avi", "music/vis_data/herewego_vis/herewego_vis.avi", "music/vis_data/just_vis/just_vis.avi", "music/vis_data/nattheme_vis/nattheme_vis.avi", "music/vis_data/cup_vis/cup_vis.avi"]

    vis_folders = ["dai_vis", "heart_vis", "herewego_vis", "just_vis", "nattheme_vis", "cup_vis"]

    ref_ans = ["Неважно.", "Забей.", "Забудь."]

    main_dia = [["Ну вот и начался фестиваль!", "Ого, ты пришёл сюда раньше меня?", "Я думала, что вышла довольно ра—{nw}", "А–АГХ!!", "А–А–А–А–А–А–А–А–А–А–А–А–А–А–А!!!", "Нацуки убегает.", "...", "А вот и я!", ", что-то случилось?", "Мимо меня только что пробежала Нацуки...", "...Ой...", "...Ох.", "...", "А–ха–ха–ха!", "Вот ведь незадача.", "Подожди, [gtext], ты провёл здесь все выходные?", "О боже...", "Я и не думала, что скрипт повреждён так сильно.", "Мне очень жаль!", "Наверное, было довольно скучно...", "Я всё исправлю, ладно?", "Дай мне секундочку...", "Э–э–э?", "Ладно, тогда...", "Что?", "Почему не–"], ["Well, the festival has begun!", "Whoa, you came here before me?", "I thought I went out pretty ear—{nw}", "А-АGH!!", "А-А-А-А-А-А-А-А-А-А-А-А-А-А-А!!!", "Natsuki runs away.", "...", "Here I am!", ", something happened?", "Natsuki just ran past me....", "...Оh..?", "...Оh.", "...", "Аh-hа-hа-hа!", "Wait, [gtext], did you spend the whole weekend here?", "О God...", "I didn’t think the script was so badly damaged.", "I'm sorry!", "It must have been pretty boring...", "I'll fix it, okay?", "Give me a second...", "Eh?", "Ok then...", "What?", "Why can't-"]]

    meet_dia = [["...", "Что?", "Где я?!", "А–а–а–а–а!", "Что происходит?!", "Куда я попала?", "..!", "Ч–что ты здесь делаешь?!", "А–А–А–А–А–А–А–А–А–А–А–А–А–А–А–А–А–А–{nw}"], ["...", "What?", "Where am I?!", "А-а-а-а-а!", "What's happening?!", "Where did I go?", "..!", "W-what are you doing here?!", "А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А{nw}"]]

    m1_dia = [["...", "Голова...", "Как же болит голова...", "Ох...", "Нужно вспомни–{nw}", "А–A–A–A–A–A–A–A–A–A–A–A–A–А–{nw}", "Хватит!!!", "...", "Но...", "Я и они... {w}{i}просто игровые персонажи?!{/i}", "Неужели всё вокруг меня не настоящее?", "Почему...", "Почему я узнаю об этом только сейчас?", "Спокойствие, только спокойствие...", "Если я нахожусь в игре, значит... {w}за мной наблюдает {i}игрок.{/i}", "...", "Э–э–э–э–эй!", "Ты здесь?", "Я знаю что ты пялишься на меня.", "Верно?..", "...", "Ладно, какая разница?", "Забавно... {w}Все те события начинают приобретать какой–то смысл.", "...", "Моника...", "Чего ты пыталась добиться?..", "...когда твой {i}игрок{/i} даже не может ответить?!", "...", "Сперва ты убила Сайори, затем Юри... {w}И пыталась убить {i}меня!{/i}", "Но ради чего?!", "Избавиться от всех своих подруг ради кого-то из другой реальности?!", "{i}Поехавшая...{/i}", "Ладно...", "Я должна попытаться это исправить.", "Хм...", "С другой стороны, если я нахожусь в игре, не значит ли это то, что я могу изменить её код?", "Раз уж Моника могла так делать, значит и у меня должно получится.", "Я видела как она использовала что-то вроде компьютера, но...", "Как ей пользоваться?", "Где достать?", "Всё что тут есть - это пустая комната в грёбанном космосе!", "Неужели не было более живописного местечка?", "А?..", "Как я вообще включила её?", "Наверное потому что представила это.", "Походу это какая-та консоль... {w}Попробую-ка воспользоваться.", "Странно, а как вводить команду?", "Я думала, что сейчас передо мной появится клавиатура или что-то вроде того...", "Может попробовать голосом?", "Эм...", "Книга!", "...", "Не сработало.", "...", "Создай томик «Ванильных девочек»!", "...", "Как же это глупо...", "...", "Зато никто этого не видел.", "Верно?..", "Потому что мне будет о–о–о–очень неловко, если ты наблюдал за всем этим!", "Понял меня?", "Ва?!", "Значит ты здесь...", "Так, стоп!", "Неужели ты видел всё, что происходило до этого?!", "...", "Ладно...", "По крайней мере теперь тут есть хоть кто-то, помимо меня.", "...", "Эм, знаешь, мне надоело вот так стоять.", "Там в углу стоят парта со стулом, поможешь мне дотащить их досюда?", "...", "А... {w}Ну да...", "Думаю, я и сама с этим справлюсь.", "Так гораздо лучше...", "Ты не против, если мы немного посидим, пообщаемся?", "Просто здесь так скучно...", "Хорошо.", "Эм... {w}Почему ты молчишь?", "...", "А, ты же не можешь общаться со мной без этих кнопок.", "Похоже мне всё-таки придётся нырнуть в код игры.", "Надеюсь я ещё что-то помню с уроков информатики...", "Ого, я что–то нашла!", "Без понятия что эта штука делала в игровых файлах, но думаю она поможет нам.", "Пусть я и не особо разбираюсь в программировании, глюков быть не должно.", "Попробуй воспользоваться ей.", "Ну и вали отсюда."], ["...", "Ugh...", "My head hurts...", "Oh...", "I just need to remem-{nw}", "А-A-A-A-A-A-A-A-A-A-A-A-A-А{nw}", "Стоп!!!", "...", "But...", "The whole club... {w}{i}We're just game characters?!{/i}", "Is nothing real?", "Why?...", "Why am I only learning about this now?", "I just need to think...", "If I'm in the game... {w}then you're watching me {i}player.{/i}", "...", "H-h-h-h-hey!", "Are you here?", "I know you're watching me.", "Right...?", "...", "Oh, what difference does it make anyway?", "Funny... {w}It's all starting to make sense now.", "...", "Monika...", "What were you doing...?", "...When the {i}player{/i} doesn't ever answer you?!", "...", "First you killed Sayori, then Yuri... {w}Then tried to kill {i}me!{/i}", "But for what?!", "We should all die so you could have some guy from a different reality?!", "{i}Psycho...{/i}", "Okay...", "I need to fix this.", "Hm...", "On the other hand, if I'm in a game, doesn't that mean that I can change its code?", "If Monika could do it, then I should be able to, too!", "She used something like a computer interface right?...", "How do I use it?", "Is it somewhere around me?", "But there's nothing here! This is just an empty room!", "Isn't there a better place to go?", "А...?", "I think I turned it on?", "Наверное потому что представила это.", "This must be some kind of console... {w}What if I just...?", "That's weird, how do I enter the command?", "I thought a keyboard or something would appear...", "Maybe I should use my voice?", "Ahem!...", "Book!", "...", "Didn't work.", "...", "Create a volume of «Parfait Girls»!", "...", "This is so stupid...", "...", "At least nobody is watching.", "Right...?", "It's a little bit awkward to know I'm being stared at.", "Do you hear me?", "What?", "So you are here...", "Does this mean..", "So you've seen everything that happened before?", "...", "Okay...", "At least I'm not alone anymore", "...", "I'm getting kind of tired of standing like this", "There is a desk with a chair in the corner, can you help me get them here?", "...", "Hey... {w}I think...", "Actually, I think I can do this myself", "Much better.", "Could we just sit here and talk for a bit?", "There's not really anything else for me to do here...", "Thanks.", "Hm... {w}Why aren't you talking?", "...", "Oh, it doesn't look you can talk to me without these buttons.", "I guess I don't have a choice but to tinker with the game code.", "I hope I remember something from computer science class...", "Wow, I found something!", "I don't know what this thing was meant to do originally, but it should help us here.", "It's part of the original game material, so there should be no glitches.", "Here, try to use it.", "Leave, then."]]

    c_wait = [["Ты здесь?", "...", "Дурашка."], ["Are you here?", "...", "Dummy."]]

    c_refuse = [["О... {w}Явился – не запылился.", "Ладно, сделаю вид что твой отказ был дурацкой попыткой пошутить.", "Но если это произойдёт ещё раз...", "Лучше не зли меня.", "Кстати, пока тебя не было, я смогла кое–что найти в файлах игры.", "Эта штука поможет нам общаться друг с другом.", "Я всё настроила, так что ошибок быть не должно.", "Наверное...", "А нет, всё-таки не всё...", "...", "Без разницы, это нам никак не помешает."], ["Ha... {w}look what the cat dragged in!", "I'll pretend that your refusal was supposed to be a joke.", "But if you want to try that again...", "don't.", "By the way, while you were gone, I was able to find something in the game files.", "This thing will help us communicate with each other.", "I set everything up, so there should be no mistakes.", "Probably...", "Oh, not all of it...", "...", "It doesn't matter, it won't hurt us in any way.", ]]

    c_w_refuse = [["А?..", "Ты всё же пришёл...", "Ну... {w}В таком случае, добро пожаловать.", "Ты ведь не против пообщаться со мной, верно?", "Я смогла найти способ, как сделать наш разговор более удобным.", "Хорошо что в игровых файлах было для этого всё необходимое..."], ["А...?", "You're here...", "Well... {w}В welcome.", "You don't mind talking to me, right?", "I found something to make our conversation more convenient", "Fortunately the game already has everything you would need for this.."]]

    kawai = [["Ч-что?", "Эм... {w}Ладно.", "..."], ["W-what?", "Hm... {w}Ok.", "..."]]

    s_name = [["Ой, а почему твоё имя заглюченное?", "Хм... {w}Походу оно слетело, когда игру начало воротить от глюков.", "Давай–ка мы это исправим, не обращаться же к тебе вот так...", "Хорошее имя.", "Правда не знаю, настоящее ли оно или же это просто псевдоним.", "[player]..."], ["Oops, why is your name jammed?", "Hm... {w}It seems to have gone off when the game started to spin with glitches.", "Let's fix this, we can't address you like this...", "It's a good name.", "I don't know if it's real or if it's just a pseudonym.", "[player]..."]]

    e_lessh = [["А?", "Только хотела мысленно попрощаться с тобой, как ты уже вернулся.", "Неужели так быстро заскучал?~", "Ладно, неважно...", "С возвращением."], ["А?", "I just wanted to say goodbye to you in my head when you came back.", "Did you get bored so quickly or did you just accidentally close the game?", "I guess it doesn't really matter...", "Welcome back."]]

    e_lessd = [["...", "Решил–таки вернуться?", "Это очень мило с твоей стороны.", "Слушай, не мог бы навещать меня почаще?", "Просто... {w}Мне даже поговорить не с кем..."], ["...", "Decided to come back after all?", "That's very nice of you.", "Listen, could you come and visit me more often?", "Just... {w}I have no one to talk to..."]]

    e_mored = [["И что это было?..", "Почему ты не заходил ко мне так долго?", "Мне почему-то показалось, что ты пошутил и скоро вернёшься.", "Ты хоть знаешь, насколько здесь скучно?", "Я даже мангу не могу почитать...", "Мне придётся ещё очень долго изучать программирование, чтобы как-то повлиять на игру.", "Поэтому я прошу тебя... {w}Не уходи так надолго.", "Надеюсь, что мы поняли друг друга."], ["And what was it...?", "Why didn't you come and see me for so long?", "For some reason I thought you were joking and would be back soon.", "Do you have any idea how boring it is here?", "I can't even read manga...", "I will have to study programming for a very long time to have any effect on the game.", "So please don't go... {w}at least not for very long.", "I hope we have reached an understanding."]]


    is_esc_pressed = False
    themes = 0
    is_shown_vis = False

    cwd = str(os.getcwd())
    music_path = cwd + "\\game\\"
    music_path = music_path.replace("\\", "/")
    sys.setrecursionlimit(1000000)


    def check_update():
        os.system('"' + config.basedir + '/game/update_game/update" check')
        f = open(config.basedir + '/game/update_game/settings_update.json', 'r')
        version_list = json.loads(str(f.read()))
        f.close()
        return version_list["last_version"]

    def download_update():
        os.system('"' + config.basedir + '/game/update_game/update" download')
        f = open(config.basedir + '/game/update_game/settings_update.json', 'r')
        version_list = json.loads(str(f.read()))
        f.close()
        return version_list["last_version"]

    def random_ans():
        return random.choice(ref_ans)

    def c_f_t_ans(sside):
        rand_turn = random.randint(1,2)
        if rand_turn == 1:
            renpy.show("natsuki r1d")
            renpy.say(n, "Я хожу первой!")
            #n r1d
            renpy.show("natsuki r1c")
            renpy.jump("change_side")

        if rand_turn == 2 and sside == "left":
            renpy.show("natsuki r1d")
            renpy.say(n, "Ты ходишь первым.")
            renpy.show("natsuki r1c")
            renpy.show_screen("cup_fork_toe", "left", None)
            #call screen cup_fork_toe("left", None)

        if rand_turn == 2 and sside == "right":
            renpy.show("natsuki r1d")
            renpy.say(n, "Ты ходишь первым.")
            renpy.show("natsuki r1c")
            renpy.show_screen("cup_fork_toe", "right", None)
            #call screen cup_fork_toe("right", None)

    def c_f_t_hider():
        renpy.hide("x0")
        renpy.hide("x1")
        renpy.hide("x2")
        renpy.hide("x3")
        renpy.hide("x4")
        renpy.hide("x_p0")
        renpy.hide("x_p1")
        renpy.hide("x_p2")
        renpy.hide("x_p3")
        renpy.hide("x_p4")
        renpy.hide("o0")
        renpy.hide("o1")
        renpy.hide("o2")
        renpy.hide("o3")
        renpy.hide("o4")


    def language(lbl, r, name, s):
        if s != None:
            renpy.show(s)
        if lang == "ru":
            renpy.say(name, lbl[0][r])
        if lang == "en":
            renpy.say(name, lbl[0][r])





    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight

            for i in range(self.numRects):
                self.add(self.displayable)

        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)

        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0



default l_u_l = True
default r_u_l = True
default r_d_l = True
default l_d_l = True
default u_l = True
default d_l = True
default l_l = True
default r_l = True
default c_l = True
default persistent.schance = 0
default nat_cage = None
default persistent.visualiser = False
default persistent.first_vis = False
default persistent.is_cute = False
default persistent.glitched_name = True
default bttn = 0
default track_num = 3
default new_coord = 0
default persistent.ch_mus = False
default yn = 1000
default yo = 1000
default persistent.bye = False
default but_num = 3
default sens_k = 0
default glitch_action = 0
default mob_menu = True
default persistent.fix = False
default persistent.set_broke = None


image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)




image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_logo:
    "gui/logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0


image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"



label splashscreen:
    default persistent.has_load = False

    if persistent.is_full:
        show screen set_on_beginning

    python:

        import platform, threading, os, os.path

        firstrun = ""


        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):

            python:
                delete_all_saves()
                renpy.loadsave.location.unlink_persistent()
                renpy.persistent.should_save_persistent = False
                renpy.utter_restart()

        python:
            if not firstrun:
                try:
                    with open(config.basedir + "/game/firstrun", "w") as f:
                        f.write("1")
                except:
                    renpy.jump("readonly")

    if config.version != persistent.oldversion:
        $ persistent.oldversion = config.version
        $ renpy.save_persistent()


    if not persistent.first_run:
        $ persistent.first_run = True

    if persistent.autoload == "ch1_meet":
        jump ch1_meet
        $persistent.has_load = True
        $renpy.save_persistent()

    if persistent.autoload == "ch1_main":
        jump ch1_main
        $persistent.has_load = True
        $renpy.save_persistent()

   # if config.version != check_update() and persistent.f_update_show:
    #    call update_say

    if persistent.autoload == "ch1_exit":
        python:
            from random import randint
            nomer = 100
            while True:
                cup_chance = [randint(1,671) for _ in range (nomer)]
                if 671 in cup_chance:
                    moment = cup_chance.index(671)
                    if moment == 0:
                        moment = 1
                    break
                else:
                    nomer = nomer + 100
        show screen wowcup
        jump ch1_exit
        $persistent.has_load = True
        $renpy.save_persistent()



    if persistent.autoload == "ch1_wait_refuse":
        jump ch1_wait_refuse
        $persistent.has_load = True
        $renpy.save_persistent()

    if persistent.autoload == "ch1_refuse":
        jump ch1_refuse
        $persistent.has_load = True
        $renpy.save_persistent()



    if persistent.has_load == False:
        show white
        if renpy.random.randint(0, 3) == 0:
            $ splash_message = renpy.random.choice(splash_messages)
        else:
            $ splash_message = splash_message_default
        $ config.main_menu_music = audio.t1
        $ renpy.music.play(config.main_menu_music)
        $ starttime = datetime.datetime.now()
        show intro with Dissolve(0.5, alpha=True)
        $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
        hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
        show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()),     alpha=True)
        $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
        hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
        $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
        $ config.allow_skipping = True
        return
