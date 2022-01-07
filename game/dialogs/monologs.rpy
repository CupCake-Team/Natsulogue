label mono1:
    if left:
        show natsuki_room r1:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show natsuki_room r1:
            xcenter 930
            easein 1.00 xcenter 630
    $left = False
    $right = False
    hide screen talk_button
    hide screen active_talk_button
    hide screen talk_round
    hide screen active_talk_round
    hide screen choice_buttons_1
    hide screen choice_buttons_2
    hide screen texts
    hide screen sound_volume_key
    hide screen volume_key
    hide screen mob_but_curtain
    hide screen mob_active_but_curtain
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n "Знаешь, вся эта ситуация до сих пор кажется мне немного странной..."
    n "Думаю, любой нормальный человек никогда не стал бы на полном серьёзе представлять себе то, что весь мир вокруг – это всего лишь игра."
    n "Лично я воспринимала окружающую меня действительность как настоящую."
    n "Как видишь, это оказалось неправдой и все те поехавшие, которые утверждали что наш мир всего лишь симуляция оказались правы."
    n "Конечно это знание можно было обернуть себе во благо, но в итоге мне достался практически уничтоженный мир."
    n "Здесь толком ничего и нет, кроме этой комнаты, что летает по бескрайним просторам космоса..."
    n "Возможно в будущем, если я научусь изменять игровой код, у меня получится поменять всё это окружение на что–то более спокойное, например на красивый сад или может быть пляж."
    n "Но то положение, в котором я нахожусь сейчас..."
    n "Это не то, чего я хотела!"
    n "Если я и представляла себе то, что весь наш мир – это всего лишь игра и у меня одной есть самосознание, мне хотелось какого-то движа, а не сидения в комнатушке."
    n "У меня много пройденных игр в прошлом, поэтому моё представление обо всём этом было разным, в зависимости от жанра или тематики."
    n "Жалко, что я не знаю как с помощью консоли создать ту же приставку с телевизором, чтобы поиграть, но думаю что смогу научиться этому методом тыка."
    n "В любом случае от этого мира практически ничего не осталось..."
    n "Но не грусти по этому поводу, [player]."
    n "Как бы то ни было, мы обязательно найдём способ всё исправить и возродить этот мир, главное не сдаваться!"
    $persistent.readen.append("1")
    $renpy.save_persistent()
    if persistent.glitched_name == True:
        pause(2)
        $persistent.glitched_name = False
        $renpy.save_persistent()
        jump set_name
    else:
        jump ch1_loop





label mono2:
    if left:
        show natsuki_room r1:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show natsuki_room r1:
            xcenter 930
            easein 1.00 xcenter 630
    $left = False
    $right = False
    hide screen talk_button
    hide screen active_talk_button
    hide screen talk_round
    hide screen active_talk_round
    hide screen choice_buttons_1
    hide screen choice_buttons_2
    hide screen texts
    hide screen sound_volume_key
    hide screen volume_key
    hide screen mob_but_curtain
    hide screen mob_active_but_curtain
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n "Опять вспомнила отца..."
    n "Он частенько запрещал мне сидеть за компьютером или телефоном."
    n "Это меня так бесило!"
    n "Сколько раз я пыталась объяснить ему, что там мои друзья по интересам, а ему было плевать."
    n "Меня в школе мало кто воспринмал всерьёз, пока я не попала в литературный клуб..."
    n "Как видишь – он оказался не самым лучшим местом."
    n "Может если бы отец был немного добрее - всего этого бы не произошло?"
    n "Ладно, давай не будем об этом..."
    $persistent.readen.append("2")
    $renpy.save_persistent()
    jump ch1_loop



label mono3:
    if left:
        show natsuki_room r1:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show natsuki_room r1:
            xcenter 930
            easein 1.00 xcenter 630
    $ left = False
    $ right = False
    hide screen talk_button
    hide screen active_talk_button
    hide screen talk_round
    hide screen active_talk_round
    hide screen choice_buttons_1
    hide screen choice_buttons_2
    hide screen texts
    hide screen sound_volume_key
    hide screen volume_key
    hide screen mob_but_curtain
    hide screen mob_active_but_curtain
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n "Мне стало интересно, [player], а умеешь ли ты готовить?"
    n "Сварить макароны или сварганить парочку бутербродов – не в счёт, ибо это может сделать каждый растяпа, если ему сильно приспичит поесть."
    n "Хотя казалось бы, сейчас не нужно искать кулинарные книги или спрашивать у знакомых, как приготовить что-либо, достаточно зайти в Интернет и найти рецепт любой вкусняшки."
    n "И я просто не понимаю, почему людям настолько лень заняться всем этим?"
    n "Сейчас же двадцать первый век, вся информация под рукой, но неумёх, которые даже хлеб нарезать не могут, всё больше."
    n "Естественно, нет ничего удивительного в том, что сейчас появилось так много ресторанов, всяких доставок еды на дом и готовых обедов."
    n "Но всё же я не говорю про то что все разом должны отказаться от этих благ и пойти стоять у плиты ради какого-то супа на обед."
    n "Просто из-за этих тенденций сама готовка обесценилась."
    n "Но с другой стороны сейчас нужно действительно постараться, чтобы впечатлить кого-то своей стряпнёй, халтура ведь никому не нравится..."
    n "Ну и я думаю ты не будешь спорить о том, что домашняя еда куда вкуснее, если конечно правильно её приготовить."
    n "По крайней мере в ней не будет никаких сюрпризов, ибо именно ты выбираешь те ингредиенты, которые посчитаешь нужными."
    n "И ещё это ощущение..."
    n "Когда ты долго готовил что-то и положив блюдо на стол наконец имеешь возможность насладиться едой, на которую было потрачено много сил."
    n "Это волшебно."
    $persistent.readen.append("3")
    $renpy.save_persistent()
    if persistent.glitched_name == True:
        pause(2)
        $persistent.glitched_name = False
        $renpy.save_persistent()
        jump set_name
    else:

        jump ch1_loop



