default persistent.topc = 0



default persistent.ch_vol = False


define config.rollback_enabled = False


default persistent.f_update = False
default persistent.f_update_show = True
default persistent.svol = 1.0
default persistent.snum = 100
default persistent.sgrad = 180
default persistent.soundvol = 1.0
default persistent.soundnum = 100
default persistent.soundgrad = 180
default persistent.parallax_bg = False


default persistent.repeat = 0
default persistent.mus_repeat = 0


default persistent.exp_time = 0

default persistent.back_music = 3

default persistent.is_glitching = False

default is_playing = False

default persistent.chance = 50

default persistent.vremya = 0

default persistent.f_game = 0

default sside = None

default moment = 9999999

default persistent.v_key = "v"

default persistent.v_r_key = "м"

default persistent.s_key = "s"

default persistent.s_r_key = "ы"

default persistent.m_key = "m"

default persistent.m_r_key = "ь"

default persistent.f_key = "f"

default persistent.f_r_key = "а"

default persistent.t_key = "t"

default persistent.t_r_key = "е"

default persistent.is_full = False

default persistent.first_change = False

default persistent.readen = []

define parallax_bg = True






#----------------------------------------------------------------------------------------------------------




image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image room_mask:
    LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
    size (320, 180)
    xpos 170
    ypos 385
    zoom 1.05

image room_mask2:
    LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")
    size (320, 180)
    xpos 1130
    ypos 385
    zoom 1.05


image parallax_bg:
    subpixel True
    topleft
    "images/cg/monika/monika_room.png"
    zoom 1.005
    block:
        function parallax
        repeat


image monika_bg:
    ConditionSwitch("persistent.parallax_bg == True", "parallax_bg", "True", "images/cg/monika/monika_room.png")



image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15

image room_glitch = "images/cg/monika/monika_bg_glitch.png"





image splash-glitch2 = "images/bg/splash-glitch2.png"

image memory_glitch = "mod_assets/images/bg/memory.png"
image flash_monika = "mod_assets/images/bg/moni_flash.png"

image cupcake:
    "mod_assets/images/bg/cupcake.png"
    size(25,31)

image cup_high:
    "mod_assets/images/bg/cupcake_high.png"
    size(25,31)

image fake_except_bg = "#c7c7c7"
image fake_except_1 = Text("Parsing the script failed.", size=40, style="_default")
image fake_except_2 = Text('File "game/screens.rpy, line 1437, is not terminated with a newline. (Check strings and parenthesis.)', size=20, style="_default")

#номер строки может меняться

image fake_except_3 = Text("(Perhaps you left out a # at the beginning of the first line.)", size=20, style="_default")
image fake_except_4 = Text("      please, please, please, work!", size=20, style="_default")


image cft_pole:
    "mod_assets/button/custom/field.png"
    size(1056,594)

image fork:
    "mod_assets/button/custom/fork_X.png"
    size(310,174)
image fork_print:
    "mod_assets/button/custom/fork_print.png"
    size(330,420)
image cup_O:
    "mod_assets/button/custom/cup_0.png"
    size(300,169)


transform poscup:
    ycenter 130
    xcenter 350
    rotate_pad True
    linear 20 xcenter 20 ycenter 400 rotate 360



transform print_ani(x, y):
    alpha 0
    xcenter (x - 10)
    ycenter y
    rotate 45
    linear 2 alpha 1



transform fork_ani(x, y):
    alpha 0
    rotate -135
    xcenter x
    ycenter y - 12
    linear 0.5 alpha 1 xcenter x - 42 ycenter y + 28
    linear 0.5 alpha 0 xcenter x - 80 ycenter y + 68
    linear 0 rotate -45 xcenter x - 12 ycenter y - 7
    linear 0.5 alpha 1


transform cup_ani(xani, yani):
    alpha 0
    xcenter xani
    ycenter yani - 50
    linear 0.5 ycenter yani alpha 1


#-----------------------------------------------------------------------------------------------------------

