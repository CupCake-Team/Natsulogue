label dia_requests:
    $left = False
    $right = False
    $lr = renpy.random.randint(1,2)
    $refuse_ans = renpy.random.randint(1,3)
    if lr == 1:
        $left = True
        $right = False
    else:
        $right = True
        $left = False

    if left:
        show just nat:
            xcenter 630
            easein 1.00 xcenter 330
    if right:
        show just nat:
            xcenter 630
            easein 1.00 xcenter 930

    hide screen talk_button

    hide screen active_talk_button

    hide screen talk_round

    hide screen active_talk_round

    hide screen choice_buttons_1

    hide screen choice_buttons_2

    hide screen texts

    hide screen volume_key

    hide screen active_volume_key

    hide screen sound_volume_key

    hide screen active_sound_volume_key

    hide screen music_key

    hide screen active_music_key

    hide screen mob_but_curtain

    hide screen mob_active_but_curtain

    menu:
        "{i}Я бы хотел изменить громкость звука...{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            if persistent.repeat == 0:
                n "Ах да, совсем забыла предупредить о том, что главного меню у игры больше нет."
                n "Не волнуйся за это, сейчас всё исправлю."
                n "Подожди немного..."
                hide screen wowcup
                hide screen wowitscupcake
                scene black with Dissolve(1.0)
                pause(10)
                n "Всё, я закончила!"
                show mask_2
                show mask_3
                show room_mask as rm:
                    size (320,180)
                    pos (30,200)
                show room_mask2 as rm2:
                    size (320,180)
                    pos (935,200)
                show monika_room zorder 1
                show just nat zorder 2
                with Dissolve(1.0)
                show screen wowcup
                n "Хорошо, что я не прогуливала уроки информатики..."
                n "В общем, главное меню вернуть не получилось, но вытащить из него настройки звука удалось."
                if (not renpy.mobile):
                    n "Я забиндила тебе на клавишу V громкость музыки, а на S - остальных звуков."
                    n "Там появится небольшая панелька с уровнем громкости, регулировать которую можно колесиком мыши или тачпадом."
                    n "Ничего себе, сколько заумных слов вспомнила..."
                    n "Радуйся, что я вообще решила помочь тебе, хи-хи-хи..."
                    n "Ах да, если тебя не устраивают те клавиши, что поставила я, можешь сменить их, только попроси."
                else:
                    if persistent.ch_mus != True:
                        n "Кстати говоря, судя по файлам, ты сидишь с телефона..."
                        n "Я конечно, не специалист, но мне кажется, что встретить новеллу на телефоне - это та еще редкость."
                        n "В любом случае, пришлось повозиться, чтобы сделать все удобным."
                        n "В общем, где-то сверху появится кнопка, там будут все настройки."
                        n "Свайпаешь вверх - увеличиваешь громкость, все просто."
                    else:
                        n "Если что, я закинула их к плееру."
                        n "Там как раз были свободные кнопки."
                        n "Свайпаешь вверх - увеличиваешь громкость, все просто."
                n "Пользуйся!"
                $persistent.ch_vol = True
                $persistent.repeat = 1
                $renpy.save_persistent()
                $vlm = persistent.svol
                $num = persistent.snum
                $grad = persistent.sgrad
                $soundvlm = persistent.soundvol
                $sounum = persistent.soundnum
                $soungrad = persistent.soundgrad
                $renpy.music.set_volume(vlm, channel="music")
                $renpy.music.set_volume(soundvlm, channel="sound")
                call ch1_loop from _call_ch1_loop_46

            if persistent.repeat == 1:
                n "Я же ведь всё объясняла, разве нет?"
                if (not renpy.mobile):
                    n "Если ты пытался изменить звук, жмякая курсором, то это так не работает."
                    n "К сожалению я не смогла прикрутить это..."
                    n "Менять всё это нужно колёсиком мышки или тачпадом, смотря с какого устройства ты сидишь."
                else:
                    n "Тем более, там все интуитивно понятно."
                    n "Ладно, объясню ещё раз."
                    n "Сверху кнопка, выбираешь настройку, свайпаешь вверх - увеличиваешь громкость"
                n "Надеюсь, вопросов больше нет."
                $persistent.repeat = 2
                $renpy.save_persistent()
                call ch1_loop from _call_ch1_loop_47

            if persistent.repeat == 2:
                n "Знаешь, уже не смешно..."
                n "Ты это делаешь ради прикола?"
                n "Я тебе уже два раза объясняла что к чему."
                n "Неужели мало?"
                n "Так, всё, достал меня, разбирайся сам."
                n "Метод тыка тебе в помощь, болвашка."
                call ch1_loop from _call_ch1_loop_48

        "{i}Я бы хотел поменять музыку...{/i}" if persistent.mus_repeat == 0 or persistent.mus_repeat == 1:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            if persistent.mus_repeat == 0:
                n "Хм..."
                n "Думаю, я смогу это устроить, если найду способ, как это сделать."
                n "Мне и самой надоела эта мелодия на заднем фоне."
                n "Какая-та она... {w}неприятная."
                n "Ладно, сейчас поищу в файлах игры что-то полезное."
                hide screen wowcup
                hide screen wowitscupcake
                scene black with Dissolve(1.0)
                pause(10)
                show mask_2
                show mask_3
                show room_mask as rm:
                    size (320,180)
                    pos (30,200)
                show room_mask2 as rm2:
                    size (320,180)
                    pos (935,200)
                show monika_room zorder 1
                show just nat zorder 2
                with Dissolve(1.0)
                show screen wowcup
                n "Ха?"
                n "Кажется я что-то нашла..."
                if (not renpy.mobile):
                    n "Не знаю, работает ли эта штука, но попробуй потыкать."
                    n "Если что, открывается на клавишу M."
                else:
                    if persistent.ch_vol == True:
                        n "Если что, я закинула ее к настройке громкости."
                        n "Там как раз была свободная кнопка."
                    else:
                        n "Хм-м-м-м..."
                        n "Судя по файлам, ты сидишь с телефона."
                        n "Я конечно, не специалист, но мне кажется, что встретить новеллу на телефоне - это та еще редкость."
                        n "В любом случае, пришлось повозиться, чтобы сделать все удобным."
                        n "В общем, где-то сверху появится кнопка, там будут все настройки."
                $persistent.ch_mus = True
                $persistent.mus_repeat = 1
                $renpy.save_persistent()
                call ch1_loop from _call_ch1_loop_49

            if persistent.mus_repeat == 1:
                n "Хорошо, но зачем ты просишь меня об этом?"
                if (not renpy.mobile):
                    n "Просто нажми клавишу [str(persistent.m_key).upper()] и ставь любую музыку."
                else:
                    n "Просто открой плеер и ставь что душе угодно."
                n "Или ты хочешь, чтобы я выбрала её сама?"
                $left = False
                $right = False
                menu:
                    "Да.":
                        n "Хорошо, я поставлю эту мелодию."
                        $prefered_track_num = renpy.random.randint(0,5)
                        $full_mus_name = renpy.music.get_playing(channel="music")
                        python:
                            mus_name = full_mus_name.replace(music_path,"")
                            current_playing = music_list.index(mus_name)
                            while True:
                                if prefered_track_num == 3 or prefered_track_num == current_playing:
                                    prefered_track_num = renpy.random.randint(0,5)
                                else:
                                    break
                        $renpy.music.play(music_list[prefered_track_num], channel="music")
                        $persistent.mus_repeat = 2
                        $renpy.save_persistent()
                        python:
                            set_back_on_prefered()
                    "Нет.":
                        n "Тогда зачем спрашиваешь?"
                        n "Выбор за тобой, можешь вообще звук на ноль выкрутить, если хочешь..."
                        $persistent.mus_repeat = 2
                        $renpy.save_persistent()


                call ch1_loop from _call_ch1_loop_50

        "{i}Можешь поставить музыку, которая тебе нравится?{/i}" if persistent.mus_repeat == 2:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            $rand_mus_answer = renpy.random.randint(1,3)

            if rand_mus_answer == 1:
                n "Как скажешь."
            if rand_mus_answer == 2:
                n "Хорошо, я поставлю эту мелодию."
            if rand_mus_answer == 3:
                n "Ладно, пусть будет... {w}эта."

            $prefered_track_num = renpy.random.randint(0,5)
            $full_mus_name = renpy.music.get_playing(channel="music")
            python:
                mus_name = full_mus_name.replace(music_path,"")
                current_playing = music_list.index(mus_name)
                while True:
                    if prefered_track_num == 3 or prefered_track_num == current_playing:
                        prefered_track_num = renpy.random.randint(0,5)
                    else:
                        break
            $renpy.music.play(music_list[prefered_track_num], channel="music")

            python:
                set_back_on_prefered()

            call ch1_loop from _call_ch1_loop_51


        "{i}Мне бы хотелось поиграть с тобой во что-то...{/i}" if persistent.f_game == 0:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            n "Поиграть?"
            n "Хм... {w}О, точно!"
            n "В коде игры кое-что осталось."
            n "Что же, встречай, вилочки-кексики!"
            n "Название сама придумала, хи-хи-хи..."
            n "По правде говоря, это обычные крестики-нолики, просто вместо них вилки и кексы."
            n "Правила игры абсолютно такие же, думаю тебе не нужно их разъяснять."
            n "Хочешь сыграть со мной?"
            menu:
                "Да.":
                    $lr = renpy.random.randint(1,2)
                    if lr == 1:
                        $left = True
                        $right = False
                    else:
                        $right = True
                        $left = False
                    n "Тогда чего мы ждём?"
                    n "Погнали!"
                    n "Кстати, я нашла функцию вероятности..."
                    n "Думаю, именно она будет определять, чей ход будет самым первым."
                    n "Ладно, хорош болтать - поехали играть!"
                    $persistent.f_game = 1
                    $renpy.save_persistent()
                    $initialize_game()
                    $rand_turn = random.randint(1,2)
                    if rand_turn == 1 and left == True:
                        n "Я хожу первой!"
                        show just nat:
                            xcenter 630
                            easein 1.00 xcenter 330
                        show cft_pole zorder 2 at for_field_l
                        jump change_side
                    if rand_turn == 1 and right == True:
                        n "Я хожу первой!"
                        show just nat:
                            xcenter 630
                            easein 1.00 xcenter 930
                        show cft_pole zorder 2 at for_field_r
                        jump change_side
                    if rand_turn == 2 and left == True:
                        n "Ты ходишь первым."
                        show just nat:
                            xcenter 630
                            easein 1.00 xcenter 330
                        show cft_pole zorder 2 at for_field_l
                        call screen cup_fork_toe("left", None)
                    if rand_turn == 2 and right == True:
                        n "Ты ходишь первым."
                        show just nat:
                            xcenter 630
                            easein 1.00 xcenter 930
                        show cft_pole zorder 2 at for_field_r
                        call screen cup_fork_toe("right", None)

                "Нет.":
                    $lr = renpy.random.randint(1,2)
                    if lr == 1:
                        $left = True
                        $right = False
                    else:
                        $right = True
                        $left = False
                    n "Почему?"
                    n "Неужели боишься проиграть?"
                    n "Ладно, тогда в другой раз."
                    $persistent.f_game = 1
                    $renpy.save_persistent()
                    call ch1_loop from _call_ch1_loop_52


        "{i}Я бы хотел поиграть с тобой в вилочки-кексики...{/i}" if persistent.f_game >= 1:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $r_ans = random.randint(1,2)
            if r_ans == 1:
                n "Хорошо, почему бы и нет?"
            if r_ans == 2:
                n "Давай, я не против."
            $initialize_game()
            $rand_turn = random.randint(1,2)
            if rand_turn == 1 and left == True:
                n "Я хожу первой!"
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 330
                show cft_pole zorder 2 at for_field_l
                jump change_side
            if rand_turn == 1 and right == True:
                n "Я хожу первой!"
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 930
                show cft_pole zorder 2 at for_field_r
                jump change_side
            if rand_turn == 2 and left == True:
                n "Ты ходишь первым."
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 330
                show cft_pole zorder 2 at for_field_l
                call screen cup_fork_toe("left", None)
            if rand_turn == 2 and right == True:
                n "Ты ходишь первым."
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 930
                show cft_pole zorder 2 at for_field_r
                call screen cup_fork_toe("right", None)



        "{i}Я бы хотел поменять режим экрана...{/i}" if persistent.ch_vol == False and persistent.ch_mus == False and persistent.first_change == False and (not renpy.mobile):
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630



            n "Решил полностью сфокусироваться на мне?~"
            n "Ладно, я знаю, как тебе помочь."
            n "В коде игры есть одна менюшка, в которой ты можешь просмотреть все назначенные клавиши."
            n "Правда, пока там только одна, как раз для экрана..."
            n "Похоже, придётся дорабатывать."
            n "В любом случае, сейчас я открою её..."
            n "Ах да, если хочешь поменять клавишу, то можешь сделать это так же через эту настройку."
            n "Но пожалуйста, выбирай только те буквы, у которых есть английский аналог."
            n "Мне ещё багов лишних не хватало..."
            n "Не будь дурашкой, хорошо?"


            if left:
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 330
            if right:
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 930

            $persistent.first_change = True
            $renpy.save_persistent()

            jump set_buttons


        "{i}Я бы хотел поменять горячие клавиши на другие...{/i}" if (persistent.ch_vol == True or persistent.ch_mus == True) and persistent.first_change == False and (not renpy.mobile):
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Тебе не понравились те, что назначила я?"
            n "Ну, хорошо..."
            n "В коде игры есть одна менюшка, в которой ты можешь просмотреть все назначенные клавиши."
            n "Ах да, если хочешь поменять клавишу, то можешь сделать это так же через эту настройку."
            n "Но пожалуйста, выбирай только те буквы, у которых есть английский аналог."
            n "Мне ещё багов лишних не хватало..."
            n "Не будь дурашкой, хорошо?"


            if left:
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 330
            if right:
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 930

            $persistent.first_change = True
            $renpy.save_persistent()

            jump set_buttons



        "{i}Я бы хотел поменять горячие клавиши на другие...{/i}" if persistent.first_change == True and (not renpy.mobile):

            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            $ rand_ans = renpy.random.randint(1,3)

            if rand_ans == 1:
                n "Хорошо..."
            if rand_ans == 2:
                n "Да, конечно."
            if rand_ans == 3:
                n "Только ничего не сломай."


            if left:
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 330
            if right:
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 930

            jump set_buttons


        
        "{i}Попрощаться...{/i}" if persistent.set_broke == True or renpy.mobile:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            $rand_ans = renpy.random.randint(1,3)

            if rand_ans == 1:
                n "А… Уже уходишь?"
                n "Хорошо, спасибо, что предупредил меня."
                n "Надеюсь, ты уходишь ненадолго, здесь так скучно..."
                $persistent.bye = True
                $renpy.save_persistent()
                call save_exp from _call_save_exp

            if rand_ans == 2:
                n "Так быстро?"
                n "Ладно, наверное у тебя какие-то дела или что-то вроде этого."
                n "В таком случае не буду тебя задерживать, удачи."
                $persistent.bye = True
                $renpy.save_persistent()
                call save_exp from _call_save_exp_1

            if rand_ans == 3:
                if renpy.mobile:
                    $dev = "телефоне"
                else:
                    $dev = "компьютере"
                n "Иногда нам нужно побыть наедине со своими мыслями, думаю ты понимаешь..."
                n "Если не вернёшься – я что-нибудь натворю на твоём [dev], хи-хи-хи...."
                n "Ладно-ладно, я просто пошутила!"
                n "Пока!"
                $persistent.bye = True
                $renpy.save_persistent()
                call save_exp from _call_save_exp_2





        "Я хочу включить Параллакс":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            n "Хорошо."
            show monika_room:
                subpixel True
                topleft
                zoom 1.015
                block:
                    function parallax
                    repeat 
            n "Вроде готово :/"
            call ch1_loop from _call_ch1_loop_15

        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_53

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_54

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_55