label dia_hobbies:
    $set_side()

    $dia_hide()

    $ans = random_ans()

    menu:
        "{i}Почему тебе так нравится готовка?{/i}":
            hide screen countdown
            $side_return()

            if "Почему тебе так нравится готовка?" in persistent.repeats and persistent.repeats["Почему тебе так нравится готовка?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "Я же сказала, почему..."
                    n "Мне нравилась готовка с самого детства, неужели ты всё проигнорировал?"
                    n "Пожалуйста, не делай так больше..."
                    n "Хорошо?"

                if cur_relation == "Positive":
                    n "Я чего-то недосказала или хочется узнать подробностей?"
                    n "Ах да, точно..."
                    n "Был такой период в жизни, когда я решила устроить небольшой бизнес, будучи в средней школе."
                    n "Сейчас это звучит очень глупо, а тогда всё было серьёзно..."
                    n "В общем, я продавала в школе свои кексы ученикам и получала немного денег."
                    n "И знаешь, что самое забавное?"
                    n "Это сработало!"
                    n "Ко мне иногда даже очередь была..."
                    n "Правда потом меня вызвали к директору и в итоге мне пришлось прикрыть своё подполье."
                    n "У школьного буфета выручка упала в три раза из-за меня, прикинь!"
                    n "Меня потом в шутку называли «Бизнесцуки»..."

                if cur_relation == "Negative":
                    n "Я тебе больше ничего не скажу о том, как научилась готовить."

            else:
                if cur_relation == "Neutral":
                    n "Тебе это так интересно?"
                    n "Ну, начнём с того, что готовка даёт возможность понять, из чего состоит та еда, что ты готовишь."
                    n "Правда теперь это не имеет смысла..."
                    n "Приготовить для себя что-нибудь никак не получится."
                    n "В этой комнате даже нет кухонной плиты, какого чёрта, Моника?"
                    n "Может ей просто не нравилось готовить?.."
                    n "Ладно, ничего, когда-нибудь я научусь создавать объекты и обставлю эту комнату мебелью."
                    n "Просто, ещё в детстве мне понравилась одна манга, из-за которой я стала интересоваться готовкой."
                    n "Впридачу мама часто радовала меня домашней едой, от чего желание стать поваром становилось ещё больше."
                    n "А вот отец..."
                    n "Он обходил плиту стороной, ибо совсем не умел готовить."
                    n "Если же он и давал мне какую-то стряпню – её было неохота даже пробовать."
                    n "Вкус был просто отвратительным..."
                    n "В итоге я решила, что пора учиться готовить самой."
                    n "Сперва это было не так уж и просто..."
                    n "Ингредиентов часто не хватало, да и блюда получались не самыми вкусными."
                    n "Мне даже хотелось бросить эту затею, благо я вовремя одумалась и вместо того, чтобы опустить руки - продолжила заниматься готовкой."
                    n "Как видишь, у меня получилось не только познать кулинарию, но ещё и найти себя в ней..."
                    n "Так что я усвоила один урок."
                    n "Не нужно бросать своё увлечение на пол пути к совершенству, так как ты можешь добиться больших успехов."
                    n "Поэтому [persistent.player], не будь лентяем, хорошо?"
                    $persistent.repeats["Почему тебе так нравится готовка?"] = "Neutral"

                if cur_relation == "Positive":
                    n "Я рада, что ты спросил меня об этом."
                    n "Готовка для меня не просто увлечение, на которое я трачу свободное время, а ещё и прекрасная возможность стать настоящим шеф–поваром и связать с этим жизнь."
                    n "Только вот, есть одна проблема..."
                    n "Кафе и ресторанов всё равно больше не существует, как и плиты в этой комнате."
                    n "Походу Моника не любила готовить, хе-хе-хе..."
                    n "Нет, серьёзно, мне тяжело без готовки, она меня успокаивает."
                    n "Ещё в детстве мне понравилась одна манга..."
                    n "Она была про коллектив одного из ресторанов, который участвовал в кулинарном шоу, где проводилась битва между заведениями со всей Японии, а потом..."
                    n "...я познакомилась с «Ванильными девочками» и мою любовь к готовке уже ничего не могло остановить!"
                    n "Правда это ещё не все причины."
                    n "Когда моя семья была ещё полной – практически всегда у плиты стояла мама и радовала всех домашней едой, но она..."
                    n "..."
                    n "В общем, я осталась наедине с отцом."
                    n "Он старался не приближаться к плите, ибо совсем не умел готовить, поэтому у меня не было возможности нормально поесть."
                    n "Его блюда, если он пытался что-то приготовить для меня, даже бездомные коты не стали бы даже пробовать."
                    n "Вкус был просто ужасным!"
                    n "Некоторое время я питалась в школьной столовой и изредка баловала себя полуфабрикатами, но потом мне попались те томики манги и я решила научиться готовить."
                    n "Мне понадобилась огромная выдержка..."
                    n "В основном мне не хватало ингредиентов, от чего мои блюда были такими же плохими, как и уотца."
                    n "Из-за этого я начинала думать о том, что ничего не получится..."
                    n "Но потом пришло осознание того, что это не выход из ситуации."
                    n "Что лучше, питаться помоями или же нормальной едой?"
                    n "Выбора просто не оставалось.."
                    n "Зато я добилась больших успехов на этом поприще!"
                    n "Вот такая история..."
                    $persistent.repeats["Почему тебе так нравится готовка?"] = "Positive"

                if cur_relation == "Negative":
                    n "Уже не знаешь о чём поговорить и решил затронуть готовку, серьёзно?"
                    n "Неужели тебе не очевидно, что это из-за манги?"
                    n "Ну ты и идиот, такие глупые вопросы задавать..."
                    n "Как ты ко мне относишься, так и я буду к тебе относиться."
                    n "Придурок..."
                    $persistent.repeats["Почему тебе так нравится готовка?"] = "Negative"

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

        "{i}Как ты полюбила мангу?{/i}":
            hide screen countdown
            $side_return()

            if "Как ты полюбила мангу?" in persistent.repeats and persistent.repeats["Как ты полюбила мангу?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "Ты всё прослушал, или что?"
                    n "Разве я не ясно расссказала тебе об этом?"
                    n "Манга была очень важной частью моей жизни, начиная с самого детства."
                    n "Этого, думаю, достаточно."
                    n "И да, надеюсь ты всё-таки найдёшь способ, как показать мне мангу из своего мира."
                    n "Не забудь об этом, хорошо?"
                    $relationcount(0,-2,0)

                if cur_relation == "Positive":
                    n "М?"
                    n "Я чего-то забыла упомянуть?"
                    n "Ах да... {w}Точно!"
                    n "Слушай, если найдёшь в игре какую-то лазейку, чтобы показать мне мангу из твоего мира - обязательно воспользуйся ей."
                    n "Просто мне очень хочется почитать её, в вашем мире она ведь тоже есть, в конце концов..."
                    n "Я буду ждать."

                if cur_relation == "Negative":
                    n "Отцепись ты с этой мангой от меня."

            else:
                if cur_relation == "Neutral":
                    n "Ну... {w}На самом деле это долгая история."
                    n "Как и многим детям, мама иногда читала мне мангу, в основном перед сном."
                    n "Научившись читать, я стала покорять её самостоятельно."
                    n "Уже тогда мама покупала мне новые томики манги за хорошее поведение."
                    n "Это побуждало меня быть послушной..."
                    n "В итоге коллекция всего этого добра росла стремительными темпами, я иногда даже не успевала всё прочитать."
                    n "Знакомые ребята мне очень сильно завидовали."
                    n "Ко мне в гости часто приходили дети со двора чтобы просто почитать мангу и пообсуждать её."
                    n "Мне очень нравились такие посиделки..."
                    n "Я росла и всё это прекратилось, так как манга стала ассоциироваться у всех с детской побрякушкой."
                    n "После этого можно было забыть про новые томики, а всё из-за отца, который считал что мне пора вырасти и прекратить читать эти дурацкие «комиксы»."
                    n "Поэтому мне приходилось тратить все свои карманные деньги на покупку новой манги и постоянно всё прятать."
                    n "Хорошо, что я смогла найти укромное местечко для всей своей коллекции..."
                    n "Но время шло и количество томиков тоже."
                    n "Я редко кому рассказывала об этом, ведь в итоге кто-то обязательно проговаривался и все надо мной лишь смеялись."
                    n "Сперва мне было очень обидно, но потом пришло осознание..."
                    n "Насколько у людей всё плохо в жизни, что они самоутверждаются за счёт девушки с иным увлечением."
                    n "Те ещё дураки в общем."
                    n "И вот так чтение манги стало для меня чем-то вроде протеста против общества."
                    n "Естественно, я продолжала читать мангу, несмотря ни на что!"
                    n "Хм..."
                    n "Раз уж наш мир основан на твоём, то это значит, что в нём тоже есть манга."
                    n "Интересно, какая?"
                    n "Мне было бы интересно её полистать..."
                    $persistent.repeats["Как ты полюбила мангу?"] = "Neutral"

                if cur_relation == "Positive":
                    n "На самом деле это довольно занятная история."
                    n "Ещё в детстве, мама часто читала мне мангу."
                    n "У нас была небольшая традиция..."
                    n "Когда я ложилась спать, она заходила ко мне в комнату, садилась рядом со мной и читала мне перед сном мангу."
                    n "Понятное дело, что она была детской, с примитивным сюжетом, но уже тогда она начала мне нравится."
                    n "Затем я вместе с мамой начала учиться читать, догадайся, по каким учебникам я училась?"
                    n "Вот именно, что не по каким, я читала те самые тома манги."
                    n "Это было легко, все истории из них были известны мне на зубок."
                    n "..."
                    n "К сожалению, отец мою любовь к манге не разделял."
                    n "Мама пыталась объяснять ему, что в этом нет ничего плохого и что я, благодаря ней, достигла каких-то успехов."
                    n "Это работало до поры до времени, пока..."

                    if "Как ты относишься к своему отцу?" in persistent.repeats and persistent.repeats["Как ты относишься к своему отцу?"] == "Positive":
                        n "Ну, ты и так знаешь что произошло, не хочу об этом говорить."
                        n "В итоге, одним прекрасным утром моему отцу после очередной попойки в голову «гениальная» идея»."
                        n "Запрет на чтение и покупки манги..."

                    else:
                        n "В общем, мамы не стало, от чего отец превратился в алкоголика и просто идиота."
                        n "Приходя с работы, он каждый день нажирался пива, а мне приходилось наблюдать за этим."
                        n "Иногда он даже засыпал на полу, бормоча какой-то бред себе под нос."
                        n "С таким человеком жить было невозможно..."
                        n "Мало того, после очередной белочки, он вообще запретил мне читать и покупать мангу!"

                    n "В эту пору мне приходилось совсем не весело."
                    n "Карманные деньги, если и каким-то образом перепадали, то их было совсем немного, а кушать-то всегда хочется."
                    n "Отец обычно закупался пивом, да вяленой рыбой, о нормальной еде не могло идти и речи."
                    n "Иногда мне казалось, что он вообще меня не замечает, но это было ложное чувство..."
                    n "Это... {w}Мой отец был очень непредсказуемым и мне не хотелось перечить ему."
                    n "Но, как ты понимаешь, любовь к манге у меня в крови,
                    поэтому мне приходилось прятать томики у себя дома."
                    n "Хорошо что он ни разу не додумывался до того, чтобы посмотреть под кровать в моей комнате..."
                    n "Я пополняла свою коллекцию манги несмотря ни на что!"
                    n "Конечно, это вызывало лишь усмешки со стороны одноклассников, но мне было плевать..."
                    n "Эти идиоты ничего не смыслили в литературе, им лишь бы над слабаками поиздеваться."
                    n "Хорошо что я не повелась на их тупые провокации!"
                    n "Хм... {w}Сейчас я бы могла читать мангу хоть целую вечность, но..."
                    n "Ни один томик не сохранился."
                    n "Я бы могла поискать их в коде игры, если бы она не разваливалась от каждой попытки вмешаться в неё."
                    n "Сейчас лезть туда - это самоубийство настоящее."
                    $persistent.repeats["Как ты полюбила мангу?"] = "Positive"

                if cur_relation == "Negative":
                    n "Хмф... {w}И с чего бы тебе вообще интересоваться этим, дурак?"
                    n "Собрался посмеяться надо мной или что?"
                    n "Ну мне мама в детстве её читала, что дальше?"
                    n "Тебе это та-а-ак было нужно?"
                    n "..."
                    n "Да пошёл ты!"
                    $persistent.repeats["Как ты полюбила мангу?"] = "Negative"



            $relationcount(1,1,-1)
            call ch1_loop

        "{i}Ты играешь в видеоигры?{/i}":
            hide screen countdown
            $side_return()
            $random_ans()

            if "Ты играешь в видеоигры?" in persistent.repeats and persistent.repeats["Ты играешь в видеоигры?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "Я ведь уже отвечала тебе что да, играю."
                    n "И что хочу сыграть с тобой в «вилочки–кексики»..."
                    n "Не потеряй такую возможность, пока я добрая."

                if cur_relation == "Positive":
                    n "А?"
                    n "Для чего ты опять задаёшь этот вопрос?"
                    n "Я вроде всё объяснила, хотя... {w}Кое-что упустила."
                    n "У меня есть игра мечты, которая никогда не выйдет, но в которую мне бы хотелось играть днями напролёт."
                    n "Шутер от первого лица с кучей монстров и головоломок в самых разных странных локациях."
                    n "К примеру, в царстве сладостей или вообще в каком-нибудь мире, к примеру, где всё вверх дном."
                    n "Ну и конечно же, огромный арсенал оружия, чтобы враги не расслабляли булки."
                    n "Эх... {w}Мечты."

                if cur_relation == "Negative":
                    n "Я всё сказала, топай."

            else:
                if cur_relation == "Neutral":
                    n "Конечно, ведь это прекрасная возможность уйти на некоторое время от реального мира."
                    n "Если при чтении манги всё равно приходится напрягать воображение, а при просмотре аниме лишь наблюдать за происходящим, то игра даёт возможность во всём поучаствовать."
                    n "В придачу у них очень много жанров на любой вкус."
                    n "Мне самой больше всего нравилось играть во всякие стрелялки."
                    n "Всё-таки иногда нужно выпускать пар..."
                    n "Конечно, почти все девочки в школе играли во всякие фермы и симуляторы жизни, но мне это было не особо интересно."
                    n "Ну а ты, как погляжу, любитель визуальных новелл?"
                    n "Или просто решил проверить этот жанр?"
                    n "Хотя, игру, в которой я нахожусь, хорошей не считаю..."
                    n "В любом случае, игровая индустрия прекрасно справляется со своей задачей, а именно развлекает игрока."
                    n "Поэтому ничего удивительно в том, что виртуальные миры так популярны..."
                    $persistent.repeats["Ты играешь в видеоигры?"] = "Neutral"

                    if persistent.f_game == 0:
                        n "Эх... {w}Жалко что из всех забав в коде игры остались лишь «вилочки–кексики»."
                        n "Я написала эту игру, так как на уроке информатики нам дали домашнее задание – принести на флешке какой-то солидный проект."
                        n "За «вилочки–кексики» мне дали высокий балл, да и всем они показались очень милыми."
                        n "Если хочешь, то можем сыграть в них вместе."
                        n "Может быть в будущем я создам ещё какие-то игры, заодно немного улучшу свои навыки программирования."

                if cur_relation == "Positive":
                    n "А как же!"
                    n "Было бы странно, если бы я в них не играла."
                    n "Ты же не думаешь, что у меня всё на манге зациклено?"
                    n "Мой самый любимый жанр - это шутеры конечно же!"
                    n "Желательно, чтобы они были от первого лица и с более-менее интересным повествованием, а то стрелять просто потому что не очень интересно."
                    n "Да и по сети я играла очень редко, да и так, пару матчей."
                    n "Конечно, я играла и в другие игры, самых разных жанров, но довольно редко."
                    n "Всё-таки у меня было не настолько много времени, чтобы проводить его в виртуальных мирах."
                    n "В этом и прелесть этой индустрии, огромное количество проектов на любой вкус и цвет."
                    n "И  гонки тебе, и стрелялки, и какие-то головоломки, и даже визуальные новеллы с упором на романтику, хи-хи-хи..."
                    n "Тебе нравится игра, в которой я нахожусь?"
                    n "Вот мне лично нет, хотя... {w}Без её глюков я бы не смогла с тобой встретиться."
                    n "Конечно, мы не можем полноценно общаться, но согласись, это лучше чем ничего."
                    n "Ладно, я, кажись, отошла от темы..."
                    $persistent.repeats["Ты играешь в видеоигры?"] = "Positive"

                    if persistent.f_game == 0:
                        n "Ах да, ты же до сих пор не попробвал сыграть в «вилочки–кексики»..."
                        n "Давай поиграем, не будь трусишкой, хи-хи-хи..."
                        n "Обещаю, буду поддаваться."

                if cur_relation == "Negative":
                    n "Какой дурацкий вопрос..."
                    n "Положительно конечно же, только вот жалею о том, что моя реальность оказалась игрой."
                    n "Лучше бы вообще тебя не встречала."
                    $persistent.repeats["Ты играешь в видеоигры?"] = "Negative"

            show natsuki r1c
            $relationcount(1,1,-1)
            call ch1_loop



        "{i}Как ты относишься к серьёзной литературе?{/i}":
            hide screen countdown
            $side_return()

            if "Как ты относишься к серьёзной литературе?" in persistent.repeats and persistent.repeats["Как ты относишься к серьёзной литературе?"] == cur_relation:
                if cur_relation == "Neutral":
                    n "Что такое?"
                    n "Я ведь уже ответила, что отношусь к ней нейтрально."
                    n "Не приставай ко мне с этим вопросом, мне уже хватило докапываний Юри в своё время."
                    n "..."
                    n "Так, неважно!"

                if cur_relation == "Positive":
                    n "Чего тебе?"
                    n "Про ту мангу что ли подробности узнать хочется?"
                    n "Ну не-е-ет, я пока что спойлерить ничего не буду, пока сама не достану её из лап игры."
                    n "Не хочу портить тебе первое впечатление о ней."
                    n "Прости уж, но таков мой принцип."

                if cur_relation == "Negative":
                    n "Нейтрально отношусь, уйди."

            else:
                if cur_relation == "Neutral":
                    n "Эм... {w}В каком плане?"
                    n "Ты про те книжки что читала Юри или в целом?"
                    n "Если честно, я отношусь к подобному нейтрально, ибо каждый имеет право на свои предпочтения."
                    n "Увы, но классическая литература – это не моё."
                    n "Я читаю для того чтобы расслабиться и погрузиться в какую-нибудь интересную историю, а не заниматься поиском скрытого смысла и поглощением писательской философии."
                    n "И, как ты понимаешь, манга как раз подходит мне по всем параметрам."
                    n "Правда иногда хочется чего–то более глубокого и продуманного…"
                    n "Но благо манги столько, что каждый найдёт ту, которая зайдёт больше всего."
                    n "Мне даже хотелось одну Юри посоветовать, но, как видишь, я не успела..."
                    $persistent.repeats["Как ты относишься к серьёзной литературе?"] = "Neutral"

                if cur_relation == "Positive":
                    n "Если говорить по правде, то как-то всё равно."
                    n "То что мы там с Юри в своё время насчёт этого ругались - это просто потому, что мы не нашли общий язык."
                    n "И наши увлечения нас же и разделили, благо мы хоть забили на это."
                    n "Я пробовала читать действительно серьёзную литература и не раз, но в основном ближе к середине бросала это."
                    n "Ну не моё это всё!"
                    n "Что я могу с собой поделать?"
                    n "Хотя, одно произведение я всё-таки смогла осилить и оно мне даже понравилось, но..."
                    n "Это было единственное исключение из правил!"
                    n "Просто мне не нравится, когда автор насильно запихивает в тебя какую-то точку зрения, а в серьёзной литературе такое повсюду."
                    n "Я читаю не для того, чтобы думать о проблемах реального мира, мне просто хочется расслабиться и на миг оказаться в альтернативной вселенной."
                    n "Хорошо, что за всё время столько манги хорошей смогли выпустить..."
                    n "Правда в последнее время были одни лишь попаданцы, да гаремы, которые читать - себя не уважать."
                    n "И всё это потому, что в индустрию пришли большие дяди и куча денег..."
                    n "Что же, теперь всего этого добра нет, ну и ладно, думаю я смогу вернуть мангу, когда получше освоюсь в коде игры."
                    n "Эх..."
                    n "А всё-таки жаль, что я так и не смогла предложить Юри прочесть ту мангу..."
                    n "Она будто под её вкусы создавалась."
                    n "Серьёзно, один в один «Портрет Маркова», но с иллюстрациями."
                    n "Видать мангака решил адаптировать эту книгу под мангу и как мне кажется, он справился на пять с плюсом!"
                    n "Даже мне было интересно её полистать, несмотря на то, что все эти ужастики терпеть не могу."
                    n "Ну, как-то так..."
                    $persistent.repeats["Как ты относишься к серьёзной литературе?"] = "Positive"

                if cur_relation == "Negative":
                    n "Мх..."
                    n "Будешь пытаться подколоть меня, да?"
                    n "Или ещё чего хуже..."
                    n "Ты и так прекрасно знаешь о том, что я ничего не имела против подобной литературы."
                    n "Я знаю, ты специально задал этот вопрос, желая увидеть какую-то не такую реакцию..."
                    n "Хах... {w}Ну и дурак же ты."
                    n "Или ты думал, что я настолько съехавшая на теме манги?"
                    n "Отстань уже, а..."
                    $persistent.repeats["Как ты относишься к серьёзной литературе?"] = "Negative"


            show natsuki r1b
            $relationcount(0,0,-1)
            call ch1_loop

        "{i}[ans]{/i}":
            $side_return()
            call ch1_loop
