label dia_other:
    $left = False
    $right = False
    $lr = renpy.random.randint(1,2)
    $refuse_ans = renpy.random.randint(1,3)
    $cur_time = datetime.datetime.now()
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
        "{i}Где бы тебе сейчас хотелось оказаться?{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            n r1e "Думаю, далеко отсюда."
            n r1b "Мне здесь не очень нравится..."
            n r1e "Несмотря на то, что я никогда не страдала клаустрофобией, эти стены вокруг выносят мне мозг."
            n "Откуда здесь вообще есть воздух и тепло?"
            n "Хотя, судя по логам, здесь хозяйничала Моника."
            n "Наверное она хотела использовать эту комнату для общения с тобой."
            n r1b "Правда всё пошло не по её плану..."
            n r1e "Эх, а ведь как было бы классно оказаться не в этой коробке посреди космоса, а где–нибудь на природе."
            n "Тот же лес, пляжик на море, горы хотя бы..."
            n r1b "Просто лечь на землю и закрыть глаза, безмятежно наслаждаясь спокойствием."
            n r1e "Если бы я знала, как нормально редактировать игровой код – мы бы уже давно проводили время в другом месте."
            n "Мне здесь всё равно больше нечего делать."
            n "Вот ты, например, выйдешь из игры, чем же мне тогда здесь заниматься?"
            n r1b "Разве что разглядывать космос и с ума сходить."
            n r1e "Серьёзно, неужели Моника не думала о том, чтобы оставить здесь какие-то вещи для досуга?"
            n "Или ей казалось, что ты будешь сидеть с ней целую вечность?"
            n "Как недальновидно с её стороны, оказывается."
            n r1c "Ничего, со скуки я уж точно не умру, хи-хи-хи..."
            call ch1_loop from _call_ch1_loop_23




        "{i}Чего тебе не хватает в этой комнате?{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630

            n r1e "Много чего, на самом деле..."
            n "Плиты, например, нет."
            n "И как мне, спрашивается, готовить?"
            n r1b "Это моё самое любимое занятие, как не крути..."
            n r1e "Та же коллекция манги, она ведь утеряна."
            n "Почему кладовка не перенеслась сюда?"
            n "Сидела бы себе там и читала томик за томиком, наслаждаясь всеми этими историями..."
            n "Да тут даже кровати нет!"
            n "Вот захотелось мне полежать, а на чём?"
            n "Либо ложиться на пол, либо..."
            n r1j "Н-нет, на стол я точно не лягу!"
            n r1n "Серьёзно, тут от скуки помереть можно..."
            n "Ладно, ничего, если разберусь с кодом – может быть смогу обставить эту комнату."
            n r1l "Ты же ведь не будешь сидеть тут постоянно, и мне придётся проводить время в компании с собой..."


            call ch1_loop from _call_ch1_loop_24



        "{i}2+2*2?{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630


            n r1f "А–ха–ха–ха, что за глупый вопрос?"
            n r1o "Конечно же восемь!"
           show natsuki r1b
            pause(3)
            n r1d "Ладно–ладно, шучу, шесть это, шесть!"
            n r1a "Тебе совсем не о чем поговорить со мной, или что?"


            call ch1_loop from _call_ch1_loop_25



        "{i}Как ты относишься к Новому Году?{/i}" if cur_time.strftime("%d") >= "24" and cur_time.strftime("%d") <= "31" and cur_time.strftime("%m") == "12":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630


            n r1e "Ты спрашиваешь у меня только потому, что у тебя скоро этот праздник?"
            n "Блин... {w}Прости, что сходу придираюсь."
            n r1d "Сказать по правде, мне нравится Новый Год."
            n "Всё-таки сам понимаешь, всё наполняется счастьем, весельем, будто бы следующий год действительно принесёт что–то хорошее."
            n r1a "Это сложно игнорировать..."
            n "Правда отцу, например, не нравилось праздновать после того, как мамы не стало."
            n r1b "Он понимал, что дальше для него будет всё хуже и хуже..."
            n r1c "Я же не была настолько пессимистична, поэтому мне этот праздник нравился."
            n "Перед Новым Годом город как будто оживал..."
            n r1d "Проходили какие-то соревнования по лепке снеговиков, магазины завлекали новогодними скидками, толпы людей гуляли по улицам..."
            n r1g "И вдобавок ко всему ещё и снег!"
            n r1c "Когда ещё поиграешь в снежки, как не зимой?"
            n r1b "Конечно, отец мне редко что дарил…"
            n r1c "Но в любом случае, я ещё давно знала, что все эти подарки появляются благодаря родителям, так что мне не было обидно."
            n r1b "Да уж... {w}Такой простой вопрос, а сколько воспоминаний."
            n r1d "В общем, думаю ты уже понял, что Новый Год, как праздник, мне нравится."
            n r1b "Жаль только, что эти беззаботные деньки рано или поздно закончатся и вновь вернутся серые будни..."
            n "Ладно, не буду портить тебе настроение."

            call ch1_loop from _call_ch1_loop_26




        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_27

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_28

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_29
