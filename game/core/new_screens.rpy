init python:
    from random import choice
    import platform, math, json
    from os import system

    mob_dict = {"1":[0.385, 1.13], "1a":[0.36, 1.09], "2":[0.43, 0.99], "2a":[0.415, 0.95], "3":[0.5, 0.90], "3a":[0.5, 0.87], "4":[0.573, 0.99], "4a":[0.588, 0.95], "5":[0.615, 1.13], "5a":[0.64, 1.09], "but":[145, 260], "1b":[0.375, 1.032], "2b":[0.420, 0.88], "3b":[0.5, 0.8], "4b":[0.58, 0.88], "5b":[0.625, 1.032], "sens":[True, False]}

    pc_dict = {"1":[0.422, 1.072], "1a":[0.398, 1.033], "2":[0.452, 0.98], "2a":[0.437, 0.943], "3":[0.5, 0.918], "3a":[0.5, 0.858], "4":[0.549, 0.982], "4a":[0.564, 0.937], "5":[0.58, 1.072], "5a":[0.607, 1.034], "but":[120, 213], "1b":[0.422, 1.032], "2b":[0.452, 0.940], "3b":[0.5, 0.878], "4b":[0.549, 0.942], "5b":[0.580, 1.032]}

    def next_song():
        global track_num, delta, mus_pos, dur
        if persistent.track_num + 1 == 6:
            persistent.track_num = 0
        else:
            persistent.track_num = persistent.track_num + 1

        if not renpy.mobile:
            if persistent.track_num == persistent.back_music:
                renpy.hide_screen("button_set_back")
                renpy.show_screen("inactive_set_back")
            else:
                renpy.show_screen("button_set_back")
                renpy.hide_screen("inactive_set_back")

        renpy.music.play(music_list[persistent.track_num], channel="music")





    def previous_song():
        global track_num, delta, mus_pos, dur
        if persistent.track_num - 1 == -1:
            persistent.track_num = 5
        else:
            persistent.track_num = persistent.track_num - 1

        if not renpy.mobile:
            if persistent.track_num == persistent.back_music:
                renpy.hide_screen("button_set_back")
                renpy.show_screen("inactive_set_back")
            else:
                renpy.show_screen("button_set_back")
                renpy.hide_screen("inactive_set_back")


        renpy.music.play(music_list[persistent.track_num], channel="music")


    def vis_sens():
        if renpy.music.get_pause() == True:
            return False
        else:
            return True


    def save_back():
        global track_num
        persistent.back_music = persistent.track_num
        renpy.save_persistent()
        renpy.show_screen("inactive_set_back")
        renpy.show_screen("music_name")
        renpy.hide_screen("actions_name")
        renpy.hide_screen("button_set_back")

    def set_back_on_exit():
        global track_num
        persistent.back_music = persistent.track_num
        renpy.save_persistent()

    def set_back_on_prefered():
        global prefered_track_num
        persistent.back_music = prefered_track_num
        renpy.save_persistent()

    def set_value(v):
        global bttn
        bttn = v

    def new_mouse_pos():
        global yn
        xn, yn = renpy.get_mouse_pos()
        return yn


    def but_coord(but, coord):
        global mob_dict, pc_dict

        if renpy.mobile and but == "sens":
            return False
        elif (not renpy.mobile) and but == "sens":
            return True
        else:
            return pc_dict[but][coord]


    def label_choose(lbl_num):
        lbl_list = {1:"dia_personality", 2:"dia_hobbies", 3:None, 4:"dia_recipes", 5:"dia_past", 6:"dia_romance", 7:"dia_philosophy", 8:None, 9:"dia_requests", 10:"dia_other"}

        if renpy.get_screen("choice_buttons_2"):
            return lbl_list[lbl_num+5]
        else:
            return lbl_list[lbl_num]




    def mob_pages(l, r):
        global but_num, bttn
        if l ==True:
            but_num -= 1
            bttn -= 1
            if but_num == 0:
                but_num = 5

                renpy.show("i_1", zorder=2, at_list = [but_idle(1)])
            else:
                renpy.show("i_"+str(but_num+1), zorder=2, at_list=[but_idle(but_num+1)])

            renpy.show("i_"+str(but_num), zorder=2, at_list=[but_hover(but_num)])


            if bttn == 0:
                bttn = 5
            if renpy.get_screen("choice_buttons_2") and bttn == 5:
                bttn = 10
            renpy.show_screen("texts")

        if r == True:
            but_num += 1
            bttn += 1
            if but_num == 6:
                but_num = 1
                renpy.show("i_5", zorder=2, at_list=[but_idle(5)])
            else:
                renpy.show("i_"+str(but_num-1), zorder=2, at_list=[but_idle(but_num-1)])

            renpy.show("i_"+str(but_num), zorder=2, at_list=[but_hover(but_num)])

            if bttn == 6 and renpy.get_screen("choice_buttons_1"):
                bttn = 1
            if bttn == 11:
                bttn = 6
            renpy.show_screen("texts")




    def ani_talk_show():
        global but_num, bttn
        k=1
        if renpy.mobile:
            while k < 6:
                if k == but_num:
                    renpy.show("i_"+str(k), zorder=2, at_list=[but_hover(k)])
                else:
                    renpy.show("i_"+str(k), zorder=2, at_list=[but_idle(k)])
                k += 1
        else:
            while k < 6:
                renpy.show("i_"+str(k), zorder=2, at_list=[but_idle(k)])
                k += 1

        if renpy.mobile:
            if renpy.get_screen("choice_buttons_2"):
                bttn = but_num + 5
                renpy.show_screen("texts")
            else:
                bttn = but_num
                renpy.show_screen("texts")



    def theme_but_show():
        k=1
        while k < 6:
            renpy.show("th_"+str(k), zorder=2, at_list=[but_idle(k)])
            k += 1


    def change_sens(scr):
        global mob_menu
        if scr == "idle" and mob_menu == True:
            return True
        if scr == "idle" and mob_menu == False:
            return False
        if scr == "act" and mob_menu == True:
            return False
        if scr == "act" and mob_menu == False:
            return True



    def set_glitch():
        global is_glitching
        persistent.is_glitching = True
        renpy.save_persistent()


    def side():
        if left:
            renpy.show("natsuki r1a", at_list = [left_side])

        if right:
            renpy.show("natsuki r1a", at_list = [right_side])

    def side_return():
        if left:
            renpy.show("natsuki r1a", at_list = [r_left_side])

        if right:
            renpy.show("natsuki r1a", at_list = [r_right_side])


    def dia_hide():
        renpy.hide_screen("talk_button")
        renpy.hide_screen("active_talk_button")
        renpy.hide_screen("talk_round")
        renpy.hide_screen("active_talk_round")
        renpy.hide_screen("choice_buttons_1")
        renpy.hide_screen("choice_buttons_2")
        renpy.hide_screen("texts")
        renpy.hide_screen("volume_key")
        renpy.hide_screen("active_volume_key")
        renpy.hide_screen("sound_volume_key")
        renpy.hide_screen("active_sound_volume_key")
        renpy.hide_screen("music_key")
        renpy.hide_screen("active_music_key")
        renpy.hide_screen("sett_curtain")
        renpy.hide_screen("mob_active_but_curtain")
        renpy.hide_screen("theme_key")





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
        imagebutton xcenter 810 ycenter 230:
            idle "mod_assets/button/custom/corner_but_hit.png"
            sensitive current_state[0][0][1]
            action [Function(play, 0, 0, "X", 810, 230), Jump("change_side")]


        imagebutton xcenter 1050 ycenter 230:
            idle "mod_assets/button/custom/corner_but_hit.png"
            sensitive current_state[0][2][1]
            action [Function(play, 0, 2, "X", 1065, 230), Jump("change_side")]


        imagebutton xcenter 1050 ycenter 495:
            idle "mod_assets/button/custom/corner_but_hit.png"
            sensitive current_state[2][2][1]
            action [Function(play, 2, 2, "X", 1065, 495), Jump("change_side")]






        imagebutton xcenter 805 ycenter 495:
            idle "mod_assets/button/custom/corner_but_hit.png"
            sensitive current_state[2][0][1]
            action [Function(play, 2, 0, "X", 805, 495), Jump("change_side")]





        imagebutton xcenter 930 ycenter 230:
            idle "mod_assets/button/custom/edge_but_hit.png"
            sensitive current_state[0][1][1]
            action [Function(play, 0, 1, "X", 940, 220), Jump("change_side")]





        imagebutton xcenter 927 ycenter 495:
            idle "mod_assets/button/custom/edge_but_hit.png"
            sensitive current_state[2][1][1]
            action [Function(play, 2, 1, "X", 940, 495), Jump("change_side")]





        imagebutton xcenter 805 ycenter 363:
            idle "mod_assets/button/custom/s_edge_but_hit.png"
            sensitive current_state[1][0][1]
            action [Function(play, 1, 0, "X", 805, 363), Jump("change_side")]







        imagebutton xcenter 1055 ycenter 36:
            idle "mod_assets/button/custom/s_edge_but_hit.png"
            sensitive current_state[1][2][1]
            action [Function(play, 1, 2, "X", 1070, 363), Jump("change_side")]





        imagebutton xcenter 930 ycenter 363:
            idle "mod_assets/button/custom/center_but_hit.png"
            sensitive current_state[1][1][1]
            action [Function(play, 1, 1, "X", 940, 363), Jump("change_side")]


    if sst == "right":


        imagebutton xcenter 210 ycenter 230:
            idle "mod_assets/button/custom/corner_but_hit.png"
            sensitive current_state[0][0][1]
            action [Function(play, 0, 0, "X", 210, 230), Jump("change_side")]
        imagebutton xcenter 450 ycenter 230:
            idle "mod_assets/button/custom/corner_but_hit.png"
            sensitive current_state[0][2][1]
            action [Function(play, 0, 2, "X", 465, 230), Jump("change_side")]

        imagebutton xcenter 450 ycenter 495:
            idle "mod_assets/button/custom/corner_but_hit.png"
            sensitive current_state[2][2][1]
            action [Function(play, 2, 2, "X", 465, 495), Jump("change_side")]


        imagebutton xcenter 205 ycenter 495:
            idle "mod_assets/button/custom/corner_but_hit.png"
            sensitive current_state[2][0][1]
            action [Function(play, 2, 0, "X", 205, 495), Jump("change_side")]



        imagebutton xcenter 330 ycenter 230:
            idle "mod_assets/button/custom/edge_but_hit.png"
            sensitive current_state[0][1][1]
            action [Function(play, 0, 1, "X", 340, 220), Jump("change_side")]



        imagebutton xcenter 327 ycenter 495:
            idle "mod_assets/button/custom/edge_but_hit.png"
            sensitive current_state[2][1][1]
            action [Function(play, 2, 1, "X", 340, 495), Jump("change_side")]



        imagebutton xcenter 205 ycenter 363:
            idle "mod_assets/button/custom/s_edge_but_hit.png"
            sensitive current_state[1][0][1]
            action [Function(play, 1, 0, "X", 205, 363), Jump("change_side")]



        imagebutton xcenter 455 ycenter 363:
            idle "mod_assets/button/custom/s_edge_but_hit.png"
            sensitive current_state[1][2][1]
            action [Function(play, 1, 2, "X", 470, 363), Jump("change_side")]


        imagebutton xcenter 330 ycenter 363:
            idle "mod_assets/button/custom/center_but_hit.png"
            sensitive current_state[1][1][1]
            action [Function(play, 1, 1, "X", 340, 363), Jump("change_side")]






