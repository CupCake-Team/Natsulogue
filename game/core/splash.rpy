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
    music_list = ["bgm/5.ogg", "music/heart.ogg", "music/herewego.ogg", "bgm/m1.ogg", "music/nattheme.ogg", "music/cupcake.ogg"]

    broken_list = ["music/dai_broken.ogg", "music/heart_broken.ogg", "music/herewego_broken.ogg", "bgm/m1.ogg", "music/nattheme_broken.ogg", "music/cupcake_broken.ogg"]

    reversed_list = ["music/dai_reverse.ogg", "music/heart_reverse.ogg", "music/herewego_reverse.ogg", "bgm/m1.ogg", "music/nattheme_reverse.ogg", "music/cupcake_reverse.ogg"]

    ref_ans = ["Неважно.", "Забей.", "Забудь."]

    mus_files = []

    for file in renpy.list_files():
        if file.startswith("music/") and file.endswith(".txt"):
            mus_files.append(file)


    data = []
    prom = []

    for mname in mus_files:
        mus_data = ((renpy.file(mname).read()).split("\n"))
        for string in mus_data:
            edit = string[:-1]
            prom.append(edit.split(" "))

        data.append(prom)
        prom = []


    is_esc_pressed = False
    themes = 0
    is_shown_vis = False
    music_path = os.getcwd() + "\\game\\"
    music_path = music_path.replace("\\", "/")

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

    class VisBar(renpy.Displayable):
        def __init__(self, child, f, **kwargs):
            super(VisBar, self).__init__()
            self.child = renpy.displayable(child)
            self.x = f*10
            self.y = None
            self.freq = f

        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            cr = renpy.render(self.child, width, height, st, at)
            cw, ch = cr.get_size()
            rv.blit(cr, (self.x, self.y))

            if renpy.music.get_pos() == None:
                mpos = 0
            else:
                mpos = int(renpy.music.get_pos()/0.0334)

            self.coord = data[persistent.track_num][mpos][self.freq]
            self.y = float(self.coord)*(-2)
            renpy.redraw(self, 0.01)

            return rv


    def parallax(tf, st, tb):
        x, y = renpy.get_mouse_pos()
        w, h = renpy.get_physical_size()
        tf.align = (float(x) / w, float(y) / h)
        return 0

    def vis_coord(freq):
        return 3*freq, 540

    def Visualiser():
        i = LiveComposite((680,600), (vis_coord(0)), VisBar("gui/button/custom/visbar.png", 0),
        (vis_coord(1)), VisBar("gui/button/custom/visbar.png", 1),
        (vis_coord(2)), VisBar("gui/button/custom/visbar.png", 2),
        (vis_coord(3)), VisBar("gui/button/custom/visbar.png", 3),
        (vis_coord(4)), VisBar("gui/button/custom/visbar.png", 4),
        (vis_coord(5)), VisBar("gui/button/custom/visbar.png", 5),
        (vis_coord(6)), VisBar("gui/button/custom/visbar.png", 6),
        (vis_coord(7)), VisBar("gui/button/custom/visbar.png", 7),
        (vis_coord(8)), VisBar("gui/button/custom/visbar.png", 8),
        (vis_coord(9)), VisBar("gui/button/custom/visbar.png", 9),
        (vis_coord(10)), VisBar("gui/button/custom/visbar.png", 10),
        (vis_coord(11)), VisBar("gui/button/custom/visbar.png", 11),
        (vis_coord(12)), VisBar("gui/button/custom/visbar.png", 12),
        (vis_coord(13)), VisBar("gui/button/custom/visbar.png", 13),
        (vis_coord(14)), VisBar("gui/button/custom/visbar.png", 14),
        # (vis_coord(15)), VisBar("gui/button/custom/visbar.png", 15),
        # (vis_coord(16)), VisBar("gui/button/custom/visbar.png", 16),
        # (vis_coord(17)), VisBar("gui/button/custom/visbar.png", 17),
        # (vis_coord(18)), VisBar("gui/button/custom/visbar.png", 18),
        # (vis_coord(19)), VisBar("gui/button/custom/visbar.png", 19),
        # (vis_coord(20)), VisBar("gui/button/custom/visbar.png", 20),
        # (vis_coord(21)), VisBar("gui/button/custom/visbar.png", 21),
        # (vis_coord(22)), VisBar("gui/button/custom/visbar.png", 22),
        # (vis_coord(23)), VisBar("gui/button/custom/visbar.png", 23),
        # (vis_coord(24)), VisBar("gui/button/custom/visbar.png", 24),
        # (vis_coord(25)), VisBar("gui/button/custom/visbar.png", 25),
        # (vis_coord(26)), VisBar("gui/button/custom/visbar.png", 26),
        # (vis_coord(27)), VisBar("gui/button/custom/visbar.png", 27),
        # (vis_coord(28)), VisBar("gui/button/custom/visbar.png", 28),
        # (vis_coord(29)), VisBar("gui/button/custom/visbar.png", 29),
        # (vis_coord(30)), VisBar("gui/button/custom/visbar.png", 30),
        # (vis_coord(31)), VisBar("gui/button/custom/visbar.png", 31),
        # (vis_coord(32)), VisBar("gui/button/custom/visbar.png", 32),
        # (vis_coord(33)), VisBar("gui/button/custom/visbar.png", 33),
        # (vis_coord(34)), VisBar("gui/button/custom/visbar.png", 34),
        # (vis_coord(35)), VisBar("gui/button/custom/visbar.png", 35),
        # (vis_coord(36)), VisBar("gui/button/custom/visbar.png", 36),
        (vis_coord(37)), VisBar("gui/button/custom/visbar.png", 37),
        (vis_coord(38)), VisBar("gui/button/custom/visbar.png", 38),
        (vis_coord(39)), VisBar("gui/button/custom/visbar.png", 39),
        (vis_coord(40)), VisBar("gui/button/custom/visbar.png", 40),
        (vis_coord(41)), VisBar("gui/button/custom/visbar.png", 41),
        (vis_coord(42)), VisBar("gui/button/custom/visbar.png", 42),
        (vis_coord(43)), VisBar("gui/button/custom/visbar.png", 43),
        (vis_coord(44)), VisBar("gui/button/custom/visbar.png", 44),
        (vis_coord(45)), VisBar("gui/button/custom/visbar.png", 45),
        (vis_coord(46)), VisBar("gui/button/custom/visbar.png", 46),
        (vis_coord(47)), VisBar("gui/button/custom/visbar.png", 47),
        (vis_coord(48)), VisBar("gui/button/custom/visbar.png", 48),
        (vis_coord(49)), VisBar("gui/button/custom/visbar.png", 49),
        (vis_coord(50)), VisBar("gui/button/custom/visbar.png", 50))
        return i




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
default persistent.track_num = 3
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
default persistent.themes = False


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
