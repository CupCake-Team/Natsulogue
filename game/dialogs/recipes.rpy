label dia_recipes:
    $set_side()

    $dia_hide()

    $ans = random_ans()

    menu:
        "{i}Как испечь вкусные кексы?{/i}":
            hide screen countdown
            $side_return()

            if "Как испечь вкусные кексы?" in persistent.repeats and persistent.repeats["Как испечь вкусные кексы?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "Ты что, никуда не записал мой рецепт?"
                    n "..."
                    n "Ладно, повторяю его, но потом не переспрашивай меня об этих кексах."
                    n "Достаёшь из холодильника два яйца, сто грамм сливочного масла, сто двадцать грамм масла."
                    n "Растительного естественно..."
                    n "Далее – сахар или пудра, в зависимости от того, что у тебя есть, сто двадцать грамм."
                    n "Ну и ещё необходимы щепотка соли, половина чайной ложки соды,чуть меньше половины чайной ложки разрыхлителя и, конечно же, глазурь, по своему секретному рецепту."
                    n "Что же, теперь начинаем само приготовление."
                    n "Сперва нужно растопить сливочное масло в микроволновке."
                    n "Пока оно там мучается – взбей миксером яйца и сахар."
                    n "Когда поймёшь, что достаточно всё взбил, то добавляй туда растительное масло и взбивай повторно."
                    n "Затем, когда сливочное масло будет готово, засыпай его в эту семь и помешивай, но ме-е-едленнее."
                    n "Далее, тебе понадобится просеять муку вместе с разрыхилетелем и содой, перемешав их вечником, но это надо делать отдельно."
                    n "Затем добавляешь всю эту смесь во взбитые яйца, масло и так далее, после чего начинаешь замешивать тесто."
                    n "Перед тем как выкладывать его в формочки, оставь его минут на пять, чтобы оно загустело."
                    n "Тем временем разогрей духовку, её температура должна составлять сто восемьдесят градусов либо с режимом верх-низ, или просто низ."
                    n "Когда тесто станет густым – выложи его в формочки и поставь в духовку."
                    n "По времени кексы должны там находится чуть меньше, чем двадцать минут."
                    n "Затем достаёшь из духовки формочки, наносишь глазурь, все дела, и готово."
                    n "..."
                    n "Надеюсь ты всё записал?"
                    n "Я два раза повторять не буду!"
                    n "Жду отчёта о проделанной работе, хи-хи-хи..."

                if cur_relation == "Positive":
                    n "Ты забыл записать мой рецепт?"
                    n "..."
                    n "Ничего страшного!"
                    n "Я напишу его в отдельном файле, который помещу в папку с игрой."
                    n "Надеюсь это поможет тебе в твоих кулинарных похождениях, хех."
                    n "Или ты просто не понял рецепт глазури?"
                    n "Всё-таки он мой собственный, хи-хи-хи..."
                    n "..."
                    n "Вот как повторишь рецепт кексов, будет тебе рецепт глазури."
                    n "Договорились?"

                    python:
                        res = open(config.gamedir+'//Рецептик.txt', 'w')
                        res.write("Тебе понадобятся два яйца, сто двадцать грамм растительного масла и сто грамм сливочного масла.\n"+
                        "Затем раздобудь сахар или же пудру, ровно сто восемьдесят грамм.\n"+
                        "Далее – мука, сто двадцать грамм.\n"+
                        "Осталось только взять щепотку соли, половину чайной ложки соды и чуть меньше половиной чайной ложки разрыхлителя.\n"+
                        "Положи сливочное масло в микроволновку, чтобы оно растопилось.\n"+
                        "Пока оно шкварится, взбей миксером яйца и сахар, ну или пудру, смотря что ты выбрал.\n"+
                        "Затем добавляй растительное масло во всё это месиво, после чего взбей её снова.\n"+
                        "Когда сливочное масло достаточно расплавится – отправляй его прямиком к остальным ингредиентам, только помешивай уже не так быстро.\n"+
                        "Как закончишь - смешай в отдельной посуде муку, соль, разрыхлитель и соду. Затем смешай это с уже готовой смесью.\n"+
                        "После этого оставь тесто на пять минут, чтобы оно успело загустеть, и выложи его в формочки.\n"+
                        "Только заполни их наполовину, кексы еще поднимутся в духовке.\n"+
                        "Разогрей её до 180 градусов, можешь использовать два режима: верх-низ или же просто низ, выбирай по желанию.\n"+
                        "Чуть меньше, чем 20 минут и кексики готовы!\n"+
                        "Удачи!")
                        res.close()

                if cur_relation == "Negative":
                    n "Ты не получишь рецепт."
                    n "Ни за что!"
                    n "Какой вообще смысл тебе интересоваться чем-то подобным, если ты так плохо со мной обращаешься?"
                    n "Кушать захотелось?"
                    n "Ну ты и клоун конечно..."
                    n "Обойдёшься без моих кексов!"

            else:
                if cur_relation == "Neutral":
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
                    show screen countdown
                    menu:
                        "Прямо как ты.":
                            hide screen countdown
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
                    $persistent.repeats["Как испечь вкусные кексы?"] = "Neutral"

                if cur_relation == "Positive":
                    n "На самом деле это не так уж и сложно, если не делать их какими-нибудь замудрёнными."
                    n "У меня есть один простой рецепт кексов, который даже ты можешь повторить."
                    n "Надеюсь ты не спалишь плиту, пока будешь готовить, хи-хи-хи..."
                    n "Ладненько, бери блокнот, ручку и записывай."
                    n "Тебе понадобятся два яйца, сто двадцать грамм растительного масла и сто грамм сливочного масла."
                    n "Надеюсь, всё это добро найдётся у тебя на кухне."
                    n "Затем раздобудь сахар или же пудру, ровно сто восемьдесят грамм."
                    n "Осталось только взять щепотку соли, половину чайной ложки соды и чуть меньше половиной чайной ложки разрыхлителя."
                    n "Ах да, ещё... {w}Мука, понадобится сто двадцать грамм."
                    n "Думаю, стоит начать со сливочного масла."
                    n "Положи его в микроволновку, чтобы оно растопилось."
                    n "Пока масло шкварится – взбей миксером яйца и сахар, ну или пудру, смотря что ты выбрал."
                    n "Затем добавляй растительное масло во всё это месиво, после чего взбей её снова."
                    n "Когда уже сливочное масло достаточно расплавится – отправляй его прямиком к остальным ингредиентам, только помешивай уже не так быстро."
                    n "Когда закончишь с этим, тебе придётся создать отдельную смесь из муки, соли, разрыхлителя и соды."
                    n "Перемешай их венчиком и добавь их в жидкую консистенцию."
                    n "После этого оставь тесто на пять минут, чтобы оно успело загустеть, и выложи его в формочки."
                    n "Только заполни их наполовину, а то кексы получатся слишком пышными."
                    n "Что же, могу поздравить, настало время духовки!"
                    n "Ты должен разогреть её на сто восемьдесят градусов, у тебя на выбор два режима: верх-низ или же просто низ, выбирай по желанию."
                    n "Отправляй формочки жариться на период чуть меньше чем двадцать минут, и-и-и..."
                    n "Кексы готовы!"
                    n "Ну, почти..."
                    n "Осталось только нанести глазурь и выпечку можно подавать к столу."
                    n "Вот такой простенький рецепт."
                    n "Надеюсь, у тебя получится испечь прекрасные кексики, [player]!"
                    $persistent.repeats["Как испечь вкусные кексы?"] = "Positive"

                if cur_relation == "Negative":
                    n "Дурак..."
                    n "Ты недостоин этой великой тайны!"
                    n "А теперь попрошу выметаться отсюда."
                    $persistent.repeats["Как испечь вкусные кексы?"] = "Negative"

            $relationcount(1,1,-1)
            call ch1_loop



        "{i}С какого блюда ты бы посоветовала начать обучаться кулинарии?{/i}":
            hide screen countdown
            $side_return()

            if "С какого блюда ты бы посоветовала начать обучаться кулинарии?" in persistent.repeats and persistent.repeats["С какого блюда ты бы посоветовала начать обучаться кулинарии?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "С бутербродов."
                    n "Слушай меня внимательнее, пожалуйста..."
                    n "Мне неприятно когда меня игнорируют."
                    $relationcount(0,-2,0)

                if cur_relation == "Positive":
                    n "Бутерброды, коктейли, салаты."
                    n "Не заставляй меня превращаться в злюку, [player]."
                    n "Когда-нибудь мне надоест повторяться."
                    $relationcount(-2,0,0)

                if cur_relation == "Negative":
                    n "Блин, ты совсем глупый или прикидываешься?"
                    n "Даже комментировать это не буду..."

            else:
                if cur_relation == "Neutral":
                    n "Знаешь, ты задал довольно интересный вопрос."
                    n "Я сама не помню с чего начинала, то ли с макарон, то ли с риса."
                    n "Но знаешь, лучше всего начать с бутербродов."
                    n "Нет, серьёзно!"
                    n "По сути, именно они помогут научиться базовым навыкам готовки."
                    n "Нарезке ингредиентов, их укладке, терпению в конце концов..."
                    n "Сделать действительно потрясный бутерброд не так уж и просто, как может показаться."
                    n "Даже если все ингредиенты создают идеальный вкус, сама конструкция может развалиться."
                    n "Ты же не хочешь этого, не так ли?"
                    n "Поэтому, прежде чем лезть к плите – нужно заняться чем-то более простым."
                    n "Когда научишься делать прекрасные бутерброды, переходи к салатам."
                    n "Там научишься обращаться и с другими приблудами для готовки."
                    n "И только потом плита, [player], только потом..."
                    $persistent.repeats["С какого блюда ты бы посоветовала начать обучаться кулинарии?"] = "Neutral"

                if cur_relation == "Positive":
                    n "Хм... {w}Даже не знаю чего бы тебе конкретного посоветовать."
                    n "Наверное какие-нибудь салаты, простенькие коктейли, бутерброды..."
                    n "В общем теми блюдами, где во время их приготовления контакта с плитой либо нет, либо он минимален."
                    n "Да, возможно это покажется чем-то слишком простым, но ведь начинать нужно всегда с малого."
                    n "Просто лично мне кажется, что сперва лучше попрактиковаться в таких базовых вещах, а уже потом начать практиковать плиту."
                    n "Хороший салат тоже не просто сделать, знаешь ли."
                    n "Как и бутерброд..."
                    n "Положить колбасу на хлебушек может каждый, а ты попробуй что-нибудь более сложное."
                    n "Рецептов тех же бутербродов тысячи, я не преувеличиваю."
                    n "Или те же коктейли, там столько комбинаций, и ведь их не так уж и сложно сделать, было бы желание."
                    n "Я надеюсь, что это поможет тебе в твоих кулинарных начинаниях."
                    n "На этом кулинарный совет на сегодня окончен."
                    $persistent.repeats["С какого блюда ты бы посоветовала начать обучаться кулинарии?"] = "Positive"

                if cur_relation == "Negative":
                    n "Тебе – ни с чего, даже не думай о том, чтобы начать готовить."
                    n "Боюсь представить, какими будут твои блюда..."
                    n "Клоунские с дурной приправой?"
                    n "Или может быть жаренная идиотина?"
                    n "Ты серьёзно думаешь о том, что я буду помогать тебе?"
                    n "Наивный... {w}Даже не надейся на это."
                    $persistent.repeats["С какого блюда ты бы посоветовала начать обучаться кулинарии?"] = "Negative"


            $relationcount(1,1,-1)
            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                $input_count = 0
                jump set_name
            else:
                call ch1_loop



        "{i}Почему ты решила приготовить к фестивалю именно кексы?{/i}":
            hide screen countdown
            $side_return()

            if "Почему ты решила приготовить к фестивалю именно кексы?" in persistent.repeats and persistent.repeats["Почему ты решила приготовить к фестивалю именно кексы?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "Догадайся сам, если не умеешь внимательно слушать."
                    n "Наверное потому что твоё вступление произошло благодаря кексам, или ты этого так и не понял?"
                    n "Странный ты..."
                    $relationcount(0,-2,0)

                if cur_relation == "Positive":
                    n "Я ведь уже сказала..."
                    n "Благодаря кексам клуб стал таким, каким он был последнюю неделю своего существования."
                    n "Эта выпечка смогла объединить всех участников клуба, пусть и ненадолго..."
                    n "Просто тот же торт большой, например, это как-то слишком банально, я считаю."
                    n "Да и притащить его в школу было бы куда сложнее, чем кексики."
                    n "Поэтому мой выбор пал на них."
                    n "В конце концов, их было действительно весело готовить, жалко что мы не смогли насладиться ими."

                if cur_relation == "Negative":
                    n "Хах..."
                    n "Ты тот ещё идиот, оказывается, раз уж с первого раза не дошло."

            else:
                if cur_relation == "Neutral":
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
                    $persistent.repeats["Почему ты решила приготовить к фестивалю именно кексы?"] = "Neutral"

                if cur_relation == "Positive":
                    n "Ну, тут сыграло роль сразу несколько причин."
                    n "В первую очередь, потому что благодаря кексам ты и вступил к нам в клуб, уж я об этом тогда позаботилась."
                    n "Да и в целом, если так подумать, больше всего девочкам нравились именно кексы."
                    n "Поэтому я и решила, что эта выпечка идеально подойдёт к фестивалю."
                    n "Конечно мы их не успели съесть, но по крайней мере мы их приготовили."
                    n "Они ведь очень даже ничего вышли, красивые, пышные..."
                    n "Так ещё и со словами разными, это делало каждый кекс уникальным в чём-то."
                    n "Жалко конечно что сейчас я не могу готовить..."
                    n "Без плиты и всякой кухонной утвари в этой комнатушке скучновато, но думаю мы найдём способ как разместить здесь всё это."
                    n "Ведь так, [player]?"
                    $persistent.repeats["Почему ты решила приготовить к фестивалю именно кексы?"] = "Positive"

                if cur_relation == "Negative":
                    n "Потому что символизм, дурак."
                    n "Это же так очевидно..."
                    n "Или тебе ещё нужно всё в подробностях разложить и на блюдечке принести?"
                    n "Ты такие глупые вопросы задаёшь, я просто в шоке..."
                    n "Может быть тебе ещё спросить у меня, какого цвета мои волосы?"
                    n "Придурок!"
                    $persistent.repeats["Почему ты решила приготовить к фестивалю именно кексы?"] = "Negative"
            $relationcount(1,1,-1)
            call ch1_loop

        "{i}[ans]{/i}":
            $side_return()
            call ch1_loop
