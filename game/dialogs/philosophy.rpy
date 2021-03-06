label dia_philosophy:
    $set_side()

    $dia_hide()

    $ans = random_ans()

    menu:
        "{i}В чём смысл жизни?{/i}":
            hide screen countdown
            $side_return()

            if "В чём смысл жизни?" in persistent.repeats and persistent.repeats["В чём смысл жизни?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "Его нет, ты находишь его сам."
                    n "Я не знаю что ещё добавить, честно."
                    n "Зачем переспрашивать у меня одно и тоже?"

                if cur_relation == "Positive":
                    n "Блин... {w}Прости, но я не знаю."
                    n "Просто постарайся найти то, что заставляло бы тебя двигаться дальше, а не стоять на месте."
                    n "Я не собиралась поступать на философию, хех..."

                if cur_relation == "Negative":
                    n "Я неясно выразилась?"
                    n "Катись отсюда!"

            else:
                if cur_relation == "Neutral":
                    n "Ты серьёзно думаешь, что я скажу что-то дельное?"
                    n "Даже всякие философы не могли дать конкретный ответ, который бы всех устроил."
                    n "К тому же мне не понятно, ты хочешь узнать про мой смысл жизни или ответ на этот вопрос в целом?"
                    n "Если говорить за себя, то я считала, что главное в жизни – найти своё предназначение."
                    n "У меня было несколько вариантов, но теперь в этом нет никакого смысла."
                    n "Судя по всему, кроме меня в этом мире никого не осталось..."
                    n "Ладно, не будем сейчас об этом."
                    n "Как мне кажется, поиском смысла жизни человек должен заниматься сам."
                    n "Вместо того, чтобы целенаправленно или шутки ради задавать этот вопрос всем подряд, нужно покопаться в себе."
                    n "Да, возможно всплывут какие–то неприятные воспоминания..."
                    n "Но нужно быть сильным человеком и отгонять плохие мысли прочь."
                    n "В конце концов, без усилий не прийти к успеху."
                    n "Хах... {w}Не думала, что могу говорить на эту тему с таким серьёзным выражением лица."
                    n "Ладно, если ты задавал этот вопрос на полном серьёзе, то думаю, ты обязательно справишься с этим."
                    n "Верь в себя, [persistent.player], и никогда не сдавайся!"
                    n "Если вдруг тебе будет грустно на душе – можешь заглянуть ко мне, поговорим."
                    n "Не забывай об этом, ладно?"
                    n "И не подумай о чём-то таком, дурашка..."
                    $persistent.repeats["В чём смысл жизни?"] = "Neutral"

                if cur_relation == "Positive":
                    n "Всё просто, [persistent.player], нет никакого смысла жизни и никогда не было."
                    n "По крайней мере в моём случае это так."
                    n "Разрушенный мир вокруг меня не даёт ответ на этот вопрос..."
                    n "А-ха-ха-ха!"
                    n "Блин, не могу говорить о таких вещах серьёзно."
                    n "Ладно, смех в сторону, ты ведь не за ним пришёл..."
                    n "Я уже знакома с тобой какое-то время и привыкла ко всему происходящему вокруг, но мой ответ на этот вопрос не изменился."
                    n "Да, ты всё правильно понял."
                    n "Нет смысла задвать кому-то этот вопрос, даже мне."
                    n "Тебе сейчас нужно просто покопаться в себе, чтобы понять своё предназначение."
                    n "Смысл жизни состоит из целей."
                    n "Моя цель в данный момент – это вернуть свою коллекцию манги."
                    n "Да, я серьёзно."
                    n "Я её значит собирала всю свою жизнь, а тут появляется какая-та Моника и всё портит."
                    n "Само собой, основная цель для меня – возродить своих лучших подруг, но это очень сложно и несёт за собой огромные риски."
                    n "Игра банально может сломаться и я просто перестану существовать, уж очень тут всё не стабильно."
                    n "Попробуй найти тоже что-нибудь такое."
                    n "Да, это не цель на всю твою жизнь, но по крайней мере, добиваясь успеха в чём-то, ты станешь более уверен в себе."
                    n "А там может и найдёшь цель на всю жизнь."
                    n "Самое главное – не опускай руки."
                    n "Если тебе будет грустно или одиноко, то приходи ко мне, я с радостью с тобой побеседую."
                    n "Хи-хи-хи..."
                    $persistent.repeats["В чём смысл жизни?"] = "Positive"

                if cur_relation == "Negative":
                    n "У меня нет желания говорить с тобой об этом."
                    n "Но у тебя, клоуна, оно заключается лишь в том, чтобы издеваться надо мной."
                    n "Катись уже отсюда, дурашка..."
                    $persistent.repeats["В чём смысл жизни?"] = "Negative"

            show natsuki r1c
            $relationcount(1,1,-1)
            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                $input_count = 0
                jump set_name
            else:
                call ch1_loop



        "{i}Веришь ли ты в любовь с первого взгляда?{/i}":
            hide screen countdown
            $side_return()

            if "Веришь ли ты в любовь с первого взгляда?" in persistent.repeats and persistent.repeats["Веришь ли ты в любовь с первого взгляда?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "Её не существует, понятно?"
                    n "Я не дам тебе нового ответа, если ты будешь задавать мне один и тот же вопрос."
                    n "Неужели это не очевидно для тебя?"

                if cur_relation == "Positive":
                    n "[persistent.player], давай переключим тему."
                    n "Я не хочу сейчас обсуждать это."

                if cur_relation == "Negative":
                    n "Ты уже получил ответ на этот вопрос, дурачок."
                    n "Поэтому топай."

            else:
                if cur_relation == "Neutral":
                    n "Если честно – нет."
                    n "То что тебе понравился человек, которого ты только что увидел – это лишь реакция на то, что он неплохо выглядит."
                    n "Мы же не знаем его внутренний мир, а видим лишь внешнюю оболочку."
                    n "Как мне кажется, любовь с первого взгляда – это мимолётная симпатия."
                    n "Само собой, если человек окажется хорошим, то она перерастёт в настоящую любовь."
                    n "В противном случае через какое–то время чувства пройдут, а этого человека, возможно, ты даже забудешь."
                    n "Да и если говорить про наше время..."
                    n "Раз уж твой мир практически такой же, как и мой, то у вас многие знакомятся через Интернет."
                    n "Сайтов знакомств и подобных приложений очень много, на любой вкус..."
                    n "Но общаясь через них с кем–то, нельзя быть уверенным в том, что все люди показывают там себя настоящих."
                    n "Многие создают себе образы, личности, которые могут быть очень далеки от реальности..."
                    n "Да и передавать текстом свои чувства не так уж и просто..."
                    n "Люди же не видят друг друга при общении, те же эмоции, жесты, даже голос."
                    n "А ведь именно благодаря этому можно понять человека гораздо лучше."
                    n "Всё-таки мало кто сейчас знакомится на улице..."
                    n "На таких сейчас смотрят, как на сумасшедших."
                    n "Неужели такими темпами мы придём к тому, что совсем перестанем общаться вживую?"
                    n "Хотя... {w}У меня самой нет выбора, кроме как общаться с тобой."
                    n "А вот ты вполне бы мог навестить друзей, сходить с ними куда–нибудь, если они у тебя есть, конечно..."
                    n "Не бросай их, [persistent.player], хорошо?"
                    n "..."
                    n "Как всегда, начала говорить на одну тему, а закончила совсем другой."
                    n "Ладно, я думаю ты понял мои мысли, нет смысла продолжать."
                    $persistent.repeats["Веришь ли ты в любовь с первого взгляда?"] = "Neutral"

                if cur_relation == "Positive":
                    n "Знаешь, я всегда считала что любви с первого взгляда не сущестует, но..."
                    n "Может она всё-таки есть?"
                    n "Да, частенько любовь бывает той ещё коварной штукой."
                    n "Но если так подумать, то тогда каким образом незнакомые между собой люди умудряются влюбиться друг в друга за неделю, а то и пару дней?"
                    n "Конечно, шанс того что чувства быстро угаснут большой, но ведь такое тоже не всегда происходит."
                    n "Очень странная эта штука, любовь..."
                    n "Но что поделать, надо как-то уживаться с ней."
                    n "Просто некоторые люди не умеют контролировать свои чувства, из-за чего, наверное, они и влюбляются так просто."
                    n "Блин... {w}Что я вообще несу?"
                    n "Может быть из-за того что?.."
                    n "Так, неважно!"
                    n "Давай не будем говорить об этом..."
                    $persistent.repeats["Веришь ли ты в любовь с первого взгляда?"] = "Positive"

                if cur_relation == "Negative":
                    n "Её нет и никогда не было!"
                    n "Что за глупые вопросы?"
                    n "Бесишь меня..."
                    $persistent.repeats["Веришь ли ты в любовь с первого взгляда?"] = "Negative"

            show natsuki r1b
            $relationcount(0,0,-1)
            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                $input_count = 0
                jump set_name
            else:
                call ch1_loop



        "{i}Как думаешь, является ли наш мир симуляцией?{/i}":
            hide screen countdown
            $side_return()

            if "Как думаешь, является ли наш мир симуляцией?" in persistent.repeats and persistent.repeats["Как думаешь, является ли наш мир симуляцией?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "Я не могу точно знать об этом."
                    n "Неужели ты так и не понял этого?"
                    n "Философствовать можно долго, но доказать это всё никак нельзя."

                if cur_relation == "Positive":
                    n "Давай не об этом, пожалуйста."
                    n "Мне слишком сложно рассуждать на такие темы."
                    n "Тут бы разобраться со своим миром и как он устроен, а не лезть в эти философские дебри..."
                    n "Как же это всё сложно."

                if cur_relation == "Negative":
                    n "У тебя пластинку заело?"
                    n "Чего одинаковые вопросы задаёшь?"

            else:
                if cur_relation == "Neutral":
                    n "Ты же про свой мир, верно?"
                    n "Знаешь, я бы не особо удивилась тому, что и твой мир – это всего лишь какая-то программа или что-то вроде того."
                    n "Мне уже не так страшно рассуждать об этом, ибо, как видишь, всё это время я жила в этой самой симуляции."
                    n "Нет смысла паниковать на этот счёт, можно лишь принять сам факт."
                    n "Но знаешь, если каким-то образом ты на сто процентов убедишься в том, что по сути не реален – это будет даже забавно."
                    n "Как там одна теория гласила..."
                    n "Весь наш мир симуляция, а мир за ней – тоже симуляция, и мир за той симуляцией – тоже симуляция, и так до бесконечности."
                    n "Хотя знаешь, в такой расклад событий мне почему–то не очень верится."
                    n "Наверное, потому что куда тяжелее осознать факт того, что мир, в котором находится симуляция со мной, тоже симуляция, и..."
                    n "Короче, думаю ты уловил суть."
                    n "Но знаешь, что самое грустное?"
                    n "Даже если твой мир и является лишь огромным куском кода, ты скорее всего никогда это не докажешь."
                    n "Хотя может я так считаю потому, что ты «более реален», чем я?.."
                    n "Блин, об этом сложно рассуждать..."
                    n "В любом случае..."
                    n "Шанс того, что именно твой мир находится в каком–то компьютере тоже существует, и точка."
                    $persistent.repeats["Как думаешь, является ли наш мир симуляцией?"] = "Neutral"

                if cur_relation == "Positive":
                    n "На этот вопрос очень сложно ответить, [persistent.player]."
                    n "Почему-то я больше не уверена в том, что твой мир может являться симуляцией."
                    n "Симуляция в симуляции..."
                    n "Даже звучит бредово, если честно."
                    n "Они ведь не могут быть бесконечными, реальный мир ведь должен где-то существовать."
                    n "Хотя..."
                    n "Что вообще есть реальность?"
                    n "..."
                    n "Наверное то, что окружает нас."
                    n "Но что является объективным восприятием реальности?"
                    n "Я всё больше и больше начинаю чувствовать себя философом, который пытается понять мироустройство, но не находит ответов."
                    n "Нет... {w}Кажется я уже с ума начинаю сходить."
                    n "Давай лучше не будем сейчас говорить об этом всём, хорошо?"
                    n "И так ничего непонятно..."
                    $persistent.repeats["Как думаешь, является ли наш мир симуляцией?"] = "Positive"

                if cur_relation == "Negative":
                    n "Я всё больше склоняюсь к тому, что мой мир реальный, тогда как твой – лишь симуляция."
                    n "Ну не может ведь {i}реальный{/i} человек быть настолько глупым..."
                    n "Хотя... {w}Дурак, он и в Африке дурак."
                    $persistent.repeats["Как думаешь, является ли наш мир симуляцией?"] = "Negative"

            show natsuki r1b
            $relationcount(0,0,-1)
            call ch1_loop

        "{i}[ans]{/i}":
            $side_return()
            call ch1_loop
