label dia_requests:
    $left = False
    $right = False
    $lr = renpy.random.randint(1,2)
    if lr == 1:
        $left = True
        $right = False
    else:
        $right = True
        $left = False

    $side()

    $dia_hide()

    $ans = random_ans()

    menu:
        "{i}Я бы хотел изменить громкость звука...{/i}":
            hide screen countdown
            $side_return()

            if persistent.repeat == 0:
                n r1d "Ах да, совсем забыла предупредить о том, что главного меню у игры больше нет."
                n r1c "Не волнуйся за это, сейчас всё исправлю."
                n r1b "Подожди немного..."
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
                show monika_bg zorder 1
                show natsuki r1 zorder 2
                with Dissolve(1.0)
                show screen wowcup
                n r1e "Хорошо, что я не прогуливала уроки информатики..."
                n r1c "В общем, главное меню вернуть не получилось, но вытащить из него настройки звука удалось."
                if (not renpy.mobile):
                    n r1d "Я забиндила тебе на клавишу V громкость музыки, а на S – остальных звуков."
                    n "Там появится небольшая панелька с уровнем громкости, регулировать которую можно колесиком мыши или тачпадом."
                    n r1e "Ничего себе, сколько заумных слов вспомнила..."
                    n r1o "Радуйся, что я вообще решила помочь тебе, хи-хи-хи..."
                    n r1d "Ах да, если тебя не устраивают те клавиши, что поставила я, можешь сменить их, только попроси."
                else:
                    if persistent.ch_mus != True:
                        n r1e "Кстати говоря, судя по файлам, ты сидишь с телефона..."
                        n r1c "Я конечно не специалист, но мне кажется, что встретить новеллу на телефоне – это та ещё редкость."
                        n "В любом случае, пришлось повозиться, чтобы сделать всё удобным."
                        n r1d "Где-то наверху должна появиться кнопка, там будут все настройки."
                        n "Свайпаешь вверх – увеличиваешь громкость, всё просто."
                    else:
                        n r1c "Если что, я закинула их к плееру."
                        n r1d "Там как раз были свободные кнопки."
                        n "Свайпаешь вверх – увеличиваешь громкость, все просто."
                n r1g "Пользуйся!"
                show natsuki r1c
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
                call ch1_loop

            if persistent.repeat == 1:
                n " r1e Я же ведь всё объясняла, разве нет?"
                if (not renpy.mobile):
                    n "Если ты пытался изменить звук, жмякая курсором, то это так не работает."
                    n r1b "К сожалению я не смогла прикрутить это..."
                    n r1e "Менять всё это нужно колёсиком мышки или тачпадом, смотря с какого устройства ты сидишь."
                else:
                    n "Тем более, там все интуитивно понятно."
                    n r1b "Ладно, объясню ещё раз."
                    n r1e "Сверху кнопка, выбираешь настройку, свайпаешь вверх - увеличиваешь громкость"
                n r1b "Надеюсь, вопросов больше нет."
                show natsuki r1b
                $persistent.repeat = 2
                $renpy.save_persistent()
                call ch1_loop

            if persistent.repeat == 2:
                n r1l "Знаешь, уже не смешно..."
                n r1n "Ты это делаешь ради прикола?"
                n "Я тебе уже два раза объясняла что к чему."
                n "Неужели мало?"
                n "Так, всё, достал меня, разбирайся сам."
                n r1m "Метод тыка тебе в помощь, болвашка."
                show natsuki r1b
                call ch1_loop

        "{i}Я бы хотел поменять музыку...{/i}" if persistent.mus_repeat == 0 or persistent.mus_repeat == 1:
            hide screen countdown
            $side_return()
            if persistent.mus_repeat == 0:
                n r1a "Хм..."
                n r1d "Думаю, я смогу устроить нечто подобное, если найду способ, как это сделать."
                n r1e "Мне и самой надоела эта мелодия на заднем фоне."
                n "Какая-та она... {w}неприятная."
                n r1c "Ладно, сейчас поищу в файлах игры что-то полезное."
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
                show monika_bg zorder 1
                show natsuki r1 zorder 2
                with Dissolve(1.0)
                show screen wowcup
                n "Ха?"
                n "Кажется я что-то нашла..."
                if (not renpy.mobile):
                    n r1d "Не знаю, работает ли эта штука, но попробуй потыкать."
                    n "Если что, открывается на клавишу M."
                    show natsuki r1c
                else:
                    if persistent.ch_vol == True:
                        n r1d "Если что, я закинула ее к настройке громкости."
                        n r1c "Там как раз была свободная кнопка."
                    else:
                        n r1a "Хм-м-м-м..."
                        n r1c "Судя по файлам, ты сидишь с телефона."
                        n r1d "Я конечно, не специалист, но мне кажется, что встретить новеллу на телефоне – это та еще редкость."
                        n "В любом случае, пришлось повозиться, чтобы сделать все удобным."
                        n "Где-то наверху должна появиться кнопка, там будут все настройки."
                        show natsuki r1c
                $persistent.ch_mus = True
                $persistent.mus_repeat = 1
                $renpy.save_persistent()
                call ch1_loop

            if persistent.mus_repeat == 1:
                n r1e "Хорошо, но зачем ты просишь меня об этом?"
                if (not renpy.mobile):
                    n "Просто нажми клавишу [str(persistent.m_key).upper()] и ставь любую музыку."
                else:
                    n r1e "Просто открой плеер и ставь что душе угодно."
                n "Или ты хочешь, чтобы выбор сделала я?"
                $left = False
                $right = False
                menu:
                    "Да.":
                        n r1d "Хорошо, я поставлю эту мелодию."
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
                        n r1e "Тогда зачем спрашиваешь?"
                        n r1b "Выбор за тобой, можешь вообще звук на ноль выкрутить, если хочешь..."
                        $persistent.mus_repeat = 2
                        $renpy.save_persistent()


                call ch1_loop

        "{i}Можешь поставить музыку, которая тебе нравится?{/i}" if persistent.mus_repeat == 2:
            hide screen countdown
            $side_return()

            $rand_mus_answer = renpy.random.randint(1,3)

            if rand_mus_answer == 1:
                n r1e "Как скажешь."
                show natsuki r1c
            if rand_mus_answer == 2:
                n r1e "Хорошо, я поставлю эту мелодию."
                show natsuki r1c
            if rand_mus_answer == 3:
                n r1e "Ладно, пусть будет... {w}эта."
                show natsuki r1b

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

            call ch1_loop


        "{i}Мне бы хотелось поиграть с тобой во что-то...{/i}" if persistent.f_game == 0:
            hide screen countdown
            $side_return()
            $left = False
            $right = False
            n r1e "Поиграть?"
            n r1d "Хм... {w}О, точно!"
            n r1c "В коде игры кое–что осталось."
            n r1g "Что же, встречай, вилочки-кексики!"
            n r1f "Название сама придумала, хи-хи-хи..."
            n r1d "По правде говоря, это обычные крестики–нолики, просто вместо них вилки и кексы."
            n r1e "Правила игры абсолютно такие же, думаю тебе не нужно их разъяснять."
            n r1f "Хочешь сыграть со мной?"
            show natsuki r1c
            menu:
                "Да.":
                    $lr = renpy.random.randint(1,2)
                    if lr == 1:
                        $left = True
                        $right = False
                    else:
                        $right = True
                        $left = False
                    n r1e "Тогда чего мы ждём?"
                    n r1g "Погнали!"
                    n r1f "Кстати, я нашла функцию вероятности..."
                    n r1c "Думаю, именно она будет определять, чей ход будет самым первым."
                    n r1g "Ладно, хорош болтать – поехали играть!"
                    $persistent.f_game = 1
                    $renpy.save_persistent()
                    $initialize_game()
                    $rand_turn = random.randint(1,2)
                    if rand_turn == 1 and left == True:
                        n r1d "Я хожу первой!"
                        show natsuki r1c:
                            xcenter 630
                            easein 1.00 xcenter 330
                        show cft_pole zorder 2 at for_field_l
                        jump change_side
                    if rand_turn == 1 and right == True:
                        n r1d "Я хожу первой!"
                        show natsuki r1c:
                            xcenter 630
                            easein 1.00 xcenter 930
                        show cft_pole zorder 2 at for_field_r
                        jump change_side
                    if rand_turn == 2 and left == True:
                        n r1d "Ты ходишь первым."
                        show natsuki r1c:
                            xcenter 630
                            easein 1.00 xcenter 330
                        show cft_pole zorder 2 at for_field_l
                        call screen cup_fork_toe("left", None)
                    if rand_turn == 2 and right == True:
                        n r1d "Ты ходишь первым."
                        show natsuki r1c:
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
                    n r1e "Почему?"
                    n r1f "Неужели боишься проиграть?"
                    n r1c "Ладно, тогда в другой раз."
                    $persistent.f_game = 1
                    $renpy.save_persistent()
                    call ch1_loop


        "{i}Я бы хотел поиграть с тобой в вилочки-кексики...{/i}" if persistent.f_game >= 1:
            hide screen countdown
            $side_return()
            $r_ans = random.randint(1,2)
            if r_ans == 1:
                n r1d "Хорошо, почему бы и нет?"
            if r_ans == 2:
                n r1d "Давай, я не против."
            $initialize_game()
            $rand_turn = random.randint(1,2)
            if rand_turn == 1 and left == True:
                n r1d "Я хожу первой!"
                show natsuki r1c:
                    xcenter 630
                    easein 1.00 xcenter 330
                show cft_pole zorder 2 at for_field_l
                jump change_side
            if rand_turn == 1 and right == True:
                n r1d "Я хожу первой!"
                show natsuki r1c:
                    xcenter 630
                    easein 1.00 xcenter 930
                show cft_pole zorder 2 at for_field_r
                jump change_side
            if rand_turn == 2 and left == True:
                n r1d "Ты ходишь первым."
                show natsuki r1c:
                    xcenter 630
                    easein 1.00 xcenter 330
                show cft_pole zorder 2 at for_field_l
                call screen cup_fork_toe("left", None)
            if rand_turn == 2 and right == True:
                n r1d "Ты ходишь первым."
                show natsuki r1c:
                    xcenter 630
                    easein 1.00 xcenter 930
                show cft_pole zorder 2 at for_field_r
                call screen cup_fork_toe("right", None)



        "{i}Я бы хотел поменять режим экрана...{/i}" if persistent.ch_vol == False and persistent.ch_mus == False and persistent.first_change == False and (not renpy.mobile):
            hide screen countdown
            $side_return()



            n r1f "Решил полностью сфокусироваться на мне?~"
            n r1d "Ладно, я знаю, как тебе помочь."
            n r1d "В коде игры есть одна менюшка, в которой ты можешь просмотреть все назначенные клавиши."
            n r1e "Правда, пока там только одна, как раз для экрана..."
            n "Похоже, придётся дорабатывать."
            n r1c "В любом случае, сейчас я открою её..."
            n r1d "Ах да, если хочешь поменять клавишу, то можешь сделать это так же через эту настройку."
            n "Но пожалуйста, выбирай только те буквы, у которых есть английский аналог."
            n r1e "Мне ещё багов лишних не хватало..."
            n r1c "Не будь дурашкой, хорошо?"


            $side_return()

            n r1e "Тебе не понравились те, что назначила я?"
            n r1c "Ну, хорошо..."
            n r1d "В коде игры есть одна менюшка, в которой ты можешь просмотреть все назначенные клавиши."
            n "Ах да, если хочешь поменять клавишу, то можешь сделать это так же через эту настройку."
            n "Но пожалуйста, выбирай только те буквы, у которых есть английский аналог."
            n r1b "Мне ещё багов лишних не хватало..."
            n r1c "Не будь дурашкой, хорошо?"


            $side_return()

            $ rand_ans = renpy.random.randint(1,3)

            if rand_ans == 1:
                n r1e "Хорошо..."
            if rand_ans == 2:
                n r1d "Да, конечно."
            if rand_ans == 3:
                n r1f "Только ничего не сломай."


            $side_return()

            $rand_ans = renpy.random.randint(1,3)

            if rand_ans == 1:
                n r1e "А... Уже уходишь?"
                n r1d "Хорошо, спасибо что предупредил меня."
                n r1b "Надеюсь ты уходишь ненадолго, здесь так скучно..."
                $persistent.bye = True
                $renpy.save_persistent()
                call save_exp from _call_save_exp

            if rand_ans == 2:
                n r1e "Так быстро?"
                n "Ладно, наверное у тебя какие–то дела или что-то вроде этого."
                n r1d "В таком случае не буду тебя задерживать, удачи."
                $persistent.bye = True
                $renpy.save_persistent()
                call save_exp from _call_save_exp_1

            if rand_ans == 3:
                if renpy.mobile:
                    $dev = "телефоне"
                else:
                    $dev = "компьютере"
                n r1b "Иногда нам нужно побыть наедине со своими мыслями, думаю ты понимаешь..."
                n r1f "Если не вернёшься – я что–нибудь натворю на твоём [dev], хи–хи–хи...."
                n r1o "Ладно–ладно, я просто пошутила!"
                n r1g "Пока!"
                $persistent.bye = True
                $renpy.save_persistent()
                call save_exp from _call_save_exp_2





        "{i}Я бы хотел включить параллакс...{/i}" if persistent.parallax_bg == False:
            hide screen countdown
            $side_return()
            n r1d "Хорошо."
            $ persistent.parallax_bg = True
            $ print(persistent.parallax_bg)
            n r1e "Вроде готово."
            call ch1_loop

        "{i}Можешь выключить параллакс?{/i}" if persistent.parallax_bg == True:
            hide screen countdown
            $side_return()
            n r1d "Хорошо."
            $ persistent.parallax_bg = False
            
            call ch1_loop


        "{i}[ans]{/i}":
            $side_return()
            call ch1_loop