transform for_field_l():
    ycenter 365
    xcenter 940


transform for_field_r():
    ycenter 365
    xcenter 340


transform left_side():
    zoom 0.5
    xcenter 630
    linear 0 zoom 1
    easein 1.00 xcenter 330
transform right_side():
    zoom 0.5
    xcenter 630
    linear 0 zoom 1
    easein 1.00 xcenter 930 zoom 1

transform r_left_side():
    xcenter 330
    easein 1.00 xcenter 630
transform r_right_side():
    xcenter 930
    easein 1.00 xcenter 630

#-----------------------------------------Плеер----------------------------------------------


image button_back_inactive = inactive_but("back")

image button_eq_inactive:
    im.Scale("mod_assets/button/custom/round_inactive.png", 120, 214)
    xalign 0.549
    yalign 0.982
    alpha 0.0
    rotate 36.0
    easein 0.3 alpha 1.0

image cursed = im.Scale("mod_assets/button/custom/round_glitched.png", 120, 214)

image Youshouldnthavedonethat = LiveComposite((1280,720), (560,315), "n_rects1", (660,295), "n_rects2", (640,390), "n_rects3")

image Reverse = "mod_assets/images/cg/monika/reverse.png"

image full_vis = Visualiser()

image curtain:
    ConditionSwitch("persistent.ch_vol==True and persistent.ch_mus==True and persistent.themes == True", "mod_assets/button/custom/mob_curtain_all.png", "persistent.ch_vol != True and persistent.ch_mus != True and persistent.themes == True", "mod_assets/button/custom/mob_curtain_theme.png",
    "persistent.ch_vol != True and persistent.ch_mus == True and persistent.themes != True", "mod_assets/button/custom/mob_curtain_vis.png",
    "persistent.ch_vol != True and persistent.ch_mus == True and persistent.themes == True", "mod_assets/button/custom/mob_curtain_vis_theme.png",
    "persistent.ch_vol==True and persistent.ch_mus != True and persistent.themes != True", "mod_assets/button/custom/mob_curtain_vol.png",
    "persistent.ch_vol == True and persistent.ch_mus != True and persistent.themes == True", "mod_assets/button/custom/mob_curtain_vol_theme.png",
    "persistent.ch_vol==True and persistent.ch_mus==True and persistent.themes != True", "mod_assets/button/custom/mob_curtain_vol_vis.png",
    "True", "mod_assets/button/custom/mob_curtain_none.png")
    xcenter 0.5
    ycenter -0.1



image mob_menu_but = ConditionSwitch("persistent.theme == -90", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_menu.png", 100, 100), im.matrix.hue(-90)), "persistent.theme == 75", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_menu.png", 100, 100), im.matrix.hue(50)), "persistent.theme == -180", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_menu.png", 100, 100), im.matrix.hue(-200)), "persistent.theme == 45", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_menu.png", 100, 100), im.matrix.hue(50)), "True", im.Scale("mod_assets/button/custom/mob_menu.png", 100, 100))


image next = ConditionSwitch("persistent.theme == -90", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_next.png", 100, 100), im.matrix.hue(-90)), "persistent.theme == 75", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_next.png", 100, 100), im.matrix.hue(50)), "persistent.theme == -180", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_next.png", 100, 100), im.matrix.hue(-200)), "persistent.theme == 45", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_next.png", 100, 100), im.matrix.hue(50)), "True", im.Scale("mod_assets/button/custom/mob_next.png", 100, 100))



image prev = ConditionSwitch("persistent.theme == -90", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_prev.png", 100, 100), im.matrix.hue(-90)), "persistent.theme == 75", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_prev.png", 100, 100), im.matrix.hue(50)), "persistent.theme == -180", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_prev.png", 100, 100), im.matrix.hue(-200)), "persistent.theme == 45", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_prev.png", 100, 100), im.matrix.hue(50)), "True", im.Scale("mod_assets/button/custom/mob_prev.png", 100, 100))


image next_in = ConditionSwitch("persistent.theme == -90", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_next_in.png", 100, 100), im.matrix.hue(-90)), "persistent.theme == 75", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_next_in.png", 100, 100), im.matrix.hue(50)), "persistent.theme == -180", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_next_in.png", 100, 100), im.matrix.hue(-200)), "persistent.theme == 45", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_next_in.png", 100, 100), im.matrix.hue(50)), "True", im.Scale("mod_assets/button/custom/mob_next_in.png", 100, 100))

image prev_in = ConditionSwitch("persistent.theme == -90", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_prev_in.png", 100, 100), im.matrix.hue(-90)), "persistent.theme == 75", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_prev_in.png", 100, 100), im.matrix.hue(50)), "persistent.theme == -180", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_prev_in.png", 100, 100), im.matrix.hue(-200)), "persistent.theme == 45", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_prev_in.png", 100, 100), im.matrix.hue(50)), "True", im.Scale("mod_assets/button/custom/mob_prev_in.png", 100, 100))

image cycle = im.Scale("mod_assets/button/custom/mob_cycle.png", 100, 100)

image mob_pause = ConditionSwitch("persistent.theme == -90", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_pause.png", 100, 100), im.matrix.hue(-90)), "persistent.theme == 75", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_pause.png", 100, 100), im.matrix.hue(50)), "persistent.theme == -180", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_pause.png", 100, 100), im.matrix.hue(-200)), "persistent.theme == 45", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_pause.png", 100, 100), im.matrix.hue(55)), "True", im.Scale("mod_assets/button/custom/mob_pause.png", 100, 100))


image mob_active_pause = ConditionSwitch("persistent.theme == -90", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_active_pause.png", 100, 100), im.matrix.hue(-90)), "persistent.theme == 75", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_active_pause.png", 100, 100), im.matrix.hue(50)), "persistent.theme == -180", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_active_pause.png", 100, 100), im.matrix.hue(-200)), "persistent.theme == 45", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_active_pause.png", 100, 100), im.matrix.hue(55)), "True", im.Scale("mod_assets/button/custom/mob_active_pause.png", 100, 100))


image vis = ConditionSwitch("persistent.theme == -90", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_vis_but.png", 100, 100), im.matrix.hue(-90)), "persistent.theme == 75", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_vis_but.png", 100, 100), im.matrix.hue(50)), "persistent.theme == -180", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_vis_but.png", 100, 100), im.matrix.hue(-200)), "persistent.theme == 45", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_vis_but.png", 100, 100), im.matrix.hue(50)), "True", im.Scale("mod_assets/button/custom/mob_vis_but.png", 100, 100))


image vis_in = ConditionSwitch("persistent.theme == -90", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_vis_but_in.png", 100, 100), im.matrix.hue(-90)), "persistent.theme == 75", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_vis_but_in.png", 100, 100), im.matrix.hue(50)), "persistent.theme == -180", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_vis_but_in.png", 100, 100), im.matrix.hue(-200)), "persistent.theme == 45", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_vis_but_in.png", 100, 100), im.matrix.hue(50)), "True", im.Scale("mod_assets/button/custom/mob_vis_but_in.png", 100, 100))

#image act_vis = im.Scale("mod_assets/button/custom/mob_active_vis_but.png", 100, 100)

image act_vis = ConditionSwitch("persistent.theme == -90", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_active_vis_but.png", 100, 100), im.matrix.hue(-90)), "persistent.theme == 75", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_active_vis_but.png", 100, 100), im.matrix.hue(50)), "persistent.theme == -180", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_active_vis_but.png", 100, 100), im.matrix.hue(-200)), "persistent.theme == 45", im.MatrixColor(im.Scale("mod_assets/button/custom/mob_active_vis_but.png", 100, 100), im.matrix.hue(50)), "True", im.Scale("mod_assets/button/custom/mob_active_vis_but.png", 100, 100))

image mob_player_but_hit = im.Scale("mod_assets/button/custom/mob_player_but_hit.png", 100, 100)

transform mob_menu_coord:
    alpha 0
    xalign 0.5
    yalign 0.8
    easein 0.5 alpha 1


transform mob_add_but_vis:
    alpha 0
    xalign 0.6
    yalign 0.578
    easein 0.5 alpha 1

transform mob_add_but_pause:
    alpha 0
    xalign 0.4
    yalign 0.578
    easein 0.5 alpha 1


