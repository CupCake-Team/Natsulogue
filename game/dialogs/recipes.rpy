label dia_recipes:
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
        "{i}Как испечь вкусные кексы?{/i}":
            #hide screen countdown
            $side_return()

            n r1f "Ого, так тебя заинтересовала лучшая часть моей выпечки?"
            n r1d "Говорю сразу, никакого секретного ингредиента в них нет, просто нужно уметь их печь."
            n "Благо я помню принцип их приготовления, так что вот тебе рецептик."
            n r1c "Записывай..."
            n r1d "Для начала, само собой, нужно иметь доступ к плите и всякой кухонной утвари."
            n "Затем достань из холодильника два яйца, ровно сто грамм сливочного масла и около ста двадцати грамм растительного масла."
            n "Далее поищи сахар, его нам понадобится сто восемьдесят грамм, но если его нет, можно взять и пудру."
            n "Естественно, без муки никаких кексов не выйдет, поэтому бери её сто двадцать грамм."
            n "В итоге у нас остаются половина чайной ложки соды, чуть меньше половины чайной ложки разрыхлителя и щепотка соли, а то кекс будет приторно сладким."
            show natsuki r1c

            $left = False
            $right = False
            $count = 1
            $timer_jump = "baking_con"
            #show screen countdown
            menu:
                "Прямо как ты.":
                    #hide screen countdown
                    jump cute
            label baking_con:
            n r1e "Ах да, глазурь... {w}Не забудь про неё."
            n r1d "Для начала необходимо взбить миксером яйца и сахар."
            n "Параллельно с этим надо растопить сливочное масло в микроволновке."
            n "Затем добавляй масло к яйцам и взбивай всё это повторно, после чего добавляй туда сливочное масло, но помешивай теперь всё медленнее."
            n r1e "Ах да, ты же не забыл про остальные ингредиенты?"
            n r1d "Просей муку, соль, разрыхлитель, соду и перемешай их венчиком."
            n "После этого добавляй получившуюся сухую смесь к остальному жидкому месиву и замешай тесто, только не переусердствуй!"
            n r1f "Мы всё ближе к финалу..."
            n r1d "Оставь тесто на пять минут, чтобы оно стало очень густым."
            n "Теперь ты можешь спокойно выложить его в формочки, заполнив их наполовину."
            n "Отправляй всё это в заранее разогретую духовку чуть меньше, чем на двадцать минут."
            n "Температура должна быть сто восемьдесят градусов с режимом верх–низ, или же низ, как хочешь."
            n r1g "Вуаля, кексы готовы!"
            n r1d "Осталось нанести глазурь и можешь наслаждаться ими."
            n r1c "Желаю удачи повторить рецепт, если надумаешь."
            call ch1_loop



        "{i}С какого блюда ты бы посоветовала начать обучаться кулинарии?{/i}":
            #hide screen countdown
            $side_return()


            n r1e "Знаешь, ты задал довольно интересный вопрос."
            n r1a "Я сама не помню с чего начинала, то ли с макарон, то ли с риса."
            n r1c "Но знаешь, лучше всего начать с бутербродов."
            n r1g "Нет, серьезно!"
            n r1d "По сути, именно они помогут научиться базовым навыкам готовки."
            n r1e "Нарезке ингредиентов, их укладке, терпению в конце концов..."
            n r1f "Сделать действительно потрясный бутерброд не так уж и просто, как может показаться."
            n r1d "Даже если все ингредиенты создают идеальный вкус, сама конструкция может развалиться."
            n "Ты же не хочешь этого, не так ли?"
            n r1c "Поэтому, прежде чем лезть к плите – нужно заняться чем-то более простым."
            n r1d "Когда научишься делать прекрасные бутерброды, переходи к салатам."
            n "Там научишься обращаться и с другими приблудами для готовки."
            n r1c "И только потом плита, [player], только потом..."

            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                $input_count = 0
                jump set_name
            else:
                call ch1_loop



        "{i}Почему ты решила приготовить к фестивалю именно кексы?{/i}":
            #hide screen countdown
            $side_return()


            n r1e "Ха?"
            n r1d "Ну, тут всё дело в символизме."
            n r1f "Клуб не мог полноценно существовать до твоего прихода, а какую именно выпечку я принесла в тот самый день?"
            n r1o "Пра-а-авильно, кексики!"
            n r1g "Они всем очень понравились, в том числе и тебе, поэтому мне захотелось, чтобы они стали главным блюдом на фестивале."
            n r1d "Конечно можно было испечь те же печеньки с предсказаниями, или огромный торт, но согласись, это немного не то…"
            n r1e "Да и к тому же, твоя идея написать на кексах слова мне сильно понравилась."
            n r1f "Было бы интересно понаблюдать за всякими зеваками, которые выбирали кекс, исходя из слова."
            n r1d "Конечно, с фестивалем не сложилось, но по крайней мере эти кексы мы всё–таки испекли."
            n "Лично для меня процесс готовки всяких вкусняшек имеет не меньшее значение, чем дегустация."
            n "Я же не для себя в конце концов готовила, а для всей школы."
            n r1f "Пришлось выложиться по полной, чтобы выставить наш клуб в хорошем свете."
            n r1c "Чувствуется ответственность, знаешь ли..."

            call ch1_loop

        "{i}[ans]{/i}":
            $side_return()
            call ch1_loop
