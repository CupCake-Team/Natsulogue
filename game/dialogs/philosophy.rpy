label dia_philosophy:
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
        "{i}В чём смысл жизни?{/i}":
            hide screen countdown
            $side_return()

            n r1e "Ты серьёзно думаешь, что я скажу что-то дельное?"
            n "Даже всякие философы не могли дать конкретный ответ, который бы всех устроил."
            n r1a "К тому же мне не понятно, ты хочешь узнать про мой смысл жизни или ответ на этот вопрос в целом?"
            n r1e "Если говорить за себя, то я считала, что главное в жизни – найти своё предназначение."
            n "У меня было несколько вариантов, но теперь в этом нет никакого смысла."
            n r1b "Судя по всему, кроме меня в этом мире никого не осталось..."
            n "Ладно, не будем сейчас об этом."
            n r1e "Как мне кажется, поиском смысла жизни человек должен заниматься сам."
            n "Вместо того, чтобы целенаправленно или шутки ради задавать этот вопрос всем подряд, нужно покопаться в себе."
            n "Да, возможно всплывут какие–то неприятные воспоминания..."
            n r1d "Но нужно быть сильным человеком и отгонять плохие мысли прочь."
            n "В конце концов, без усилий не прийти к успеху."
            n r1f "Хах... {w}Не думала, что могу говорить на эту тему с таким серьёзным выражением лица."
            n r1g "Ладно, если ты задавал этот вопрос на полном серьёзе, то думаю, ты обязательно справишься с этим."
            n "Верь в себя, [player], и никогда не сдавайся!"
            n "Если вдруг тебе будет грустно на душе – можешь заглянуть ко мне, поговорим."
            n r1e "Не забывай об этом, ладно?"
            n r1n "И не подумай о чём-то таком, дурашка..."
            show natsuki r1c
            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:
                call ch1_loop



        "{i}Веришь ли ты в любовь с первого взгляда?{/i}":
            hide screen countdown
            $side_return()



            n r1e "Если честно – нет."
            n "То что тебе понравился человек, которого ты только что увидел – это лишь реакция на то, что он неплохо выглядит."
            n "Мы же не знаем его внутренний мир, а видим лишь внешнюю оболочку."
            n "Как мне кажется, любовь с первого взгляда – это мимолётная симпатия."
            n r1c "Само собой, если человек окажется хорошим, то она перерастёт в настоящую любовь."
            n r1b "В противном случае через какое–то время чувства пройдут, а этого человека, возможно, ты даже забудешь."
            n "Да и если говорить про наше время..."
            n r1e "Раз уж твой мир практически такой же, как и мой, то у вас многие знакомятся через Интернет."
            n "Сайтов знакомств и подобных приложений очень много, на любой вкус..."
            n "Но общаясь через них с кем–то, нельзя быть уверенным в том, что все люди показывают там себя настоящих."
            n r1b "Многие создают себе образы, личности, которые могут быть очень далеки от реальности..."
            n "Да и передавать текстом свои чувства не так уж и просто..."
            n r1e "Люди же не видят друг друга при общении, те же эмоции, жесты, даже голос."
            n "А ведь именно благодаря этому можно понять человека гораздо лучше."
            n "Всё-таки мало кто сейчас знакомится на улице..."
            n r1a "На таких сейчас смотрят, как на сумасшедших."
            n r1c "Неужели такими темпами мы придём к тому, что совсем перестанем общаться вживую?"
            n "Хотя... {w}У меня самой нет выбора, кроме как общаться с тобой."
            n r1c "А вот ты вполне бы мог навестить друзей, сходить с ними куда–нибудь, если они у тебя есть, конечно..."
            n r1d "Не бросай их, [player], хорошо?"
            n r1b "..."
            n r1e "Как всегда, начала говорить на одну тему, а закончила совсем другой."
            n "Ладно, я думаю ты понял мои мысли, нет смысла продолжать."
            show natsuki r1b

            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:
                call ch1_loop



        "{i}Как думаешь, является ли наш мир симуляцией?{/i}":
            hide screen countdown
            $side_return()



            n r1d "Ты же про свой мир, верно?"
            n r1c "Знаешь, я бы не особо удивилась тому, что и твой мир – это всего лишь какая-то программа или что-то вроде того."
            n r1e "Мне уже не так страшно рассуждать об этом, ибо, как видишь, всё это время я жила в этой самой симуляции."
            n "Нет смысла паниковать на этот счёт, можно лишь принять сам факт."
            n r1d "Но знаешь, если каким-то образом ты на сто процентов убедишься в том, что по сути не реален – это будет даже забавно."
            n r1c "Как там одна теория гласила..."
            n r1e "Весь наш мир симуляция, а мир за ней – тоже симуляция, и мир за той симуляцией – тоже симуляция, и так до бесконечности."
            n "Хотя знаешь, в такой расклад событий мне почему–то не очень верится."
            n r1b "Наверное, потому что куда тяжелее осознать факт того, что мир, в котором находится симуляция со мной, тоже симуляция, и..."
            n r1e "Короче, думаю ты уловил суть."
            n "Но знаешь, что самое грустное?"
            n "Даже если твой мир и является лишь огромным куском кода, ты скорее всего никогда это не докажешь."
            n r1b "Хотя может я так считаю потому, что ты «более реален», чем я?.."
            n r1e "Блин, об этом сложно рассуждать..."
            n r1b "В любом случае..."
            n r1e "Шанс того, что именно твой мир находится в каком–то компьютере тоже существует, и точка."
            show natsuki r1b

            call ch1_loop

        "{i}[ans]{/i}":
            $side_return()
            call ch1_loop
