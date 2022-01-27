label set_name_input: 
    $ player = renpy.input("Как тебя зовут?", length=32)
    $ player = player.strip()
    if player.lower() == "natsuki" or player.lower() == "нацуки":
        $ input_count_n += 1
    elif player.lower() == "yuri" or player.lower() == "юри":
        $ input_count_y += 1
    elif player.lower() == "monika" or player.lower() == "моника":
        $ input_count_m += 1
    elif player.lower() == "sayori" or player.lower() == "сайори":
        $ input_count_s += 1
    $ input_count += 1
    return
label set_name_joker:
    if (input_count_s + input_count_m + input_count_y == 1 and input_count_n == 2) or (input_count_s + input_count_m + input_count_y == 2 and input_count_n == 1):
                n "Ты мне надоел..."
                n "Отныне я буду величать тебе Клоуном, хи-хи-хи."
                n "Сам напросился, а я ведь предупреждала."
                n "Если будешь хорошо себя вести, то так и быть, дам возможность поменять имя ещё раз."
                n "Ну или останешься Клоуном навсегда."
                n "Хех." 
                $ input_count_n = 0
                $ input_count_y = 0
                $ input_count_m = 0
                $ input_count_s = 0
                $ player = "Клоун"
                n "[player]...."
                show natsuki r1b
                call ch1_loop
    else:
        return 
