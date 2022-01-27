init python: 
    react_names = [
        "yuri", "юри", 
        "monica", "monika", "моника",
        "sayori", "сайори", "саёри", "саери",
        "natsuki", "нацуки", "натсуки", "насуки"
    ]
    react_n = [ "natsuki", "нацуки", "натсуки", "насуки"]
    react_s = ["sayori", "сайори", "саёри", "саери"]
    react_m = ["monica", "monika", "моника"]

label set_name_input: 
    $ player = renpy.input("Как тебя зовут?", length=32)
    $ player = player.strip()
    if player.lower() in react_n:
        $ input_count_n += 1
    elif player.lower() == "yuri" or player.lower() == "юри":
        $ input_count_y += 1
    elif player.lower() in react_m:
        $ input_count_m += 1
    elif player.lower() in react_s:
        $ input_count_s += 1
    $ input_count += 1
    return
label set_name_joker:
    $ print(input_count_s + input_count_m + input_count_y == 1 and input_count_n == 2)
    $ print(input_count_s + input_count_m + input_count_y == 2 and input_count_n == 1)
    if (input_count_s + input_count_m + input_count_y == 1 and input_count_n == 2) or (input_count_s + input_count_m + input_count_y == 2 and input_count_n == 1):
        n r1b "Ты мне надоел..."
        n r1d "Отныне я буду величать тебе Клоуном, хи-хи-хи."
        n r1c "Сам напросился, а я ведь предупреждала."
        n r1d "Если будешь хорошо себя вести, то так и быть, дам возможность поменять имя ещё раз."
        n "Ну или останешься Клоуном навсегда."
        n r1c "Хех." 
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
    show natsuki r1b    
    call set_name_input 
    $ print(player.lower())
    if player.lower() in react_n:
        # НАЦ НАЗЫВАЕТ КЛОУНОМ
        call set_name_joker
        if input_count_n == 1:
            n r1e "Эй, это же моё имя!"
            n "Почему ты называешь себя именно так?"
            n r1b "Желание поиздеваться надо мной такой глупой шуткой?"
            n "Я уверена почти на сто процентов, что твоё имя совершенно другое."
            n r1a "Назови себя как-нибудь иначе."
            jump set_name

        if input_count_n == 2:
            n r1b "Так, мы уже говорили об этом..."
            n r1j "Я. {w}Не. {w}Верю тебе!"
            n r1l "Хватит валять дурака, ставь другое имя."
            show natsuki r1k
            jump set_name

        # НАЦ НАЗЫВАЕТ ДУРАШКОЙ  
        if input_count_s + input_count_m + input_count_y == 0 and input_count_n > 2:
            n r1b "Достал ты меня..."
            n r1e"Я сама выберу тебе имя."
            n r1d "Как насчёт Дурашки?"
            n r1o "Мне оно очень сильно нравится, да и как раз подходит тебе."
            n r1c "..."
            n r1d "Если ты перестанешь быть клоуном – так и быть, я дам тебе возможность поменять своё имя на другое, ну а пока что ходи с этим."
            $ input_count_n = 0
            $ input_count_m = 0
            $ input_count_y = 0
            $ input_count_s = 0
            $ player = "Дурашка"
            n "[player]...."
            show natsuki r1c
            call ch1_loop 

    elif player.lower() in react_names:
        # НАЦ НАЗЫВАЕТ КЛОУНОМ
        call set_name_joker
        # 3 РАЗА ОДНА ИЗ ДОКИЧЕЙ
        if input_count_n == 0:
            # НАЦ НАЗЫВАЕТ ГЛУПЫШКОЙ
            if input_count_s + input_count_m + input_count_y > 2:
                n r1e "Всё, игры закончились."
                n r1g "Отныне ты будешь... {w}{i}Глупышкой!{/i}"
                n r1c "Хи-хи-хи..."
                n r1d "Так и быть, я дам тебе шанс исправиться, но только после того, как ты начнёшь себя нормально вести."
                n r1c "Думаю, мы договорились."
                $ input_count_n = 0
                $ input_count_m = 0
                $ input_count_y = 0
                $ input_count_s = 0
                $ player = "Глупышка"
                n "[player]...."
                call ch1_loop 

        # САЙОРИ
        if player.lower() in react_s:       
            if input_count_s == 1:
                n r1e "Плохая шутка, переделывай."
                n "Ты серьёзно думаешь, что я поведусь на это?"
                n "Я знаю, что ты играл в эту игру и знаешь о том, как всех нас зовут."
                n r1b "Да и будь ты Сайори..."
                n r1e "Нет, Сайори не умела так шутить."
                n r1b "Лучше поменяй своё имя, ладно?"   
                jump set_name
            if input_count_s == 2:
                n r1e "Ты дурак?"
                n r1b "Меняй имя на другое, иначе я сделаю то, что тебе не понравится..."
                jump set_name
        # ЮРИ
        if player.lower() == "yuri" or player.lower() == "юри":
            if input_count_y == 1:
                n "..."
                n r1e "Хмф... {w}Я не куплюсь на такое."
                n "Ты не можешь быть Юри, её больше нет."
                n "Пожалуйста, скажи своё {i}настоящее{/i} имя, ну или хотя бы кличку придумай."
                n "Я понимаю, что тебе скорее всего просто хотелось посмотреть на мою реакцию, но сейчас совсем не до шуток."
                n r1b "Давай, меняй своё имя."    
                jump set_name
            if input_count_y == 2:
                n r1d "С первого раза не доходит?"
                n "Повторяю для дурашек – пиши другое имя."
                n "И да, знаешь, Юри бы на твоём месте уже давно сменила своё имя."
                n r1b "Всё-таки она была такой стеснительной..."
                n r1f "Так, короче, даю тебе последний раз исправится, иначе... {w}Я что-нибудь придумаю."
                show natsuki r1b
                jump set_name
        # МОНИКА
        if player.lower() in react_m:
            if input_count_m == 1:
                n r1a "Ха?"
                n r1e "Да ну, не может быть, Моника похоронена в коде игры."
                n "Забавно, что это произошло из-за её же ошибки."
                n r1b "..."
                n r1e "Какой тебе смысл брать её имя?"
                n "Я уверена, что тебя не зовут Моника."
                n "Поменяй его, хорошо?"
                show natsuki r1b     
                jump set_name
            if input_count_m == 2:
                n r1e "Повторяю для особо одарённых - поменяй имя."
                n "Сейчас у меня нет желания даже вспоминать о нём."
                n "Давай, смелее, пока я добрая." 
                show natsuki r1b
                jump set_name                
    else:
        if input_count_s + input_count_m + input_count_y == 0 and input_count_n > 0:
            n r1e "Вот так бы и сразу."
            n "Я понимаю, что моё имя, возможно, тебе понравилось, но это было бы очень тупо."
            n r1d "Представь себе, как я называю тебя Нацуки."
            n r1b "Глупость какая-та..."
        elif input_count_n == 0 and input_count_s + input_count_m + input_count_y > 0:
            n r1e "Молодец, что прекратил это."
            n "Серьёзно, подобные приколы меня очень сильно бесят."
            n r1d "В любом случае, [player], теперь у тебя есть нормальное имя."
            n r1e "[player]..."
        elif input_count_n > 0 and input_count_s + input_count_m + input_count_y > 0:
            n r1e "Неужели этот дурацкий цирк прекратился?"
            n "Я понимаю, что скорее всего ты делал это от скуки, но пожалуйста, не беси меня так больше."
            n r1b "Просто... {w}Это как-то странно, что я буду общаться с тобой, применяя одно из имён своих подруг."
            n r1e "Конечно, их сейчас нет в живых, но..."
            n "В общем, закроем тему, [player], я не хочу сейчас говорить об этом."
            show natsuki r1b 
        else:
            n r1d "Хорошее имя."
            n r1i "Правда не знаю, настоящее ли оно или же это просто псевдоним."
            n r1e "[player]..."
        show natsuki r1b
        call ch1_loop