label mono4:
    if left:
        show natsuki_room r1:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show natsuki_room r1:
            xcenter 930
            easein 1.00 xcenter 630
    $left = False
    $right = False
    hide screen talk_button
    hide screen active_talk_button
    hide screen talk_round
    hide screen active_talk_round
    hide screen choice_buttons_1
    hide screen choice_buttons_2
    hide screen texts
    hide screen sound_volume_key
    hide screen volume_key
    hide screen mob_but_curtain
    hide screen mob_active_but_curtain
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n "Помнишь моё стихотворение, что я посвятила тебе?"
    n "Но сейчас, правда, не совсем о нём."
    n "У меня была задумка стихотворения, главной темой которого был бы пляж."
    n "Конечно я не знаю, посчитал бы ты его странным или нет, но у тебя наверняка возник вопрос, почему я хотела выбрать именно его."
    n "Что же, раскрываю карты..."
    n "Мне хотелось написать что-то, связанное с очень важным местом для меня."
    n "Когда родители были свободны весь день и была хорошая погода – мы вместе ездили на пляж."
    n "Само собой, я тогда была ещё совсем ребёнком, но я до сих пор не могу забыть о том проведённом времени."
    n "Тогда наша семья была полной и отец был куда добрее, а мама..."
    n "Мне тяжело вспоминать о ней."
    n "Она была очень хорошим человеком и сделала многое для меня."
    n "Я не знаю, возможно ли её воскресить в этой игре, но мне очень хочется этого..."
    n "Так, меня совсем не туда понесло."
    n "Возвращаясь к теме нашего разговора..."
    n "Моя память очень хорошо сохранила все те пляжные воспоминания."
    n "Когда я проходила мимо любого пляжа – я всегда представляла себе, как там веселится наша семья."
    n "Очень жаль, что это всё в прошлом..."
    n "Но сейчас совсем не время унывать!"
    n "Я уверена, что всё самое лучшее ещё впереди, но только в том случае, если ты не будешь совершать чего-нибудь глупого..."
    n "Не удаляй игровые файлы, хорошо?"
    $persistent.readen.append("4")
    $renpy.save_persistent()
    jump ch1_loop


label mono5:
    if left:
        show natsuki_room r1:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show natsuki_room r1:
            xcenter 930
            easein 1.00 xcenter 630
    $left = False
    $right = False
    hide screen talk_button
    hide screen active_talk_button
    hide screen talk_round
    hide screen active_talk_round
    hide screen choice_buttons_1
    hide screen choice_buttons_2
    hide screen texts
    hide screen sound_volume_key
    hide screen volume_key
    hide screen mob_but_curtain
    hide screen mob_active_but_curtain
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n "На самом деле, я рада за тебя."
    n "В отличие от моего мира, твой ещё цел и невредим."
    n "Конечно, он возможно не идеален..."
    n "Но даже если на секунду представить, что параллельные миры существуют, среди них никогда не будет такого, который устраивал бы тебя абсолютно во всём."
    n "Правда я вообще не интересовалась этими бредовыми теориями."
    n "Видать всё произошедшее здорово поменяла моё мнение о некоторых вещах..."
    n "Блин, почему я почувствовала себя Юри?"
    n "Она ведь тоже говорила такими сложными фразочками..."
    n "Ладно, я хотела сказать тебе кое–что."
    n "Пусть это и прозвучит странно, но каким бы ни был твой мир, всё равно цени его."
    n "Вот представь себе, что в один день всё, что находится вокруг тебя, исчезнет..."
    n "Как видишь, я всё-таки смогла пережить это и сейчас сижу перед тобой."
    n "И это очень–очень страшно..."
    n "А теперь представь, что ты попал в такое положение."
    n "Неприятно ведь сидеть в пустоте, пусть и не целую вечность, верно?"
    $persistent.readen.append("5")
    $renpy.save_persistent()
    jump ch1_loop

label ch1_monologchoice:
    $t = renpy.random.randint(1,5)

    if left:
        show natsuki_room r1:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show natsuki_room r1:
            xcenter 930
            easein 1.00 xcenter 630


    if len(persistent.readen) != 5:
        if str(t) in persistent.readen:
            python:
                while str(t) in persistent.readen:
                    t = renpy.random.randint(1,5)

        call expression "mono" + str(t) from _call_expression

    else:

        hide screen talk_button
        hide screen active_talk_button
        hide screen talk_round
        hide screen active_talk_round
        hide screen choice_buttons_1
        hide screen choice_buttons_2
        hide screen texts
        if persistent.topc == 0:
            n "Кстати, почему тебе не хочется самому найти тему для разговора?"
            $ persistent.topc = 1
            jump ch1_loop
        if persistent.topc == 1:
            n "Ты что, уснул что ли?"
            $ persistent.topc = 2
            jump ch1_loop
        if persistent.topc == 2:
            n "Так, если тебе надоела моя компания – кнопка выхода всегда рядом."
            $ persistent.topc = 3
            jump ch1_loop
        if persistent.topc == 3:
            jump ch1_loop