transform prev_but:
    alpha 0
    xalign 0.3
    yalign 0.8
    easein 0.5 alpha 1


transform next_but:
    alpha 0
    xalign 0.7
    yalign 0.8
    easein 0.5 alpha 1


transform v_but:
    rotate 0
    xcenter 0.4
    ycenter 0.5
    linear 0 rotate 36.5 xcenter 0.488 ycenter 0.579

transform p_but:
    rotate 0
    xcenter 0.4
    ycenter 0.5
    linear 0 rotate -71 ycenter 0.59 xcenter 0.49

transform n_but:
    rotate 0
    xcenter 0.4
    ycenter 0.5
    linear 0 rotate 71 ycenter 0.59 xcenter 0.51

transform b_but:
    rotate 0
    xalign 0.4
    yalign 0.5
    linear 0 rotate -36.5 xalign 0.453 yalign 0.980



transform show_cur():
    xcenter 0.5
    ycenter -0.1
    easein 0.5 ycenter 0.05

transform hide_cur():
    xcenter 0.5
    ycenter 0.05
    easein 0.5 ycenter -0.1



screen music_name:
    $ y_music_name_1 = 0.80
    $ y_music_name_2 = 0.85
    if renpy.mobile:
        $ y_music_name_1 = 0.90
        $ y_music_name_2 = 0.95

    if persistent.track_num == 0:
        text "{size=20}Dan Salvato{/size}" xalign 0.5 yalign y_music_name_1
        text "{size=20}Daijobu!{/size}" xalign 0.5 yalign y_music_name_2
    if persistent.track_num == 1:
        text "{size=20}Vincienty{/size}" xalign 0.5 yalign y_music_name_1
        text "{size=20}Heartbroken{/size}" xalign 0.5 yalign y_music_name_2
    if persistent.track_num == 2:
        text "{size=20}Vincienty{/size}" xalign 0.5 yalign y_music_name_1
        text "{size=20}Here We Go Again, Natsuki!{/size}" xalign 0.5 yalign y_music_name_2
    if persistent.track_num == 3:
        text "{size=20}Dan Salvato{/size}" xalign 0.5 yalign y_music_name_1
        text "{size=20}SnVzdCBNb25pa2E={/size}" xalign 0.5 yalign y_music_name_2
    if persistent.track_num == 4:
        text "{size=20}Dan Salvato{/size}" xalign 0.5 yalign y_music_name_1
        text "{size=20}Okay, Everyone! (Natsuki){/size}" xalign 0.5 yalign y_music_name_2
    if persistent.track_num == 5:
        text "{size=20}Vincienty{/size}" xalign 0.5 yalign y_music_name_1
        text "{size=20}Sweetest Cupcake{/size}" xalign 0.5 yalign y_music_name_2


screen actions_name:
    if bttn == 3:
        text "Пауза" xalign 0.5 yalign 0.85
    if bttn == 1:
        text "Предыдущий" xalign 0.5 yalign 0.85
    if bttn == 5:
        text "Следующий" xalign 0.5 yalign 0.85
    if bttn == 6:
        text "Продолжить" xalign 0.5 yalign 0.85
    if bttn == 2:
        text "Установить как фон" xalign 0.5 yalign 0.85
    if bttn == 4:
        text "Повтор" xalign 0.5 yalign 0.85
    if bttn == 7:
        text "Показать визуализатор" xalign 0.5 yalign 0.85
    if bttn == 9:
        text "Скрыть визуализатор" xalign 0.5 yalign 0.85



screen broke_music():
    $broke_pos = get_pos()
    $broke = "<from " + str(broke_pos) + ">" + broken_list[persistent.track_num]
    $renpy.music.play(broke, channel="music")

screen reverse_music():
    $reverse_pos = get_pos()
    $reverse = "<from " + str(reverse_pos) + ">" + reversed_list[persistent.track_num]
    $renpy.music.play(reverse, channel="music")






#music player
    imagebutton xcenter 0.642 yalign 0:
        idle "mod_assets/button/custom/mob_but_hit.png"
        sensitive persistent.ch_mus
        action [Function(renpy.show, "curtain", at_list=[hide_cur], zorder=10), Hide("mob_active_but_curtain"), Show("mob_music_player"), Hide("talk_button"), Hide("countdown")]

#volume
    imagebutton xcenter 0.497 yalign 0:
        idle "mod_assets/button/custom/mob_but_hit.png"
        sensitive persistent.ch_vol
        action [Function(renpy.show, "curtain", at_list=[hide_cur], zorder=10), Hide("mob_active_but_curtain"), SetVariable("set", "music"), Show("mob_active_volume_but"), Jump("mob_vol"), Hide("talk_button"), Hide("countdown")]

#sound volume
    imagebutton xcenter 0.353 yalign 0:
        idle "mod_assets/button/custom/mob_but_hit.png"
        sensitive persistent.ch_vol
        action [Function(renpy.show, "curtain", at_list=[hide_cur], zorder=10), Hide("mob_active_but_curtain"), SetVariable("set", "sound"), Show("mob_active_sound_but"), Jump("mob_sound"), Hide("talk_button"), Hide("countdown")]









screen broke_buttons():

    imagebutton xalign 0.5 yalign 0.878:
        idle "cursed"
        action NullAction()

    imagebutton xalign 0.452 yalign 0.940:
        idle "cursed"
        action NullAction()

    imagebutton xalign 0.422 yalign 1.032:
        idle "cursed"
        action NullAction()

    imagebutton xalign 0.549 yalign 0.942:
        idle "cursed"
        action NullAction()

    imagebutton xalign 0.580 yalign 1.032:
        idle "cursed"
        action NullAction()


screen button_pause():
    imagebutton xalign 0.5 yalign 0.878:
        idle "round_3_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 3), Function(renpy.show, "i_3", zorder=2, at_list=[but_hover(3)]), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.show, "i_3", zorder=2, at_list=[but_idle(3)])]
        focus_mask "round_3_hit"
        action [Hide("button_pause"), Show("button_active_pause"), Function(renpy.music.set_pause, True, channel=u'music'), If(renpy.get_screen("active_vis_button") == None, true=NullAction(), false=Function(renpy.hide, "full_vis"))]



screen mob_button_pause():
    on "show" action Function(renpy.show, "mob_pause", at_list=[mob_add_but_pause], zorder=2)
    on "hide" action Function(renpy.hide, "mob_pause")
    imagebutton xalign 0.4 yalign 0.578:
        idle "mob_player_but_hit"
        action [Hide("mob_button_pause"), Show("mob_button_active_pause"), Function(renpy.music.set_pause, True, channel=u'music'), If(renpy.get_screen("mob_active_vis_button") == None, true=NullAction(), false=Function(renpy.hide, "full_vis"))]


screen button_active_pause():
    imagebutton xalign 0.5 yalign 0.878:
        idle "round_3_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 6), Function(renpy.show, "i_3", zorder=2, at_list=[but_hover(3)]), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.show, "i_3", zorder=2, at_list=[but_idle(3)]),]
        focus_mask "round_3_hit"
        action [Hide("button_active_pause"), Show("button_pause"), Function(renpy.music.set_pause, False, channel=u'music'), If(renpy.get_screen("vis_button") != None, true=NullAction(), false=Function(renpy.show, "full_vis", zorder = 1))]



screen mob_button_active_pause():
    on "show" action Function(renpy.show, "mob_active_pause", at_list=[mob_add_but_pause], zorder=2)
    on "hide" action Function(renpy.hide, "mob_active_pause")
    imagebutton xalign 0.4 yalign 0.578:
        idle "mob_player_but_hit"
        action [Hide("mob_button_active_pause"), Show("mob_button_pause"), Function(renpy.music.set_pause, False, channel=u'music'), If(is_shown_vis == False, true=NullAction(), false=Function(renpy.show, "full_vis", zorder = 1))]




screen button_set_back():
    on "show" action [Function(renpy.show, "i_2", zorder=2), Function(renpy.hide, "button_back_inactive")]
    imagebutton xalign 0.452 yalign 0.940:
        idle "round_2_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 2), Function(renpy.show, "i_2", zorder=2, at_list=[but_hover(2)]), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.show, "i_2", zorder=2, at_list=[but_idle(1)]),]
        focus_mask "round_2_hit"
        action [Function(save_back), Function(renpy.show, "button_back_inactive")]


screen inactive_set_back():
    on "show" action Function(renpy.hide, "i_2"), Function(renpy.show, "button_back_inactive", zorder=2)
    imagebutton xalign 0.452 yalign 0.940:
        idle "round_2_hit"
        focus_mask "round_2_hit"
        action NullAction()


screen button_broken_cycle():
    $glitch_action = renpy.random.randint(1,3)
    imagebutton xalign 0.549 yalign 0.942:
        idle "round_4_hit"
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 4), Function(renpy.show, "i_4", zorder=2, at_list=[but_hover(4)]), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.show, "i_4", zorder=2, at_list=[but_idle(4)]),]
        focus_mask "round_4_hit"
        action [Function(renpy.music.set_pause, False), If(glitch_action == 1,
            true=[Function(renpy.play, "mod_assets/sfx/baa.ogg", channel='sound'), Hide("music_player_buttons"), Hide("button_broken_cycle"), Jump("what_was_that")], false=NullAction()),
        If(glitch_action == 2,
            true=[Function(renpy.music.set_volume, 1.0, channel="music"), Function(renpy.show, "Youshouldnthavedonethat", zorder=100), Show("broke_music"), Show("broke_buttons"), Show("active_broken_cycle"), Hide("button_broken_cycle"), Hide("music_player_buttons")],
            false=NullAction()),
        If(glitch_action == 3,
            true=[Show("broke_buttons"), Show("reverse_music"), Show("active_broken_cycle"), Hide("button_broken_cycle"), Hide("music_player_buttons"), Function(renpy.show, "Reverse", zorder=100)],
            false=NullAction())]
    $persistent.is_glitching = True
    $renpy.save_persistent()



