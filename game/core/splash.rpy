init -100 python:
    if not renpy.android:
        for archive in ['audio','images','fonts']:
            if archive not in config.archives:
                renpy.error("DDLC archive files not found in /game folder. Check your installation and try again.")




init python:
    import sys, pickle, random, os
    from os.path import abspath
    menu_trans_time = 1
    splash_message_default = _("Эта игра не предназначена для детей,\nбеременных женщин и лиц с неустойчивой психикой.")
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

    is_esc_pressed = False
    themes = 0
    is_shown_vis = False
    music_path = os.getcwd() + "\\game\\"
    music_path = music_path.replace("\\", "/")
    sys.setrecursionlimit(1000000)
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


    def parallax(tf, st, tb):
        x, y = renpy.get_mouse_pos()
        w, h = renpy.get_physical_size()
        tf.align = (float(x) / w, float(y) / h)
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
