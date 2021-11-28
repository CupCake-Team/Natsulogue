#coinit offset = -1



init python:

    #from math import infinity
    from random import choice
    import platform, math, json
    from os import system
    #from threading import Event

    renpy.music.register_channel("movie")



    def FinishEnterName():
        if not player: return
        persistent.playername = player
        renpy.save_persistent()
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")


    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 1 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            return Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
                ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))
        elif persistent.playthrough == 3 and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="There's no point in saving anymore.\nDon't worry, I'm not going anywhere.", ok_action=Hide("dialog"))
        else:
            return FileAction(name)


    def next_song():
        global track_num, delta, mus_pos, dur
        track_num = track_num + 1
        if track_num == persistent.back_music:
            renpy.hide_screen("button_set_back")
            renpy.show_screen("inactive_set_back")
        else:
            renpy.show_screen("button_set_back")
            renpy.hide_screen("inactive_set_back")
        if track_num == 6:
            track_num = 0
            renpy.music.play(music_list[0], channel="music")
        else:
            renpy.music.play(music_list[track_num], channel="music")

        if renpy.get_screen("vis_button") == False:
            mus_pos = 0
            while not renpy.music.is_playing(channel='music'):
                dur = renpy.music.get_duration()

            renpy.show("resumed_visual", zorder=1)



    def previous_song():
        global track_num, delta, mus_pos, dur
        track_num = track_num - 1
        if track_num == persistent.back_music:
            renpy.hide_screen("button_set_back")
            renpy.show_screen("inactive_set_back")
        else:
            renpy.show_screen("button_set_back")
            renpy.hide_screen("inactive_set_back")
        if track_num == -1:
            track_num = 5
            renpy.music.play(music_list[5], channel="music")
        else:
            renpy.music.play(music_list[track_num], channel="music")

        if renpy.get_screen("vis_button") == False:
            mus_pos = 0
            while not renpy.music.is_playing(channel='music'):
                dur = renpy.music.get_duration()

            renpy.show("resumed_visual", zorder=1)







    def vis_pause(st, at):
        global track_num, cadre

        c = "music/vis_data/" + vis_folders[track_num] + "/c" + str(int(cadre)) + ".png"
        return c, None



    def vis_res(st, at):
        global track_num, mus_pos, dur
        name = '<from ' + str(int(mus_pos)) + ' to ' + str(dur) + '>' + vis_list[track_num]

        ost = Movie(play = name, channel='movie', mask = name, side_mask=True)

        return ost, None



    def ani_vis_pause():
        global cadre
        mus_pos = renpy.music.get_pos()
        cadre = 25 * mus_pos
        is_shown_vis = False
        renpy.music.set_pause(True)
        renpy.show("pause_visual", zorder=1, at_list=[slow_vis_fade])
        renpy.hide("resumed_visual")



    def ani_vis_resume():
        global delta, mus_pos, dur
        mus_pos = renpy.music.get_pos()
        dur = renpy.music.get_duration()
        delta = dur - mus_pos
        renpy.music.set_pause(False)
        renpy.show("resumed_visual", zorder=1, at_list=[fade_vis_resume])
        renpy.hide("pause_visual")



    def save_back():
        global track_num
        persistent.back_music = track_num
        renpy.save_persistent()
        renpy.show_screen("inactive_set_back")
        renpy.show_screen("music_name")
        renpy.hide_screen("actions_name")
        renpy.hide_screen("button_set_back")

    def set_back_on_exit():
        global track_num
        persistent.back_music = track_num
        renpy.save_persistent()

    def set_back_on_prefered():
        global prefered_track_num
        persistent.back_music = prefered_track_num
        renpy.save_persistent()

    def set_value(v):
        global button
        button = v