screen mob_broken_cycle():
    on "show" action Function(renpy.show, "cycle", at_list=[mob_add_but_vis], zorder=2)
    on "hide" action Function(renpy.hide, "cycle")
    $glitch_action = renpy.random.randint(1,3)
    imagebutton xalign 0.6 yalign 0.578:
        idle "mob_player_but_hit"
        action [Function(renpy.music.set_pause, False), Function(set_glitch), If(glitch_action == 1,
            true=[Function(renpy.play, "mod_assets/sfx/baa.ogg", channel='sound'), Hide("mob_music_player"), Hide("mob_broken_cycle"), Jump("what_was_that")], false=NullAction()),
        If(glitch_action == 2,
            true=[Function(renpy.music.set_volume, 1.0, channel="music"), Function(renpy.show, "Youshouldnthavedonethat", zorder=100), Show("broke_music"), Show("broke_buttons"), Show("active_broken_cycle"), Hide("mob_broken_cycle"), Hide("mob_music_player")],
            false=NullAction()),
        If(glitch_action == 3,
            true=[Show("broke_buttons"), Show("reverse_music"), Show("active_broken_cycle"), Hide("mob_broken_cycle"), Hide("mob_music_player"), Function(renpy.show, "Reverse", zorder=100)],
            false=NullAction())]



screen active_broken_cycle():
    imagebutton xanchor 0 yanchor 0:
        idle "mod_assets/button/custom/mob_exit_hit.png"
        action Function(renpy.quit)



screen vis_button():
    imagebutton xalign 0.549 yalign 0.942:
        idle "round_4_hit"
        sensitive vis_sens()
        insensitive inactive_but("vis")
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 7), Function(renpy.show, "i_4", zorder=2, at_list=[but_hover(4)]), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.show, "i_4", zorder=2, at_list=[but_idle(4)]),]
        focus_mask "round_4_hit"
        action [Hide("vis_button"), Show("active_vis_button"), SetVariable("is_shown_vis", True), Function(renpy.show, "full_vis", zorder = 1)]


screen mob_vis_button():
    on "show" action Function(renpy.show, "vis", at_list = [mob_add_but_vis], zorder = 2)
    on "hide" action Function(renpy.hide, "vis")
    imagebutton xalign 0.6 yalign 0.578:
        idle "mob_player_but_hit"
        sensitive vis_sens()
        insensitive "vis_in"
        action [If(renpy.music.get_pause(channel=u'music') == False,
            true=[SetVariable("is_shown_vis", True), Function(renpy.show, "full_vis", zorder = 1)],
            false=NullAction()), Hide("mob_vis_button"), Show("mob_active_vis_button")]



screen active_vis_button():
    imagebutton xalign 0.549 yalign 0.942:
        idle "round_4_hit"
        sensitive vis_sens()
        insensitive inactive_but("vis")
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 9), Function(renpy.show, "i_4", zorder=2, at_list=[but_hover(4)]), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Show("music_name", transition = Dissolve(0.2)), Hide("actions_name", transition = Dissolve(0.2)), Function(set_value, 0), Function(renpy.show, "i_4", zorder=2, at_list=[but_idle(4)])]
        focus_mask "round_4_hit"
        action [Show("vis_button"), Hide("active_vis_button"), SetVariable("is_shown_vis", False), Function(renpy.hide, "full_vis")]


screen mob_active_vis_button():
    on "show" action Function(renpy.show, "act_vis", at_list = [mob_add_but_vis], zorder = 2)
    on "hide" action Function(renpy.hide, "act_vis")
    imagebutton xalign 0.6 yalign 0.578:
        idle "mob_player_but_hit"
        sensitive vis_sens()
        insensitive "vis_in"
        action [Show("mob_vis_button"), Hide("mob_active_vis_button"), SetVariable("is_shown_vis", False), Function(renpy.hide, "full_vis")]




screen mob_menu_player():                #менюшка для остальных кнопок


    imagebutton xalign 0.5 yalign 0.8:
        idle "mob_player_but_hit"
        action [If(persistent.fix == True,
            true=If(is_shown_vis == True,
                    true=[Show("mob_active_vis_button"),
                    If(renpy.music.get_pause(channel=u'music') == False,
                        true=[],
                        false=NullAction())],
                    false=Show("mob_vis_button")),
            false=Show("mob_broken_cycle")),
        If(renpy.music.get_pause(channel=u'music') == False,
            true=Show("mob_button_pause"),
            false=Show("mob_button_active_pause")),
        Show("mob_active_menu_player"), Hide("mob_menu_player")]




screen mob_active_menu_player():                    #активная менюшка для кнопок
    imagebutton xalign 0.5 yalign 0.8:
        idle "mob_player_but_hit"
        action [Hide("mob_button_pause"), Hide("mob_button_active_pause"), Hide("mob_active_vis_button"),
        Hide("mob_vis_button"), Hide("mob_broken_cycle"), Show("mob_menu_player"), Hide("mob_active_menu_player")]




screen mob_music_player():

    on "show" action [Show("mob_menu_player"), Function(renpy.show, "mob_menu_but", at_list = [mob_menu_coord], zorder=2), Function(renpy.show, "prev", at_list = [prev_but], zorder=2), Function(renpy.show, "next", at_list = [next_but], zorder=2), Show("music_name"), If(persistent.fix == True and is_shown_vis == True, true=Function(renpy.show, "full_vis", zorder = 1), false=NullAction())]

    on "hide" action [Hide("mob_menu_player"), Hide("mob_active_menu_player"), Hide("mob_button_pause"), Hide("mob_button_active_pause"), Hide("mob_broken_cycle"), Hide("music_name"), Hide("actions_name"), Hide("mob_vis_button"),
    Hide("mob_active_vis_button"), Function(renpy.hide, "pause_visual"), Function(renpy.hide, "resumed_visual"), Hide("music_name"), Function(renpy.hide, "mob_menu_but"), Function(renpy.hide, "prev"), Function(renpy.hide, "next")]




    imagebutton xanchor 0 yanchor 0:          #закрыть плеер
        idle "mod_assets/button/custom/mob_exit_hit.png"
        action [Function(renpy.hide, "mob_menu_but"), Function(renpy.hide, "prev"), Function(renpy.hide, "next"), Hide("mob_music_player"), Show("sett_curtain"), Function(set_back_on_exit), Jump("ch1_loop")]




    imagebutton xalign 0.3 yalign 0.8:      #пред. песня
        idle "mob_player_but_hit"
        sensitive vis_sens()
        insensitive "prev_in"
        action [Function(previous_song)]



    imagebutton xalign 0.7 yalign 0.8:            #след. песня
        idle "mob_player_but_hit"
        sensitive vis_sens()
        insensitive "next_in"
        action [Function(next_song)]






screen music_player_buttons():

    on "show" action [If(renpy.music.get_playing(channel=u'music') != None,
        true=Show("button_pause"),
        false=Show("button_active_pause")),
    If(renpy.music.get_playing(channel="music") == (music_path + music_list[persistent.back_music]) or renpy.music.get_playing(channel="music") == music_list[persistent.back_music],
        true=Show("inactive_set_back"),
        false=Show("button_set_back")),
        If(persistent.fix == True,
            true=If(is_shown_vis == True,
                    true=[Show("active_vis_button")],
                    false=Show("vis_button")),
            false=Show("button_broken_cycle")),
        Show("music_name"), Hide("talk_button"), Hide("countdown"), Function(renpy.show, "i_1", zorder=2, at_list=[but_idle(1)]), Function(renpy.show, "i_3", zorder=2, at_list=[but_idle(3)]), Function(renpy.show, "i_4", zorder=2, at_list=[but_idle(4)]), Function(renpy.show, "i_5", zorder=2, at_list=[but_idle(5)]), Function(renpy.show, "button_back_inactive", zorder=2)]

    on "hide" action [Hide("button_pause"), Hide("button_active_pause"), Hide("button_set_back"), Hide("inactive_set_back"), Hide("button_broken_cycle"), Hide("music_name"), Hide("actions_name"), Hide("vis_button"),
    Hide("active_vis_button"), Function(renpy.hide, "pause_visual"), Function(renpy.hide, "resumed_visual"),
    Function(renpy.hide, "i_1"), Function(renpy.hide, "i_2"), Function(renpy.hide, "i_3"), Function(renpy.hide, "i_4"),
    Function(renpy.hide, "i_5"), Function(renpy.hide, "button_back_inactive"), Function(renpy.hide, "button_eq_inactive")]





    imagebutton xalign 0.422 yalign 1.032:
        idle "round_1_hit"
        sensitive vis_sens()
        insensitive inactive_but("prev")
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 1), Function(renpy.show, "i_1", zorder=2, at_list=[but_hover(1)]), Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Function(set_value, 0), Function(renpy.show, "i_1", zorder=2, at_list=[but_idle(1)]), Hide("actions_name", transition = Dissolve(0.2)), Show("music_name", transition = Dissolve(0.2))]
        focus_mask "round_1_hit"
        action [Function(previous_song)]

    imagebutton xalign 0.580 yalign 1.032:
        idle "round_5_hit"
        sensitive vis_sens()
        insensitive inactive_but("next")
        hovered [Hide("music_name", transition = Dissolve(0.2)), Function(set_value, 5), Function(renpy.show, "i_5", zorder=2, at_list=[but_hover(5)]),Show("actions_name", transition = Dissolve(0.2))]
        unhovered [Function(set_value, 0), Function(renpy.show, "i_5", zorder=2, at_list=[but_idle(5)]), Hide("actions_name", transition = Dissolve(0.2)), Show("music_name", transition = Dissolve(0.2))]
        focus_mask "round_5_hit"
        action [Function(next_song)]



