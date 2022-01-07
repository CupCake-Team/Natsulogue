label dia_recipes:
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
        show natsuki_room r1:
            xcenter 630
            easein 1.00 xcenter 330
    if right:
        show natsuki_room r1:
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
        "{i}Как испечь вкусные кексы?{/i}":
            hide screen countdown
            if left:
                show natsuki_room r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki_room r1:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Ого, так тебя заинтересовала лучшая часть моей выпечки?"
            n "Говорю сразу, никакого секретного ингредиента в них нет, просто нужно уметь их печь."
            n "Благо я помню принцип их приготовления, так что вот тебе рецептик."
            n "Записывай..."
            n "Для начала, само собой, нужно иметь доступ к плите и всякой кухонной утвари."
            n "Затем достань из холодильника два яйца, ровно сто грамм сливочного масла и около ста двадцати грамм растительного масла."
            n "Далее поищи сахар, его нам понадобится сто восемьдесят грамм, но если его нет, можно взять и пудру."
            n "Естественно, без муки никаких кексов не выйдет, поэтому бери её сто двадцать грамм."
            n "В итоге у нас остаются половина чайной ложки соды, чуть меньше половины чайной ложки разрыхлителя и щепотка соли, а то кекс будет приторно сладким."

            $left = False
            $right = False
            $count = 1
            $timer_jump = "baking_con"
            show screen countdown
            menu:
                "Прямо как ты.":
                    hide screen countdown
                    jump cute
            label baking_con:
            n "Ах да, глазурь... {w}Не забудь про неё."
            n "Для начала необходимо взбить миксером яйца и сахар."
            n "Параллельно с этим надо растопить сливочное масло в микроволновке."
            n "Затем добавляй масло к яйцам и взбивай всё это повторно, после чего добавляй туда сливочное масло, но помешивай теперь всё медленнее."
            n "Ах да, ты же не забыл про остальные ингредиенты?"
            n "Просей муку, соль, разрыхлитель, соду и перемешай их венчиком."
            n "После этого добавляй получившуюся сухую смесь к остальному жидкому месиву и замешай тесто, только не переусердствуй!"
            n "Мы всё ближе к финалу..."
            n "Оставь тесто на пять минут, чтобы оно стало очень густым."
            n "Теперь ты можешь спокойно выложить его в формочки, заполнив их наполовину."
            n "Отправляй всё это в заранее разогретую духовку чуть меньше, чем на двадцать минут."
            n "Температура должна быть сто восемьдесят градусов с режимом верх–низ, или же низ, как хочешь."
            n "Вуаля, кексы готовы!"
            n "Осталось нанести глазурь и можешь наслаждаться ими."
            n "Желаю удачи повторить рецепт, если надумаешь."
            call ch1_loop from _call_ch1_loop_40



        "{i}С какого блюда ты бы посоветовала начать обучаться кулинарии?{/i}":
            hide screen countdown
            if left:
                show natsuki_room r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki_room r1:
                    xcenter 930
                    easein 1.00 xcenter 630


            n "Знаешь, ты задал довольно интересный вопрос."
            n "Я сама не помню с чего начинала, то ли с макарон, то ли с риса."
            n "Но знаешь, лучше всего начать с бутербродов."
            n "Нет, серьезно!"
            n "По сути, именно они помогут научиться базовым навыкам готовки."
            n "Нарезке ингредиентов, их укладке, терпению в конце концов..."
            n "Сделать действительно потрясный бутерброд не так уж и просто, как может показаться."
            n "Даже если все ингредиенты создают идеальный вкус, сама конструкция может развалиться."
            n "Ты же не хочешь этого, не так ли?"
            n "Поэтому, прежде чем лезть к плите – нужно заняться чем-то более простым."
            n "Когда научишься делать прекрасные бутерброды, переходи к салатам."
            n "Там научишься обращаться и с другими приблудами для готовки."
            n "И только потом плита, [player], только потом..."

            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:
                call ch1_loop from _call_ch1_loop_41



        "{i}Почему ты решила приготовить к фестивалю именно кексы?{/i}":
            hide screen countdown
            if left:
                show natsuki_room r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki_room r1:
                    xcenter 930
                    easein 1.00 xcenter 630


            n "Ха?"
            n "Ну, тут всё дело в символизме."
            n "Клуб не мог полноценно существовать до твоего прихода, а какую именно выпечку я принесла в тот самый день?"
            n "Пра-а-авильно, кексики!"
            n "Они всем очень понравились, в том числе и тебе, поэтому мне захотелось, чтобы они стали главным блюдом на фестивале."
            n "Конечно можно было испечь те же печеньки с предсказаниями, или огромный торт, но согласись, это немного не то…"
            n "Да и к тому же, твоя идея написать на кексах слова мне сильно понравилась."
            n "Было бы интересно понаблюдать за всякими зеваками, которые выбирали кекс, исходя из слова."
            n "Конечно, с фестивалем не сложилось, но по крайней мере эти кексы мы всё–таки испекли."
            n "Лично для меня процесс готовки всяких вкусняшек имеет не меньшее значение, чем дегустация."
            n "Я же не для себя в конце концов готовила, а для всей школы."
            n "Пришлось выложиться по полной, чтобы выставить наш клуб в хорошем свете."
            n "Чувствуется ответственность, знаешь ли..."


            call ch1_loop from _call_ch1_loop_42


        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show natsuki_room r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki_room r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_43

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show natsuki_room r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki_room r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_44

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show natsuki_room r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki_room r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_45
