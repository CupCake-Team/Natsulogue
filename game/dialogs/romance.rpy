label dia_romance:
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
        show natsuki r1:
            xcenter 630
            easein 1.00 xcenter 330
    if right:
        show natsuki r1:
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
        "{i}Ты милая!{/i}" if persistent.is_cute == False:
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            n r1k "..!"
            n r1m "Я..."
            n r1n "Не..."
            n r1j "...{i}милая!{/i}"
            n r1n "Ты специально, да?"
            n "Уже забыл, как я отношусь к этому?"
            n "Ты же сто процентов играл в игру и заранее знаешь мою реакцию."
            n "Хотя кого я обманываю?"
            n "На самом деле, мне приятно, когда я слышу в свою сторону такую фразу, но..."
            n "...не слышать же её по сто раз в день!"
            n "Вот представь себе, что тебя постоянно называют в школе милой."
            n "Раньше я старалась это игнорировать, но потом..."
            n "Ух... {w}Неважно."
            n "Просто знай, что мне было приятно услышать это от тебя, только не нужно повторяться, ладно?"
            $persistent.is_cute = True
            $renpy.save_persistent
            call ch1_loop from _call_ch1_loop_30




        "{i}Ты милая!{/i}" if persistent.is_cute == True:
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            n r1n "Так... {w}Решил поиздеваться надо мной?"
            n r1l "Вместо кучи слов я сделаю гораздо проще."
            n r1n "Не видать тебе этой кнопки, дурак."
            $persistent.is_cute = "baka"
            $renpy.save_persistent
            call ch1_loop from _call_ch1_loop_31



        "{i}Ты красивая!{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630

            n r1n "Э... {w}Ну..."
            n "Спасибо, наверное..."
            n "Я редко слышала от кого–то нечто подобное."
            n r1l "Хотя казалось бы, такие простые слова..."
            n r1n "Конечно, у меня нет каких-то комплексов на этот счёт, но я никогда не считала себя красавицей."
            n r1h "Просто обычная и приятная внешность, разве этого недостаточно?"
            n r1n "Сейчас красота в какой-то абсолют возведена."
            n r1l "Ладно, опять начинаю философствовать..."
            n r1o "В общем, мне было приятно услышать от тебя это, всё..."


            call ch1_loop from _call_ch1_loop_32




        "{i}Ты очаровашка!{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630



            n r1n "М... {w}Пытаешься заставить меня покраснеть?"
            n "Конечно, слышать такое в свой адрес, непривычно, но у тебя не получится этого сделать."
            n r1h "Хе–хе–хе..."
            n "Но всё равно, спасибо что делаешь меня счастливой, [player]."
            n r1n "Похвала от тебя, ну...{w} Это конечно приятно, но не переусердствуй, а то верить перестану."
            n r1l "И да..."
            n r1h "Пусть я тебя и не видела, но мне кажется, что ты тоже очаровашка."
            n "Хи–хи–хи..."

            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:
                call ch1_loop from _call_ch1_loop_33






        "{i}Ты умная!{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630



            n r1e "Как–то это странно прозвучало, не находишь?"
            n "Хотя, если мы тут сидим и при этом нашли способ общаться друг с другом..."
            n "r1d Значит ты прав, я смогла немного укротить код игры."
            n "Мне нравится твой ход мыслей, [player]."
            n r1e "Но признаюсь, ты сперва сбил меня с толку такими словами."
            n r1c "Я, конечно, человек не глупый, но и гением мысли никогда не являлась."
            n r1d "Хотя, сейчас мы остались лишь вдвоём, можно развиваться сколько душе угодно."
            n "Тот же игровой код, сколько же он ещё в себе таит?"

            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:
                call ch1_loop from _call_ch1_loop_34






        "{i}Ты лучшая!{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630





            n r1j "А... {w}Я... {w}Д-дурак!"
            n r1n "Ты специально, да?"
            n r1m "Просто... {w}Мне приятен сам факт того, что кто-то считает меня лучшей..."
            n "Н–не подумай ни о чём таком!"
            n r1n "И не вздумывай обманывать."
            n "Иначе я пойму, что ты только льстить умеешь."





            call ch1_loop from _call_ch1_loop_35




        "{i}Ты хороша!{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630



            n r1e "Эм... {w}И что это должно значить?"
            n "Что за странная фраза?"
            n r1b "Это ненавязчивая попытка подкатить, или что?"
            n "Я бы посоветовала тебе следить за своим языком, [player]."
            n r1e "Так ведь и девушку задеть можно."

            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:
                call ch1_loop from _call_ch1_loop_36







        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_37

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_38

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_39