screen music_key():

    key persistent.m_key action [Hide("music_key"), Hide("sett_curtain"), Show("active_music_key"), Show("hide_all_talk"), Hide("countdown"), Show("music_player_buttons")]

    key persistent.m_key.upper() action [Hide("music_key"), Hide("sett_curtain"), Show("active_music_key"), Show("hide_all_talk"), Hide("countdown"), Show("music_player_buttons")]

    key persistent.m_r_key action [Hide("music_key"), Hide("sett_curtain"), Show("active_music_key"), Show("hide_all_talk"), Hide("countdown"), Show("music_player_buttons")]

    key persistent.m_r_key.upper() action [Hide("music_key"), Hide("sett_curtain"), Show("active_music_key"), Show("hide_all_talk"), Hide("countdown"), Show("music_player_buttons")]

screen active_music_key():

    key persistent.m_key action [Hide("music_player_buttons"), Show("sett_curtain"), Show("music_key"), Hide("active_music_key"), Show("talk_button"), Show("countdown"), Function(set_back_on_exit)]

    key persistent.m_key.upper() action [Hide("music_player_buttons"), Show("sett_curtain"), Show("music_key"), Hide("active_music_key"), Show("talk_button"), Show("countdown"), Function(set_back_on_exit)]

    key persistent.m_r_key action [Hide("music_player_buttons"), Show("sett_curtain"), Show("music_key"), Hide("active_music_key"), Show("talk_button"), Show("countdown"), Function(set_back_on_exit)]

    key persistent.m_r_key.upper() action [Hide("music_player_buttons"), Show("sett_curtain"), Show("music_key"), Hide("active_music_key"), Show("talk_button"), Show("countdown"), Function(set_back_on_exit)]

    key "K_ESCAPE" action [Hide("music_player_buttons"), Show("sett_curtain"), Show("music_key"), Hide("active_music_key"), Show("talk_button"), Show("countdown"), Function(set_back_on_exit)]





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
    ycenter 0.955
    xalign 0.49


transform pos_cup_button:
    xalign 0.5
    yalign 0.95



image level_cir = ConditionSwitch("persistent.theme == -90", im.MatrixColor("mod_assets/button/custom/volume_circle_level.png", im.matrix.hue(-90)), "persistent.theme == 75", im.MatrixColor("mod_assets/button/custom/volume_circle_level.png", im.matrix.hue(50)), "persistent.theme == -180", im.MatrixColor("mod_assets/button/custom/volume_circle_level.png", im.matrix.hue(-200)), "persistent.theme == 45", im.MatrixColor("mod_assets/button/custom/volume_circle_level.png", im.matrix.hue(30)), "True", "mod_assets/button/custom/volume_circle_level.png")
image anim_cir = "mod_assets/button/custom/volume_circle.png"
image cup_but = place_but()
image cup_but_hover = place_hover_but()