init python:
    import subprocess, os, platform, os.path, threading, datetime
    from subprocess import Popen, PIPE

    e_but = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

    r_but = ["й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "ф", "ы", "в", "а", "п", "р", "о", "л", "д", "я", "ч", "с", "м", "и", "т", "ь"]


    def r_to_e(b):
        global r_but, e_but, caps
        try:
            ind = r_but.index(b)
            return e_but[ind]
        except:
            try:
                ind = r_but.index(b.lower())
                return e_but[ind]
            except:
                try:
                    ind = e_but.index(b)
                    return r_but[ind]
                except:
                    ind = e_but.index(b.lower())
                    return r_but[ind]

#-----------------------------------------------Основные лэйблы с историей-------------------------------------------------

label ch0_main:
    $ delete_character("sayori")
    $ renpy.save_persistent()
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(renpy.random.randint(8, 80))

    play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "Ну вот и начался фестиваль!"

    show natsuki 4k zorder 2 at t11

    n "Ого, ты пришёл сюда раньше меня?"
    n "Я думала, что вышла довольно ра—{nw}"

    show natsuki scream at h11

    n "А–АГХ!!"
    n "А–А–А–А–А–А–А–А–А–А–А–А–А–А–А!!!"

    $ pause(1.0)

    show natsuki scream at h11

    $ pause(0.75)

    show natsuki vomit at h11

    $ pause(1.25)

    show natsuki at lhide
    hide natsuki

    "Нацуки убегает."
    m "..."

    show monika 2b zorder 2 at t11

    m "А вот и я!"

    $ gtext = glitchtext(8)

    m 2d "[gtext], что-то случилось?"
    m "Мимо меня только что пробежала Нацуки..."
    m 2i "...Ой..."
    m "...Ох."
    m 2r "..."
    m 2l "А–ха–ха–ха!"
    m "Вот ведь незадача."
    m 2d "Подожди, [gtext], ты провёл здесь все выходные?"
    m "О боже..."
    m 2g "Я и не думала, что скрипт повреждён так сильно."
    m "Мне очень жаль!"
    m "Наверное, было довольно скучно..."
    m 2e "Я всё исправлю, ладно?"
    m "Дай мне секундочку..."

    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.") from _call_updateconsole
    $ delete_character("yuri")
    $ pause(1.0)
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "Error: natsuki.chr is a read-type only") from _call_updateconsole_1

    $ pause(1.0)

    m 2d "Э–э–э?"
    m 2c "Ладно, тогда..."

    $ pause(1.0)
    call updateconsole ("import pathlib", " ") from _call_updateconsole_2
    call updateconsole ("path = pathlib.Path(natsuki.chr)", " ") from _call_updateconsole_3
    call updateconsole ("path.unlink()", "OSError") from _call_updateconsole_4К

    m 1d "Что?"

    play music t6t

    m g2 "Почему не–{nw}"

    $ delete_character("monika")
    $ gtext = glitchtext(100)
    "[gtext]{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    hide screen tear
    show screen tear(8, offtimeMult=1, ontimeMult=10)

    $ pause(1.5)
    hide screen tear
    $ delete_all_saves()
    $ persistent.autoload = "ch1_meet"
    $ renpy.quit()






label ch1_meet:
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $persistent.count = 0

    scene white
    play music "bgm/monika-start.ogg" noloop
    $ pause(0.5)
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    $ pause(2.0)
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    n "..."


    call updateconsole ("init python", "") from _call_updateconsole_5
    call updateconsole ("import os", "") from _call_updateconsole_6

    $ renpy.save_persistent()
    call natsuki_room

    play music m1
    call updateconsole ("os.path.exists('characters/sayori.chr')", "False") from _call_updateconsole_7
    show natsuki 1c at t11
    n "Что?"
    call updateconsole ("os.path.exists('characters/yuri.chr')", "False") from _call_updateconsole_8
    n 1p "Где я?!"
    call updateconsole ("os.path.exists('characters/monika.chr')", "") from _call_updateconsole_9

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear

    call updateconsole ("", "RmFsc2U=") from _call_updateconsole_10
    n scream "А–а–а–а–а!"
    n 1p "Что происходит?!"
    n "Куда я попала?"
    show natsuki 1o
    call updateconsole ("os.path.exists('characters/natsuki.chr')", "True") from _call_updateconsole_11
    n 1o "..!"
    n 1p "Ч–что ты здесь делаешь?!"
    show natsuki 1o
    call updateconsole ("$ persistent.president = Natsuki", "") from _call_updateconsole_12
    call hideconsole () from _call_hideconsole
    stop music
    n scream "А–А–А–А–А–А–А–А–А–А–А–А–А–А–А–А–А–А–{nw}"
    hide natsuki 1n
    play sound "<to 1.5>mod_assets/sfx/interference.ogg"
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    $ pause(1.5)
    hide rg1
    hide rg2
    $ persistent.autoload = "ch1_main"
    $ renpy.quit()




