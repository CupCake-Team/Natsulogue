init python:
    import sys, pickle, random, os, socket, time
    from os.path import abspath
    from threading import Thread
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
    music_list = ["bgm/5.ogg", "mod_assets/music/heart.ogg", "mod_assets/music/herewego.ogg", "bgm/m1.ogg", "mod_assets/music/nattheme.ogg", "mod_assets/music/cupcake.ogg"]

    broken_list = ["mod_assets/music/dai_broken.ogg", "mod_assets/music/heart_broken.ogg", "mod_assets/music/herewego_broken.ogg", "bgm/m1.ogg", "mod_assets/music/nattheme_broken.ogg", "mod_assets/music/cupcake_broken.ogg"]

    reversed_list = ["mod_assets/music/dai_reverse.ogg", "mod_assets/music/heart_reverse.ogg", "mod_assets/music/herewego_reverse.ogg", "bgm/m1.ogg", "mod_assets/music/nattheme_reverse.ogg", "mod_assets/music/cupcake_reverse.ogg"]

    ref_ans = ["Неважно.", "Забей.", "Забудь."]

    cwd = config.basedir
    os.startfile(cwd + '/game/mod_assets/server.exe')

    time.sleep(2)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 3030)) 

    is_esc_pressed = False
    themes = 0
    is_shown_vis = False
    bars = 66
    audio_data = [0]*bars
    music_path = cwd + "\\game\\"
    music_path = music_path.replace("\\", "/")

    base_dir = config.basedir.replace("\\", "/")

    def get_audio(a):
        buff = 512
        while True:
            s.sendall(str(bars).encode('utf-8'))
            data = s.recv(buff)
            a_d = data.decode('utf-8').split()

            if len(a_d) < bars-1:
                buff = buff*2
                continue

            for i in range(0, len(a_d)-1):
                a[i] = int(a_d[i])

    t1 = Thread(target=get_audio, args=(audio_data, ))
    t1.start()



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
            w, h = renpy.get_physical_size()
            rv.blit(cr, (self.x, self.y))

            maximum = 0.1 if int(max(audio_data)) == 0 else max(audio_data)/20

            delta = (h - 522) / maximum #522 - макс. высота

            if audio_data[self.freq] == max(audio_data):
                self.coord = (audio_data[self.freq]*0.7)/20
            else:
                self.coord = (audio_data[self.freq]*0.9)/20

            
            self.y =  -1 * (float(self.coord)) * delta - 7


            renpy.redraw(self, 0.016)

            return rv


    def parallax(tf, st, tb):
        x, y = renpy.get_mouse_pos()
        w, h = renpy.get_physical_size()
        tf.align = (float(x) / w, float(y) / h)
        return 0

    def vis_coord(freq):
        if freq > bars/2-2:
            x = freq-freq*5 + 393
        else:
            x = freq-freq*5 + 123
            
        return x, 533

    def Visualiser():
        i = Composite((880,600), 
        (vis_coord(0)), VisBar("mod_assets/button/custom/visbar.png", 0),
        (vis_coord(1)), VisBar("mod_assets/button/custom/visbar.png", 1),
        (vis_coord(2)), VisBar("mod_assets/button/custom/visbar.png", 2),
        (vis_coord(3)), VisBar("mod_assets/button/custom/visbar.png", 3),
        (vis_coord(4)), VisBar("mod_assets/button/custom/visbar.png", 4),
        (vis_coord(5)), VisBar("mod_assets/button/custom/visbar.png", 5),
        (vis_coord(6)), VisBar("mod_assets/button/custom/visbar.png", 6),
        (vis_coord(7)), VisBar("mod_assets/button/custom/visbar.png", 7),
        (vis_coord(8)), VisBar("mod_assets/button/custom/visbar.png", 8),
        (vis_coord(9)), VisBar("mod_assets/button/custom/visbar.png", 9),
        (vis_coord(10)), VisBar("mod_assets/button/custom/visbar.png", 10),
        (vis_coord(11)), VisBar("mod_assets/button/custom/visbar.png", 11),
        (vis_coord(12)), VisBar("mod_assets/button/custom/visbar.png", 12),
        (vis_coord(13)), VisBar("mod_assets/button/custom/visbar.png", 13),
        (vis_coord(14)), VisBar("mod_assets/button/custom/visbar.png", 14),
        (vis_coord(15)), VisBar("mod_assets/button/custom/visbar.png", 15),
        (vis_coord(16)), VisBar("mod_assets/button/custom/visbar.png", 16),
        (vis_coord(17)), VisBar("mod_assets/button/custom/visbar.png", 17),
        (vis_coord(18)), VisBar("mod_assets/button/custom/visbar.png", 18),
        (vis_coord(19)), VisBar("mod_assets/button/custom/visbar.png", 19),
        (vis_coord(20)), VisBar("mod_assets/button/custom/visbar.png", 20),
        (vis_coord(21)), VisBar("mod_assets/button/custom/visbar.png", 21),
        (vis_coord(22)), VisBar("mod_assets/button/custom/visbar.png", 22),
        (vis_coord(23)), VisBar("mod_assets/button/custom/visbar.png", 23),
        (vis_coord(24)), VisBar("mod_assets/button/custom/visbar.png", 24),
        (vis_coord(25)), VisBar("mod_assets/button/custom/visbar.png", 25),
        (vis_coord(26)), VisBar("mod_assets/button/custom/visbar.png", 26),
        (vis_coord(27)), VisBar("mod_assets/button/custom/visbar.png", 27),
        (vis_coord(28)), VisBar("mod_assets/button/custom/visbar.png", 28),
        (vis_coord(29)), VisBar("mod_assets/button/custom/visbar.png", 29),
        (vis_coord(30)), VisBar("mod_assets/button/custom/visbar.png", 30),
        (vis_coord(31)), VisBar("mod_assets/button/custom/visbar.png", 31),
        (vis_coord(32)), VisBar("mod_assets/button/custom/visbar.png", 32),
        (vis_coord(33)), VisBar("mod_assets/button/custom/visbar.png", 33),
        (vis_coord(34)), VisBar("mod_assets/button/custom/visbar.png", 34),
        (vis_coord(35)), VisBar("mod_assets/button/custom/visbar.png", 35),
        (vis_coord(36)), VisBar("mod_assets/button/custom/visbar.png", 36),
        (vis_coord(37)), VisBar("mod_assets/button/custom/visbar.png", 37),
        (vis_coord(38)), VisBar("mod_assets/button/custom/visbar.png", 38),
        (vis_coord(39)), VisBar("mod_assets/button/custom/visbar.png", 39),
        (vis_coord(40)), VisBar("mod_assets/button/custom/visbar.png", 40),
        (vis_coord(41)), VisBar("mod_assets/button/custom/visbar.png", 41),
        (vis_coord(42)), VisBar("mod_assets/button/custom/visbar.png", 42),
        (vis_coord(43)), VisBar("mod_assets/button/custom/visbar.png", 43),
        (vis_coord(44)), VisBar("mod_assets/button/custom/visbar.png", 44),
        (vis_coord(45)), VisBar("mod_assets/button/custom/visbar.png", 45),
        (vis_coord(46)), VisBar("mod_assets/button/custom/visbar.png", 46),
        (vis_coord(47)), VisBar("mod_assets/button/custom/visbar.png", 47),
        (vis_coord(48)), VisBar("mod_assets/button/custom/visbar.png", 48),
        (vis_coord(49)), VisBar("mod_assets/button/custom/visbar.png", 49),
        (vis_coord(50)), VisBar("mod_assets/button/custom/visbar.png", 50),
        (vis_coord(51)), VisBar("mod_assets/button/custom/visbar.png", 51),
        (vis_coord(52)), VisBar("mod_assets/button/custom/visbar.png", 52),
        (vis_coord(53)), VisBar("mod_assets/button/custom/visbar.png", 53),
        (vis_coord(54)), VisBar("mod_assets/button/custom/visbar.png", 54),
        (vis_coord(55)), VisBar("mod_assets/button/custom/visbar.png", 55),
        (vis_coord(56)), VisBar("mod_assets/button/custom/visbar.png", 56),
        (vis_coord(57)), VisBar("mod_assets/button/custom/visbar.png", 57),
        (vis_coord(58)), VisBar("mod_assets/button/custom/visbar.png", 58),
        (vis_coord(59)), VisBar("mod_assets/button/custom/visbar.png", 59),
        (vis_coord(60)), VisBar("mod_assets/button/custom/visbar.png", 60),
        (vis_coord(61)), VisBar("mod_assets/button/custom/visbar.png", 61),
        (vis_coord(62)), VisBar("mod_assets/button/custom/visbar.png", 62),
        (vis_coord(63)), VisBar("mod_assets/button/custom/visbar.png", 63),
        (vis_coord(64)), VisBar("mod_assets/button/custom/visbar.png", 64),
        (vis_coord(65)), VisBar("mod_assets/button/custom/visbar.png", 65))
        return i


    def relationship(points):
        if points < 20:
            relation = "Negative"
        elif points > 20 and points < 80:
            relation = "Neutral"
        elif points > 80:
            relation = "Positive"

        return relation

    def relationcount(posi, neut, nega):
        global cur_relation, relation, start_relation
        if cur_relation == "Positive":
            persistent.relation += posi
        if cur_relation == "Neutral":
            persistent.relation += neut
        if cur_relation == "Negative":
            persistent.relation += nega
        cur_relation = relationship(persistent.relation)
        renpy.save_persistent()
        if cur_relation != start_relation:

            renpy.show_screen("relation_chibi_show_l")
            renpy.show_screen("relation_chibi_show_r")
            renpy.show_screen("relation_show")

            if persistent.show_relation == True:
                rel_chibi_coord_l = [get_chibi_coord("left"), 10]
                rel_chibi_coord_r = [get_chibi_coord("right"), 10]
            else:
                rel_chibi_coord_l = [get_chibi_coord("left"), 624]
                rel_chibi_coord_r = [get_chibi_coord("right"), 624]

            if start_relation == "Neutral" and cur_relation == "Positive":
                start_relation = cur_relation
                persistent.relation += 10
                renpy.call("respect")
            if start_relation == "Neutral" and cur_relation == "Negative":
                start_relation = cur_relation
                persistent.relation -= 10
                renpy.call("disappointment")
            if start_relation == "Positive" and cur_relation == "Neutral":
                start_relation = cur_relation
                persistent.relation -= 10
                renpy.call("badfeelings")
            if start_relation == "Negative" and cur_relation == "Neutral":
                start_relation = cur_relation
                persistent.relation += 10
                renpy.call("muchbetter")


    sprite_names = [{"d":"default.png", "q1":"quote_1.png", "q2":"quote_2.png", "a":"angry.png"},
    {"a1":"angry_1.png", "a2":"angry_2.png", "a3":"angry_3.png", "c":"calm.png", "s1":"surprise_1.png", "s2":"surprise_2.png"},
    {"c":"calm.png", "cute":"cute.png", "h":"happy.png", "st1":"straight_1.png", "st2":"straight_2.png", "su1":"surprise_1.png", "su2":"surprise_2.png"},
    {"a":"angry.png", "fa":"fang.png", "fr":"fright.png", "h":"hugesmile.png", "s":"sad.png", "sh":"smile.png", "su":"surprise.png", "t1":"talk_1.png", "t2":"talk_2.png"},
    {"l":"light.png", "h":"heavy.png"}]

    def nat_sprite(body, eyebrow, eyes, mouth, blush):
        if body[0] == "s":
            body_name = "body/school_"+sprite_names[0][body[1:]]
        else:
            body_name = "body/casual_"+sprite_names[0][body[1:]]

        if blush != None:
            blush_name = "blush/blush_"+sprite_names[4][blush]
            return LiveComposite((1280, 720), (640-298,720-605-62), "mod_assets/natsuki/sitting/"+body_name,
            (640-298,720-605-62), "mod_assets/natsuki/sitting/eyebrows/"+sprite_names[1][eyebrow],
            (640-298,720-605-62), "mod_assets/natsuki/sitting/eyes/"+sprite_names[2][eyes],
            (640-298,720-605-62), "mod_assets/natsuki/sitting/mouth/"+sprite_names[3][mouth],
            (640-298,720-605-62), "mod_assets/natsuki/sitting/"+blush_name,
            (0,12), "mod_assets/natsuki/table/desk.png",
            (0,12), "mod_assets/natsuki/table/desk_sh.png")
        else:
            return LiveComposite((1280, 720), (640-298,720-605-62), "mod_assets/natsuki/sitting/"+body_name,
            (640-298,720-605-62), "mod_assets/natsuki/sitting/eyebrows/"+sprite_names[1][eyebrow],
            (640-298,720-605-62), "mod_assets/natsuki/sitting/eyes/"+sprite_names[2][eyes],
            (640-298,720-605-62), "mod_assets/natsuki/sitting/mouth/"+sprite_names[3][mouth],
            (0,12), "mod_assets/natsuki/table/desk.png",
            (0,12), "mod_assets/natsuki/table/desk_sh.png")


        #размеры спрайта: 597x605




    cur_side = "left"




    def hit_coord(b, state, coord):
        global button_coord, avai_but, but_count, cur_side
        if state == False:
            return 0
        else:
            i = avai_but.index(b)
            if coord == "x":
                return button_coord[cur_side][but_count][i][0]
            else:
                return button_coord[cur_side][but_count][i][1]


    def relation_chibi(s, yp):
        ani_var = renpy.random.randint(1,100)
        if ani_var <= 30:
            if cur_relation == "Positive":
                if s == "left":
                    if rel_chibi_coord_l[0] == 480 or rel_chibi_coord_l[0] == 520:
                        ani_choice = renpy.random.randint(1,2)
                        if ani_choice == 1:
                            renpy.hide("rel_chibi_r")
                            renpy.show("rel_chibi_l", at_list=[bounce(rel_chibi_coord_l[0], rel_chibi_coord_l[1])], zorder = 10, tag="l")
                        else:
                            if rel_chibi_coord_l[0] == 480:
                                renpy.hide("rel_chibi_r")
                                renpy.show("rel_chibi_l", at_list=[bounce_right(rel_chibi_coord_l[0], rel_chibi_coord_l[1])], zorder = 10, tag="l")
                                rel_chibi_coord_l[0] += 10
                            else:
                                renpy.hide("rel_chibi_l")
                                renpy.show("rel_chibi_r", at_list=[bounce_left(rel_chibi_coord_l[0], rel_chibi_coord_l[1])], zorder = 10, tag="l")
                                rel_chibi_coord_l[0] -= 10

                    else:
                        ani_choice = renpy.random.randint(1,3)
                        if ani_choice == 1:
                            renpy.hide("rel_chibi_r")
                            renpy.show("rel_chibi_l", at_list=[bounce(rel_chibi_coord_l[0], rel_chibi_coord_l[1])], zorder = 10, tag="l")
                        if ani_choice == 2:
                            renpy.hide("rel_chibi_r")
                            renpy.show("rel_chibi_l", at_list=[bounce_right(rel_chibi_coord_l[0], rel_chibi_coord_l[1])], zorder = 10, tag="l")
                            rel_chibi_coord_l[0] += 10
                        if ani_choice == 3:
                            renpy.hide("rel_chibi_l")
                            renpy.show("rel_chibi_r", at_list=[bounce_left(rel_chibi_coord_l[0], rel_chibi_coord_l[1])], zorder = 10, tag="l")
                            rel_chibi_coord_l[0] -= 10

                else:
                    if rel_chibi_coord_r[0] == 680 or rel_chibi_coord_r[0] == 720:
                        ani_choice = renpy.random.randint(1,2)
                        if ani_choice == 1:
                            renpy.hide("rel_chibi_r")
                            renpy.show("rel_chibi_l", at_list=[bounce(rel_chibi_coord_r[0], rel_chibi_coord_r[1])], zorder = 10, tag="r")
                        else:
                            if rel_chibi_coord_r[0] == 680:
                                renpy.hide("rel_chibi_r")
                                renpy.show("rel_chibi_l", at_list=[bounce_right(rel_chibi_coord_r[0], rel_chibi_coord_r[1])], zorder = 10, tag="r")
                                rel_chibi_coord_r[0] += 10
                            else:
                                renpy.hide("rel_chibi_l")
                                renpy.show("rel_chibi_r", at_list=[bounce_left(rel_chibi_coord_r[0], rel_chibi_coord_r[1])], zorder = 10, tag="r")
                                rel_chibi_coord_r[0] -= 10

                    else:
                        ani_choice = renpy.random.randint(1,3)
                        if ani_choice == 1:
                            renpy.hide("rel_chibi_r")
                            renpy.show("rel_chibi_l", at_list=[bounce(rel_chibi_coord_r[0], rel_chibi_coord_r[1])], zorder = 10, tag="r")
                        if ani_choice == 2:
                            renpy.hide("rel_chibi_r")
                            renpy.show("rel_chibi_l", at_list=[bounce_right(rel_chibi_coord_r[0], rel_chibi_coord_r[1])], zorder = 10, tag="r")
                            rel_chibi_coord_r[0] += 10
                        if ani_choice == 3:
                            renpy.hide("rel_chibi_l")
                            renpy.show("rel_chibi_r", at_list=[bounce_left(rel_chibi_coord_r[0], rel_chibi_coord_r[1])], zorder = 10, tag="r")
                            rel_chibi_coord_r[0] -= 10

            if cur_relation == "Neutral":
                if s == "left":
                    ani_choice = renpy.random.randint(1,2)
                    if ani_choice == 1:
                        renpy.hide("rel_chibi_r")
                        renpy.show("rel_chibi_l", at_list=[bounce(rel_chibi_coord_l[0], rel_chibi_coord_l[1])], zorder = 10, tag="l")
                    else:
                        renpy.hide("rel_chibi_l")
                        renpy.show("rel_chibi_r", at_list=[bounce(rel_chibi_coord_l[0], rel_chibi_coord_l[1])], zorder = 10, tag="l")

                else:
                    ani_choice = renpy.random.randint(1,2)
                    if ani_choice == 1:
                        renpy.hide("rel_chibi_r")
                        renpy.show("rel_chibi_l", at_list=[bounce(rel_chibi_coord_r[0], rel_chibi_coord_r[1])], zorder = 10, tag="r")
                    else:
                        renpy.hide("rel_chibi_l")
                        renpy.show("rel_chibi_r", at_list=[bounce(rel_chibi_coord_r[0], rel_chibi_coord_r[1])], zorder = 10, tag="r")




    relation_stat = {"Positive":{"ru":"Позитивное","en":"Positive"}, "Neutral":{"ru":"Нейтральное", "en":"Neutral"}, "Negative":{"ru":"Негативное", "en":"Negative"}}

    def return_relation_stat(rel):
        global lang
        #return relation_stat[rel][lang]
        return relation_stat[rel]["ru"]

    def get_chibi_coord(s):
        sym_len = len(return_relation_stat(cur_relation))
        if persistent.show_relation == True:
            if s == "left":
                if sym_len%2==0:
                    return 640 - sym_len/2*16 - 77 - 20
                else:
                    return 640 - (sym_len-1)/2*16 - 77 - 20
            else:
                if sym_len%2==0:
                    return 640 + sym_len/2*16 + 20
                else:
                    return 640 + (sym_len-1)/2*16 + 20
        else:
            if s == "left":
                c = random.randint(330, 460)
                return c
            else:
                c = random.randint(830, 970)
                return c


    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"

    def glitchtext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode)
        return output


    def get_cur_persistent(old, new, current):
        current.update(new)
        current.update(old)
        return current

    renpy.register_persistent('visualiser', get_cur_persistent)
    renpy.register_persistent('first_vis', get_cur_persistent)
    renpy.register_persistent('is_cute', get_cur_persistent)
    renpy.register_persistent('glitched_name', get_cur_persistent)
    renpy.register_persistent('track_num', get_cur_persistent)
    renpy.register_persistent('ch_mus', get_cur_persistent)
    renpy.register_persistent('bye', get_cur_persistent)
    renpy.register_persistent('fix', get_cur_persistent)
    renpy.register_persistent('set_broke', get_cur_persistent)
    renpy.register_persistent('themes', get_cur_persistent)
    renpy.register_persistent('relation', get_cur_persistent)
    renpy.register_persistent('repeats', get_cur_persistent)
    renpy.register_persistent('clothes', get_cur_persistent)
    renpy.register_persistent('change_clothes', get_cur_persistent)
    renpy.register_persistent('sprite_side', get_cur_persistent)
    renpy.register_persistent('show_relation', get_cur_persistent)
    renpy.register_persistent('first_relation', get_cur_persistent)
    renpy.register_persistent('show_chibis', get_cur_persistent)
    renpy.register_persistent('topc', get_cur_persistent)
    renpy.register_persistent('ch_vol', get_cur_persistent)
    renpy.register_persistent('parallax_bg', get_cur_persistent)
    renpy.register_persistent('mus_repeat', get_cur_persistent)
    renpy.register_persistent('exp_time', get_cur_persistent)
    renpy.register_persistent('back_music', get_cur_persistent)
    renpy.register_persistent('is_glitching', get_cur_persistent)
    renpy.register_persistent('chance', get_cur_persistent)
    renpy.register_persistent('f_game', get_cur_persistent)
    renpy.register_persistent('v_key', get_cur_persistent)
    renpy.register_persistent('v_r_key', get_cur_persistent)
    renpy.register_persistent('s_key', get_cur_persistent)
    renpy.register_persistent('s_r_key', get_cur_persistent)
    renpy.register_persistent('m_key', get_cur_persistent)
    renpy.register_persistent('m_r_key', get_cur_persistent)
    renpy.register_persistent('f_key', get_cur_persistent)
    renpy.register_persistent('f_r_key', get_cur_persistent)
    renpy.register_persistent('t_key', get_cur_persistent)
    renpy.register_persistent('t_r_key', get_cur_persistent)
    renpy.register_persistent('is_full', get_cur_persistent)
    renpy.register_persistent('first_change', get_cur_persistent)
    renpy.register_persistent('readen', get_cur_persistent)
    renpy.register_persistent('theme', get_cur_persistent)
    renpy.register_persistent('is_theme_default', get_cur_persistent)





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
default persistent.relation = 95
default persistent.repeats = {}
default persistent.clothes = "school"
default persistent.change_clothes = False
default persistent.sprite_side = "Rand"
default persistent.show_relation = False
default persistent.first_relation = False
default persistent.show_chibis = False



image rel_chibi_r = im.Scale(base_dir+"/game/mod_assets/button/custom/cup_button_nat.png", 77, 78)
image rel_chibi_l = im.Flip(im.Scale(base_dir+"/game/mod_assets/button/custom/cup_button_nat.png", 77, 78), horizontal = True)

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
    $cur_relation = relationship(persistent.relation)
    $start_relation = cur_relation
    if persistent.show_relation == True:
        $rel_chibi_coord_l = [get_chibi_coord("left"), 10]
        $rel_chibi_coord_r = [get_chibi_coord("right"), 10]
    else:
        $rel_chibi_coord_l = [get_chibi_coord("left"), 620]
        $rel_chibi_coord_r = [get_chibi_coord("right"), 620]

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
