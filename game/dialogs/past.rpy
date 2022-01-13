label dia_past:
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
        "{i}Что ты думаешь о литературном клубе?{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630



            n r1a "Поначалу он был не самым приятным местом..."
            n r1c "Я захотела вступить в него, ибо искала спокойное место где можно быть собой."
            n r1e "На листовках так и было написано, поэтому я отправилась туда."
            n "Мне казалось, что это хороший шанс найти новых друзей и заняться любимым делом."
            n "В конце концов, в прошлом году я состояла в аниме–клубе, но там мне было не очень комфортно из-за некоторых людей..."
            n r1b "Поэтому мне не хотелось туда возвращаться..."
            n r1e "Так вот, уже в клубе я рассказала о себе и своём увлечении мангой, с трудом уговорив Монику перетащить мою коллекцию в кладовку."
            n "Кстати, там уже состояли Юри и Сайори и всё было бы хорошо, но..."
            n "Они все молча осуждали мою страсть к манге, что это, видите ли, детская забава."
            n "В итоге я чуть ли не покинула клуб, но в конце концов вся заваренная каша оказалась расхлёбана."
            n "Мы приняли интересы друг друга, пусть и с небольшой натяжкой, в конце концов помирившись и всё стало идеально."
            n r1b "..."
            n r1f "Ха–ха–ха!"
            n "Всё {i}это{/i} оказалось ложью!"
            n r1e "Если та же Сайори перестала принижать мои интересы, а Юри просто молчала, то Моника..."
            n "Я сейчас даже не говорю про то, что она переставляла мою мангу без спроса и в целом совала нос не в свои дела."
            n "Она манипулировала сознанием участников клуба и, как ты прекрасно знаешь, доводила своих поруг до самоубийства."
            n r1b "Это просто..."
            n r1e "У меня нет слов, предательство какое–то."
            n "Моника превратила свой же клуб в настоящий ад, заставляя его участников мучиться просто потому, что ей хотелось достичь тебя."
            n r1a "После такого я не могу воспринимать это место в положительном ключе."
            n r1b "Хорошо, что тебя не было на моём месте..."
            n r1e "Это был ужас."

            call ch1_loop from _call_ch1_loop_15

        "{i}Ты ненавидишь Монику за её поступки?{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630

            $broknbase = renpy.random.randint(1,2)
            if broknbase == 1:
                n r1e "Это ещё мягко сказано..."
                n "Никогда не думала, что она может вести себя так безрассудно."
                n r1b "Моника всегда проявляла чуткость и поддерживала меня и остальных..."
                n r1e "И всё это для того, чтобы потом обращаться с нами как со скотом!"
                n "Ходить по трупам своих подруг, чтобы достичь какой-то призрачной цели..."
                n "А я ведь считала её хорошей подругой."
                n "Дискуссионный клуб, оказывается, очень хорошо обучает людей врать и при этом не краснеть."
                n r1b "Я не знаю, осталась ли она ещё в игре или нет, но если, Моника, ты это слышишь..."
                n r1j "Можешь раскаиваться хоть миллион лет, не прощу!"
                n "Из-за тебя моих настоящих подруг больше нет!"
                n "Ненавижу тебя!"
                n r1k "..."
                n r1l "Наверное сейчас это выглядело глупо, но мне нужно было выговориться."
                n r1n "Мне хочется высказать ей лично куда больше ласковых слов..."
            else:
                n r1e "VGhhdCdzIHB1dHRpbmcgaXQgbWlsZGx5Li4u"
                n "SSBuZXZlciB0aG91Z2h0IHNoZSBjb3VsZCBhY3Qgc28gcmVja2xlc3NseS4="
                n r1b "TW9uaWthIGhhcyBhbHdheXMgYmVlbiBzZW5zaXRpdmUgYW5kIHN1cHBvcnRpdmUgb2YgbWUgYW5kIHRoZSBvdGhlcnMuLi4="
                n r1e "QW5kIGFsbCB0aGlzIHRvIHRoZW4gdHJlYXQgdXMgbGlrZSBjYXR0bGUh"
                n "V2Fsa2luZyBvdmVyIHRoZSBkZWFkIGJvZGllcyBvZiBoZXIgZnJpZW5kcyB0byBhY2hpZXZlIHNvbWUgZ2hvc3RseSBnb2FsLi4u"
                n "QW5kIEkgdGhvdWdodCBzaGUgd2FzIGEgZ29vZCBmcmllbmQu"
                n "VGhlIGRlYmF0ZSBjbHViIHR1cm5zIG91dCB0byBiZSB2ZXJ5IGdvb2QgYXQgdGVhY2hpbmcgcGVvcGxlIGhvdyB0byBsaWUgd2l0aG91dCBibHVzaGluZy4="
                n r1b "SSBkb24ndCBrbm93IGlmIHNoZSdzIHN0aWxsIGluIHRoZSBnYW1lIG9yIG5vdCwgYnV0IGlmLCBNb25pa2EsIHlvdSBjYW4gaGVhciB0aGlzLi4u"
                n r1j "WW91IGNhbiBnbyBvbiBmb3IgYSBtaWxsaW9uIHllYXJzLCBJIHdvbid0IGZvcmdpdmUgeW91IQ=="
                n "QmVjYXVzZSBvZiB5b3UsIG15IHJlYWwgZnJpZW5kcyBhcmUgZ29uZSE="
                n "SSBoYXRlIHlvdSE="
                n r1k "Li4u"
                n r1l "SXQgbXVzdCBoYXZlIHNlZW1lZCBzaWxseSBub3csIGJ1dCBJIG5lZWRlZCB0byBnZXQgaXQgb3V0Lg=="
                n r1n "SSB3YW50IHRvIHNheSBtb3JlIMKrc3dlZXTCuyB0aGluZ3MgdG8gaGVyIGluIHBlcnNvbi4="

            call ch1_loop from _call_ch1_loop_16

        "{i}Что скажешь про Юри?{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630

            n r1e "Как минимум ничего такого."
            n r1d "Да, у нас возникали какие–то споры, но это только потому, что я и она имели противоположные интересы."
            n "Это нормально для людей, у которых разные точки зрения и предпочтения, но в итоге мы всё равно мирились."
            n "Само собой, как только я вступила в литературный клуб – у меня не получилось найти с Юри общий язык."
            n r1e "У неё был слишком застенчивый характер и она не умела подбирать слова в нужный момент..."
            n r1d "Но в итоге мы поняли, что нет смысла пытаться перечить друг другу."
            n r1a "Мы свели подобные темы к минимуму, но потом в клуб пришёл друг Сайори."
            $jm = renpy.random.randint(1,2)
            if jm == 1:
                n r1e "То есть ты, хотя на тот момент об этом знала лишь Моника."
            else:
                n r1e "То есть ты, хотя на тот момент об этом знала только Моника.{nw}"
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                $ pause(0.25)
                stop sound
                hide screen tear
                n r1e "То есть ты, хотя на тот момент об этом знала{fast} лишь Моника."
            n r1c "Такое, казалось бы, небольшое пополнение вновь привело к конфликтам, благо всё уладили."
            n r1b "Эх... {w}А я ведь подозревала, что она резалась."
            n "Почему у меня не возникало идеи насильно повести её к психологу?"
            n "Теперь меня мучает совесть..."
            n r1e "Жаль, что вряд ли получится что-то изменить."
            n "Для меня Юри навсегда останется хорошей подругой, пусть и со своими странными увлечениями."
            n r1b "В конце концов, зачем за них осуждать?"

            call ch1_loop from _call_ch1_loop_17

        "{i}Как ты относишься к Сайори?{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630

            n r1b "Скажем так..."
            n r1d "Она была очень хорошей подругой, которая всегда поддерживала меня."
            n r1e "Сайори никогда не делала кому–то больно, ведь ей хотелось, чтобы все вокруг были счастливы."
            n r1a "Конечно, она не была экспертом в литературе, но я понимаю, почему Моника назначила её вице-президентом..."
            n r1c "Сайори прекрасно справлялась со всеми конфликтами, что происходили в клубе."
            n r1b "Хотя в основном и спорили только я, да Юри..."
            n "Если бы не она – мы бы наверное так и продолжали ненавидеть друг друга."
            n r1a "Поэтому я не могу относиться к ней плохо, но..."
            n r1b "Её больше нет, как и остальных."
            n "А ведь знала бы я, что у неё депрессия, то обязательно помогла."
            n r1e "Почему же ты не рассказала никому об этом?"
            n r1b "Может быть, мы смогли бы ей помочь и отогнать все эти тучки от неё куда подальше..."
            n "Жалко мне её, хорошим человеком ведь...{w}{i}была.{/i}"

            call ch1_loop from _call_ch1_loop_18


        "{i}Что бы ты делала на месте Моники?{/i}":
            hide screen countdown
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630

            n r1e "Хороший вопрос..."
            n "Тут зависит от того, на сколько сильно пришлось бы менять код, чтобы встретиться с тобой лично."
            n "Хотя, насколько я поняла, сама игра не позволяла этого сделать."
            n r1b "Само собой, я бы хотела увидеться с тобой, но не причиняя своим подругам вреда."
            n r1e "У меня нет желания мучить их ради собственного эгоизма, да и Моника показала, чем всё это может закончиться."
            n "Если бы при любом раскладе изменение игры стоило бы их жизней, то я бы точно не стала пытаться дальше."
            n "Люди, которых я знаю долгое время, важнее, чем кто-то за экраном."
            n "Да, у меня больше знаний о том, что происходит в игре, но это не делает меня выше остальных."
            n "В конце концов, я ведь даже внешности твоей не знаю, что уж о характере говорить?"
            n r1l "Мне бы очень хотелось свободного общения с тобой, но игра..."
            n r1k "Мх..."
            n r1n "Она не предоставляет такой возможности."
            n r1h "Но ничего, если у меня всё получится, мы избавимся от этих барьеров!"
            n r1n "И, надеюсь, вернём обратно остальных..."

            call ch1_loop from _call_ch1_loop_19

        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_20

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_21

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            call ch1_loop from _call_ch1_loop_22