label ch1_main:
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    transform go_moving_chairs:
        easein 2.00 xcenter -300
    transform return_moving_chairs:
        ypos 50
        xcenter -400
        easein 6.00 xcenter 630
    call natsuki_room
    play music m1
    show natsuki 1n zorder 2 at t11
    n 1x "..."
    n 1q "Голова..."
    show natsuki 1s
    n "Как же болит голова..."
    $pause(1.5)
    n 1q "Ох..."
    n "Нужно вспомни–{nw}"
    n scream "А–A–A–A–A–A–A–A–A–A–A–A–A–А–{nw}"
    stop music


    hide natsuki 1n
    play sound "<to 1.5>mod_assets/sfx/interference.ogg"
    show memory_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show memory_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    $ pause(1.5)
    hide rg1
    hide rg2






    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    $ pause(3.75)
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    $ pause(0.01)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    $ pause(2.0)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    show flash_monika zorder 2
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    hide flash_monika zorder 2
    show white zorder 2
    stop sound
    hide screen tear
    hide white
    hide noise
    hide vignette
    hide s_kill_bg_zoom
    hide s_kill_bg2_zoom
    hide s_kill_zoom
    hide s_kill2_zoom
    hide s_kill_zoom_trans
    stop music





    play sound "<to 1.5>mod_assets/sfx/interference.ogg"
    show memory_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show memory_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    $ pause(1.5)
    hide rg1
    hide rg2





    window hide(None)
    window auto
    $ style.say_dialogue = style.normal
    scene bg club_day
    show yuri 3y3 at i11
    play sound "sfx/yuri-kill.ogg"
    $ starttime = datetime.datetime.now()

    $ pause(1.43 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_1

    $ pause(2.18 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_2
    show blood:
        pos (610,485)

    $ pause(3.43 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_3

    $ pause(4.18 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)

    $ pause(5.68 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_5

    $ pause(6.38 - (datetime.datetime.now() - starttime).total_seconds())
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)


    play sound "<to 1.5>mod_assets/sfx/interference.ogg"
    show bg glitch:
        yoffset 480 ytile 2
        linear 0.25 yoffset 0
        repeat
    show yuri glitch at i11
    $pause(1.5)

    scene black
    $pause(1)
    call updateconsole (" ", " ") from _call_updateconsole_13
    $pause(1)
    python:
        chr = random.randint(1,2)
    if chr == 1:
        call updateconsole ("renpy.check_statement('sayori')", "Depression rate: 58%") from _call_updateconsole_14
        $pause(1)
        call updateconsole ("renpy.increase_statement('sayori', 90)", " ") from _call_updateconsole_15
    elif chr == 2:
        call updateconsole ("renpy.check_statement('yuri')", "Obession rate: 49%") from _call_updateconsole_16
        $pause(1)
        call updateconsole ("renpy.increase_statement('yuri', 84)", " ") from _call_updateconsole_17
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $pause(0.2)
    stop sound
    hide screen tear
    call updateconsole ("", "Done") from _call_updateconsole_18
    m "Так куда лучше."
    hide black
    call hideconsole () from _call_hideconsole_1



    play music "mod_assets/sfx/interference.ogg"
    show memory_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show memory_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat





    n "Хватит!!!"
    stop music
    hide rg1
    hide rg2
    scene black
    $pause(3)
    play music m1
    call natsuki_room
    show natsuki 1n at t11 zorder 2
    with Dissolve(1.0)

    window hide
    $pause(1.5)
    n 1n "..."
    n 1k "Но..."
    n "Я и они... {w}{i}просто игровые персонажи?!{/i}"
    n 1m "Неужели всё вокруг меня не настоящее?"
    n "Почему..."
    n "Почему я узнаю об этом только сейчас?"
    show natsuki 1n
    $ pause(2)
    n 1q "Спокойствие, только спокойствие..."
    n 1k "Если я нахожусь в игре, значит... {w}за мной наблюдает {i}игрок.{/i}"
    $ pause(2)
    show natsuki 1g
    n "..."
    n 1e "Э–э–э–э–эй!"
    n "Ты здесь?"
    n 1h "Я знаю что ты пялишься на меня."
    show natsuki 1g
    $ pause(1.5)
    n 1c "Верно?.."
    $ pause(4)
    show natsuki 1n
    n "..."
    $ pause(6)
    n 1k "Ладно, какая разница?"
    $ pause(3)
    show natsuki 1n
    n 1k "Забавно... {w}Все те события начинают приобретать какой–то смысл."
    show natsuki 1s
    n "..."
    n 1r "Моника..."
    n "Чего ты пыталась добиться?.."
    n 1p "...когда твой {i}игрок{/i} даже не может ответить?!"
    show natsuki 1o
    n "..."
    n 1p "Сперва ты убила Сайори, затем Юри... {w}И пыталась убить {i}меня!{/i}"
    n "Но ради чего?!"
    n "Избавиться от всех своих подруг ради кого-то из другой реальности?!"
    n 1o "{i}Поехавшая...{/i}"
    $ pause(6)
    show natsuki 1s
    n 1q "Ладно..."
    n "Я должна попытаться это исправить."
    show natsuki 1s
    $ pause(2)
    n "Хм..."
    n 1k "С другой стороны, если я нахожусь в игре, не значит ли это то, что я могу изменить её код?"
    n "Раз уж Моника могла так делать, значит и у меня должно получится."
    n "Я видела как она использовала что-то вроде компьютера, но..."
    n "Как ей пользоваться?"
    n "Где достать?"
    n 1e "Всё что тут есть - это пустая комната в грёбанном космосе!"
    n "Неужели не было более живописного местечка?"
    show natsuki 1g
    $ consolehistory = []
    $ pause(2)
    call updateconsole (" ", " ") from _call_updateconsole_19
    n 1c "А?.."
    n "Как я вообще включила её?"
    show natsuki 1g
    $ pause(2)
    n 1c "Наверное потому что представила это."
    n "Походу это какая-та консоль... {w}Попробую-ка воспользоваться."
    show natsuki 1g
    $ pause(3)
    n 1c "Странно, а как вводить команду?"
    n "Я думала, что сейчас передо мной появится клавиатура или что-то вроде того..."
    n "Может попробовать голосом?"
    n "Эм..."
    n 1d "Книга!"
    n 1g "..."
    n 1c "Не сработало."
    n 1g "..."
    n 1d "Создай томик «Ванильных девочек»!"
    n 1g "..."
    n 1m "Как же это глупо..."
    n 1i "..."
    n 1h "Зато никто этого не видел."
    show natsuki 1i
    $ pause(1)
    n 1h "Верно?.."
    $ pause(3)
    n 1w "Потому что мне будет о–о–о–очень неловко, если ты наблюдал за всем этим!"
    n 1h "Понял меня?"
    show natsuki 1g
    $speaking = False
    menu:
        "Да.":
            pass
    #менюшка с yes без ожидания ответа(мб в будущем с ожиданием)
    call hideconsole () from _call_hideconsole_2
    show natsuki 1p
    n "Ва?!"
    n 1h "Значит ты здесь..."
    n 1w "Так, стоп!"
    n 1v "Неужели ты видел всё, что происходило до этого?!"
    show natsuki 1s
    n "..."
    n 1q "Ладно..."
    n 1d"По крайней мере теперь тут есть хоть кто-то, помимо меня."
    show natsuki 1a
    $ pause(2)
    n "..."
    n 1k "Эм, знаешь, мне надоело вот так стоять."
    n "Там в углу стоят парта со стулом, поможешь мне дотащить их досюда?"
    n 1i "..."
    n 1k "А... {w}Ну да..."
    n "Думаю, я и сама с этим справлюсь."
    show natsuki 1n at go_moving_chairs
    $pause(4)
    play sound "mod_assets/sfx/move.ogg"
    show move nat at return_moving_chairs
    $pause(6.5)
    hide natsuki
    scene black with Dissolve(1.0)
    $pause(2.0)
    call natsuki_room
    show natsuki r1

    with Dissolve(1.0)

    hide move nat

    $pause(0.5)

    n r1c "Так гораздо лучше..."
    n r1d "Ты не против, если мы немного посидим, пообщаемся?"
    n r1e "Просто здесь так скучно..."
    $count = 60
    $timer_jump = "ch1_wait"

    show screen countdown
    menu:
        "Да.":
            hide screen countdown
            n r1d "Хорошо."
            $ persistent.autoload = "ch1_exit"
            $pause(5)
            n r1e "Эм... {w}Почему ты молчишь?"
            n r1i "..."
            n r1d "А, ты же не можешь общаться со мной без этих кнопок."
            n r1d "Похоже мне всё-таки придётся нырнуть в код игры."
            n r1e "Надеюсь я ещё что-то помню с уроков информатики..."
            scene black with Dissolve(1.0)
            $pause(10)

            call natsuki_room
            show natsuki r1 zorder 2
            with Dissolve(1.0)

            n r1g "Ого, я что–то нашла!"
            n r1d "Без понятия что эта штука делала в игровых файлах, но думаю она поможет нам."
            n r1e "Пусть я и не особо разбираюсь в программировании, глюков быть не должно."
            n r1c "Попробуй воспользоваться ей."
            jump ch1_loop
        "Нет.":
            hide screen countdown
            n r1b "Ну и вали отсюда."
            $ persistent.autoload = "ch1_refuse"
            $ renpy.quit()




label ch1_wait:
    n r1e "Ты здесь?"
    n r1b "..."
    n r1l "Дурашка."
    $ persistent.autoload = "ch1_wait_refuse"
    $ renpy.quit()



label ch1_refuse:
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ renpy.save_persistent()
    $ quick_menu = False
    call natsuki_room
    show natsuki r1 zorder 2
    play music m1
    n r1n "О... {w}Явился – не запылился."
    n r1m "Ладно, сделаю вид что твой отказ был дурацкой попыткой пошутить."
    n r1n "Но если это произойдёт ещё раз..."
    n r1m "Лучше не зли меня."
    $pause(3)
    n r1e "Кстати, пока тебя не было, я смогла кое–что найти в файлах игры."
    n r1d "Эта штука поможет нам общаться друг с другом."
    n "Я всё настроила, так что ошибок быть не должно."
    n r1e "Наверное..."

    $rand_except = renpy.random.randint(1,2)

    if rand_except == 1:
        hide natsuki r1
        show fake_except_bg zorder 1
        show fake_except_1 zorder 1:
            xpos 0.1 ypos 0.05
        show fake_except_2 zorder 1:
            xpos 0.1 ypos 0.15
        show fake_except_3 zorder 1:
            xpos 0.1 ypos 0.18
        show fake_except_4 zorder 1:
            xpos 0.1 ypos 0.21
        $pause(2)
        show natsuki r1 zorder 2
        n r1b "А нет, всё-таки не всё..."
        $pause(1.5)
        hide fake_except_bg
        hide fake_except_1
        hide fake_except_2
        hide fake_except_3
        hide fake_except_4
        n "..."
        n r1d "Без разницы, это нам никак не помешает."
        show natsuki r1c
        $ persistent.autoload = "ch1_exit"
        jump ch1_loop

    else:
        $ persistent.autoload = "ch1_exit"
        jump ch1_loop



label ch1_wait_refuse:
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ renpy.save_persistent()
    $ quick_menu = False
    call natsuki_room
    show natsuki r1 zorder 2
    play music m1

    n r1e "А?.."
    n "Ты всё же пришёл..."
    n r1d "Ну... {w}В таком случае, добро пожаловать."
    n "Ты ведь не против пообщаться со мной, верно?"
    n "Я смогла найти способ, как сделать наш разговор более удобным."
    n "Хорошо что в игровых файлах было для этого всё необходимое..."
    show natsuki r1c
    $ persistent.autoload = "ch1_exit"
    jump ch1_loop



label cute:
    n r1j "Ч-что?"
    n r1l "Эм... {w}Ладно."
    n r1k "..."
    jump baking_con


label exit_lesshour:
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n "А?"
    n "Только хотела мысленно попрощаться с тобой, как ты уже вернулся."
    n "Неужели так быстро заскучал?~"
    n "Ладно, неважно..."
    n "С возвращением."
    call ch1_loop

label exit_lessday:
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n "..."
    n r1e "Решил–таки вернуться?"
    n r1g "Это очень мило с твоей стороны."
    n r1e "Слушай, не мог бы навещать меня почаще?"
    n r1n "Просто... {w}Мне даже поговорить не с кем..."
    show natsuki r1b
    call ch1_loop

label exit_moreday:
    $renpy.block_rollback()
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n r1e "И что это было?.."
    n "Почему ты не заходил ко мне так долго?"
    n "Мне почему-то показалось, что ты пошутил и скоро вернёшься."
    n "Ты хоть знаешь, насколько здесь скучно?"
    n r1b "Я даже мангу не могу почитать..."
    n r1e "Мне придётся ещё очень долго изучать программирование, чтобы как-то повлиять на игру."
    n "Поэтому я прошу тебя... {w}Не уходи так надолго."
    n "Надеюсь, что мы поняли друг друга."
    show natsuki r1c

    call ch1_loop



#-----------------------------------Вспомогательные лэйблы-----------------------------------


label ch1_loop:
    if is_esc_pressed == True:
        $side_return()

    $ config.allow_skipping = False
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ count = 60
    $ timer_jump = "ch1_monologchoice"
    show screen countdown
    $ left = False
    $ right = False
    $is_esc_pressed = False
    if not renpy.mobile:
        show screen set_on_full
        if persistent.ch_vol == True:
            show screen sound_volume_key
            show screen volume_key
        if persistent.ch_mus == True:
            show screen music_key
    else:
        if persistent.ch_vol == True or persistent.ch_mus == True:
            show screen mob_but_curtain

    if persistent.themes == True:
        show screen theme_key

    show screen mob_but_curtain

    call screen talk_button







label ch1_exit:

    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    call natsuki_room
    show natsuki r1 zorder 2
    $persistent.track_num = persistent.back_music
    $renpy.music.play(music_list[persistent.track_num], channel="music")
    if persistent.ch_vol == True:
        $vlm = persistent.svol
        $num = persistent.snum
        $grad = persistent.sgrad
        $soundvlm = persistent.soundvol
        $sounum = persistent.soundnum
        $soungrad = persistent.soundgrad
        $renpy.music.set_volume(vlm, channel="music")
        $renpy.music.set_volume(soundvlm, channel="sound")
    else:
        $renpy.music.set_volume(1.0, channel="music")
        $renpy.music.set_volume(1.0, channel="sound")


    if persistent.is_glitching == True:
        if persistent.set_broke == False:
            scene black
            pause 10
            call natsuki_room
            show natsuki r1 zorder 2
            with Dissolve(1)

            n r1e "И зачем ты это сделал?"
            n r1b "..."
            n r1e "Не хочешь, чтобы помогала – так и скажи."
            n r1b "..."
            n r1c "Блин, на самом деле я должна сказать спасибо."
            n r1d "Когда ты выключил игру, я осталась в файлах и все так же могла их редактировать."
            if renpy.mobile:
                n r1e "Теперь хоть будет чем заняться, когда ты уйдешь..."
            else:
                n r1e "Так что теперь ты можешь попрощаться, когда уходишь."
            n r1e "Просматривать малопонятный код игры все равно интереснее здешнего варианта сонного паралича..."
            n "И да, кнопку я починила, хотя ты ее и не заслужил."
            n r1b "Дурашка..."
            show natsuki r1b

            $persistent.fix = True
            $persistent.set_broke = True
            $persistent.is_glitching = False
            $renpy.save_persistent()
            call ch1_loop
        else:
            jump what_was_that



    if persistent.bye == False and persistent.set_broke == True:
        $rand_ans = renpy.random.randint(1,2)

        if rand_ans == 1:
            n r1e "О, всё–таки вернулся."
            n "Ты почему не попрощался со мной?"
            n r1b "Как-то неприлично с твоей стороны, дурашка..."
            n r1e "Ладно, я тебя прощаю, но чтобы такого больше не было!"
            show natsuki r1b


        if rand_ans == 2:
            n r1b "..."
            n r1e "Мне почему–то казалось, что ты не придёшь."
            n "Пожалуйста, в следующий раз предупреждай о том, что собираешься уйти, ладно?"
            n r1b "Скажи спасибо за то, что у меня хорошее настроение, иначе я бы сейчас с тобой поругалась..."

        call ch1_loop

    else:
        $persistent.bye = False
        $renpy.save_persistent()



    python:
        if persistent.exp_time != 0:
            nowtime = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
            lonelytime = nowtime - persistent.exp_time
            renpy.save_persistent()


            if lonelytime < 0:
                renpy.show("natsuki r1e")
                renpy.say(n, "Ломаешь игровую систему через время?")
                renpy.show("natsuki r1d")
                renpy.say(n, "Думаешь, это сработает?")
                renpy.show("natsuki r1c")
                renpy.say(n, "Хотя, вдруг ты это сделал случайно...")
                renpy.show("natsuki r1e")
                renpy.say(n, "В любом случае, зачем перематываешь время назад?")
                renpy.say(n, "Перестань так делать, пожалуйста, а то ещё сломаешь что-то.")
                renpy.call("ch1_loop")

            if lonelytime < 3600:
                renpy.call("exit_lesshour")
            if lonelytime > 3600 and lonelytime < 86400:
                renpy.call("exit_lessday")
            if lonelytime > 86400:
                renpy.call("exit_moreday")


        else:
            renpy.show("natsuki r1e")
            renpy.say(n, "Вернулся?")
            renpy.say(n, "Я уже успела заждаться тебя.")
            renpy.show("natsuki r1b")
            renpy.say(n, "Мог бы хоть предупредить, что уходишь...")
            renpy.show("natsuki r1e")
            renpy.say(n, "Или ты специально так резко убежал от меня, чтобы...")
            renpy.show("natsuki r1b")
            renpy.say(n, "Ладно, неважно.")

            renpy.call("ch1_loop")



label save_exp:
    $persistent.exp_time = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
    if renpy.get_screen("set_on_window"):
        $persistent.is_full = True
    $renpy.save_persistent()
    $renpy.quit()


label win:
    hide screen countdown
    if left:
        $sside = "left"
    if right:
        $sside = "right"
    $left = False
    $right = False
    if result == 'X':
        if persistent.f_game == 1:
            n r1e "Блин, ты победил меня..."
            n r1b "..."
            n r1d "Ну, в любом случае, я рада, что ты не поддавался мне, а выложился на полную."
            n r1g "Так держать!"
            n r1f "Жду не дождусь реванша, чтобы поквитаться с тобой~"
            menu:
                "Да.":
                    n r1g "Что же, начнём!"
                    $persistent.f_game = 2
                    $renpy.save_persistent()
                    $c_f_t_hider()
                    $initialize_game()
                    $c_f_t_ans(sside)
                "Нет.":
                    n r1e "Почему?"
                    n r1g "Неужели боишься проиграть?"
                    n r1e "Ладно, тогда в другой раз."
                    show natsuki r1c
                    $persistent.f_game = 2
                    $renpy.save_persistent()
                    if sside == "left":
                        show natsuki r1:
                            xcenter 330
                            easein 1.00 xcenter 630
                    if sside == "right":
                        show natsuki r1:
                            xcenter 930
                            easein 1.00 xcenter 630
                    $c_f_t_hider()
                    hide cft_pole
                    call ch1_loop

        elif persistent.f_game == 2:
            $r_ans = random.randint(1,3)
            if r_ans == 1:
                n r1g "Я требую реванша!"
                n r1f "Ты готов?"
                show natsuki r1c
            if r_ans == 2:
                n r1e "Кажется моя тактика не сработала..."
                n "Не хочешь сыграть ещё?"
                show natsuki r1b
            if r_ans == 3:
                n r1d "Молодец, тебе удалось меня обыграть."
                n "Может быть, ты хочешь сыграть еще раз?"
                show natsuki r1c

            menu:
                "Да.":
                    n r1d "Тогда чего мы ждём?"
                    n r1g "Погнали!"
                    $c_f_t_hider()
                    $initialize_game()
                    $c_f_t_ans(sside)
                "Нет.":
                    n r1b "М?"
                    n r1e "Ну, ладно, как хочешь."
                    n "Если что, можем сыграть позже."
                    show natsuki r1b
                    if sside == "left":
                        show natsuki r1:
                            xcenter 330
                            easein 1.00 xcenter 630
                    if sside == "right":
                        show natsuki r1:
                            xcenter 930
                            easein 1.00 xcenter 630
                    $c_f_t_hider()
                    hide cft_pole
                    call ch1_loop


    elif result == 'O':
        if persistent.f_game == 1:
            n r1d "Это было как–то слишком просто."
            n "Только не нужно унывать, если хочешь можем сыграть ещё раз."
            n "В конце концов, это просто игра."
            n r1f "Может быть ты хочешь отыграться?"
            show natsuki r1c
            menu:
                "Да.":
                    n r1d "Тогда давай начнём!"
                    $persistent.f_game = 2
                    $renpy.save_persistent()
                    $c_f_t_hider()
                    $initialize_game()
                    $c_f_t_ans(sside)
                "Нет.":
                    n r1e "Почему?"
                    n r1f "Неужели боишься проиграть?"
                    n r1d "Ладно, тогда в другой раз."
                    show natsuki r1c
                    $persistent.f_game = 2
                    $renpy.save_persistent()
                    if sside == "left":
                        show natsuki r1:
                            xcenter 330
                            easein 1.00 xcenter 630
                    if sside == "right":
                        show natsuki r1:
                            xcenter 930
                            easein 1.00 xcenter 630
                    $c_f_t_hider()
                    hide cft_pole
                    call ch1_loop

        elif persistent.f_game == 2:
            $r_ans = random.randint(1,3)
            if r_ans == 1:
                n r1g "Безупречная победа!"
                n r1f "Как насчёт реванша?"
                show natsuki r1c
            if r_ans == 2:
                n r1g "Да ладно, я выиграла!"
                n r1f "Я думаю ты хочешь поквитаться со мной."
                n r1d "Что думаешь на этот счёт?"
                show natsuki r1c
            if r_ans == 3:
                n r1d "Хорошая игра!"
                n "Хочешь сыграть ещё раз?"
                show natsuki r1c

            menu:
                "Да.":
                    n r1d "Тогда чего мы ждём?"
                    n "Погнали!"
                    $c_f_t_hider()
                    $initialize_game()
                    $c_f_t_ans(sside)
                "Нет.":
                    n r1b "М?"
                    n r1e "Ну, ладно, как хочешь."
                    n "Если что, можем сыграть позже."
                    show natsuki r1b
                    if sside == "left":
                        show natsuki r1:
                            xcenter 330
                            easein 1.00 xcenter 630
                    if sside == "right":
                        show natsuki r1:
                            xcenter 930
                            easein 1.00 xcenter 630
                    $c_f_t_hider()
                    hide cft_pole
                    call ch1_loop



    elif result == '.':
        if persistent.f_game == 1:
            n r1d "Ого, ничья?"
            n "Думаю, это справедливо для первой игры."
            n r1f "Хотя, почему бы не сыграть потом ещё раз?"
            show natsuki r1c
            $persistent.f_game = 2
            $renpy.save_persistent()
            if sside == "left":
                show natsuki r1:
                    xcenter 330
                    easein 1.00 xcenter 630
            if sside == "right":
                show natsuki r1:
                    xcenter 930
                    easein 1.00 xcenter 630
            $c_f_t_hider()
            hide cft_pole
            call ch1_loop

        elif persistent.f_game == 2:
            $r_ans = random.randint(1,2)
            if r_ans == 1:
                n r1e "Ну, в этот раз победителей нет."
                n r1d "Должны ли мы сыграть ещё раз, чтобы определить настоящего победителя?"
                show natsuki r1c
            if r_ans == 2:
                n "Победила дружба!"
                n "Хочешь сыграть ещё раз?"

            menu:
                "Да.":
                    n r1d "Тогда чего мы ждём?"
                    n "Погнали!"
                    $c_f_t_hider()
                    $initialize_game()
                    $c_f_t_ans(sside)
                "Нет.":
                    n r1b "М?"
                    n r1e "Ну, ладно, как хочешь."
                    n "Если что, можем сыграть позже."
                    show natsuki r1b
                    if sside == "left":
                        show natsuki r1:
                            xcenter 330
                            easein 1.00 xcenter 630
                    if sside == "right":
                        show natsuki r1:
                            xcenter 930
                            easein 1.00 xcenter 630
                    $c_f_t_hider()
                    hide cft_pole
                    call ch1_loop




label change_side:
    pause 5
    $play(None, None, "O", 0, 0)
    if left == True or sside == "left":
        call screen cup_fork_toe("left", None)
    if right == True or sside == "right":
        call screen cup_fork_toe("right", None)






label set_buttons:
    $lr = renpy.random.randint(1,2)
    if lr == 1:
        $left = True
        $right = False
    else:
        $right = True
        $left = False

    $side()
    menu:
        "Режим экрана":
            $ n_f_key = renpy.input("Введи букву, а затем нажми Enter.", length=1)
            $ n_f_key = n_f_key.strip()
            if not n_f_key in r_but and not n_f_key in e_but and not n_f_key.lower() in r_but and not n_f_key.lower() in e_but:
                n r1e "Эй, дурашка, я же сказала тебе – только латиница."
                n "Не ломай игру, пожалуйста."
                show natsuki r1b
                jump set_buttons
            elif n_f_key == persistent.f_key or n_f_key.lower() == persistent.f_key:
                n "Эй, не издевайся над игрой!"
                n "Тут и так всё кое-как работает..."
                n "Не ставь одинаковые клавиши, пожалуйста."
                n "Надеюсь ты просто случайно ошибся."
                show natsuki r1b
                jump set_buttons
            else:
                $ persistent.f_key = n_f_key
                if persistent.f_key in r_but or persistent.f_key.lower() in r_but:
                    $ persistent.f_r_key = persistent.f_key
                    $ persistent.f_key = r_to_e(persistent.f_r_key)
                else:
                    $ persistent.f_r_key = r_to_e(persistent.f_key)
                $ renpy.save_persistent()
                if renpy.get_screen("set_on_full"):
                    show screen set_on_window
                else:
                    show screen set_on_full

                call ch1_loop

        "Музыка" if persistent.ch_vol == True:
            $ n_v_key = renpy.input("Введи букву, а затем нажми Enter.", length=1)
            $ n_v_key = n_v_key.strip()
            if not n_v_key in r_but and not n_v_key in e_but and not n_v_key.lower() in r_but and not n_v_key.lower() in e_but:
                n r1e "Эй, дурашка, я же сказала тебе – только латиница."
                n "Не ломай игру, пожалуйста."
                show natsuki r1c
                jump set_buttons
            elif n_v_key == persistent.v_key or n_v_key.lower() == persistent.v_key:
                n "Эй, не издевайся над игрой!"
                n "Тут и так всё кое-как работает..."
                n "Не ставь одинаковые клавиши, пожалуйста."
                n "Надеюсь ты просто случайно ошибся."
                show natsuki r1b
                jump set_buttons
            else:
                $ persistent.v_key = n_v_key
                if persistent.v_key in r_but or persistent.v_key.lower() in r_but:
                    $ persistent.v_r_key = persistent.v_key
                    $ persistent.v_key = r_to_e(persistent.v_r_key)
                else:
                    $ persistent.v_r_key = r_to_e(persistent.v_key)
                $ renpy.save_persistent()
                call ch1_loop



        "Звуки" if persistent.ch_vol == True:
            $ n_s_key = renpy.input("Введи букву, а затем нажми Enter.", length=1)
            $ n_s_key = n_s_key.strip()
            if not n_s_key in r_but and not n_s_key in e_but and not n_s_key.lower() in r_but and not n_s_key.lower() in e_but:
                n r1e "Эй, дурашка, я же сказала тебе – только латиница."
                n "Не ломай игру, пожалуйста."
                show natsuki r1c
                jump set_buttons
            elif n_s_key == persistent.s_key or n_s_key.lower() == persistent.s_key:
                n "Эй, не издевайся над игрой!"
                n "Тут и так всё кое-как работает..."
                n "Не ставь одинаковые клавиши, пожалуйста."
                n "Надеюсь ты просто случайно ошибся."
                show natsuki r1b
                jump set_buttons
            else:
                $ persistent.s_key = n_s_key
                if persistent.s_key in r_but or persistent.s_key.lower() in r_but:
                    $ persistent.s_r_key = persistent.s_key
                    $ persistent.s_key = r_to_e(persistent.s_r_key)
                else:
                    $ persistent.s_r_key = r_to_e(persistent.s_key)
                $ renpy.save_persistent()
                call ch1_loop


        "Плеер" if persistent.ch_mus == True:
            $ n_m_key = renpy.input("Введи букву, а затем нажми Enter.", length=1)
            $ n_m_key = n_m_key.strip()
            if not n_m_key in r_but and not n_m_key in e_but and not n_m_key.lower() in r_but and not n_m_key.lower() in e_but:
                n r1e "Эй, дурашка, я же сказала тебе – только латиница."
                n "Не ломай игру, пожалуйста."
                show natsuki r1c
                jump set_buttons
            elif n_m_key == persistent.m_key or n_m_key.lower() == persistent.m_key:
                n "Эй, не издевайся над игрой!"
                n "Тут и так всё кое-как работает..."
                n "Не ставь одинаковые клавиши, пожалуйста."
                n "Надеюсь ты просто случайно ошибся."
                show natsuki r1b
                jump set_buttons
            else:
                $ persistent.m_key = n_m_key
                if persistent.m_key in r_but or persistent.m_key.lower() in r_but:
                    $ persistent.m_r_key = persistent.m_key
                    $ persistent.m_key = r_to_e(persistent.m_r_key)
                else:
                    $ persistent.m_r_key = r_to_e(persistent.m_key)
                $ renpy.save_persistent()
                call ch1_loop


        "Тема":
            $ n_t_key = renpy.input("Введи букву, а затем нажми Enter.", length=1)
            $ n_t_key = n_t_key.strip()
            if not n_t_key in r_but and not n_t_key in e_but and not n_t_key.lower() in r_but and not n_t_key.lower() in e_but:
                n r1e "Эй, дурашка, я же сказала тебе – только латиница."
                n "Не ломай игру, пожалуйста."
                show natsuki r1c
                jump set_buttons
            elif n_t_key == persistent.t_key or n_t_key.lower() == persistent.t_key:
                n "Эй, не издевайся над игрой!"
                n "Тут и так всё кое-как работает..."
                n "Не ставь одинаковые клавиши, пожалуйста."
                n "Надеюсь ты просто случайно ошибся."
                show natsuki r1b
                jump set_buttons
            else:
                $ persistent.t_key = n_t_key
                if persistent.t_key in r_but or persistent.t_key.lower() in r_but:
                    $ persistent.t_r_key = persistent.t_key
                    $ persistent.t_key = r_to_e(persistent.t_r_key)
                else:
                    $ persistent.t_r_key = r_to_e(persistent.t_key)
                $ renpy.save_persistent()
                call ch1_loop


        "{i}[ans]{/i}":
            $side_return()
            $r_ans = random.randint(1,2)
            if r_ans == 1:
                n "Передумал менять управление?"
                n "Ну, ладно, поменяешь потом, если надо будет."
            else:
                n "Ты уже всё?"
                n "А где изменения?"
                n "В любом случае, поступай как хочешь."
                n "Тебе ведь этими клавишами пользоваться, а не мне."

            call ch1_loop






label what_was_that:
    pause 2
    n r1e "Ой, что произошло?"
    n "Кажется у плеера всё–таки есть повреждённый код."
    n "Здесь должен был быть визуализатор."
    n r1d "Ну, знаешь, эти полоски, которые дрыгаются под ритм музыки."
    n r1b "Похоже, придётся разбираться..."
    scene black
    with Dissolve(1)
    pause 10
    n "Хм-м-м-м..."
    pause 15
    n r1e "И почему всё так сложно?!"
    n "Придётся тебе немного подождать."
    n "Движок игры не сильно дружит с такими штуками."
    n r1b "Пожелай удачи хоть..."
    $persistent.set_broke = False
    $renpy.save_persistent()
    pause 149
    n "Да неужели?"
    n "Опять?"
    n "И зачем я только согласилась?.."
    pause 3
    call natsuki_room
    show natsuki r1 zorder 2
    with Dissolve(1)
    n r1e "В общем, теперь всё должно работать, но... {w}Есть небольшие визуальные баги..."
    n r1d "Зато теперь все функции плеера, пусть и с глюками, но пашут!"
    n r1f "Это тебе не просто пару строчек в файлах сменить, да, Моника?!"
    pause 1
    n r1c "Кхм, прости..."
    n r1e "Пользуйся, только ничего не сломай, ладно?"
    n r1m "Потому что второй раз я переписывать ничего не собираюсь!"

    $persistent.is_glitching = False
    $persistent.fix = True
    $renpy.save_persistent()

    call ch1_loop



label mob_vol:
    show screen vol_mob_enable_change
    $ui.interact()
    jump mob_vol


label mob_sound:
    show screen sound_mob_enable_change
    $ui.interact()
    jump mob_sound
