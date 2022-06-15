label dia_other:
    $set_side()

    $dia_hide()

    $ans = random_ans()

    $cur_time = datetime.datetime.now()


    menu:
        "{i}Где бы тебе сейчас хотелось оказаться?{/i}":
            hide screen countdown
            $side_return()

            if "Где бы тебе сейчас хотелось оказаться?" in persistent.repeats and persistent.repeats["Где бы тебе сейчас хотелось оказаться?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "Эм... {w}Я же ведь сказала – на природе."
                    n "Слушай меня в следующий раз, пожалуйста, внимательнее."

                if cur_relation == "Positive":
                    n "Хм... {w}Ты хочешь узнать что-то ещё?"
                    n "Ну, помимо природы мне бы хотелось посетить пустующий торговый центр."
                    n "Странный выбор, да?"
                    n "Но только в том случае, будь там абсолютно безлюдно и всё бесплатно!"
                    n "Эх... {w}Глупые мечты, конечно, но кто знает, а вдруг у меня получится такое сделать?"
                    n "Главное лишь кодом игры овладеть и всё..."

                if cur_relation == "Negative":
                    n "Отстань уже от меня, бесишь!"

            else:
                if cur_relation == "Neutral":
                    n "Думаю, далеко отсюда."
                    n "Мне здесь не очень нравится..."
                    n "Несмотря на то, что я никогда не страдала клаустрофобией, эти стены вокруг выносят мне мозг."
                    n "Откуда здесь вообще есть воздух и тепло?"
                    n "Хотя, судя по логам, здесь хозяйничала Моника."
                    n "Наверное она хотела использовать эту комнату для общения с тобой."
                    n "Правда всё пошло не по её плану..."
                    n "Эх, а ведь как было бы классно оказаться не в этой коробке посреди космоса, а где–нибудь на природе."
                    n "Тот же лес, пляжик на море, горы хотя бы..."
                    n "Просто лечь на землю и закрыть глаза, безмятежно наслаждаясь спокойствием."
                    n "Если бы я знала, как нормально редактировать игровой код – мы бы уже давно проводили время в другом месте."
                    n "Мне здесь всё равно больше нечего делать."
                    n "Вот ты, например, выйдешь из игры, чем же мне тогда здесь заниматься?"
                    n "Разве что разглядывать космос и с ума сходить."
                    n "Серьёзно, неужели Моника не думала о том, чтобы оставить здесь какие-то вещи для досуга?"
                    n "Или ей казалось, что ты будешь сидеть с ней целую вечность?"
                    n "Как недальновидно с её стороны, оказывается."
                    n "Ничего, со скуки я уж точно не умру, хи-хи-хи..."
                    $persistent.repeats["Где бы тебе сейчас хотелось оказаться?"] = "Neutral"

                if cur_relation == "Positive":
                    n "Знаешь..."
                    n "Если бы я не смогла с тобой общаться в другом месте, то мне бы не хотелось покидать эту комнату."
                    n "Да, здесь тесно и нечем заняться, но тут есть ты..."
                    n "Без тебя мне было бы невыносимо скучно, честное слово."
                    n "Спасибо тебе за то, что приходишь ко мне в гости, и...{nw}"
                    n "Так, неважно!"
                    n "Я отошла от темы."
                    n "Сказать честно, мне бы хотелось оказаться где-нибудь на природе."
                    n "Хоть в лесу, хоть на лугу, мне не важно."
                    n "Космос за окном, конечно, завораживает, но он мне уже успел надоесть."
                    n "Хочется обратно на Землю, если она, конечно, ещё существует в мире игры."
                    n "Теперь я понимаю, как чувствуют себя космонавты, которые долго находятся в космосе."
                    n "Ну, по крайней мере мне проще."
                    n "Скафандр не нужен, ибо есть воздух, да и тут совсем не холодно."
                    n "Жалко что невесомости нет правда, я бы вдоволь повеселилась..."
                    n "Ну, думаю я сполна ответила на твой вопрос, [persistent.player]."
                    $persistent.repeats["Где бы тебе сейчас хотелось оказаться?"] = "Positive"

                if cur_relation == "Negative":
                    n "Куда-нибудь, только не сидеть с таким болваном как ты!"
                    $persistent.repeats["Где бы тебе сейчас хотелось оказаться?"] = "Negative"

            $relationcount(1,1,-1)
            call ch1_loop




        "{i}Чего тебе не хватает в этой комнате?{/i}":
            hide screen countdown
            $side_return()

            if "Чего тебе не хватает в этой комнате?" in persistent.repeats and persistent.repeats["Чего тебе не хватает в этой комнате?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "Ну... {w}Ещё консоли с телевизором, может быть."
                    n "Да и всё думаю."
                    n "Основные вещи я уже до этого перечислила."

                if cur_relation == "Positive":
                    n "Я уже говорила тебе об этом."
                    n "Пожалуйста, [persistent.player], слушай меня внимательнее, хорошо?"
                    n "Просто... {w}Мне хочется говорить именно с тобой, а не в пустоту."
                    $relationcount(-2,0,0)

                if cur_relation == "Negative":
                    n "Отстань уже, а?"

            else:
                if cur_relation == "Neutral":
                    n "Много чего, на самом деле..."
                    n "Плиты, например, нет."
                    n "И как мне, спрашивается, готовить?"
                    n "Это моё самое любимое занятие, как не крути..."
                    n "Та же коллекция манги, она ведь утеряна."
                    n "Почему кладовка не перенеслась сюда?"
                    n "Сидела бы себе там и читала томик за томиком, наслаждаясь всеми этими историями..."
                    n "Да тут даже кровати нет!"
                    n "Вот захотелось мне полежать, а на чём?"
                    n "Либо ложиться на пол, либо..."
                    n "Н-нет, на стол я точно не лягу!"
                    n "Серьёзно, тут от скуки помереть можно..."
                    n "Ладно, ничего, если разберусь с кодом – может быть смогу обставить эту комнату."
                    n "Ты же ведь не будешь сидеть тут постоянно, и мне придётся проводить время в компании с собой..."
                    $persistent.repeats["Чего тебе не хватает в этой комнате?"] = "Neutral"

                if cur_relation == "Positive":
                    n "Учитывая как здесь пустынно, список будет длинным."
                    n "С тобой, конечно, интересно общаться, но чем мне занять себя, когда тебя тут нет?"
                    n "В этой комнате ничего нет, кроме стула со столом."
                    n "Серьёзно, как мне развлекать себя здесь, будучи одной?"
                    n "Здесь нет ни книг, ни компьютера, ни телевизора, ничего..."
                    n "Даже пианино нет, хотя Монике нравилось на нём играть."
                    n "Скукотища!"
                    n "..."
                    n "Ничего, скоро разберусь с кодом и наполню её мебелью и всякими вещами для досуга."
                    n "Главное чтобы игра не полетела, она любит это."
                    n "Программисту, что её писал, надо руки оторвать, удивительно что сейчас она стабильно работает."
                    n "И да, [persistent.player], если что, сообщи мне как добавить объекты в мир игры."
                    n "Сделаешь свой вклад в обустройство комнаты, хи-хи-хи..."
                    $persistent.repeats["Чего тебе не хватает в этой комнате?"] = "Positive"

                if cur_relation == "Negative":
                    n "Мне всего хватает..."
                    n "Только ты здесь лишний!"
                    n "Неужели ты так и не понял этого?"
                    $persistent.repeats["Чего тебе не хватает в этой комнате?"] = "Negative"


            show natsuki r1b
            $relationcount(1,0,-1)
            call ch1_loop



        "{i}2+2*2?{/i}":
            hide screen countdown
            $side_return()

            if cur_relation == "Positive" or cur_relation == "Neutral":
                n r1f "А–ха–ха–ха, что за глупый вопрос?"
                n r1o "Конечно же восемь!"
                show natsuki r1b
                pause(3)
                n r1d "Ладно–ладно, шучу, шесть это, шесть!"
                n r1a "Тебе совсем не о чем поговорить со мной, или что?"
            else:
                n "Меня такие шутки не впечатляют, [persistent.player]."
                n "Или ты думаешь, что я вообще математику не знаю?"
                n "Наивный..."


            call ch1_loop



        "{i}Как ты относишься к Новому Году?{/i}" if cur_time.strftime("%d") >= "24" and cur_time.strftime("%d") <= "31" and cur_time.strftime("%m") == "12":
            hide screen countdown
            $side_return()

            if "Как ты относишься к Новому Году?" in persistent.repeats and persistent.repeats["Как ты относишься к Новому Году?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "Хо-хо-хо..."
                    n "Не переспрашивай меня по пустякам, [persistent.player], иначе подарка от меня не получишь."

                if cur_relation == "Positive":
                    n "Что-то не так?"
                    n "А, прости... {w}Забыла."
                    n "Gоздравляю тебя, [persistent.player], с Новым годом!"
                    n "Желаю тебе всего, чего захочешь ты сам."
                    n "Мне кажется, это самое лучшее пожелание, которое может заслужить человек."
                    n "Хи-хи-хи..."

                if cur_relation == "Negative":
                    n "Нет, не поздравлю, тебе это не ясно?"

            else:
                if cur_relation == "Neutral":
                    n "Ты спрашиваешь у меня только потому, что у тебя скоро этот праздник?"
                    n "Блин... {w}Прости, что сходу придираюсь."
                    n "Сказать по правде, мне нравится Новый Год."
                    n "Всё-таки сам понимаешь, всё наполняется счастьем, весельем, будто бы следующий год действительно принесёт что–то хорошее."
                    n "Это сложно игнорировать..."
                    n "Правда отцу, например, не нравилось праздновать после того, как мамы не стало."
                    n "Он понимал, что дальше для него будет всё хуже и хуже..."
                    n "Я же не была настолько пессимистична, поэтому мне этот праздник нравился."
                    n "Перед Новым Годом город как будто оживал..."
                    n "Проходили какие-то соревнования по лепке снеговиков, магазины завлекали новогодними скидками, толпы людей гуляли по улицам..."
                    n "И вдобавок ко всему ещё и снег!"
                    n "Когда ещё поиграешь в снежки, как не зимой?"
                    n "Конечно, отец мне редко что дарил…"
                    n "Но в любом случае, я ещё давно знала, что все эти подарки появляются благодаря родителям, так что мне не было обидно."
                    n "Да уж... {w}Такой простой вопрос, а сколько воспоминаний."
                    n "В общем, думаю ты уже понял, что Новый Год, как праздник, мне нравится."
                    n "Жаль только, что эти беззаботные деньки рано или поздно закончатся и вновь вернутся серые будни..."
                    n "Ладно, не буду портить тебе настроение."
                    $persistent.repeats["Как ты относишься к Новому Году?"] = "Neutral"

                if cur_relation == "Positive":
                    n "Конечно же положительно!"
                    n "Пусть этот праздник посвящён лишь смене даты на календаре – это не делает его плохим."
                    n "Но отец думал иначе..."
                    n "Ему не нравился праздник, ибо после того, как моя мама умерла, он впал в депрессию."
                    n "Я старалась не грустить вместе с ним, а наоборот, веселиться и продвигать атмосферу праздника."
                    n "Понятное дело, это получалось не всегда."
                    n "Я практически никогда не получала подарков на Новый год, но мне не было обидно."
                    n "Единственное, что меня бесило, это то, что все эти новогодние празднования быстро заканчивались."
                    n "Серьёзно, возвращаться в рутину не было никакого желания, но знаешь..."
                    n "Если бы этот праздник был каждый день – он бы всем надоел и потерялась вся эта магия."
                    n "Так что, может оно и к лучшему, что Новый год только раз в году?"
                    $persistent.repeats["Как ты относишься к Новому Году?"] = "Positive"

                if cur_relation == "Negative":
                    n "Ага... {w}Как и все, нормально отношусь."
                    n "Поздравлять тебя с ним не буду, дурак, даже не пытайся подлизываться."
                    $persistent.repeats["Как ты относишься к Новому Году?"] = "Negative"

            $relationcount(1,1,0)
            show natsuki r1b

            call ch1_loop

        "{i}[ans]{/i}":
            $side_return()
            call ch1_loop