#----------------------------------------Вилочки-кексики---------------------------------




    def initialize_game():
        global current_state, cur_x_tag, cur_o_tag
        current_state = [[['.', True, 805, 205, 240], ['.', True, 930, 330, 235], ['.', True, 1060, 460, 235]],
                        [['.', True, 805, 205, 373], ['.', True, 930, 330, 375], ['.', True, 1060, 460, 375]],
                        [['.', True, 805, 205, 500], ['.', True, 930, 330, 505], ['.', True, 1060, 460, 500]]]

        cur_x_tag = 0
        cur_o_tag = 0




    def is_end():
        global current_state
        # Vertical win
        for i in range(0, 3):
            if (current_state[0][i][0] != '.' and
                current_state[0][i][0] == current_state[1][i][0] and
                current_state[1][i][0] == current_state[2][i][0]):
                return current_state[0][i][0]

        # Horizontal win
        for i in range(0, 3):
            if current_state[i][0][0] == 'X' and current_state[i][1][0] == 'X' and current_state[i][2][0] == 'X':
                return 'X'
            elif current_state[i][0][0] == 'O' and current_state[i][1][0] == 'O' and current_state[i][2][0] == 'O':
                return 'O'

        # Main diagonal win
        if (current_state[0][0][0] != '.' and
            current_state[0][0][0] == current_state[1][1][0] and
            current_state[0][0][0] == current_state[2][2][0]):
            return current_state[0][0][0]

        # Second diagonal win
        if (current_state[0][2][0] != '.' and
            current_state[0][2][0] == current_state[1][1][0] and
            current_state[0][2][0] == current_state[2][0][0]):
            return current_state[0][2][0]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (current_state[i][j][0] == '.'):
                    return None

        # It's a tie!
        return '.'






    def max_alpha_beta(alpha, beta):
        global current_state
        maxv = -2
        px = None
        py = None

        result = is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if current_state[i][j][0] == '.':
                    current_state[i][j][0] = 'O'
                    (m, min_i, in_j) = min_alpha_beta(alpha, beta)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    current_state[i][j][0] = '.'

                    # Next two ifs in Max and Min are the only difference between regular algorithm and minimax
                    if maxv >= beta:
                        return (maxv, px, py)

                    if maxv > alpha:
                        alpha = maxv

        return (maxv, px, py)





    def min_alpha_beta(alpha, beta):
        global current_state
        minv = 2

        qx = None
        qy = None

        result = is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if current_state[i][j][0] == '.':
                    current_state[i][j][0] = 'X'
                    (m, max_i, max_j) = max_alpha_beta(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    current_state[i][j][0] = '.'

                    if minv <= alpha:
                        return (minv, qx, qy)

                    if minv < beta:
                        beta = minv

        return (minv, qx, qy)





    def play(px, py, p_turn, xnew, ynew):
        global current_state, result, cur_o_tag, cur_x_tag, left, right, sside
        chance = persistent.schance

        result = is_end()

        if result != None:
            if result == 'X':

                chance = chance + 20
                if chance >= 95:
                    chance = 95
                if chance <= 0:
                    chance = 0
                persistent.schance = chance
                renpy.save_persistent()
                renpy.hide_screen("cup_fork_toe")
                renpy.call("win")
                return None
            elif result == 'O':

                chance = chance - 20
                if chance >= 95:
                    chance = 95
                if chance <= 0:
                    chance = 0
                persistent.schance = chance
                renpy.save_persistent()
                renpy.hide_screen("cup_fork_toe")
                renpy.call("win")
                return None
            elif result == '.':

                persistent.schance = chance
                renpy.save_persistent()
                renpy.hide_screen("cup_fork_toe")
                renpy.call("win")
                return None


        if p_turn == 'X':

            (m, qx, qy) = min_alpha_beta(-2, 2)
            recx = qx
            recy = qy


            if px == recx and py == recy:
                chance = chance + 5
                if chance >= 95:
                    chance = 95
                if chance <= 0:
                    chance = 0
                persistent.schance = chance
                renpy.save_persistent()

            current_state[px][py][0] = 'X'
            current_state[px][py][1] = False



            renpy.show("fork", at_list=[fork_ani(xnew, ynew)], zorder=4, tag="x" + str(cur_x_tag))
            renpy.show("fork_print", at_list=[print_ani(xnew, ynew)], zorder=3, tag="x_p" + str(cur_x_tag))
            cur_x_tag = cur_x_tag + 1


        if p_turn == "O":
            while True:

                (m, bx, by) = max_alpha_beta(-2, 2)
                rand_px = random.randint(0,2)
                rand_py = random.randint(0,2)

                ch_pos = random.randint(0,100)
                if ch_pos <= chance:
                    if current_state[bx][by][0] == ".":
                        current_state[bx][by][0] = 'O'
                        current_state[bx][by][1] = False
                        if left == True or sside == "left":
                            renpy.show("cup_O", at_list=[cup_ani(current_state[bx][by][2], current_state[bx][by][4])], zorder=3, tag="o" + str(cur_o_tag))
                        if right == True or sside == "right":
                            renpy.show("cup_O", at_list=[cup_ani(current_state[bx][by][3], current_state[bx][by][4])], zorder=3, tag="o" + str(cur_o_tag))
                        cur_o_tag = cur_o_tag + 1
                        break

                else:
                    if current_state[rand_px][rand_py][0] == ".":
                        current_state[rand_px][rand_py][0] = 'O'
                        current_state[rand_px][rand_py][1] = False
                        if left == True or sside == "left":
                            renpy.show("cup_O", at_list=[cup_ani(current_state[rand_px][rand_py][2], current_state[rand_px][rand_py][4])], zorder=3, tag="o" + str(cur_o_tag))
                        if right == True or sside == "right":
                            renpy.show("cup_O", at_list=[cup_ani(current_state[rand_px][rand_py][3], current_state[rand_px][rand_py][4])], zorder=3, tag="o" + str(cur_o_tag))
                        cur_o_tag = cur_o_tag + 1
                        break


        result = is_end()

        if result != None:
            if result == 'X':
                chance = chance + 20
                if chance >= 95:
                    chance = 95
                if chance <= 0:
                    chance = 0
                persistent.schance = chance
                renpy.save_persistent()
                renpy.hide_screen("cup_fork_toe")
                renpy.call("win")
                return None
            elif result == 'O':
                chance = chance - 20
                if chance >= 95:
                    chance = 95
                if chance <= 0:
                    chance = 0
                persistent.schance = chance
                renpy.save_persistent()
                renpy.hide_screen("cup_fork_toe")
                renpy.call("win")
                return None
            elif result == '.':
                persistent.schance = chance
                renpy.save_persistent()
                renpy.hide_screen("cup_fork_toe")
                renpy.call("win")
                return None

        return None



screen cup_fork_toe(sst, chs):

    if sst == "left":
        #add "gui/button/custom/field.png" at for_field_l
        imagebutton xcenter 810 ycenter 230:
            idle "gui/button/custom/corner_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[0][0][1]
            #action NullAction()
            action [Function(play, 0, 0, "X", 810, 230), Jump("change_side")]
        # add "gui/button/custom/corner_but_hit.png":
        #     xcenter 810
        #     ycenter 230 #левый верхний


        imagebutton xcenter 1050 ycenter 230:
            idle "gui/button/custom/corner_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[0][2][1]
            #action NullAction()
            action [Function(play, 0, 2, "X", 1065, 230), Jump("change_side")]
        #
        # add "gui/button/custom/corner_but_hit.png":
        #     xcenter 1050
        #     ycenter 230 #правый верхний


        imagebutton xcenter 1050 ycenter 495:
            idle "gui/button/custom/corner_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[2][2][1]
            #action NullAction()
            action [Function(play, 2, 2, "X", 1065, 495), Jump("change_side")]
        # add "gui/button/custom/corner_but_hit.png":
        #     xcenter 1050
        #     ycenter 495 #правый нижний






        imagebutton xcenter 805 ycenter 495:
            idle "gui/button/custom/corner_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[2][0][1]
            #action NullAction()
            action [Function(play, 2, 0, "X", 805, 495), Jump("change_side")]
        # add "gui/button/custom/corner_but_hit.png":
        #     xcenter 805
        #     ycenter 495 #левый нижний





        imagebutton xcenter 930 ycenter 230:
            idle "gui/button/custom/edge_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[0][1][1]
            #action NullAction()
            action [Function(play, 0, 1, "X", 940, 220), Jump("change_side")]
        # add "gui/button/custom/edge_but_hit.png":
        #     xcenter 930
        #     ycenter 230 #верхняя кнопка
        #





        imagebutton xcenter 927 ycenter 495:
            idle "gui/button/custom/edge_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[2][1][1]
            #action NullAction()
            action [Function(play, 2, 1, "X", 940, 495), Jump("change_side")]
        # add "gui/button/custom/edge_but_hit.png":
        #     xcenter 927
        #     ycenter 495 #нижняя кнопка
        #





        imagebutton xcenter 805 ycenter 363:
            idle "gui/button/custom/s_edge_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[1][0][1]
            #action  NullAction()
            action [Function(play, 1, 0, "X", 805, 363), Jump("change_side")]
        # add "gui/button/custom/s_edge_but_hit.png":
        #     xcenter 805
        #     ycenter 363 #левая кнопка (приписать s в начале)
        #







        imagebutton xcenter 1055 ycenter 363:
            idle "gui/button/custom/s_edge_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[1][2][1]
            #action NullAction()
            action [Function(play, 1, 2, "X", 1070, 363), Jump("change_side")]
        # add "gui/button/custom/s_edge_but_hit.png":
        #     xcenter 1055
        #     ycenter 363 #правая кнопка (приписать s в начале)
        #





        imagebutton xcenter 930 ycenter 363:
            idle "gui/button/custom/center_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[1][1][1]
            #action NullAction()
            action [Function(play, 1, 1, "X", 940, 363), Jump("change_side")]
        # add "gui/button/custom/center_but_hit.png":
        #     xcenter 930
        #     ycenter 363 #центральная кнопка



    if sst == "right":


        imagebutton xcenter 210 ycenter 230:
            idle "gui/button/custom/corner_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[0][0][1]
            #action NullAction()
            action [Function(play, 0, 0, "X", 210, 230), Jump("change_side")]
#, Function(play, None, None, "O")]

        # add "gui/button/custom/corner_but_hit.png":
        #     xcenter 210
        #     ycenter 230 #левый верхний

        imagebutton xcenter 450 ycenter 230:
            idle "gui/button/custom/corner_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[0][2][1]
            #action NullAction()
            action [Function(play, 0, 2, "X", 465, 230), Jump("change_side")]


        # add "gui/button/custom/corner_but_hit.png":
        #     xcenter 450
        #     ycenter 230 #правый верхний

        imagebutton xcenter 450 ycenter 495:
            idle "gui/button/custom/corner_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[2][2][1]
            #action NullAction()
            action [Function(play, 2, 2, "X", 465, 495), Jump("change_side")]



        # add "gui/button/custom/corner_but_hit.png":
        #     xcenter 450
        #     ycenter 495 #правый нижний


        imagebutton xcenter 205 ycenter 495:
            idle "gui/button/custom/corner_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[2][0][1]
            #action NullAction()
            action [Function(play, 2, 0, "X", 205, 495), Jump("change_side")]

        # add "gui/button/custom/corner_but_hit.png":
        #     xcenter 205
        #     ycenter 495 #левый нижний



        imagebutton xcenter 330 ycenter 230:
            idle "gui/button/custom/edge_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[0][1][1]
            #action NullAction()
            action [Function(play, 0, 1, "X", 340, 220), Jump("change_side")]


        # add "gui/button/custom/edge_but_hit.png":
        #     xcenter 330
        #     ycenter 230 #верхняя кнопка


        imagebutton xcenter 327 ycenter 495:
            idle "gui/button/custom/edge_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[2][1][1]
            #action NullAction()
            action [Function(play, 2, 1, "X", 340, 495), Jump("change_side")]

        # add "gui/button/custom/edge_but_hit.png":
        #     xcenter 327
        #     ycenter 495 #нижняя кнопка



        imagebutton xcenter 205 ycenter 363:
            idle "gui/button/custom/s_edge_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[1][0][1]
            #action  NullAction()
            action [Function(play, 1, 0, "X", 205, 363), Jump("change_side")]


        # add "gui/button/custom/s_edge_but_hit.png":
        #     xcenter 205
        #     ycenter 363 #левая кнопка (приписать s в начале)


        imagebutton xcenter 455 ycenter 363:
            idle "gui/button/custom/s_edge_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[1][2][1]
            #action NullAction()
            action [Function(play, 1, 2, "X", 470, 363), Jump("change_side")]


        # add "gui/button/custom/s_edge_but_hit.png":
        #     xcenter 455
        #     ycenter 363 #правая кнопка (приписать s в начале)

        imagebutton xcenter 330 ycenter 363:
            idle "gui/button/custom/center_but_hit.png"
            #insensitive "gui/button/custom/visbar.png"
            sensitive current_state[1][1][1]
            #action NullAction()
            action [Function(play, 1, 1, "X", 340, 363), Jump("change_side")]

        # add "gui/button/custom/center_but_hit.png":
        #     xcenter 330
        #     ycenter 363 #центральная кнопка





transform for_field_l():
    ycenter 365
    xcenter 940


transform for_field_r():
    ycenter 365
    xcenter 340

#-----------------------------------------Плеер----------------------------------------------
image button_back_inactive:
    im.Scale("gui/button/custom/round_inactive.png", 120, 214)
    xalign 0.452
    yalign 0.980
    alpha 0.0
    rotate -36.0
    easein 0.3 alpha 1.0

image button_eq_inactive:
    im.Scale("gui/button/custom/round_inactive.png", 120, 214)
    xalign 0.549
    yalign 0.982
    alpha 0.0
    rotate 36.0
    easein 0.3 alpha 1.0

image cursed = im.Scale("gui/button/custom/round_glitched.png", 120, 214)

image Youshouldnthavedonethat = LiveComposite((1280,720), (560,315), "n_rects1", (660,295), "n_rects2", (640,390), "n_rects3")

image Reverse = "images/cg/monika/reverse.png"


image pause_visual:
    DynamicDisplayable(vis_pause)
    xcenter 0.5
    ycenter 0.79
    size (673, 192)
image resumed_visual:
    DynamicDisplayable(vis_res)
    xcenter 0.5
    ycenter 0.79
    size (673, 192)



transform slow_vis_fade:
    ycenter 0.79
    linear 1 ycenter 1.1

transform fade_vis_resume:
    ycenter 1.1
    linear 0.5 ycenter 0.79

screen music_name:

    if track_num == 0:
        text "{size=20}Dan Salvato{/size}" xalign 0.5 yalign 0.80
        text "{size=20}Daijobu!{/size}" xalign 0.5 yalign 0.85
    if track_num == 1:
        text "{size=20}Vincienty{/size}" xalign 0.5 yalign 0.80
        text "{size=20}Heartbroken{/size}" xalign 0.5 yalign 0.85
    if track_num == 2:
        text "{size=20}Vincienty{/size}" xalign 0.5 yalign 0.80
        text "{size=20}Here We Go Again, Natsuki!{/size}" xalign 0.5 yalign 0.85
    if track_num == 3:
        text "{size=20}Dan Salvato{/size}" xalign 0.5 yalign 0.80
        text "{size=20}SnVzdCBNb25pa2E={/size}" xalign 0.5 yalign 0.85
    if track_num == 4:
        text "{size=20}Dan Salvato{/size}" xalign 0.5 yalign 0.80
        text "{size=20}Okay, Everyone! (Natsuki){/size}" xalign 0.5 yalign 0.85
    if track_num == 5:
        text "{size=20}Vincienty{/size}" xalign 0.5 yalign 0.80
        text "{size=20}Sweetest Cupcake{/size}" xalign 0.5 yalign 0.85


screen actions_name:
    if button == 3:
        text "Пауза" xalign 0.5 yalign 0.85
    if button == 1:
        text "Предыдущий" xalign 0.5 yalign 0.85
    if button == 5:
        text "Следующий" xalign 0.5 yalign 0.85
    if button == 6:
        text "Продолжить" xalign 0.5 yalign 0.85
    if button == 2:
        text "Установить как фон" xalign 0.5 yalign 0.85
    if button == 4:
        text "Повтор" xalign 0.5 yalign 0.85
    if button == 8:
        text "U3RvcCB0aGUgRW5kbGVzcyBDeWNsZQ==" xalign 0.5 yalign 0.85
    if button == 7:
        text "Показать визуализатор" xalign 0.5 yalign 0.85
    if button == 9:
        text "Скрыть визуализатор" xalign 0.5 yalign 0.85



screen broke_music():
    $broke_pos = get_pos()
    $broke = "<from " + str(broke_pos) + ">" + broken_list[track_num]
    $renpy.music.play(broke, channel="music")

screen reverse_music():
    $reverse_pos = get_pos()
    $reverse = "<from " + str(reverse_pos) + ">" + reversed_list[track_num]
    $renpy.music.play(reverse, channel="music")


screen set_to_normal_vis():
    timer delta action [SetVariable("mus_pos", 0), Function(renpy.show, "resumed_visual", zorder=1)]






screen broke_buttons():

    imagebutton xalign 0.5 yalign 0.878:
        idle "cursed"
        #at pos_3_broken
        action NullAction()

    imagebutton xalign 0.452 yalign 0.940:
        idle "cursed"
        #at pos_3_broken
        action NullAction()

    imagebutton xalign 0.422 yalign 1.032:
        idle "cursed"
        #at pos_3_broken
        action NullAction()

    imagebutton xalign 0.580 yalign 1.032:
        idle "cursed"
        #at pos_3_broken
        action NullAction()


screen button_pause():
    imagebutton xalign 0.5 yalign 0.878:
        idle "round_3_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 3), Function(renpy.show, "a_3", zorder=2), Function(renpy.hide, "i_3"), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.hide, "a_3"), Function(renpy.show, "i_3", zorder=2)]
        focus_mask "round_3_hit"
        #at pos_3
        action [Hide("button_pause"), Show("button_active_pause"), Function(renpy.music.set_pause, True, channel=u'music'), If(renpy.get_screen("vis_button") != None, true=NullAction(), false=[Function(ani_vis_pause), Hide("set_to_normal_vis")])]


screen button_active_pause():
    imagebutton xalign 0.5 yalign 0.878:
        idle "round_3_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 6), Function(renpy.show, "a_3", zorder=2), Function(renpy.hide, "i_3"), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.hide, "a_3"), Function(renpy.show, "i_3", zorder=2)]
        focus_mask "round_3_hit"
        #at pos_3_pause
        action [Hide("button_active_pause"), Show("button_pause"), Function(renpy.music.set_pause, False, channel=u'music'), If(renpy.get_screen("vis_button") != None, true=NullAction(), false=[Function(ani_vis_resume), Show("set_to_normal_vis")])]




screen button_set_back():
    on "show" action [Function(renpy.show, "i_2", zorder=2), Function(renpy.hide, "button_back_inactive")]
    imagebutton xalign 0.452 yalign 0.940:
        idle "round_2_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 2), Function(renpy.show, "a_2", zorder=2), Function(renpy.hide, "i_2"), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.hide, "a_2"), Function(renpy.show, "i_2", zorder=2)]
        focus_mask "round_2_hit"
        #at pos_2
        action [Function(save_back), Function(renpy.hide, "a_2"), Function(renpy.show, "button_back_inactive")]


screen inactive_set_back():
    on "show" action Function(renpy.hide, "i_2"), Function(renpy.show, "button_back_inactive", zorder=2)
    imagebutton xalign 0.452 yalign 0.940:
        idle "round_2_hit"
        focus_mask "round_2_hit"
        #at pos_2_broken
        action NullAction()


screen button_broken_cycle():
    $glitch_action = renpy.random.randint(1,3)
    imagebutton xalign 0.549 yalign 0.942:
        idle "round_4_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 4), Function(renpy.show, "a_4", zorder=2), Function(renpy.hide, "i_4"), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.hide, "a_4"), Function(renpy.show, "i_4", zorder=2)]
        focus_mask "round_4_hit"
        #at pos_4
        action [If(glitch_action == 1, true=[Function(renpy.play, "gui/sfx/baa.ogg", channel='sound'), Hide("music_player_buttons"), Hide("button_broken_cycle"), Jump("what_was_that")], false=NullAction()), If(glitch_action == 2, true=[Function(renpy.music.set_volume, 1.0, channel="music"), Function(renpy.show, "Youshouldnthavedonethat", zorder=100), Show("broke_music"), Show("broke_buttons"), Show("active_broken_cycle"), Hide("button_broken_cycle"), Hide("music_player_buttons")], false=NullAction()), If(glitch_action == 3, true=[Show("broke_buttons"), Show("reverse_music"), Show("active_broken_cycle"), Hide("button_broken_cycle"), Hide("music_player_buttons"), Function(renpy.show, "Reverse", zorder=100)], false=NullAction())]
    $persistent.is_glitching = True
    $renpy.save_persistent()



screen active_broken_cycle():
    imagebutton xalign 0.549 yalign 0.942:
        idle "round_4_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 8), Function(renpy.show, "a_4", zorder=2), Function(renpy.hide, "i_4"), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.hide, "a_4"), Function(renpy.show, "i_4", zorder=2)]
        focus_mask "round_4_hit"
        #at pos_4
        action [Function(renpy.music.set_volume, persistent.svol, channel="music"), Hide("active_broken_cycle"), Function(renpy.hide, "Youshouldnthavedonethat"), Hide("broke_music"), Hide("broke_buttons"), Hide("reverse_music"), Function(renpy.hide, "Reverse"), Hide("music_player_buttons"), Jump("what_was_that")]


screen inactive_cycle():
    on "show" action Function(renpy.hide, "i_4"), Function(renpy.show, "button_eq_inactive", zorder=2)
    imagebutton xalign 0.549 yalign 0.942:
        idle "round_4_hit"
        focus_mask "round_4_hit"
        #at pos_4_broken
        action NullAction()


screen vis_button():
    imagebutton xalign 0.549 yalign 0.942:
        idle "round_4_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 7), Function(renpy.show, "a_4", zorder=2), Function(renpy.hide, "i_4"), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.hide, "a_4"), Function(renpy.show, "i_4", zorder=2),]
        focus_mask "round_4_hit"
        #at pos_4
        action [Function(ani_vis_resume), Show("set_to_normal_vis"), Hide("vis_button"), Show("active_vis_button"), SetVariable("is_shown_vis", True)]



screen active_vis_button():
    imagebutton xalign 0.549 yalign 0.942:
        idle "round_4_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 9), Function(renpy.show, "a_4", zorder=2), Function(renpy.hide, "i_4"), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.hide, "a_4"), Function(renpy.show, "i_4", zorder=2),]
        focus_mask "round_4_hit"
        #at pos_4
        action [Function(renpy.hide, "pause_visual"), Function(renpy.hide, "resumed_visual"), Hide("set_to_normal_vis"), Show("vis_button"), Hide("active_vis_button"), SetVariable("is_shown_vis", False)]



screen music_player_buttons():

    on "show" action [Show("button_pause"), If(renpy.music.get_playing(channel="music") == (music_path + music_list[persistent.back_music]) or renpy.music.get_playing(channel="music") == music_list[persistent.back_music], true=Show("inactive_set_back"), false=Show("button_set_back")), If(persistent.is_glitching == True, true=If(persistent.first_vis == True, true=If(is_shown_vis == True, true=[Show("active_vis_button"), Function(ani_vis_resume), Show("set_to_normal_vis")], false=Show("vis_button")), false=Show("inactive_cycle")), false=Show("button_broken_cycle")), Show("music_name"), Hide("talk_button"), Hide("countdown"), Function(renpy.show, "i_1", zorder=2), Function(renpy.show, "i_3", zorder=2), Function(renpy.show, "i_4", zorder=2), Function(renpy.show, "i_5", zorder=2), Function(renpy.show, "button_back_inactive", zorder=2)]

    on "hide" action [Hide("button_pause"), Hide("button_active_pause"), Hide("button_set_back"), Hide("inactive_set_back"), Hide("inactive_cycle"), Hide("button_broken_cycle"), Hide("music_name"), Hide("actions_name"), Hide("vis_button"), Hide("active_vis_button"), Function(renpy.hide, "pause_visual"), Function(renpy.hide, "resumed_visual"), Hide("set_to_normal_vis"), Function(renpy.hide, "i_1"), Function(renpy.hide, "i_2"), Function(renpy.hide, "i_3"), Function(renpy.hide, "i_4"), Function(renpy.hide, "i_5"), Function(renpy.hide, "button_back_inactive"), Function(renpy.hide, "button_eq_inactive"), Function(renpy.hide, "a_1"), Function(renpy.hide, "a_2"), Function(renpy.hide, "a_3"), Function(renpy.hide, "a_4"), Function(renpy.hide, "a_5"),]




    imagebutton xalign 0.422 yalign 1.032:
        idle "round_1_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 1), Function(renpy.show, "a_1", zorder=2), Function(renpy.hide, "i_1"), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Function(set_value, 0), Function(renpy.hide, "a_1"), Function(renpy.show, "i_1", zorder=2), Hide("actions_name", transition = Dissolve(0.2)), Show("music_name", transition = Dissolve(0.2))]
        focus_mask "round_1_hit"
        #at pos_1
        action [Function(previous_song), Hide("set_to_normal_vis")]

    imagebutton xalign 0.580 yalign 1.032:
        idle "round_5_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 5), Function(renpy.show, "a_5", zorder=2), Function(renpy.hide, "i_5"),Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Function(set_value, 0), Function(renpy.hide, "a_5"), Function(renpy.show, "i_5", zorder=2), Hide("actions_name", transition = Dissolve(0.2)), Show("music_name", transition = Dissolve(0.2))]
        focus_mask "round_5_hit"
        #at pos_5
        action [Function(next_song), Hide("set_to_normal_vis")]







#
screen music_key():
    key persistent.m_key action [Hide("music_key"), Show("active_music_key"), Show("hide_all_talk"), Hide("countdown"), Show("music_player_buttons")]

    key persistent.m_key.upper() action [Hide("music_key"), Show("active_music_key"), Show("hide_all_talk"), Hide("countdown"), Show("music_player_buttons")]

    key persistent.m_r_key action [Hide("music_key"), Show("active_music_key"), Show("hide_all_talk"), Hide("countdown"), Show("music_player_buttons")]

    key persistent.m_r_key.upper() action [Hide("music_key"), Show("active_music_key"), Show("hide_all_talk"), Hide("countdown"), Show("music_player_buttons")]


screen active_music_key():

    key persistent.m_key action [Hide("music_player_buttons"), Show("music_key"), Hide("active_music_key"), Show("talk_button"), Show("countdown"), Function(set_back_on_exit)]

    key persistent.m_key.upper() action [Hide("music_player_buttons"), Show("music_key"), Hide("active_music_key"), Show("talk_button"), Show("countdown"), Function(set_back_on_exit)]

    key persistent.m_r_key action [Hide("music_player_buttons"), Show("music_key"), Hide("active_music_key"), Show("talk_button"), Show("countdown"), Function(set_back_on_exit)]

    key persistent.m_r_key.upper() action [Hide("music_player_buttons"), Show("music_key"), Hide("active_music_key"), Show("talk_button"), Show("countdown"), Function(set_back_on_exit)]

    key "K_ESCAPE" action [Hide("music_player_buttons"), Show("music_key"), Hide("active_music_key"), Show("talk_button"), Show("countdown"), Function(set_back_on_exit)]





#------------------------------------Настройка громкости--------------------------------------------------


transform show_vol_animation:
    alpha 1.0
    zoom 0.15
    xalign 0.5
    yalign 2.10
    easein 1.0 rotate 180

transform show_vol_level_animation:
    alpha 1.0
    zoom 0.152
    xalign 0.497
    yalign 2.15
    easein 1.0 rotate grad

transform show_sound_vol_level_animation:
    alpha 1.0
    zoom 0.152
    xalign 0.497
    yalign 2.15
    easein 1.0 rotate soungrad



transform hide_vol_animation:
    zoom 0.15
    xalign 0.5
    yalign 2.10
    easein 1.0 rotate 360
    rotate 0
    alpha 0.0

transform hide_vol_level_animation:
    zoom 0.152
    xalign 0.497
    yalign 2.15
    easein 1.0 rotate 360
    rotate 0
    alpha 0.0





transform vol_level_animation:
    zoom 0.152
    xalign 0.497
    yalign 2.15
    rotate grad

transform vol_sound_level_animation:
    zoom 0.152
    xalign 0.497
    yalign 2.15
    rotate soungrad


transform volume_mask:
    ypos 45
    xalign 0.5


transform pos_cup_button:
    xalign 0.5
    yalign 0.95



image level_cir = "gui/button/custom/volume_circle_level.png"
image anim_cir = "gui/button/custom/volume_circle.png"
image cup_but = im.Scale("gui/button/custom/cup_button.png", 100, 100)



screen volume_key():
    key persistent.v_key.upper() action [SetVariable("set", "music"), Hide("volume_key"), Show("active_volume_key"), Show("con_volume"), Hide("sound_volume_key"), Hide("talk_button"), Hide("countdown"), Function(renpy.show, "cup_but", at_list=[pos_cup_button], zorder=10), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    key persistent.v_key action [SetVariable("set", "music"), Hide("volume_key"), Show("active_volume_key"), Show("con_volume"), Hide("sound_volume_key"), Hide("talk_button"), Hide("countdown"), Function(renpy.show, "cup_but", at_list=[pos_cup_button], zorder=10), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    key persistent.v_r_key.upper() action [SetVariable("set", "music"), Hide("volume_key"), Show("active_volume_key"), Show("con_volume"), Hide("sound_volume_key"), Hide("talk_button"), Hide("countdown"), Function(renpy.show, "cup_but", at_list=[pos_cup_button], zorder=10), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    key persistent.v_r_key action [SetVariable("set", "music"), Hide("volume_key"), Show("active_volume_key"), Show("con_volume"), Hide("sound_volume_key"), Hide("talk_button"), Hide("countdown"), Function(renpy.show, "cup_but", at_list=[pos_cup_button], zorder=10), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]



screen active_volume_key():

    key persistent.v_key action [Hide("con_volume"), Show("volume_key"), Hide("active_volume_key"), Show("sound_volume_key"), Show("talk_button"), Show("countdown"), Function(renpy.hide, "cup_but"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key persistent.v_key.upper() action [Hide("con_volume"), Show("volume_key"), Hide("active_volume_key"), Show("sound_volume_key"), Show("talk_button"), Show("countdown"), Function(renpy.hide, "cup_but"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key persistent.v_r_key.upper() action [Hide("con_volume"), Show("volume_key"), Hide("active_volume_key"), Show("sound_volume_key"), Show("talk_button"), Show("countdown"), Function(renpy.hide, "cup_but"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key persistent.v_r_key action [Hide("con_volume"), Show("volume_key"), Hide("active_volume_key"), Show("sound_volume_key"), Show("talk_button"), Show("countdown"), Function(renpy.hide, "cup_but"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key "K_ESCAPE" action [Hide("con_volume"), Show("volume_key"), Hide("active_volume_key"), Show("sound_volume_key"), Show("talk_button"), Show("countdown"), Function(renpy.hide, "cup_but"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    $persistent.svol = vlm
    $persistent.snum = num
    $persistent.sgrad = grad
    $renpy.save_persistent()





screen sound_volume_key():
    key persistent.s_key.upper() action [SetVariable("set", "sound"), Hide("sound_volume_key"), Show("active_sound_volume_key"), Show("con_sound_volume"), Hide("volume_key"), Hide("talk_button"), Hide("countdown"), Show("sound_test"), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    key persistent.s_key action [SetVariable("set", "sound"), Hide("sound_volume_key"), Show("active_sound_volume_key"), Show("con_sound_volume"), Hide("volume_key"), Hide("talk_button"), Hide("countdown"), Show("sound_test"), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    key persistent.s_r_key action [SetVariable("set", "sound"), Hide("sound_volume_key"), Show("active_sound_volume_key"), Show("con_sound_volume"), Hide("volume_key"), Hide("talk_button"), Hide("countdown"), Show("sound_test"), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    key persistent.s_r_key.upper() action [SetVariable("set", "sound"), Hide("sound_volume_key"), Show("active_sound_volume_key"), Show("con_sound_volume"), Hide("volume_key"), Hide("talk_button"), Hide("countdown"), Show("sound_test"), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]


screen active_sound_volume_key():

    key persistent.s_key action [Hide("con_sound_volume"), Show("sound_volume_key"), Hide("active_sound_volume_key"), Show("volume_key"), Show("talk_button"), Show("countdown"), Hide("sound_test"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key persistent.s_key.upper() action [Hide("con_sound_volume"), Show("sound_volume_key"), Hide("active_sound_volume_key"), Show("volume_key"), Show("talk_button"), Show("countdown"), Hide("sound_test"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key persistent.s_r_key action [Hide("con_sound_volume"), Show("sound_volume_key"), Hide("active_sound_volume_key"), Show("volume_key"), Show("talk_button"), Show("countdown"), Hide("sound_test"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key persistent.s_r_key.upper() action [Hide("con_sound_volume"), Show("sound_volume_key"), Hide("active_sound_volume_key"), Show("volume_key"), Show("talk_button"), Show("countdown"), Hide("sound_test"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key "K_ESCAPE" action [Hide("con_sound_volume"), Show("sound_volume_key"), Hide("active_sound_volume_key"), Show("volume_key"), Show("talk_button"), Show("countdown"), Hide("sound_test"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]


    $persistent.soundvol = soundvlm
    $persistent.soundnum = sounum
    $persistent.soundgrad = soungrad
    $renpy.save_persistent()



screen sound_test():
    zorder 10
    imagebutton xalign 0.5 yalign 0.95:
        idle im.Scale("gui/button/custom/cup_button.png", 100, 100)
        hover im.Scale("gui/button/custom/cup_button_hover.png", 100, 100)
        hovered [Play("sound", "gui/sfx/hover.ogg")]
        action NullAction()




screen vol_texts:

    if set == "music":
        $vln = str(num)
        $sh_txt = "Музыка: " + vln
        text sh_txt xalign 0.5 yalign 0.78
    elif set == "sound":
        $vln = str(sounum)
        $sh_txt = "Звуки: " + vln
        text sh_txt xalign 0.5 yalign 0.78


screen con_volume():
    on "show" action [Function(renpy.show, "anim_cir", at_list=[show_vol_animation], zorder=3), Function(renpy.show, "level_cir", at_list=[show_vol_level_animation], zorder=4), Function(renpy.show, "move nat", at_list=[volume_mask], zorder=5), Show("vol_texts", transition=dissolve)]

    on "hide" action [Function(renpy.show, "anim_cir", at_list=[hide_vol_animation], zorder=3), Function(renpy.show, "level_cir", at_list=[hide_vol_level_animation], zorder=4), Hide("vol_texts", transition=dissolve)]


    if num > 99:

        key "mouseup_3" action [SetVariable("vlm", 1.0), SetVariable("num", 100), SetVariable("grad", 180), Function(renpy.music.set_volume, num, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]


        key "mouseup_4" action NullAction()

        key "mouseup_5" action [SetVariable("num", num - 1), SetVariable("vlm", vlm - 0.01), SetVariable("grad", grad - 1.8), Function(renpy.music.set_volume, vlm, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]





    elif num < 1:


        key "mouseup_3" action [SetVariable("vlm", 0.0), SetVariable("num", 0), SetVariable("grad", 0), Function(renpy.music.stop, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]

        key "mouseup_4" action [SetVariable("num", num + 1), SetVariable("vlm", vlm + 0.01), SetVariable("grad", grad + 1), Function(renpy.music.set_volume, vlm, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]

        key "mouseup_5" action [SetVariable("vlm", 0.0), SetVariable("num", 0), SetVariable("grad", 0), Function(renpy.music.set_pause, True, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]




    else:


        key "mouseup_4" action [Function(renpy.music.set_pause, False, channel="music"), SetVariable("num", num + 1), SetVariable("vlm", vlm + 0.01), SetVariable("grad", grad + 1.8), Function(renpy.music.set_volume, vlm, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]

        key "mouseup_5" action [SetVariable("num", num - 1), SetVariable("vlm", vlm - 0.01), SetVariable("grad", grad - 1.8), Function(renpy.music.set_volume, vlm, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]










screen con_sound_volume():
    on "show" action [Function(renpy.show, "anim_cir", at_list=[show_vol_animation], zorder=3), Function(renpy.show, "level_cir", at_list=[show_sound_vol_level_animation], zorder=4), Function(renpy.show, "move nat", at_list=[volume_mask], zorder=5), Show("vol_texts", transition=dissolve)]

    on "hide" action [Function(renpy.show, "anim_cir", at_list=[hide_vol_animation], zorder=3), Function(renpy.show, "level_cir", at_list=[hide_vol_level_animation], zorder=4), Hide("vol_texts", transition=dissolve)]


    if sounum > 99:

        key "mouseup_3" action [SetVariable("soundvlm", 1.0), SetVariable("sounum", 100), SetVariable("soungrad", 180), Function(renpy.sound.set_volume, sounum, channel="sound"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_sound_level_animation], zorder=4)]


        key "mouseup_4" action NullAction()

        key "mouseup_5" action [SetVariable("sounum", sounum - 1), SetVariable("soundvlm", soundvlm - 0.01), SetVariable("soungrad", soungrad - 1.8), Function(renpy.sound.set_volume, soundvlm, channel="sound"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_sound_level_animation], zorder=4)]





    elif sounum < 1:


        key "mouseup_3" action [SetVariable("soundvlm", 0.0), SetVariable("sounum", 0), SetVariable("soungrad", 0), Function(renpy.sound.stop, channel="sound"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_sound_level_animation], zorder=4)]

        key "mouseup_4" action [SetVariable("sounum", sounum + 1), SetVariable("soundvlm", soundvlm + 0.01), SetVariable("soungrad", soungrad + 1.8), Function(renpy.sound.set_volume, soundvlm, channel="sound"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_sound_level_animation], zorder=4)]

        key "mouseup_5" action [SetVariable("soundvlm", 0.0), SetVariable("sounum", 0), SetVariable("soungrad", 0), Function(renpy.sound.stop, channel="sound"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_sound_level_animation], zorder=4)]




    else:


        key "mouseup_4" action [Function(renpy.music.set_pause, False, channel="sound"), SetVariable("sounum", sounum + 1), SetVariable("soundvlm", soundvlm + 0.01), SetVariable("soungrad", soungrad + 1.8), Function(renpy.sound.set_volume, soundvlm, channel="sound"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_sound_level_animation], zorder=4)]

        key "mouseup_5" action [SetVariable("sounum", sounum - 1), SetVariable("soundvlm", soundvlm - 0.01), SetVariable("soungrad", soungrad - 1.8), Function(renpy.sound.set_volume, soundvlm, channel="sound"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_sound_level_animation], zorder=4)]

#-----------------------------------------Кнопки для разговора-------------------------------------



screen hide_all_talk():
    on "show" action [Hide("talk_button"), Hide("active_talk_button"), Hide("talk_round"), Hide("active_talk_round"), Hide("texts"), Hide("choice_buttons_1"), Hide("choice_buttons_2")]




image round_full = im.Scale("gui/button/custom/round_full.png", 400, 200)

image round_1_hit:
    im.Scale("gui/button/custom/round_hit.png", 110, 195)
    rotate -72
image round_2_hit:
    im.Scale("gui/button/custom/round_hit.png", 110, 195)
    rotate -36
image round_3_hit = im.Scale("gui/button/custom/round_hit.png", 110, 195)
image round_4_hit:
    im.Scale("gui/button/custom/round_hit.png", 110, 195)
    rotate 36
image round_5_hit:
    im.Scale("gui/button/custom/round_hit.png", 110, 195)
    rotate 72


image i_1:
    im.Scale("gui/button/custom/round_1.png", 120, 214)
    rotate -72
    alpha 0.0
    xalign 0.398
    yalign 1.033
    easein 0.3 xalign 0.422 yalign 1.072 alpha 1.0
image a_1:
    im.Scale("gui/button/custom/round_1.png", 120, 214)
    rotate -72
    alpha 0.0
    xalign 0.422
    yalign 1.072
    easein 0.3 xalign 0.398 yalign 1.033 alpha 1.0

image a_2:
    im.Scale("gui/button/custom/round_1.png", 120, 214)
    rotate -36.0
    alpha 0.0
    xalign 0.452
    yalign 0.980
    easein 0.3 xalign 0.437 yalign 0.943 alpha 1.0
image i_2:
    im.Scale("gui/button/custom/round_1.png", 120, 214)
    rotate -36.0
    alpha 0.0
    xalign 0.437
    yalign 0.943
    easein 0.3 xalign 0.452 yalign 0.980 alpha 1.0

image a_3:
    im.Scale("gui/button/custom/round_1.png", 120, 214)
    alpha 0.0
    yalign 0.918
    easein 0.3 yalign 0.858 alpha 1.0
image i_3:
    im.Scale("gui/button/custom/round_1.png", 120, 214)
    alpha 0.0
    yalign 0.858
    easein 0.3 yalign 0.918 alpha 1.0

image a_4:
    im.Scale("gui/button/custom/round_1.png", 120, 214)
    rotate 36.0
    alpha 0.0
    xalign 0.549
    yalign 0.982
    easein 0.3 xalign 0.564 yalign 0.937 alpha 1.0
image i_4:
    im.Scale("gui/button/custom/round_1.png", 120, 214)
    rotate 36.0
    alpha 0.0
    xalign 0.564
    yalign 0.937
    easein 0.3 xalign 0.549 yalign 0.982 alpha 1.0

image a_5:
    im.Scale("gui/button/custom/round_1.png", 120, 214)
    rotate 72
    alpha 0.0
    xalign 0.580
    yalign 1.072
    easein 0.3 xalign 0.607 yalign 1.034 alpha 1.0
image i_5:
    im.Scale("gui/button/custom/round_1.png", 120, 214)
    rotate 72
    alpha 0.0
    xalign 0.607
    yalign 1.034
    easein 0.3 xalign 0.580 yalign 1.072 alpha 1.0




screen talk_button():
    zorder 10
    imagebutton xalign 0.5 yalign 0.95:
        idle im.Scale("gui/button/custom/talk.png", 100, 100)
        hover im.Scale("gui/button/custom/talk_hover.png", 100, 100)
        hovered [Play("sound", "gui/sfx/hover.ogg")]
        action [Show("talk_round"), Hide("volume_key"), Hide("sound_volume_key"), Hide("music_key"), Play("sound", "gui/sfx/select.ogg"), Show("key_hider_talk")]
        #activate_sound gui.activate_sound

screen active_talk_button():
    zorder 10
    imagebutton xalign 0.5 yalign 0.95:
        idle im.Scale("gui/button/custom/talk.png", 100, 100)
        hover im.Scale("gui/button/custom/talk_hover.png", 100, 100)
        hovered [Play("sound", "gui/sfx/hover.ogg")]
        action [Show("active_talk_round"), Show("volume_key"), Show("sound_volume_key"), Show("music_key"), Play("sound", "gui/sfx/select.ogg"), Hide("key_hider_talk")]
        #activate_sound gui.activate_sound

screen talk_round:
    on "show" action [Hide("talk_button"), Show("active_talk_button"), Hide("active_talk_round"), Show("choice_buttons_1")]

screen active_talk_round:
    on "show" action [Hide("choice_buttons_1", transition = dissolve), Hide("choice_buttons_2", transition = dissolve), Hide("active_talk_button"), Hide("talk_round"), Show("talk_button")]

screen key_hider_talk():
    key "K_ESCAPE" action [Hide("choice_buttons_1", transition = dissolve), Hide("choice_buttons_2", transition = dissolve), Hide("active_talk_button"), Hide("talk_round"), Show("talk_button"), Show("active_talk_round"), If(persistent.ch_vol == True, true=[Show("volume_key"), Show("sound_volume_key")], false=NullAction()), If(persistent.ch_mus == True, true=Show("music_key"), false=NullAction()), SetVariable("is_esc_pressed", True), Jump("ch1_loop")]

screen texts:
    if button == 1:
        text "Личность" xalign 0.5 yalign 0.78
    elif button == 2:
        text "Увлечения" xalign 0.5 yalign 0.78
    elif button == 3:
        text "Вперёд" xalign 0.5 yalign 0.78
    elif button == 4:
        text "Готовка" xalign 0.5 yalign 0.78
    elif button == 5:
        text "Прошлое" xalign 0.5 yalign 0.78
    elif button == 6:
        text "Романтика" xalign 0.5 yalign 0.78
    elif button == 7:
        text "Философия" xalign 0.5 yalign 0.78
    elif button == 8:
        text "Назад" xalign 0.5 yalign 0.78
    elif button == 9:
        text "Просьбы" xalign 0.5 yalign 0.78
    elif button == 10:
        text "Другое" xalign 0.5 yalign 0.78

screen choice_buttons_1():
    on "show" action [Function(renpy.show, "i_1", zorder=2), Function(renpy.show, "i_2", zorder=2), Function(renpy.show, "i_3", zorder=2), Function(renpy.show, "i_4", zorder=2), Function(renpy.show, "i_5", zorder=2)]

    on "hide" action [Function(renpy.hide, "i_1"), Function(renpy.hide, "i_2"), Function(renpy.hide, "i_3"), Function(renpy.hide, "i_4"), Function(renpy.hide, "i_5"), Function(renpy.hide, "a_1"), Function(renpy.hide, "a_2"), Function(renpy.hide, "a_3"), Function(renpy.hide, "a_4"), Function(renpy.hide, "a_5"), Hide("texts")]

    imagebutton xalign 0.5 yalign 0.878:
        idle "round_3_hit"
        hovered [Function(set_value, 3), Function(renpy.show, "a_3", zorder=2), Function(renpy.hide, "i_3"), Show("texts", transition = Dissolve(0.2)), Play("sound", "gui/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.hide, "a_3"), Function(renpy.show, "i_3", zorder=2), Hide("texts", transition = Dissolve(0.2))]
        focus_mask "round_3_hit"
        #at pos_3
        action [Hide("choice_buttons_1", transition = Dissolve(0.2)), Show("choice_buttons_2", transition = Dissolve(0.2))]

    imagebutton xalign 0.452 yalign 0.940:
        idle "round_2_hit"
        hovered [Function(set_value, 2), Function(renpy.show, "a_2", zorder=2), Function(renpy.hide, "i_2"), Show("texts", transition = Dissolve(0.2)), Play("sound", "gui/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.hide, "a_2"), Function(renpy.show, "i_2", zorder=2), Hide("texts", transition = Dissolve(0.2))]
        focus_mask "round_2_hit"
        #at pos_2
        action Jump("dia_hobbies")

    imagebutton xalign 0.549 yalign 0.942:
        idle "round_4_hit"
        hovered [Function(set_value, 4), Function(renpy.show, "a_4", zorder=2), Function(renpy.hide, "i_4"), Show("texts", transition = Dissolve(0.2)), Play("sound", "gui/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.hide, "a_4"), Function(renpy.show, "i_4", zorder=2), Hide("texts", transition = Dissolve(0.2))]
        focus_mask "round_4_hit"
        #at pos_4
        action Jump("dia_recipes")

    imagebutton xalign 0.422 yalign 1.032:
        idle "round_1_hit"
        hovered [Function(set_value, 1), Function(renpy.show, "a_1", zorder=2), Function(renpy.hide, "i_1"), Show("texts", transition = Dissolve(0.2)), Play("sound", "gui/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.hide, "a_1"), Function(renpy.show, "i_1", zorder=2), Hide("texts", transition = Dissolve(0.2))]
        focus_mask "round_1_hit"
        #at pos_1
        action Jump("dia_personality")

    imagebutton xalign 0.580 yalign 1.032:
        idle "round_5_hit"
        hovered [Function(set_value, 5), Function(renpy.show, "a_5", zorder=2), Function(renpy.hide, "i_5"),Show("texts", transition = Dissolve(0.2)), Play("sound", "gui/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.hide, "a_5"), Function(renpy.show, "i_5", zorder=2), Hide("texts", transition = Dissolve(0.2))]
        focus_mask "round_5_hit"
        #at pos_5
        action Jump("dia_past")




screen choice_buttons_2():
    on "show" action [Function(renpy.show, "i_1", zorder=2), Function(renpy.show, "i_2", zorder=2), Function(renpy.show, "i_3", zorder=2), Function(renpy.show, "i_4", zorder=2), Function(renpy.show, "i_5", zorder=2)]

    on "hide" action [Function(renpy.hide, "i_1"), Function(renpy.hide, "i_2"), Function(renpy.hide, "i_3"), Function(renpy.hide, "i_4"), Function(renpy.hide, "i_5"), Function(renpy.hide, "a_1"), Function(renpy.hide, "a_2"), Function(renpy.hide, "a_3"), Function(renpy.hide, "a_4"), Function(renpy.hide, "a_5"), Hide("texts")]

    imagebutton xalign 0.5 yalign 0.878:
        idle "round_3_hit"
        hovered [Function(set_value, 8), Function(renpy.show, "a_3", zorder=2), Function(renpy.hide, "i_3"), Show("texts", transition = Dissolve(0.2)), Play("sound", "gui/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.hide, "a_3"), Function(renpy.show, "i_3", zorder=2), Hide("texts", transition = Dissolve(0.2))]
        focus_mask "round_3_hit"
        #at pos_3
        action [Hide("choice_buttons_2", transition = Dissolve(0.2)), Show("choice_buttons_1", transition = Dissolve(0.2))]

    imagebutton xalign 0.452 yalign 0.940:
        idle "round_2_hit"
        hovered [Function(set_value, 7), Function(renpy.show, "a_2", zorder=2), Function(renpy.hide, "i_2"), Show("texts", transition = Dissolve(0.2)), Play("sound", "gui/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.hide, "a_2"), Function(renpy.show, "i_2", zorder=2), Hide("texts", transition = Dissolve(0.2))]
        focus_mask "round_2_hit"
        #at pos_2
        action Jump("dia_philosophy")

    imagebutton xalign 0.549 yalign 0.942:
        idle "round_4_hit"
        hovered [Function(set_value, 9), Function(renpy.show, "a_4", zorder=2), Function(renpy.hide, "i_4"), Show("texts", transition = Dissolve(0.2)), Play("sound", "gui/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.hide, "a_4"), Function(renpy.show, "i_4", zorder=2), Hide("texts", transition = Dissolve(0.2))]
        focus_mask "round_4_hit"
        #at pos_4
        action Jump("dia_requests")

    imagebutton xalign 0.422 yalign 1.032:
        idle "round_1_hit"
        hovered [Function(set_value, 6), Function(renpy.show, "a_1", zorder=2), Function(renpy.hide, "i_1"), Show("texts", transition = Dissolve(0.2)), Play("sound", "gui/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.hide, "a_1"), Function(renpy.show, "i_1", zorder=2), Hide("texts", transition = Dissolve(0.2))]
        focus_mask "round_1_hit"
        #at pos_1
        action Jump("dia_romance")

    imagebutton xalign 0.580 yalign 1.032:
        idle "round_5_hit"
        hovered [Function(set_value, 10), Function(renpy.show, "a_5", zorder=2), Function(renpy.hide, "i_5"), Show("texts", transition = Dissolve(0.2)), Play("sound", "gui/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.hide, "a_5"), Function(renpy.show, "i_5", zorder=2), Hide("texts", transition = Dissolve(0.2))]
        focus_mask "round_5_hit"
        #at pos_5
        action Jump("dia_other")


#please, please, please, work!

#-------------------------------------------Модовые экраны--------------------------------------

screen countdown:
    timer 1 repeat True action If(count > 0, true=SetVariable('count', count - 1), false=[Hide('countdown'), Jump(timer_jump)])



screen wowcup:
    timer 1 repeat True action If(moment > 0, true=SetVariable('moment', moment - 1), false=[Hide('wowcup'), Show('wowitscupcake')])



screen wowitscupcake:
    on "show" action Function(renpy.show, "cupcake", at_list = [poscup], zorder = 0)



screen set_on_full():
    key persistent.f_key action [Preference("display", "fullscreen"), Hide("set_on_full"), Show("set_on_window")]

screen set_on_window():
    key persistent.f_key action [Preference("display", "window"), Show("set_on_full"), Hide("set_on_window")]

screen set_on_beginning():
    on "show" action Preference("display", "fullscreen")


#-----------------------------------------------Оригинальные экраны----------------------------------------------------



screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"



    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu



screen input(prompt):
    style_prefix "input"

    window:

        # has vbox:
        #     xpos gui.text_xpos
        #     xanchor 0.5
        #     ypos gui.text_ypos

        text prompt xalign 0.5 yalign 0.45
        input id "input" xalign 0.5 yalign 0.70



screen choice(items):
    vbox:

        style_prefix "choice"

        if left == True:
            xalign 0.85
            yalign 0.5
        elif right == True:
            xalign 0.15
            yalign 0.5
        else:
            xalign 0.5
            yalign 0.5
        for i in items:
            textbutton i.caption action i.action


screen quick_menu():


    zorder 100

    if quick_menu:


        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995


            textbutton _("История") action ShowMenu('history')
            textbutton _("Пропуск") action Skip()
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Сохранить") action ShowMenu('save')
            textbutton _("Загрузить") action ShowMenu('load')


            textbutton _("Настройки") action ShowMenu('preferences')


screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.8

        spacing gui.navigation_spacing

        if not persistent.autoload or not main_menu:

            if main_menu:
                textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, false=Start())

            else:

                textbutton _("История") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]

                textbutton _("Сохранить") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]

            textbutton _("Загрузить") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]

            if _in_replay:

                textbutton _("Завершить повтор") action EndReplay(confirm=True)

            elif not main_menu:
                if persistent.playthrough != 3:
                    textbutton _("Главное меню") action MainMenu()
                else:
                    textbutton _("Главное меню") action NullAction()

            textbutton _("Настройки") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]



            if renpy.variant("pc"):


                textbutton _("Помощь") action [Help("README.html"), Show(screen="dialog", message="Файл справки открыт в браузере.", ok_action=Hide("dialog"))]


                textbutton _("Выход") action Quit(confirm=not main_menu)
        else:
            timer 1.75 action Start("autoload_yurikill")



screen main_menu():




    style_prefix "main_menu" tag menu

    add "menu_bg"
    add "menu_art_y"
    add "menu_art_n"
    frame




    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        add "menu_logo"
    if persistent.ghost_menu:
        add "menu_art_s_ghost"
        add "menu_art_m_ghost"
    else:
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            add "menu_art_s_glitch"
        else:
            add "menu_art_s"
        add "menu_particles"
        if persistent.playthrough != 4:
            add "menu_art_m"
        add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)



screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

screen game_menu(title, scroll=None):


    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    yinitial 1.0

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial 1.0

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    transclude

            else:

                transclude

    use navigation

    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show" action Show("game_menu_m")

    textbutton _("Назад"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")



screen about():
    tag menu



    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



screen save():
    tag menu


    use file_slots(_("Save"))


screen load():
    tag menu


    use file_slots(_("Загрузить"))



screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=u'Страница {}')

    use game_menu(title):

        fixed:



            order_reverse True



            button:
                style "page_label"


                xalign 0.5


                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileActionMod(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("пустой слот")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)



screen preferences():
    tag menu


    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Настройки"), scroll="viewport"):

        vbox:
            xoffset 50

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Режим экрана")
                        textbutton _("Оконный") action Preference("display", "window")
                        textbutton _("Полноэкранный") action Preference("display", "fullscreen")
                #if config.developer:
                    #vbox:
                        #style_prefix "radio"
                        #label _("Rollback Side")
                        #textbutton _("Disable") action Preference("rollback side", "disable")
                        #textbutton _("Left") action Preference("rollback side", "left")
                        #textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Пропускать")
                    textbutton _("Непрочитанное") action Preference("skip", "toggle")
                    textbutton _("После выбора") action Preference("after choices", "toggle")





            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Скорость вывода текста")


                    bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, style="slider", offset=20)

                    label _("Задержка при авточтении")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Громкость музыки")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Громкость звуков")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Отключить звук"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
    text "v[config.version]":
        xalign 1.0 yalign 1.0
        xoffset -10 yoffset -10
        style "main_menu_version"




screen history():




    predict False tag menu

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")





screen name_input(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "" value VariableInputValue("player") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"






        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

screen dialog(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action



screen fake_skip_indicator():
    use skip_indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 6

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')



#------------------------------------------Оригинальные стили----------------------------------------------------------


style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1

style default_monika is normal:
    slow_cps 30

style edited is default:
    font "gui/font/comic.ttf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

style splash_text:
    size 24
    color "#000"
    font gui.default_font
    text_align 0.5
    outlines []

style poemgame_text:
    yalign 0.5
    font "gui/font/comic.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size







style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True


style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True






style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style window_monika is window:
    background Image("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]

style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")


style input_prompt is default

style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.5
    text_align 0.5



style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    #action Play("sound", gui.activate_sound)

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines []



style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    outlines []




style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/font/Rotonda.ttf"
    color "#fff"
    outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]
    insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]



style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background "menu_nav"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font "gui/font/Rotonda.ttf"
    size gui.title_text_size
    color "#fff"
    outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30



style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size



style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []



style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font "gui/font/Rotonda.ttf"
    size 24
    color "#fff"
    outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/comic.ttf"
    outlines []

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/comic.ttf"
    outlines []

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450



style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")



style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"



style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size



#--------------------------------------Оригинальные изображения-----------------------------------------------


image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat

image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat


image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat


#-------------------------------------Оригинальные трансформы--------------------------------------------


transform delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


#----------------------------------------------Прочее--------------------------------------------------------

define config.narrator_menu = True

default quick_menu = False

define gui.about = ""