label set_name:
    if input_count == 0:
        n r1e "Ой, а почему твоё имя заглюченное?"
        n r1a "Хм... {w}Походу оно слетело, когда игру начало воротить от глюков."
        n r1e "Давай–ка мы это исправим, не обращаться же к тебе вот так..."
        $ input_count_n = 0
        $ input_count_y = 0
        $ input_count_m = 0
        $ input_count_s = 0
    call set_name_input 
    $ print(player.lower())
    if player.lower() == "":
        $ pass
    if player.lower() == "natsuki" or player.lower() == "нацуки":
        # НАЦ НАЗЫВАЕТ КЛОУНОМ
        call set_name_joker
        if input_count_n == 1:
            n "Эй, это же моё имя!"
            n "Почему ты называешь себя именно так?"
            n "Желание поиздеваться надо мной глупой шуткой?"
            n "Я уверена почти на сто процентов, что твоё имя совершенно другое."
            n "Назови себя как-нибудь иначе."
            jump set_name

        if input_count_n == 2:
            n "Так, мы уже говорили об этом..."
            n "Я. {w}Не. {w}Верю тебе!"
            n "Хватит валять дурака, ставь другое имя."
            jump set_name

        # НАЦ НАЗЫВАЕТ ДУРАШКОЙ  
        if input_count_s + input_count_m + input_count_y == 0 and input_count_n > 2:
            n "Достал ты меня..."
            n "Я сама выберу тебе имя."
            n "Как насчёт Дурашки?"
            n "Мне оно очень сильно нравится, да и как раз подходит тебе."
            n "..."
            n "Если ты перестанешь быть клоуном - так и быть, ты сможешь поменять своё имя на другое, ну а пока ходи с этим."
            $ input_count_n = 0
            $ player = "Дурашка"
            n "[player]...."
            show natsuki r1b
            call ch1_loop 

    elif player.lower() in react_names:
        # НАЦ НАЗЫВАЕТ КЛОУНОМ
        call set_name_joker
        # 3 РАЗА ОДНА ИЗ ДОКИЧЕЙ
        if input_count_n == 0:
            # НАЦ НАЗЫВАЕТ ГЛУПЫШКОЙ
            if input_count_s + input_count_m + input_count_y > 2:
                n "Всё, игры закончились."
                n "Отныне ты будешь... {w}{i}Глупышкой!{/i}"
                n "Хи-хи-хи..."
                n "Так и быть, я дам тебе шанс исправиться, но только после того, как ты станешь нормально себя вести."
                n "Думаю, мы договорились."
                $ input_count_m = 0
                $ input_count_s = 0
                $ input_count_y = 0
                $ player = "Глупышка"
                n "[player]...."
                show natsuki r1b
                call ch1_loop 

            # САЙОРИ
            if player.lower() == "sayori" or player.lower() == "сайори":       
                if input_count_s == 1:
                    n "Плохая шутка, переделывай."
                    n "Ты серьёзно думаешь, что я поведусь на это?"
                    n "Я знаю, что ты играл в эту игру и знаешь о том, как всех нас зовут."
                    n "Да и будь ты Сайори..."
                    n "Нет, Сайори не умела так шутить."
                    n "Лучше поменяй своё имя, ладно?"
                    $ input_count += 1    
                    jump set_name
                if input_count_s == 2:
                    n "Ты дурак?"
                    n "Меняй имя на другое, иначе я сделаю то, что тебе не понравится..."
                    $ input_count += 1
                    jump set_name
            # ЮРИ
            if player.lower() == "yuri" or player.lower() == "юри":
                if input_count_y == 1:
                    n "..."
                    n "Хмф... {w}Я не куплюсь на такое."
                    n "Ты не можешь быть Юри, её больше нет."
                    n "Пожалуйста, скажи своё {i}настоящее{/i} имя, ну или хотя бы кличку придумай."
                    n "Я понимаю, что тебе скорее всего просто хотелось посмотреть на мою реакцию, но сейчас совсем не до шуток."
                    n "Давай, меняй своё имя."
                    $ input_count += 1    
                    jump set_name
                if input_count_y == 2:
                    n "С первого раза не доходит?"
                    n "Повторяю для дурашек - пиши другое имя."
                    n "И да, знаешь, Юри бы на твоём месте уже давно сменила своё имя."
                    n "Всё-таки она была такой стеснительной..."
                    n "Так, короче, даю тебе последний раз исправиться, иначе... {w}Я что-нибудь придумаю."
                    $ input_count += 1
                    jump set_name
            # МОНИКА
            if player.lower() == "monika" or player.lower() == "моника":
                if input_count_m == 1:
                    n "Ха?"
                    n "Да ну, не может быть, Моника похоронена в коде игры."
                    n "Забавно, что это произошло из-за её же ошибки."
                    n "..."
                    n "Какой тебе смысл брать её имя?"
                    n "Я уверена, что тебя не зовут Моника."
                    n "Поменяй его, хорошо?"
                    $ input_count += 1    
                    jump set_name
                if input_count_m == 2:
                    n "Повторяю для особо одарённых - поменяй имя."
                    n "Сейчас у меня нет желания даже вспоминать о нём."
                    n "Давай, смелее, пока я добрая." 
                    $ input_count += 1
                    jump set_name                
    else:
        if input_count_s + input_count_m + input_count_y == 0 and input_count_n > 0:
            n "Вот так бы и сразу."
            n "Я понимаю, что моё имя, возможно, тебе понравилось, но это было бы очень тупо."
            n "Представь себе, как я называю тебя Нацуки."
            n "Глупость какая-та..."
        elif input_count_n == 0 and input_count_s + input_count_m + input_count_y > 0:
            n "Молодец, что прекратил это."
            n "Серьёзно, подобные приколы меня очень сильно бесят."
            n "В любом случае, [player], теперь у тебя есть нормальное имя."
            n "[player]..."
        elif input_count_n > 0 and input_count_s + input_count_m + input_count_y > 0:
            n "Неужели этот дурацкий цирк прекратился?"
            n "Я понимаю, что скорее всего ты делал это от скуки, но пожалуйста, не делай так больше."
            n "Просто... {w}Это как-то странно, что я буду общаться с тобой, применяя имя своих подруг."
            n "Конечно, их сейчас нет в живых, но..."
            n "В общем, закроем тему, [player], я не хочу сейчас говорить об этом."
        else:
            n r1d "Хорошее имя."
            n r1i "Правда не знаю, настоящее ли оно или же это просто псевдоним."
            n r1e "[player]..."
        show natsuki r1b
        call ch1_loop