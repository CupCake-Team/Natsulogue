label dia_hobbies:
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
        "{i}Почему тебе так нравится готовка?{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            n r1g "Я рада, что ты спросил меня об этом."
            n r1d "Готовка для меня не просто увлечение, на которое я трачу свободное время, а ещё и прекрасная возможность стать настоящим шеф–поваром и связать с этим жизнь."
            n r1b "Правда теперь это не имеет смысла..."
            n "Кафе и ресторанов всё равно больше не существует, а приготовить для себя что-нибудь никак не получится."
            n r1e "В этой комнате даже нет кухонной плиты, какого чёрта, Моника?"
            n r1d "Ничего, когда-нибудь я научусь создавать объекты и обставлю эту комнату мебелью."
            n r1e "Серьёзно, мне тяжело без готовки, она меня успокаивает."
            n r1c "Ещё в детстве мне понравилась одна манга..."
            n "Она была про коллектив одного из ресторанов, который участвовал в кулинарном шоу, где проводилась битва между заведениями со всей Японии, а потом..."
            n r1e "...я познакомилась с «Ванильными девочками» и мою любовь к готовке уже ничего не могло остановить!"
            n r1b "Правда это ещё не все причины."
            n "Когда моя семья была ещё полной – практически всегда у плиты стояла мама и радовала всех домашней едой, но она..."
            n "..."
            n "В общем, я осталась наедине с отцом."
            n r1e "Он обходил плиту стороной, ибо совсем не умел готовить, поэтому у меня не было возможности нормально поесть."
            n "Если же он и давал мне какую-то стряпню – её было неохота даже пробовать."
            n r1b "Вкус был просто отвратительным..."
            n "Некоторое время я питалась в школьной столовой и изредка баловала себя полуфабрикатами, но потом мне попались те томики манги и я решила научиться готовить."
            n r1e "Сперва это было не так уж и просто..."
            n "Ингредиентов часто не хватало, да и блюда получались не самыми вкусными."
            n r1d "Мне даже хотелось бросить эту затею, благо я вовремя одумалась и вместо того, чтобы опустить руки - продолжила заниматься готовкой."
            n "Как видишь, у меня получилось не только познать кулинарию, но ещё и найти себя в ней..."
            n r1c "Так что я усвоила один урок."
            n r1d "Не нужно бросать своё увлечение на пол пути к совершенству, так как ты можешь добиться больших успехов."
            n r1g "Поэтому [player], не будь лентяем, хорошо?"
            show natsuki r1c

            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:
                call ch1_loop from _call_ch1_loop_8

        "{i}Как ты полюбила мангу?{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630

            n r1e "Ну... {w}На самом деле это долгая история."
            n "Как и многим детям, родители иногда читали мне мангу, в основном перед сном."
            n "Научившись читать, я стала покорять её самостоятельно."
            n r1d "Уже тогда мне покупали новые томики манги за хорошее поведение."
            n r1e "Это побуждало меня быть послушной..."
            n "В итоге коллекция всего этого добра росла стремительными темпами, я иногда даже не успевала всё прочитать."
            n r1f "Знакомые ребята мне очень сильно завидовали."
            n r1d "Ко мне в гости часто приходили дети со двора чтобы просто почитать мангу и пообсуждать её."
            n r1e "Мне очень нравились такие посиделки..."
            n r1l "Я росла и всё это прекратилось, ибо манга у всех стала ассоциироваться с детской побрякушкой."
            n r1k "Да и мамы не стало..."
            n r1e "Отец не покупал мне мангу, ибо терпеть её не мог."
            n "Мне приходилось тратить все свои карманные деньги на покупку нового томика и постоянно всё прятать."
            n r1a "Хорошо, что я смогла найти укромное местечко для всей своей коллекции..."
            n r1e "Но время шло и количество томиков тоже."
            n "Я редко кому рассказывала об этом, ибо в итоге кто-то обязательно проговаривался и все надо мной лишь смеялись."
            n "Сперва мне было очень обидно, но потом пришло осознание..."
            n r1o "Насколько у людей всё плохо в жизни, что они самоутверждаются за счёт девушки с иным увлечением."
            n r1f "Те ещё дураки в общем."
            n r1e "И вот так чтение манги стало для меня чем-то вроде протеста против общества."
            n r1g "Естественно, я продолжала читать мангу, не смотря ни на что!"
            n r1b "Хм..."
            n r1d "Раз уж наш мир основан на твоём, то это значит, что в нём тоже есть манга."
            n "Интересно, какая?"
            n r1c "Мне было бы интересно её полистать..."

            call ch1_loop from _call_ch1_loop_9

        "{i}Ты играешь в видеоигры?{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630

            n r1g "Конечно, ведь это прекрасная возможность уйти на некоторое время от реального мира."
            n r1e "Если при чтении манги всё равно приходится напрягать воображение, а при просмотре аниме лишь наблюдать за происходящим, то игра даёт возможность во всём поучаствовать."
            n r1d "В придачу у них очень много жанров на любой вкус."
            n "Мне самой больше всего нравилось играть во всякие стрелялки."
            n r1e "Всё-таки иногда нужно выпускать пар..."
            n "Конечно, почти все девочки в школе играли во всякие фермы и симуляторы жизни, но мне это было не особо интересно."
            n r1b "Ну а ты, как погляжу, любитель визуальных новелл?"
            n "Или просто решил проверить этот жанр?"
            n r1i "Хотя, игру, в которой я нахожусь, хорошей не считаю..."
            n r1e "В любом случае игровая индустрия прекрасно справляется со своей задачей, а именно развлекает игрока."
            n "Поэтому ничего удивительно в том, что виртуальные миры так популярны..."
            n r1b "Эх... {w}Жалко что из всех забав в коде игры остались лишь «вилочки–кексики»."
            n r1d "Я написала эту игру, так как на уроке информатики нам дали домашнее задание – принести на флешке какой-то солидный проект."
            n r1g "За «вилочки–кексики» мне дали высокий балл, да и всем они показались очень милыми."
            n r1f "Если хочешь, то можем сыграть в них вместе."
            n r1d "Может быть в будущем я создам ещё какие-то игры, заодно немного разовью свои навыки программирования."
            show natsuki r1c

            call ch1_loop from _call_ch1_loop_10



        "{i}Как ты относишься к серьёзной литературе?{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630

            n r1a "Эм... {w}В каком плане?"
            n r1e "Ты про те книжки что читала Юри или в целом?"
            n "Если честно, я отношусь к подобному нейтрально, ибо каждый имеет право на свои предпочтения."
            n "Увы, но классическая литература – это не моё."
            n "Я читаю для того чтобы расслабиться и погрузиться в какую-нибудь интересную историю, а не заниматься поиском скрытого смысла и поглощением писательской философии."
            n r1c "И, как ты понимаешь, манга как раз подходит мне по всем параметрам."
            n r1e "Правда иногда хочется чего–то более глубокого и продуманного…"
            n r1c "Но благо манги столько, что каждый найдёт ту, которая зайдёт больше всего."
            n r1e "Мне даже хотелось одну Юри посоветовать, но, как видишь, я не успела..."
            show natsuki r1b


            call ch1_loop from _call_ch1_loop_11



        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_12

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_13

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_14