screen volume_key():
    key persistent.v_key.upper() action [SetVariable("set", "music"), Hide("volume_key"), Hide("sett_curtain"), Show("active_volume_key"), Show("con_volume"), Hide("sound_volume_key"), Hide("talk_button"), Hide("countdown"), Function(renpy.show, "cup_but", at_list=[pos_cup_button], zorder=10), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    key persistent.v_key action [SetVariable("set", "music"), Hide("volume_key"), Hide("sett_curtain"), Show("active_volume_key"), Show("con_volume"), Hide("sound_volume_key"), Hide("talk_button"), Hide("countdown"), Function(renpy.show, "cup_but", at_list=[pos_cup_button], zorder=10), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    key persistent.v_r_key.upper() action [SetVariable("set", "music"), Hide("volume_key"), Hide("sett_curtain"), Show("active_volume_key"), Show("con_volume"), Hide("sound_volume_key"), Hide("talk_button"), Hide("countdown"), Function(renpy.show, "cup_but", at_list=[pos_cup_button], zorder=10), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    key persistent.v_r_key action [SetVariable("set", "music"), Hide("volume_key"), Hide("sett_curtain"), Show("active_volume_key"), Show("con_volume"), Hide("sound_volume_key"), Hide("talk_button"), Hide("countdown"), Function(renpy.show, "cup_but", at_list=[pos_cup_button], zorder=10), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]



screen active_volume_key():

    key persistent.v_key action [Hide("con_volume"), Show("volume_key"), Hide("active_volume_key"), Show("sett_curtain"), Show("sound_volume_key"), Show("talk_button"), Show("countdown"), Function(renpy.hide, "cup_but"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key persistent.v_key.upper() action [Hide("con_volume"), Show("volume_key"), Hide("active_volume_key"), Show("sett_curtain"), Show("sound_volume_key"), Show("talk_button"), Show("countdown"), Function(renpy.hide, "cup_but"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key persistent.v_r_key.upper() action [Hide("con_volume"), Show("volume_key"), Hide("active_volume_key"), Show("sett_curtain"), Show("sound_volume_key"), Show("talk_button"), Show("countdown"), Function(renpy.hide, "cup_but"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key persistent.v_r_key action [Hide("con_volume"), Show("volume_key"), Hide("active_volume_key"), Show("sett_curtain"), Show("sound_volume_key"), Show("talk_button"), Show("countdown"), Function(renpy.hide, "cup_but"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key "K_ESCAPE" action [Hide("con_volume"), Show("volume_key"), Hide("active_volume_key"), Show("sett_curtain"), Show("sound_volume_key"), Show("talk_button"), Show("countdown"), Function(renpy.hide, "cup_but"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    $persistent.svol = vlm
    $persistent.snum = num
    $persistent.sgrad = grad
    $renpy.save_persistent()





screen sound_volume_key():
    key persistent.s_key.upper() action [SetVariable("set", "sound"), Hide("sound_volume_key"), Hide("sett_curtain"), Show("active_sound_volume_key"), Show("con_sound_volume"), Hide("volume_key"), Hide("talk_button"), Hide("countdown"), Show("sound_test"), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    key persistent.s_key action [SetVariable("set", "sound"), Hide("sound_volume_key"), Show("active_sound_volume_key"), Hide("sett_curtain"), Show("con_sound_volume"), Hide("volume_key"), Hide("talk_button"), Hide("countdown"), Show("sound_test"), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    key persistent.s_r_key action [SetVariable("set", "sound"), Hide("sound_volume_key"), Show("active_sound_volume_key"), Hide("sett_curtain"), Show("con_sound_volume"), Hide("volume_key"), Hide("talk_button"), Hide("countdown"), Show("sound_test"), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    key persistent.s_r_key.upper() action [SetVariable("set", "sound"), Hide("sound_volume_key"), Show("active_sound_volume_key"), Hide("sett_curtain"), Show("con_sound_volume"), Hide("volume_key"), Hide("talk_button"), Hide("countdown"), Show("sound_test"), If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]


screen active_sound_volume_key():

    key persistent.s_key action [Hide("con_sound_volume"), Show("sound_volume_key"), Hide("active_sound_volume_key"), Show("sett_curtain"), Show("volume_key"), Show("talk_button"), Show("countdown"), Hide("sound_test"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key persistent.s_key.upper() action [Hide("con_sound_volume"), Show("sound_volume_key"), Hide("active_sound_volume_key"), Show("sett_curtain"), Show("volume_key"), Show("talk_button"), Show("countdown"), Hide("sound_test"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key persistent.s_r_key action [Hide("con_sound_volume"), Show("sound_volume_key"), Hide("active_sound_volume_key"), Show("sett_curtain"), Show("volume_key"), Show("talk_button"), Show("countdown"), Hide("sound_test"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key persistent.s_r_key.upper() action [Hide("con_sound_volume"), Show("sound_volume_key"), Hide("active_sound_volume_key"), Show("sett_curtain"), Show("volume_key"), Show("talk_button"), Show("countdown"), Hide("sound_test"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]

    key "K_ESCAPE" action [Hide("con_sound_volume"), Show("sound_volume_key"), Hide("active_sound_volume_key"), Show("volume_key"), Show("sett_curtain"), Show("talk_button"), Show("countdown"), Hide("sound_test"), If(is_playing, true=Show("music_player_buttons"), false=NullAction())]


    $persistent.soundvol = soundvlm
    $persistent.soundnum = sounum
    $persistent.soundgrad = soungrad
    $renpy.save_persistent()



screen sound_test():
    zorder 10
    imagebutton xalign 0.5 yalign 0.95:
        idle "cup_but"
        hover "cup_but_hover"
        hovered [Play("sound", "mod_assets/sfx/hover.ogg")]
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


screen mob_active_volume_but():
    on "show" action [Function(renpy.show, "anim_cir", at_list=[show_vol_animation], zorder=3), Function(renpy.show, "level_cir", at_list=[show_vol_level_animation], zorder=4), Function(renpy.show, "vol_mask", at_list=[volume_mask], zorder=5), Show("vol_texts", transition=dissolve)]
    zorder 10
    imagebutton xalign 0.5 yalign 0.95:
        idle im.Scale("mod_assets/button/custom/cup_button_nat.png", 80, 80)
        hover im.Scale("mod_assets/button/custom/cup_button_hover_nat.png", 80, 80)
        action [Play("sound", "mod_assets/sfx/select.ogg"), Show("sett_curtain"), Function(renpy.show, "anim_cir", at_list=[hide_vol_animation], zorder=3), Function(renpy.show, "level_cir", at_list=[hide_vol_level_animation], zorder=4), Hide("vol_texts", transition=dissolve), Hide("vol_mob_enable_change"), Hide("vol_mob_disable_change"), Hide("vol_mob_set_volume"), Hide("mob_active_volume_but"), Jump("ch1_loop")]


screen mob_active_sound_but():
    on "show" action [Function(renpy.show, "anim_cir", at_list=[show_vol_animation], zorder=3), Function(renpy.show, "level_cir", at_list=[show_sound_vol_level_animation], zorder=4), Function(renpy.show, "vol_mask", at_list=[volume_mask], zorder=5), Show("vol_texts", transition=dissolve)]

    zorder 10
    imagebutton xalign 0.5 yalign 0.95:
        idle im.Scale("mod_assets/button/custom/cup_button_nat.png", 80, 80)
        hover im.Scale("mod_assets/button/custom/cup_button_hover_nat.png", 80, 80)
        hovered [Play("sound", "mod_assets/sfx/hover.ogg")]
        action [Play("sound", "mod_assets/sfx/select.ogg"), Show("sett_curtain"), Function(renpy.show, "anim_cir", at_list=[hide_vol_animation], zorder=3), Function(renpy.show, "level_cir", at_list=[hide_vol_level_animation], zorder=4), Hide("vol_texts", transition=dissolve), Hide("sound_mob_enable_change"), Hide("sound_mob_disable_change"), Hide("sound_mob_set_volume"), Hide("mob_active_sound_but"), Jump("ch1_loop")]



screen vol_mob_enable_change():
    key "mousedown_1" action [SetVariable("set", "music"), Show("vol_mob_set_volume"), Hide("vol_mob_enable_change"), Show("vol_mob_disable_change")]

screen vol_mob_disable_change():
    key "mouseup_1" action [Hide("vol_mob_set_volume"), Hide("vol_mob_disable_change"), Show("vol_mob_enable_change"), SetVariable("yo", 1000), SetVariable("yn", 1000)]
    $persistent.svol = vlm
    $persistent.snum = num
    $persistent.sgrad = grad
    $renpy.save_persistent()



screen vol_mob_set_volume():

    timer 0.00001 repeat True action [Function(new_mouse_pos),
    If(num>99,
        true=If(yn < yo,
            true=SetVariable("yo", yn),
            false=[SetVariable("num", num - 1), SetVariable("vlm", vlm - 0.01), SetVariable("grad", grad - 1.8), Function(renpy.music.set_volume, vlm, channel="music"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4), Show("vol_texts"), SetVariable("yo", yn)]),
        false=If(num<1,
            true=If(yn > yo,
                true=SetVariable("yo", yn),
                false=[SetVariable("num", num + 1), SetVariable("vlm", vlm + 0.01), SetVariable("grad", grad + 1.8), Function(renpy.music.set_volume, vlm, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4), SetVariable("yo", yn)]),
            false=[If(yn > yo,
                    true=[SetVariable("num", num - 1), SetVariable("vlm", vlm - 0.01), SetVariable("grad", grad - 1.8), Function(renpy.music.set_volume, vlm, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4), SetVariable("yo", yn)],
                    false=NullAction()),
                If(yn < yo,
                    true=[SetVariable("num", num + 1), SetVariable("vlm", vlm + 0.01), SetVariable("grad", grad + 1.8), Function(renpy.music.set_volume, vlm, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4), SetVariable("yo", yn)],
                    false=NullAction())]))]





screen sound_mob_enable_change():
    key "mousedown_1" action [SetVariable("set", "sound"), Show("sound_mob_set_volume"), Hide("sound_mob_enable_change"), Show("sound_mob_disable_change")]

screen sound_mob_disable_change():
    key "mouseup_1" action [Hide("sound_mob_set_volume"), Hide("sound_mob_disable_change"), Show("sound_mob_enable_change"), SetVariable("yo", 1000), SetVariable("yn", 1000)]

    $persistent.soundvol = soundvlm
    $persistent.soundnum = sounum
    $persistent.soundgrad = soungrad
    $renpy.save_persistent()



screen sound_mob_set_volume():

    timer 0.00001 repeat True action [Function(new_mouse_pos),
    If(sounum>99,
        true=If(yn < yo,
            true=SetVariable("yo", yn),
            false=[SetVariable("sounum", sounum - 1), SetVariable("soundvlm", soundvlm - 0.01), SetVariable("soungrad", soungrad - 1.8), Function(renpy.music.set_volume, soundvlm, channel="sound"), Function(renpy.show, "level_cir", at_list=[vol_sound_level_animation], zorder=4), Show("vol_texts"), SetVariable("yo", yn)]),
        false=If(sounum<1,
            true=If(yn > yo,
                true=SetVariable("yo", yn),
                false=[SetVariable("sounum", sounum + 1), SetVariable("soundvlm", soundvlm + 0.01), SetVariable("soungrad", soungrad + 1.8), Function(renpy.music.set_volume, soundvlm, channel="sound"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_sound_level_animation], zorder=4), SetVariable("yo", yn)]),
            false=[If(yn > yo,
                    true=[SetVariable("sounum", sounum - 1), SetVariable("soundvlm", soundvlm - 0.01), SetVariable("soungrad", soungrad - 1.8), Function(renpy.music.set_volume, soundvlm, channel="sound"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_sound_level_animation], zorder=4), SetVariable("yo", yn)],
                    false=NullAction()),
                If(yn < yo,
                    true=[SetVariable("sounum", sounum + 1), SetVariable("soundvlm", soundvlm + 0.01), SetVariable("soungrad", soungrad + 1.8), Function(renpy.music.set_volume, soundvlm, channel="sound"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_sound_level_animation], zorder=4), SetVariable("yo", yn)],
                    false=NullAction())]))]




screen con_volume():
    on "show" action [Function(renpy.show, "anim_cir", at_list=[show_vol_animation], zorder=3), Function(renpy.show, "level_cir", at_list=[show_vol_level_animation], zorder=4), Function(renpy.show, "vol_mask", at_list=[volume_mask], zorder=5), Show("vol_texts", transition=dissolve)]

    on "hide" action [Function(renpy.show, "anim_cir", at_list=[hide_vol_animation], zorder=3), Function(renpy.show, "level_cir", at_list=[hide_vol_level_animation], zorder=4), Hide("vol_texts", transition=dissolve)]


    if num > 99:

        key "mouseup_3" action [SetVariable("vlm", 1.0), SetVariable("num", 100), SetVariable("grad", 180), Function(renpy.music.set_volume, num, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]

        key "mouseup_4" action NullAction()

        key "mouseup_5" action [SetVariable("num", num - 1), SetVariable("vlm", vlm - 0.01), SetVariable("grad", grad - 1.8), Function(renpy.music.set_volume, vlm, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]


    elif num < 1:

        key "mouseup_3"action [SetVariable("vlm", 0.0), SetVariable("num", 0), SetVariable("grad", 0), Function(renpy.music.stop, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]

        key "mouseup_4" action [SetVariable("num", num + 1), SetVariable("vlm", vlm + 0.01), SetVariable("grad", grad + 1), Function(renpy.music.set_volume, vlm, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]

        key "mouseup_5" action [SetVariable("vlm", 0.0), SetVariable("num", 0), SetVariable("grad", 0), Function(renpy.music.set_pause, True, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]


    else:

        key "mouseup_4" action [Function(renpy.music.set_pause, False, channel="music"), SetVariable("num", num + 1), SetVariable("vlm", vlm + 0.01), SetVariable("grad", grad + 1.8), Function(renpy.music.set_volume, vlm, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]

        key "mouseup_5" action [SetVariable("num", num - 1), SetVariable("vlm", vlm - 0.01), SetVariable("grad", grad - 1.8), Function(renpy.music.set_volume, vlm, channel="music"), Show("vol_texts"), Function(renpy.show, "level_cir", at_list=[vol_level_animation], zorder=4)]




screen con_sound_volume():
    on "show" action [Function(renpy.show, "anim_cir", at_list=[show_vol_animation], zorder=3), Function(renpy.show, "level_cir", at_list=[show_sound_vol_level_animation], zorder=4), Function(renpy.show, "vol_mask", at_list=[volume_mask], zorder=5), Show("vol_texts", transition=dissolve)]

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



image round_1_hit:
    im.Scale("mod_assets/button/custom/round_hit.png", 110, 195),
    rotate -72
image round_2_hit:
    im.Scale("mod_assets/button/custom/round_hit.png", 110, 195),
    rotate -36
image round_3_hit:
    im.Scale("mod_assets/button/custom/round_hit.png", 110, 195),
image round_4_hit:
    im.Scale("mod_assets/button/custom/round_hit.png", 110, 195),
    rotate 36
image round_5_hit:
    im.Scale("mod_assets/button/custom/round_hit.png", 110, 195),
    rotate 72



image round_1_styled:
    ConditionSwitch(
        "persistent.is_theme_default == False",
        im.MatrixColor(
            im.Scale("mod_assets/button/custom/round_1.png", but_coord("but", 0), but_coord("but", 1)),
            im.matrix.hue(persistent.theme)
        ),
        "True",
        im.Scale("mod_assets/button/custom/round_1.png", but_coord("but", 0), but_coord("but", 1)))

image th_1:
    im.MatrixColor(im.Scale("mod_assets/button/custom/round_1.png", but_coord("but", 0), but_coord("but", 1)), im.matrix.hue(-180.0))
    rotate -72


image th_2:
    im.MatrixColor(im.Scale("mod_assets/button/custom/round_1.png", but_coord("but", 0), but_coord("but", 1)), im.matrix.hue(45.0))
    rotate -36.0


image th_3:
    im.MatrixColor(im.Scale("mod_assets/button/custom/round_1.png", but_coord("but", 0), but_coord("but", 1)), im.matrix.hue(0.0))


image th_4:
    im.MatrixColor(im.Scale("mod_assets/button/custom/round_1.png", but_coord("but", 0), but_coord("but", 1)), im.matrix.hue(75.0))
    rotate 36.0


image th_5:
    im.MatrixColor(im.Scale("mod_assets/button/custom/round_1.png", but_coord("but", 0), but_coord("but", 1)), im.matrix.hue(-90))
    rotate 72




transform but_hover(num):
    alpha 0.0
    xalign but_coord(str(num), 0)
    yalign but_coord(str(num), 1)
    easein 0.3 xalign but_coord(str(num)+"a", 0) yalign but_coord(str(num)+"a", 1) alpha 1.0

transform but_idle(num):
    alpha 0.0
    xalign but_coord(str(num)+"a", 0)
    yalign but_coord(str(num)+"a", 1)
    easein 0.3 xalign but_coord(str(num), 0) yalign but_coord(str(num), 1) alpha 1.0



image i_1:
    "round_1_styled"
    rotate -72

image i_2:
    "round_1_styled"
    rotate -36.0

image i_3:
    "round_1_styled"

image i_4:
    "round_1_styled"
    rotate 36.0

image i_5:
    "round_1_styled"
    rotate 72



image talk_styled:
    ConditionSwitch(
        "persistent.is_theme_default == False",
            im.MatrixColor(
                im.Scale("mod_assets/button/custom/talk.png", 100, 100),
                #im.matrix.tint(persistent.theme[0],persistent.theme[1],persistent.theme[2])
                im.matrix.hue(persistent.theme)
            ),
            "True",
            im.Scale("mod_assets/button/custom/talk.png", 100, 100)
        )

image talk_hover_styled:
    ConditionSwitch(
        "persistent.is_theme_default == False",
            im.MatrixColor(
                im.Scale("mod_assets/button/custom/talk_hover.png", 100, 100),
                #im.matrix.tint(persistent.theme[0],persistent.theme[1],persistent.theme[2])
                im.matrix.hue(persistent.theme)
            ),
            "True",
            im.Scale("mod_assets/button/custom/talk_hover.png", 100, 100)
        )

screen talk_button():
    zorder 10
    imagebutton xalign 0.5 yalign 0.95:
        idle "talk_styled"
        hover "talk_hover_styled"
        hovered [Play("sound", "mod_assets/sfx/hover.ogg")]
        action [Show("talk_round"), Hide("volume_key"), Hide("sound_volume_key"), Hide("music_key"), Play("sound", "mod_assets/sfx/select.ogg"), Show("key_hider_talk"), Function(renpy.hide, "vol_mask")]


screen active_talk_button():
    zorder 10
    imagebutton xalign 0.5 yalign 0.95:
        idle "talk_styled"
        hover "talk_hover_styled"
        hovered [Play("sound", "mod_assets/sfx/hover.ogg")]
        action [Show("active_talk_round"), Show("volume_key"), Show("sound_volume_key"), Show("music_key"), Play("sound", "mod_assets/sfx/select.ogg"), Hide("key_hider_talk")]


screen talk_round:
    on "show" action [Hide("talk_button"), Show("active_talk_button"), Hide("active_talk_round"), Show("choice_buttons_1")]

screen active_talk_round:
    on "show" action [Hide("choice_buttons_1", transition = dissolve), Hide("choice_buttons_2", transition = dissolve), Hide("active_talk_button"), Hide("talk_round"), Show("talk_button")]

screen key_hider_talk():
    key "K_ESCAPE" action [Hide("choice_buttons_1", transition = dissolve), Hide("choice_buttons_2", transition = dissolve), Hide("active_talk_button"), Hide("talk_round"), Show("talk_button"), Show("active_talk_round"), If(persistent.ch_vol == True, true=[Show("volume_key"), Show("sound_volume_key")], false=NullAction()), If(persistent.ch_mus == True, true=Show("music_key"), false=NullAction()), SetVariable("is_esc_pressed", True), Jump("ch1_loop")]

screen texts:
    if bttn == 1:
        text "Личность" xalign 0.5 yalign 0.78
    elif bttn == 2:
        text "Увлечения" xalign 0.5 yalign 0.78
    elif bttn == 3:
        text "Вперёд" xalign 0.5 yalign 0.78
    elif bttn == 4:
        text "Готовка" xalign 0.5 yalign 0.78
    elif bttn == 5:
        text "Прошлое" xalign 0.5 yalign 0.78
    elif bttn == 6:
        text "Романтика" xalign 0.5 yalign 0.78
    elif bttn == 7:
        text "Философия" xalign 0.5 yalign 0.78
    elif bttn == 8:
        text "Назад" xalign 0.5 yalign 0.78
    elif bttn == 9:
        text "Просьбы" xalign 0.5 yalign 0.78
    elif bttn == 10:
        text "Другое" xalign 0.5 yalign 0.78

screen choice_buttons_1():
    on "show" action Function(ani_talk_show)

    on "hide" action [Function(renpy.hide, "i_1"), Function(renpy.hide, "i_2"), Function(renpy.hide, "i_3"), Function(renpy.hide, "i_4"), Function(renpy.hide, "i_5"), Hide("texts")]


    if renpy.mobile:
        imagebutton xanchor 0 yanchor 0:
            idle "mod_assets/button/custom/mob_exit_hit.png"
            action [If(but_num==3, true=[Hide("choice_buttons_1", transition = Dissolve(0.2)), Show("choice_buttons_2", transition = Dissolve(0.2))], false=Function(renpy.jump, label_choose(but_num)))]

        imagebutton xalign 0.2 yalign 0.85:
            idle im.Scale("mod_assets/button/custom/page_left_but.png", 100, 100)
            focus_mask True
            action [Function(mob_pages, True, False), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]

        imagebutton xalign 0.8 yalign 0.85:
            idle im.Scale("mod_assets/button/custom/page_right_but.png", 100, 100)
            focus_mask True
            action [Function(mob_pages, False, True), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]


    imagebutton xalign but_coord("2b", 0) yalign but_coord("2b", 1):
        idle "round_2_hit"

        hovered [Function(set_value, 2), Function(renpy.show, "i_2", zorder=2, at_list=[but_hover(2)]), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.show, "i_2", zorder=2, at_list=[but_idle(2)]), Hide("texts", transition = Dissolve(0.2))]
        sensitive but_coord("sens", None)
        focus_mask True
        action Jump("dia_hobbies")

    imagebutton xalign but_coord("4b", 0) yalign but_coord("4b", 1):
        idle "round_4_hit"
        hovered [Function(set_value, 4), Function(renpy.show, "i_4", zorder=2, at_list=[but_hover(4)]), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.show, "i_4", zorder=2, at_list=[but_idle(4)]), Hide("texts", transition = Dissolve(0.2))]
        sensitive but_coord("sens", None)
        focus_mask True
        action Jump("dia_recipes")

    imagebutton xalign 0.5 yalign but_coord("3b", 1):
        idle "round_3_hit"
        hovered [Function(set_value, 3), Function(renpy.show, "i_3", zorder=2, at_list=[but_hover(3)]), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.show, "i_3", zorder=2, at_list=[but_idle(3)]), Hide("texts", transition = Dissolve(0.2))]
        sensitive but_coord("sens", None)
        focus_mask True
        action [Hide("choice_buttons_1", transition = Dissolve(0.2)), Show("choice_buttons_2", transition = Dissolve(0.2))]


    imagebutton xalign but_coord("1b", 0) yalign but_coord("1b", 1):
        idle "round_1_hit"
        hovered [Function(set_value, 1), Function(renpy.show, "i_1", zorder=2, at_list=[but_hover(1)]), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.show, "i_1", zorder=2, at_list=[but_idle(1)]), Hide("texts", transition = Dissolve(0.2))]
        sensitive but_coord("sens", None)
        focus_mask True
        action Jump("dia_personality")

    imagebutton xalign but_coord("5b", 0) yalign but_coord("5b", 1):
        idle "round_5_hit"
        hovered [Function(set_value, 5), Function(renpy.show, "i_5", zorder=2, at_list=[but_hover(5)]), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.show, "i_5", zorder=2, at_list=[but_idle(5)]), Hide("texts", transition = Dissolve(0.2))]
        sensitive but_coord("sens", None)
        focus_mask True
        action Jump("dia_past")




screen choice_buttons_2():
    on "show" action Function(ani_talk_show)

    on "hide" action [Function(renpy.hide, "i_1"), Function(renpy.hide, "i_2"), Function(renpy.hide, "i_3"), Function(renpy.hide, "i_4"), Function(renpy.hide, "i_5"), Hide("texts")]



    if renpy.mobile:
        imagebutton xanchor 0 yanchor 0:
            idle "mod_assets/button/custom/mob_exit_hit.png"
            action [If(but_num==3, true=[Hide("choice_buttons_2", transition = Dissolve(0.2)), Show("choice_buttons_1", transition = Dissolve(0.2))], false=Function(renpy.jump, label_choose(but_num)))]

        imagebutton xalign 0.2 yalign 0.85:
            idle im.Scale("mod_assets/button/custom/page_left_but.png", 100, 100)
            focus_mask True
            action [Function(mob_pages, True, False), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]

        imagebutton xalign 0.8 yalign 0.85:
            idle im.Scale("mod_assets/button/custom/page_right_but.png", 100, 100)
            focus_mask True
            action [Function(mob_pages, False, True), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]



    imagebutton xalign but_coord("2b", 0) yalign but_coord("2b", 1):
        idle "round_2_hit"
        hovered [Function(set_value, 7), Function(renpy.show, "i_2", zorder=2, at_list=[but_hover(2)]), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.show, "i_2", zorder=2, at_list=[but_idle(2)]), Hide("texts", transition = Dissolve(0.2))]
        focus_mask True
        sensitive but_coord("sens", None)
        action Jump("dia_philosophy")

    imagebutton xalign but_coord("4b", 0) yalign but_coord("4b", 1):
        idle "round_4_hit"
        hovered [Function(set_value, 9), Function(renpy.show, "i_4", zorder=2, at_list=[but_hover(4)]), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.show, "i_4", zorder=2, at_list=[but_idle(4)]), Hide("texts", transition = Dissolve(0.2))]
        focus_mask True
        sensitive but_coord("sens", None)
        action Jump("dia_requests")


    imagebutton xalign 0.5 yalign but_coord("3b", 1):
        idle "round_3_hit"
        hovered [Function(set_value, 8), Function(renpy.show, "i_3", zorder=2, at_list=[but_hover(3)]), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.show, "i_3", zorder=2, at_list=[but_idle(3)]), Hide("texts", transition = Dissolve(0.2))]
        focus_mask True
        sensitive but_coord("sens", None)
        action [Hide("choice_buttons_2", transition = Dissolve(0.2)), Show("choice_buttons_1", transition = Dissolve(0.2))]





    imagebutton xalign but_coord("1b", 0) yalign but_coord("1b", 1):
        idle "round_1_hit"
        hovered [Function(set_value, 6), Function(renpy.show, "i_1", zorder=2, at_list=[but_hover(1)]), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.show, "i_1", zorder=2, at_list=[but_idle(1)]), Hide("texts", transition = Dissolve(0.2))]
        focus_mask True
        sensitive but_coord("sens", None)
        action Jump("dia_romance")

    imagebutton xalign but_coord("5b", 0) yalign but_coord("5b", 1):
        idle "round_5_hit"
        hovered [Function(set_value, 10), Function(renpy.show, "i_5", zorder=2, at_list=[but_hover(5)]), Show("texts", transition = Dissolve(0.2)), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered [Function(set_value, 0), Function(renpy.show, "i_5", zorder=2, at_list=[but_idle(5)]), Hide("texts", transition = Dissolve(0.2))]
        focus_mask True
        sensitive but_coord("sens", None)
        action Jump("dia_other")


#-------------------------------------------Модовые экраны--------------------------------------

screen countdown():
    zorder 10
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


#-----------------------------------------------Кнопки для темы----------------------------------------------------



screen theme_key():
    key persistent.t_key.upper() action [Hide("theme_key"), Hide("sett_curtain"), Show("active_theme_key"), Show("theme_buttons"), Hide("talk_button"), Hide("countdown")]

    key persistent.t_key action [Hide("theme_key"), Hide("sett_curtain"), Show("active_theme_key"), Show("theme_buttons"), Hide("talk_button"), Hide("countdown")]

    key persistent.t_r_key.upper() action [Hide("theme_key"), Hide("sett_curtain"), Show("active_theme_key"), Show("theme_buttons"), Hide("talk_button"), Hide("countdown")]

    key persistent.t_r_key action [Hide("theme_key"), Hide("sett_curtain"), Show("active_theme_key"), Show("theme_buttons"), Hide("talk_button"), Hide("countdown")]



screen active_theme_key():

    key persistent.t_key action [Show("theme_key"), Show("sett_curtain"), Hide("active_theme_key"), Hide("theme_buttons"), Show("talk_button"), Show("countdown")]

    key persistent.t_key.upper() action [Show("theme_key"), Show("sett_curtain"), Hide("active_theme_key"), Hide("theme_buttons"), Show("talk_button"), Show("countdown")]

    key persistent.t_r_key.upper() action [Show("theme_key"), Show("sett_curtain"), Hide("active_theme_key"), Hide("theme_buttons"), Show("talk_button"), Show("countdown")]

    key persistent.t_r_key action [Show("theme_key"), Show("sett_curtain"), Hide("active_theme_key"), Hide("theme_buttons"), Show("talk_button"), Show("countdown")]

    key "K_ESCAPE" action [Show("theme_key"), Show("sett_curtain"), Hide("active_theme_key"), Hide("theme_buttons"), Show("talk_button"), Show("countdown")]



screen theme_buttons():
    on "show" action [Function(theme_but_show), Hide("talk_button")]

    on "hide" action [Function(renpy.hide, "th_1"), Function(renpy.hide, "th_2"), Function(renpy.hide, "th_3"), Function(renpy.hide, "th_4"), Function(renpy.hide, "th_5")]

    imagebutton xalign but_coord("2b", 0) yalign but_coord("2b", 1):
        idle "round_2_hit"
        hovered [Function(renpy.show, "th_2", zorder=2, at_list=[but_hover(2)]), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered Function(renpy.show, "th_2", zorder=2, at_list=[but_idle(2)])
        focus_mask True
        action [Function(ColorTheme().orange), Hide("active_theme_key"), Hide("theme_buttons"), Jump("ch1_loop"), Function(ui.interact)]

    imagebutton xalign but_coord("4b", 0) yalign but_coord("4b", 1):
        idle "round_4_hit"
        hovered [Function(renpy.show, "th_4", zorder=2, at_list=[but_hover(4)]), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered Function(renpy.show, "th_4", zorder=2, at_list=[but_idle(4)])
        focus_mask True
        action [Function(ColorTheme().yellow), Hide("active_theme_key"), Hide("theme_buttons"), Jump("ch1_loop"), Function(ui.interact)]

    imagebutton xalign 0.5 yalign but_coord("3b", 1):
        idle "round_3_hit"
        hovered [Function(renpy.show, "th_3", zorder=2, at_list=[but_hover(3)]), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered Function(renpy.show, "th_3", zorder=2, at_list=[but_idle(3)])
        focus_mask True
        action [Function(ColorTheme().default), Hide("active_theme_key"), Hide("theme_buttons"), Jump("ch1_loop"), Function(ui.interact)]


    imagebutton xalign but_coord("1b", 0) yalign but_coord("1b", 1):
        idle "round_1_hit"
        hovered [Function(renpy.show, "th_1", zorder=2, at_list=[but_hover(1)]), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered Function(renpy.show, "th_1", zorder=2, at_list=[but_idle(1)])
        focus_mask True
        action [Function(ColorTheme().green), Hide("active_theme_key"), Hide("theme_buttons"), Jump("ch1_loop"), Function(ui.interact)]

    imagebutton xalign but_coord("5b", 0) yalign but_coord("5b", 1):
        idle "round_5_hit"
        hovered [Function(renpy.show, "th_5", zorder=2, at_list=[but_hover(5)]), Play("sound", "mod_assets/sfx/hover.ogg")]
        unhovered Function(renpy.show, "th_5", zorder=2, at_list=[but_idle(5)])
        focus_mask True
        action [Function(ColorTheme().blue), Hide("active_theme_key"), Hide("theme_buttons"), Jump("ch1_loop"), Function(ui.interact)]


#----------------------------------------Шторка настроек------------------------------------------------


screen sett_curtain():
    if renpy.mobile:
        imagebutton xalign 0.5 yalign 0.05:
            idle im.Scale("mod_assets/button/custom/mob_cur_but.png", 50, 50)
            action [Function(renpy.show, "curtain", at_list=[show_cur], zorder=10), Hide("sett_curtain"), Show("act_curtain"), Show("cur_buttons")]

    else:
        mousearea:
            area (0, 0, 1280, 100)
            hovered [Function(renpy.show, "curtain", at_list=[show_cur], zorder=1), Show("act_curtain"), Show("cur_buttons")]
            unhovered [Function(renpy.show, "curtain", at_list=[hide_cur], zorder=10), Hide("cur_buttons")]


screen cur_buttons():
    imagebutton xalign 0.26 yalign 0:
        idle "mod_assets/button/custom/mob_but_hit.png"
        sensitive persistent.ch_vol
        action [Function(renpy.show, "curtain", at_list=[hide_cur], zorder=10), SetVariable("set", "music"), Hide("volume_key"), Hide("sett_curtain"), Show("active_volume_key"), If(renpy.mobile, true=[Show("mob_active_volume_but"), Jump("mob_vol")], false=Show("con_volume")), Hide("sound_volume_key"),
          Hide("talk_button"), Hide("countdown"), Function(renpy.show, "cup_but", at_list=[pos_cup_button], zorder=10),
           If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    imagebutton xalign 0.42 yalign 0:
        idle "mod_assets/button/custom/mob_but_hit.png"
        sensitive persistent.ch_vol
        action [Function(renpy.show, "curtain", at_list=[hide_cur], zorder=10), SetVariable("set", "sound"), Hide("sound_volume_key"), Hide("sett_curtain"), If(renpy.mobile, true=[Show("mob_active_sound_but"), Jump("mob_sound")], false=[Hide("sound_volume_key"), Show("active_sound_volume_key"), Show("con_sound_volume"), Show("sound_test")]),
         Hide("talk_button"), Hide("countdown"),
        If(renpy.get_screen("music_player_buttons"), true=[SetVariable("is_playing", True), Hide("music_player_buttons")], false=SetVariable("is_playing", False))]

    imagebutton xalign 0.58 yalign 0:
        idle "mod_assets/button/custom/mob_but_hit.png"
        sensitive persistent.ch_mus
        action [Hide("music_key"), Hide("sett_curtain"), Show("active_music_key"), Show("hide_all_talk"), Hide("talk_button"), Hide("countdown"), If(renpy.mobile, true=Show("mob_music_player"), false=Show("music_player_buttons")), Function(renpy.show, "curtain", at_list=[hide_cur], zorder=10)]

    imagebutton xalign 0.74 yalign 0:
        idle "mod_assets/button/custom/mob_but_hit.png"
        sensitive persistent.themes
        action [Hide("theme_key"), Hide("sett_curtain"), Show("active_theme_key"), Show("theme_buttons"), Hide("talk_button"), Hide("countdown"), Function(renpy.show, "curtain", at_list=[hide_cur], zorder=10)]





screen act_curtain():

    on "hide" action Function(renpy.show, "curtain", at_list=[hide_cur], zorder=10)

#close buttons
    imagebutton yalign 0 xalign 0:
        idle "mod_assets/button/custom/mob_hide_hit.png"
        action [Function(renpy.show, "curtain", at_list=[hide_cur], zorder=10), Hide("act_curtain"), Show("sett_curtain")]

    imagebutton yalign 0 xalign 0.9999:
        idle "mod_assets/button/custom/mob_hide_hit.png"
        action [Function(renpy.show, "curtain", at_list=[hide_cur], zorder=10), Hide("act_curtain"), Show("sett_curtain")]
