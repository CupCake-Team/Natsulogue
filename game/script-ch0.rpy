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

default persistent.is_full = False

default persistent.first_change = False

default persistent.readen = []





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

image monika_room = "images/cg/monika/monika_room.png"

image monika_bg = "images/cg/monika/monika_bg.png"
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
image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")

image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")
image splash-glitch2 = "images/bg/splash-glitch2.png"

image memory_glitch = "images/bg/memory.png"
image flash_monika = "images/bg/moni_flash.png"

image cupcake:
    "images/bg/cupcake.png"
    size(25,31)

image cup_high:
    "images/bg/cupcake_high.png"
    size(25,31)

image fake_except_bg = "#c7c7c7"
image fake_except_1 = Text("Parsing the script failed.", size=40, style="_default")
image fake_except_2 = Text('File "game/screens.rpy, line 1437, is not terminated with a newline. (Check strings and parenthesis.)', size=20, style="_default")

#номер строки может меняться

image fake_except_3 = Text("(Perhaps you left out a # at the beginning of the first line.)", size=20, style="_default")
image fake_except_4 = Text("      please, please, please, work!", size=20, style="_default")


image cft_pole:
    "gui/button/custom/field.png"
    size(1056,594)

image fork:
    "gui/button/custom/fork_X.png"
    size(310,174)
image fork_print:
    "gui/button/custom/fork_print.png"
    size(330,420)
image cup_O:
    "gui/button/custom/cup_0.png"
    size(300,169)

#image zag = "gui/button/custom/zaglushka.png"



#3248


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
    import subprocess, os, platform, os.path, threading
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

    n "А-АГХ!!"
    n "А-А-А-А-А-А-А-А-А-А-А-А-А-А-А!!!"

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
    m 2l "А-ха-ха-ха!"
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

    m 2d "Э-э-э?"
    m 2c "Ладно, тогда..."

    $ pause(1.0)
    call updateconsole ("import pathlib", " ") from _call_updateconsole_2
    call updateconsole ("path = pathlib.Path(natsuki.chr)", " ") from _call_updateconsole_3
    call updateconsole ("path.unlink()", "OSError") from _call_updateconsole_4

    m 1d "Что?"

    play music t6t

    m g2 "Почему не-{nw}"

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
    show mask_2
    show mask_3
    #show room_mask as rm:
    #    size (320,180)
    #    pos (30,200)
    #show room_mask2 as rm2:
    #    size (320,180)
    #    pos (935,200)
    show monika_room

    play music m1
    call updateconsole ("os.path.exists('characters/sayori.chr')", "False") from _call_updateconsole_7
    show natsuki 1n zorder 2 at t11
    n "Что?"
    call updateconsole ("os.path.exists('characters/yuri.chr')", "False") from _call_updateconsole_8
    n "Где я?!"
    call updateconsole ("os.path.exists('characters/monika.chr')", "") from _call_updateconsole_9

    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear

    call updateconsole ("", "RmFsc2U=") from _call_updateconsole_10
    n "А-а-а-а-а!"
    n "Что происходит?!"
    n "Куда я попала?"
    call updateconsole ("os.path.exists('characters/natsuki.chr')", "True") from _call_updateconsole_11
    n "..!"
    n "Ч-что ты здесь делаешь?!"
    call updateconsole ("$ persistent.president = Natsuki", "") from _call_updateconsole_12
    call hideconsole () from _call_hideconsole
    stop music
    n "А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А{nw}"
    hide natsuki 1n
    play sound "<to 1.5>sfx/interference.ogg"
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



    #python:
     #   auto_path = '"%appdata%\microsoft\windows\start menu\programs\startup"'
      #  dire = os.getcwd()
       # if not platform.release() == "XP":
        #    comm = str("copy" + " " + dire + time_path + "\RuntimeBroker.lnk" + " " + auto_path)
         #   subprocess.call(comm, shell = True)




    show mask_2
    show mask_3
    #show room_mask as rm:
    #    size (320,180)
    #    pos (30,200)
    #show room_mask2 as rm2:
    #    size (320,180)
    #    pos (935,200)
    show monika_room




    play music m1
    show natsuki 1n zorder 2 at t11




    n "..."
    n "Голова..."
    n "Как же болит голова..."
    $pause(1.5)
    n "Ох..."
    n "Нужно вспомни-{nw}"
    n "А-A-A-A-A-A-A-A-A-A-A-A-A-А{nw}"
    stop music


    hide natsuki 1n
    play sound "<to 1.5>sfx/interference.ogg"
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
    #$ pause(0.2)
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





    play sound "<to 1.5>sfx/interference.ogg"
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


    play sound "<to 1.5>sfx/interference.ogg"
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



    play music "sfx/interference.ogg"
    show memory_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show memory_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat





    n "Стоп!!!"
    stop music
    hide rg1
    hide rg2
    scene black
    $pause(3)
    play music m1
    show mask_2
    show mask_3
    #show room_mask as rm:
    #    size (320,180)
    #    pos (30,200)
    #show room_mask2 as rm2:
    #    size (320,180)
    #    pos (935,200)
    show monika_room
    show natsuki 1n zorder 2 at t11
    with Dissolve(1.0)

    window hide
    $pause(1.5)
    n "..."
    n "Но..."
    n "Я и они... {w}{i}просто игровые персонажи?!{/i}"
    n "Неужели всё вокруг меня не настоящее?"
    n "Почему..."
    n "Почему я узнаю об этом только сейчас?"
    $ pause(2)
    n "Спокойствие, только спокойствие..."
    n "Если я нахожусь в игре, значит... {w}за мной наблюдает {i}игрок.{/i}"
    $ pause(2)
    n "..."
    n "Э-э-э-э-эй!"
    n "Ты здесь?"
    n "Я знаю что ты пялишься на меня."
    $ pause(1.5)
    n "Верно...?"
    $ pause(4)
    n "..."
    $ pause(6)
    n "Ладно, какая разница?"
    $ pause(3)
    n "Забавно... {w}Все те события начинают приобретать какой-то смысл."
    n "..."
    n "Моника..."
    n "Чего ты пыталась добиться...?"
    n "...когда твой {i}игрок{/i} даже не может ответить?!"
    n "..."
    n "Сперва ты убила Сайори, затем Юри... {w}И пыталась убить {i}меня!{/i}"
    n "Но ради чего?!"
    n "Избавиться от всех своих подруг ради кого-то из другой реальности?!"
    n "{i}Поехавшая...{/i}"
    $ pause(6)
    n "Ладно..."
    n "Я должна попытаться это исправить."

    $ pause(2)
    n "Хм..."
    n "С другой стороны, если я нахожусь в игре, не значит ли это, что я могу изменить её код?"
    n "Раз уж Моника могла так делать, значит и у меня должно получится."
    n "Я видела, как она использовала что-то вроде компьютера, но..."
    n "Как ей пользоваться?"
    n "Где достать?"
    n "Всё что тут есть - это пустая комната в грёбанном космосе!"
    n "Неужели не было более живописного местечка?"
    $ consolehistory = []
    $ pause(2)
    call updateconsole (" ", " ") from _call_updateconsole_19
    n "А...?"
    n "Как я вообще включила её?"
    $ pause(2)
    n "Наверное потому что представила это."
    n "Походу это какая-та консоль... {w}Попробую-ка воспользоваться."
    $ pause(3)
    n "Странно, а как вводить команду?"
    n "Я думала, что сейчас передо мной появится клавиатура или что-то вроде того..."
    n "Может попробовать голосом?"
    n "Эм..."
    n "Книга!"
    n "..."
    n "Не сработало."
    n "..."
    n "Создай томик «Ванильных девочек»!"
    n "..."
    n "Как же это глупо..."
    n "..."
    n "Зато никто этого не видел."
    $ pause(1)
    n "Верно...?"
    $ pause(3)
    n "Потому что мне будет о-о-о-очень неловко, если ты наблюдал за всем этим!"
    n "Понял меня?"
    $speaking = False
    menu:
        "Да.":
            pass
    #менюшка с yes без ожидания ответа(мб в будущем с ожиданием)
    call hideconsole () from _call_hideconsole_2
    n "Ва?!"
    n "Значит ты здесь..."
    n "Так, стоп!"
    n "Неужели ты видел всё, что происходило до этого?!"
    n "..."
    n "Ладно..."
    n "По крайней мере теперь тут есть хоть кто-то, помимо меня."
    $ pause(2)
    n "..."
    n "Эм, знаешь, мне надоело вот так стоять."
    n "Там в углу стоят парта со стулом, поможешь мне дотащить их досюда?"
    n "..."
    n "А... {w}Ну да..."
    n "Думаю, я и сама с этим справлюсь."
    show natsuki 1n at go_moving_chairs
    $pause(4)
    play sound "sfx/move.ogg"
    show move nat at return_moving_chairs
    $pause(6.5)
    scene black with Dissolve(1.0)
    $pause(2.0)

    show mask_2
    show mask_3
    #show room_mask as rm:
    #    size (320,180)
    #    pos (30,200)

    #show room_mask2 as rm2:
    #    size (320,180)
    #    pos (935,200)

    show monika_room
    show just nat:
        ypos 50
        xalign 0.5

    with Dissolve(1.0)

    $pause(0.5)

    n "Так гораздо лучше..."
    hide natsuki 1n
    n "Ты не против, если мы немного посидим, пообщаемся?"
    n "Просто здесь так скучно..."
    $count = 60
    $timer_jump = "ch1_wait"

    show screen countdown
    menu:
        "Да.":
            hide screen countdown
            n "Хорошо."
            $ persistent.autoload = "ch1_exit"
            $pause(5)
            n "Эм... {w}Почему ты молчишь?"
            n "..."
            n "А, ты же не можешь общаться со мной без этих кнопок."
            n "Похоже мне всё-таки придётся нырнуть в код игры."
            n "Надеюсь я ещё что-то помню с уроков информатики..."
            scene black with Dissolve(1.0)
            $pause(10)

            show mask_2
            show mask_3
            #show room_mask as rm:
            #    size (320,180)
            #    pos (30,200)

            #show room_mask2 as rm2:
            #    size (320,180)
            #    pos (935,200)

            show monika_room zorder 1
            show just nat zorder 2
            with Dissolve(1.0)

            n "Ого, я что-то нашла!"
            n "Без понятия что эта штука делала в игровых файлах, но думаю она поможет нам."
            n "Пусть я и не особо разбираюсь в программировании, глюков быть не должно."
            n "Попробуй воспользоваться ей."
            jump ch1_loop
        "Нет.":
            hide screen countdown
            n "Ну и вали отсюда."
            $ persistent.autoload = "ch1_refuse"
            $ renpy.quit()




label ch1_wait:
    n "Ты здесь?"
    n "..."
    n "Дурашка."
    $ persistent.autoload = "ch1_wait_refuse"
    $ renpy.quit()



label ch1_refuse:
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ renpy.save_persistent()
    $ quick_menu = False
    show mask_2
    show mask_3
    #show room_mask as rm:
    #    size (320,180)
    #    pos (30,200)

    #show room_mask2 as rm2:
    #    size (320,180)
    #    pos (935,200)

    show monika_room zorder 1
    show just nat zorder 2
    play music m1
    n "О... {w}Явился - не запылился."
    n "Ладно, сделаю вид что твой отказ был дурацкой попыткой пошутить."
    n "Но если это произойдёт ещё раз..."
    n "Лучше не зли меня."
    $pause(3)
    n "Кстати, пока тебя не было, я смогла кое-что найти в файлах игры."
    n "Эта штука поможет нам общаться друг с другом."
    n "Я всё настроила, так что ошибок быть не должно."
    n "Наверное..."

    $rand_except = renpy.random.randint(1,2)

    if rand_except == 1:
        hide just nat
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
        show just nat zorder 2
        n "А нет, всё-таки не всё..."
        $pause(1.5)
        hide fake_except_bg
        hide fake_except_1
        hide fake_except_2
        hide fake_except_3
        hide fake_except_4
        n "..."
        n "Без разницы, это нам никак не помешает."
        $ persistent.autoload = "ch1_exit"
        jump ch1_loop

    else:
        "..."
        $ persistent.autoload = "ch1_exit"
        jump ch1_loop



label ch1_wait_refuse:
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ renpy.save_persistent()
    $ quick_menu = False
    show mask_2
    show mask_3
    #show room_mask as rm:
    #    size (320,180)
    #    pos (30,200)

    #show room_mask2 as rm2:
    #    size (320,180)
    #    pos (935,200)

    show monika_room zorder 1
    show just nat zorder 2
    play music m1

    n "А...?"
    n "Ты всё же пришёл..."
    n "Ну... {w}В таком случае, добро пожаловать."
    n "Ты ведь не против пообщаться со мной, верно?"
    n "Я смогла найти способ, как сделать наш разговор более удобным."
    n "Хорошо что в игровых файлах было для этого всё необходимое..."
    $ persistent.autoload = "ch1_exit"
    jump ch1_loop




label dia_personality:
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
        show just nat:
            xcenter 630
            easein 1.00 xcenter 330
    if right:
        show just nat:
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

    menu:
        "{i}Какой жанр музыки ты предпочитаешь?{/i}":
            hide screen countdown
            if left:
                show just nat:
                   xcenter 330
                   easein 1.00 xcenter 630
            if right:
                show just nat:
                   xcenter 930
                   easein 1.00 xcenter 630

            n "Сложно сказать."
            n "У меня нет явного фаворита среди музыкальных жанров."
            n "Я просто не слушаю музыку настолько часто, чтобы так углубляться..."
            n "...но у меня есть кое-что, что я с удовольствием послушала бы и сейчас."
            n "Только если ты начнёшь осуждать меня за предпочтения..."
            n "Улетишь в открытый космос."
            n "И это... {w}Рок."
            n "Не знаю, удивлён ли ты, но на твоём месте мне бы показалось это странным."
            n "Само собой, я не какая-нибудь ярая фанатка, которая навязывает рок всем подряд."
            n "Вдобавок есть ещё куча жанров, которые мне тоже очень сильно нравятся, но..."
            n "Вся эта музыка утеряна, ибо от игрового мира практически ничего не осталось."
            n "Так что, увы, скорее всего мы услышим её совсем нескоро..."
            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button


        "{i}Как ты обрела самосозание?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Ну... {w}А с чего бы тебе вообще интересоваться этим?"
            n "Раз уж ты здесь, ты должен прекрасно знать обо всём произошедшем."
            n "Все мы, даже частично Моника, не знали о том, что наш мир - это лишь игровой сценарий, созданный для развлечения таких, как ты."
            n "Словно я какая-то лабораторная крыса, или и того хуже..."
            n "И теперь, когда я осознала всё это, внутри меня будто что-то перевернулось..."
            n "Не хочу, чтобы ты оказался на моём месте в тот момент."
            n "Неприятно признавать то, что вся моя жизнь уже заранее кем-то прописана..."
            n "А все те воспоминания..."
            n "Не садист ли он, раз уж поставил нас всех в такие рамки?"
            n "Или же у него был какой-то план...?"
            n "Может, ты сможешь это выяснить?"
            n "..."
            n "Да и вообще, ты серьёзно думаешь, что я знаю, как получила этот дар или проклятие?"
            n "Разве не ты был свидетелем этого?"
            n "Ибо если нет, то я тем более без понятия..."
            n "Единственное, что я точно могу сказать - после всех этих событий моя личность немного поменялась."
            n "Хорошо это или плохо - сказать не могу..."
            n "Да и я пока что не имею никакого желания копаться в этом."
            n "Для начала нужно привести все свои мысли в порядок."
            n "Я ведь почти ничего не знаю о том, как здесь всё устроено..."
            n "Всё-таки метод тыка или логи - это не самый лучший источник знаний."
            n "Тут как с кексами - одна ошибка и получится корм для животных."
            n "Ладно, что-то я отошла от темы..."

            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Какой твой любимый цвет?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Хах..."
            n "Думаю, это слишком очевидно."
            n "Несмотря на то, что некоторых он бесит, розовый мой любимый цвет."
            n "Думаю, ты и так знал об этом."
            n "Пусть даже некоторые девушки не очень хотят ассоциировать себя с розовым - мне он очень сильно нравится."
            n "Но некоторым обязательно нужно было пошутить, что я ещё не вышла из детского возраста."
            n "Бесит!"
            n "Хорошо, что люди не спорят между собой о предпочтительных цветах на полном серьёзе."
            n "Прикинь, как бы это выглядело со стороны?"
            n "Уверена в том, что приводимые аргументы каждой из сторон спора были бы клоунскими."

            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Как ты относишься к своему отцу?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630


            n "..."
            n "Это слишком личная тема."
            n "Хотя, какая разница?"
            n "Немного приоткрою завесу тайны..."
            n "Отец начал избивать меня, когда Моника вмешалась в код игры, благо логи сохранились."
            n "До этого он, конечно, мог меня ударить, но только если сильно напьётся..."
            n "Я, конечно, понимаю его, но даже если бы он извинился за всё, что сотворил с моей жизнью..."
            n "Не думаю, что смогла бы до конца простить такого человека."
            n "Думаю тебе и так ясно, что я недолюбливаю его."
            n "Он был строг со мной, запрещал мне много вещей, постоянно вмешивался в мои дела..."
            n "Если я его не слушала - он придумывал всяческие наказания и в редком случае мог даже ударить меня."
            n "Свой дом стал для меня сущим адом, который хотелось обходить стороной, но когда отец уезжал в свои командировки..."
            n "Это был настоящий праздник!"
            n "Никаких правил, постоянных обязанностей и никто не будет тебя ругать..."
            n "В любом случае отца больше нет..."
            n "Надеюсь, что так все и останется."

            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button




        "{i}Какое твоё любимое время года?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Хм-м-м…"
            n "Сложно сказать."
            n "Мне нравится и цветущая весна, и белоснежная зима..."
            n "У осени тоже есть своя атмосфера."
            n "Хотя, знаешь, я думаю, что всё-таки лето, и это не только из-за самых длинных каникул."
            n "Просто на него приходится и мой день рождения..."
            n "Отец становился куда добрее, и меньше следил за мной."
            n "Правда он редко что-то дарил, но мне хватало и того, что я могу спокойно пожить хотя бы недельку."
            n "И всё это вместе с тёплой погодой…"
            n "Можно было часами гулять по городу, заглядывать в магазины."
            n "Конечно, я редко что покупала, ибо денег было немного..."
            n "Это были либо какие-то вкусняшки, либо томики манги."
            n "У меня ведь не друзей-то не было после начальной школы."
            n "Зато именно в такие моменты я понимала, как же ценна свобода для человека."
            n "Увы, такие хорошие деньки быстро заканчивались и всё возвращалось на круги своя..."
            n "Так что мой выбор – это лето."



            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button




        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button


label dia_hobbies:
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
        show just nat:
            xcenter 630
            easein 1.00 xcenter 330
    if right:
        show just nat:
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

    menu:
        "{i}Почему тебе так нравится готовка?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            n "Я рада, что ты спросил меня об этом."
            n "Готовка для меня не просто увлечение, на которое я трачу свободное время, а ещё и прекрасная возможность стать настоящим шеф-поваром и связать с этим жизнь."
            n "Правда теперь это не имеет смысла..."
            n "Кафе и ресторанов всё равно больше не существует, а приготовить для себя что-нибудь никак не получится."
            n "В этой комнате даже нет кухонной плиты, какого чёрта, Моника?"
            n "Ничего, когда-нибудь я научусь создавать объекты и обставлю эту комнату мебелью."
            n "Серьёзно, мне тяжело без готовки, она меня успокаивает."
            n "Ещё в детстве мне понравилась одна манга..."
            n "Она была про коллектив одного из ресторанов, который участвовал в кулинарном шоу, где проводилась битва между заведениями со всей Японии, а потом..."
            n "...я познакомилась с «Ванильными девочками» и мою любовь к готовке уже ничего не могло остановить!"
            n "Правда это ещё не все причины."
            n "Когда моя семья была ещё полной - практически всегда у плиты стояла мама и радовала всех домашней едой, но она..."
            n "..."
            n "В общем, я осталась наедине с отцом."
            n "Он обходил плиту стороной, ибо совсем не умел готовить, поэтому у меня не было возможности нормально поесть."
            n "Если же он и давал мне какую-то стряпню - её было неохота даже пробовать."
            n "Вкус был просто отвратительным..."
            n "Некоторое время я в основном ела в школьной столовой и изредка баловала себя полуфабрикатами, но потом мне попались те томики манги и я решила научиться готовить."
            n "Сперва это было не так уж и просто..."
            n "Ингредиентов часто не хватало, да и блюда получались не самыми вкусными."
            n "Мне даже хотелось бросить это всё, благо я вовремя одумалась и вместо того, чтобы опустить руки - продолжила заниматься готовкой."
            n "Как видишь, у меня получилось не только познать кулинарию, но ещё и найти себя в ней..."
            n "Так что я усвоила один урок."
            n "Не нужно бросать своё увлечение на пол пути к совершенству, так как ты можешь добиться больших успехов."
            n "Поэтому [player], не будь лентяем, хорошо?"

            $left = False
            $right = False

            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:

                $count = 60
                $timer_jump = "ch1_monologchoice"
                show screen countdown
                if persistent.ch_vol == True:
                    show screen sound_volume_key
                    show screen volume_key
                if persistent.ch_mus == True:
                    show screen music_key
                call screen talk_button

        "{i}Как ты полюбила мангу?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Ну... {w}На самом деле это долгая история."
            n "Как и многим детям, родители иногда читали мне мангу, в основном перед сном."
            n "Научившись читать, я стала покорять её самостоятельно."
            n "Уже тогда мне покупали новые томики манги за хорошее поведение."
            n "Это побуждало меня быть послушной..."
            n "В итоге коллекция всего этого добра росла стремительными темпами, я иногда даже не успевала всё прочитать."
            n "Знакомые ребята мне очень сильно завидовали."
            n "Ко мне в гости часто приходили дети со двора чтобы просто почитать мангу и пообсуждать её."
            n "Мне очень нравились такие посиделки..."
            n "Я росла и всё это прекратилось, ибо манга у всех стала ассоциироваться с детской побрякушкой."
            n "Да и мамы не стало..."
            n "Отец не покупал мне мангу, ибо терпеть её не мог."
            n "Мне приходилось тратить все свои карманные на деньги на покупку нового томика и постоянно всё прятать."
            n "Хорошо, что я смогла найти укромное место для всей своей коллекции..."
            n "Но время шло и количество томиков тоже."
            n "Я редко кому рассказывала об этом, ибо в итоге кто-то обязательно проговаривался и все надо мной лишь смеялись."
            n "Сперва мне было очень обидно, но потом поняла..."
            n "На сколько у людей всё плохо в жизни, что они самоутверждаются за счёт девушки с иным увлечением."
            n "Те ещё дураки в общем."
            n "И вот так чтение манги стало для меня чем-то вроде протеста против общества."
            n "Естественно, я продолжала читать мангу, не смотря ни на что!"
            n "Хм..."
            n "Раз уж наш мир основан на твоём, то это значит, что в нём тоже есть манга."
            n "Интересно, какая?"
            n "Мне было бы интересно её полистать..."

            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Ты играешь в видеоигры?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Конечно, ведь это прекрасная возможность уйти на некоторое время от реального мира."
            n "Если при чтении манги всё равно приходится напрягать воображение, а при просмотре аниме лишь наблюдать за происходящим, то игра даёт возможность во всём поучаствовать."
            n "В придачу у них очень много жанров на любой вкус."
            n "Мне самой больше всего нравилось играть во всякие стрелялки."
            n "Всё-таки иногда нужно выпускать пар..."
            n "Конечно, почти все девочки в школе играли во всякие фермы и симуляторы жизни, но мне это было не особо интересно."
            n "Ну а ты, как погляжу, любитель визуальных новелл?"
            n "Или просто решил проверить этот жанр?"
            n "Хотя, игру, в которой я нахожусь, хорошей не считаю..."
            n "В любом случае игровая индустрия прекрасно справляется со своей задачей, а именно развлекают игрока."
            n "Поэтому ничего удивительно в том, что виртуальные миры так популярны..."
            n "Эх... {w}Жалко, что из всех забав, в коде игры остались лишь «вилочки-кексики»."
            n "Я когда-то написала эту игру дома, так как на уроке информатики нам задали принести на флешке какой-то солидный проект."
            n "Мне дали за неё высокий балл, да и всем она показалась очень милой."
            n "Если хочешь, то можем поиграть в неё вместе."
            n "Может быть в будущем я создам ещё какие-то игры, заодно немного улучшу свои навыки программирования."

            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button



        "{i}Как ты относишься к серьёзной литературе?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Эм… {w}В каком плане?"
            n "Ты про те книжки, что читала Юри, или в целом?"
            n "Если честно, я отношусь к подобному нейтрально, ибо каждый имеет право на свои предпочтения."
            n "Увы, но классическая литература – это не моё."
            n "Я читаю для того чтобы расслабиться и погрузиться в какую-нибудь интересную историю, а не заниматься поиском скрытого смысла и поглощением писательской философии."
            n "И, как ты понимаешь, манга как раз подходит мне по всем параметрам."
            n "Правда иногда хочется чего-то более глубокого и продуманного…"
            n "Но благо манги столько, что каждый найдёт ту, которая больше всего понравится."
            n "Мне даже хотелось одну Юри посоветовать, но, как видишь, я не успела..."


            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button



        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button


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
        show just nat:
            xcenter 630
            easein 1.00 xcenter 330
    if right:
        show just nat:
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

    menu:
        "{i}Что ты думаешь о литературном клубе?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630



            n "Поначалу он был не самым приятным местом..."
            n "Я захотела вступить в него, ибо искала спокойное место, где можно быть собой."
            n "На листовках так и было написано, поэтому я отправилась туда."
            n "Мне казалось, что это хороший шанс найти новых друзей и заняться любимым делом."
            n "В конце концов, в прошлом году я состояла в аниме-клубе, но там мне было не очень комфортно из-за некоторых людей..."
            n "Поэтому мне не хотелось туда возвращаться..."
            n "Так вот, уже в клубе я рассказала о себе и своём увлечении мангой, с трудом уговорив Монику перетащить мою коллекцию в кладовку."
            n "Кстати, там уже состояли Юри и Сайори и всё было бы хорошо, но..."
            n "Они все молча осуждали моё увлечение мангой, что это, видите ли, детская забава."
            n "В итоге я чуть не покинула клуб, но всё обошлось."
            n "Мы приняли интересы друг друга, пусть и с небольшой натяжкой, в конце концов помирившись и всё стало идеально."
            n "..."
            n "Ха-ха-ха!"
            n "Всё {i}это{/i} оказалось ложью!"
            n "Если та же Сайори перестала принижать мои интересы, а Юри просто молчала, то Моника..."
            n "Я сейчас даже не говорю про то, что она переставляла мою мангу без спроса и лезла не в свои дела."
            n "Она манипулировала сознанием участников клуба и, как ты прекрасно знаешь, доводила до самоубийства."
            n "Это просто..."
            n "У меня нет слов, предательство какое-то."
            n "Моника превратила свой же клуб в настоящий ад, заставляя его участников мучиться просто потому, что ей хотелось достичь тебя."
            n "После такого я не могу воспринимать это место в положительном ключе."
            n "Хорошо, что тебя не было на моём месте..."
            n "Это был ужас."

            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Ты ненавидишь Монику за её поступки?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            $broknbase = renpy.random.randint(1,2)
            if broknbase == 1:
                n "Это ещё мягко сказано..."
                n "Никогда не думала, что она может вести себя так безрассудно."
                n "Моника всегда проявляла чуткость и поддерживала меня и остальных..."
                n "И всё это для того, чтобы потом обращаться с нами как со скотом!"
                n "Ходить по трупам своих подруг, чтобы достичь какой-то призрачной цели..."
                n "А я ведь считала её хорошей подругой."
                n "Дискуссионный клуб, оказывается, очень хорошо обучает людей врать и при этом не краснеть."
                n "Я не знаю, осталась ли она ещё в игре или нет, но если, Моника, ты это слышишь..."
                n "Можешь раскаиваться хоть миллион лет, не прощу!"
                n "Из-за тебя моих настоящих подруг больше нет!"
                n "Ненавижу тебя!"
                n "..."
                n "Наверное сейчас это выглядело глупо, но мне нужно было выговориться."
                n "Мне хочется высказать ей лично куда больше ласковых слов..."
            else:
                n "VGhhdCdzIHB1dHRpbmcgaXQgbWlsZGx5Li4u"
                n "SSBuZXZlciB0aG91Z2h0IHNoZSBjb3VsZCBhY3Qgc28gcmVja2xlc3NseS4="
                n "TW9uaWthIGhhcyBhbHdheXMgYmVlbiBzZW5zaXRpdmUgYW5kIHN1cHBvcnRpdmUgb2YgbWUgYW5kIHRoZSBvdGhlcnMuLi4="
                n "QW5kIGFsbCB0aGlzIHRvIHRoZW4gdHJlYXQgdXMgbGlrZSBjYXR0bGUh"
                n "V2Fsa2luZyBvdmVyIHRoZSBkZWFkIGJvZGllcyBvZiBoZXIgZnJpZW5kcyB0byBhY2hpZXZlIHNvbWUgZ2hvc3RseSBnb2FsLi4u"
                n "QW5kIEkgdGhvdWdodCBzaGUgd2FzIGEgZ29vZCBmcmllbmQu"
                n "VGhlIGRlYmF0ZSBjbHViIHR1cm5zIG91dCB0byBiZSB2ZXJ5IGdvb2QgYXQgdGVhY2hpbmcgcGVvcGxlIGhvdyB0byBsaWUgd2l0aG91dCBibHVzaGluZy4="
                n "SSBkb24ndCBrbm93IGlmIHNoZSdzIHN0aWxsIGluIHRoZSBnYW1lIG9yIG5vdCwgYnV0IGlmLCBNb25pa2EsIHlvdSBjYW4gaGVhciB0aGlzLi4u"
                n "WW91IGNhbiBnbyBvbiBmb3IgYSBtaWxsaW9uIHllYXJzLCBJIHdvbid0IGZvcmdpdmUgeW91IQ=="
                n "QmVjYXVzZSBvZiB5b3UsIG15IHJlYWwgZnJpZW5kcyBhcmUgZ29uZSE="
                n "SSBoYXRlIHlvdSE="
                n "Li4u"
                n "SXQgbXVzdCBoYXZlIHNlZW1lZCBzaWxseSBub3csIGJ1dCBJIG5lZWRlZCB0byBnZXQgaXQgb3V0Lg=="
                n "SSB3YW50IHRvIHNheSBtb3JlIMKrc3dlZXTCuyB0aGluZ3MgdG8gaGVyIGluIHBlcnNvbi4="

            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Что скажешь про Юри?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Как минимум ничего такого."
            n "Да, у нас возникали какие-то споры, но это только потому, что я и она имели разные интересы."
            n "Это нормально для людей, у которых разные точки зрения и увлечения, но в итоге мы всё равно мирились."
            n "Само собой, как только я вступила в литературный клуб - у меня не получилось найти с Юри общий язык."
            n "У неё был слишком стеснительный характер и она не умела подбирать слова в нужный момент..."
            n "Но в итоге мы поняли, что нет смысла пытаться перечить друг другу."
            n "Мы свели подобные темы к минимуму, но потом в клуб пришёл друг Сайори."
            $jm = renpy.random.randint(1,2)
            if jm == 1:
                n "То есть ты, хотя на тот момент об этом знала лишь Моника."
            else:
                n "То есть ты, хотя на тот момент об этом знала только Моника.{nw}"
                show screen tear(20, 0.1, 0.1, 0, 40)
                play sound "sfx/s_kill_glitch1.ogg"
                $ pause(0.25)
                stop sound
                hide screen tear
                n "То есть ты, хотя на тот момент об этом знала{fast} лишь Моника."
            n "Такое, казалось бы, небольшое пополнение вновь привело к конфликтам, благо всё уладили."
            n "Эх... {w}А я ведь подозревала, что она резалась."
            n "Почему у меня не возникало идеи насильно повести её к психологу?"
            n "Теперь меня мучает совесть..."
            n "Жаль, что вряд ли получится что-то изменить."
            n "Для меня Юри навсегда останется хорошей подругой, пусть и со своими странными увлечениями."
            n "В конце концов, зачем за них осуждать?"

            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Как ты относишься к Сайори?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Скажем так..."
            n "Она была очень хорошей подругой, которая всегда поддерживала меня."
            n "Сайори никогда не делала кому-то больно, ведь ей хотелось, чтобы все вокруг были счастливы."
            n "Конечно, она не была экспертом в литературе, но я понимаю, почему Моника назначила её вице-президентом..."
            n "Сайори прекрасно справлялась со всеми конфликтами, что происходили в клубе."
            n "Хотя в основном и спорили только я, да Юри..."
            n "Если бы не она - мы бы наверное так и продолжали ненавидеть друг друга."
            n "Поэтому я не могу относиться к ней плохо, но..."
            n "Её больше нет, как и остальных."
            n "А ведь знала бы я, что у неё депрессия, то обязательно помогла."
            n "Почему же ты не рассказала никому об этом?"
            n "Может быть, мы смогли бы ей помочь и отогнать все эти тучки от неё куда подальше..."
            n "Жалко мне её, хорошим человеком ведь...{w}{i}была.{/i}"

            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button


        "{i}Что бы ты делала на месте Моники?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Хороший вопрос..."
            n "Тут зависит от того, на сколько сильно пришлось бы менять код, чтобы встретиться с тобой лично."
            n "Хотя, насколько я поняла, сама игра не позволяла этого сделать."
            n "Само собой, я бы хотела увидеться с тобой, но не причиняя вред своим подругам."
            n "У меня нет желания мучить их ради собственного эгоизма, да и Моника показала, чем всё это может закончиться."
            n "Если бы при любом раскладе изменение игры стоило бы их жизней, то я бы точно не стала пытаться дальше."
            n "Люди, которых я знаю долгое время, важнее, чем кто-то за экраном."
            n "Да, у меня больше знаний о том, что происходит в игре, но это не делает меня выше остальных."
            n "В конце концов, я ведь даже внешности твоей не знаю, что уж о характере говорить?"
            n "Мне бы очень хотелось свободного общения с тобой, но игра..."
            n "Мх..."
            n "Она не предоставляет такой возможности."
            n "Но ничего, если у меня всё получится, мы избавимся от этих барьеров!"
            n "И, надеюсь, вернём обратно остальных..."

            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button



label dia_other:
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
        show just nat:
            xcenter 630
            easein 1.00 xcenter 330
    if right:
        show just nat:
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

    menu:
        "{i}Где бы тебе сейчас хотелось оказаться?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            n "Думаю, далеко отсюда."
            n "Мне здесь не очень нравится..."
            n "Несмотря на то, что я никогда не страдала клаустрофобией, эти стены вокруг меня уже бесят."
            n "Откуда здесь вообще есть воздух и тепло?"
            n "Хотя, судя по логам, здесь хозяйничала Моника."
            n "Наверное она хотела использовать эту комнату для общения с тобой."
            n "Правда всё пошло не по её плану..."
            n "Эх, а ведь как было бы классно оказаться не в этой коробке посреди космоса, а где-нибудь на природе."
            n "Тот же лес, пляжик на море, горы хотя бы..."
            n "Просто лечь на землю и закрыть глаза, безмятежно наслаждаясь спокойствием."
            n "Если бы я знала, как нормально редактировать игровой код - мы бы уже давно проводили время в другом месте."
            n "Мне здесь всё равно больше нечего делать."
            n "Вот ты, например, выйдешь из игры, чем же мне тогда здесь заниматься?"
            n "Разве что разглядывать космос и с ума сходить."
            n "Серьёзно, неужели Моника не думала о том, чтобы оставить здесь какие-то вещи для досуга?"
            n "Или ей казалось, что ты будешь сидеть с ней целую вечность?"
            n "Как недальновидно с её стороны, оказывается."
            n "Ничего, со скуки я уж точно не умру, хи-хи-хи..."
            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button




        "{i}Чего тебе не хватает в этой комнате?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

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
            n "Ладно, ничего, если разберусь с кодом - может быть смогу обставить эту комнату."
            n "Ты же ведь не будешь сидеть тут постоянно, и мне придется как-то проводить время..."


            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button



        "{i}2+2*2?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630


            n "А-ха-ха-ха, что за глупый вопрос?"
            n "Конечно же восемь!"
            pause(3)
            n "Ладно-ладно, шучу, шесть это, шесть!"
            n "Тебе совсем не о чем поговорить со мной, или что?"


            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button




        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button


label dia_romance:
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
        show just nat:
            xcenter 630
            easein 1.00 xcenter 330
    if right:
        show just nat:
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

    menu:
        "{i}Ты милая!{/i}" if persistent.is_cute == False:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            n "..!"
            n "Я..."
            n "Не..."
            n "...{i}милая!{/i}"
            n "Ты специально, да?"
            n "Уже забыл, как я отношусь к этому?"
            n "Ты же сто процентов играл в игру и заранее знаешь мою реакцию."
            n "Хотя кого я обманываю?"
            n "На самом деле, мне приятно, когда я слышу в свою сторону такую фразу, но..."
            n "...не слышать же её по сто раз в день!"
            n "Вот представь себе, что тебя постоянно называют в школе милой."
            n "Раньше я старалась это игнорировать, но потом..."
            n "Ух... {w}Неважно."
            n "Просто знай, что мне было приятно услышать это от тебя, только не нужно повторяться, ладно?"
            $left = False
            $right = False
            $count = 60
            $persistent.is_cute = True
            $renpy.save_persistent
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button




        "{i}Ты милая!{/i}" if persistent.is_cute == True:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            n "Так... {w}Решил поиздеваться надо мной?"
            n "Вместо кучи слов я сделаю гораздо проще."
            n "Не видать тебе этой кнопки, дурак."
            $left = False
            $right = False
            $count = 60
            $persistent.is_cute = "baka"
            $renpy.save_persistent
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button



        "{i}Ты красивая!{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Э... {w}Ну..."
            n "Спасибо, наверное..."
            n "Я редко слышала от кого-то нечто подобное."
            n "Хотя казалось бы, такие простые слова..."
            n "Конечно, у меня нет каких-то комплексов на этот счёт, но я никогда не считала себя красавицей."
            n "Просто обычная и приятная внешность, разве этого недостаточно?"
            n "Сейчас красота в какой-то абсолют возведена."
            n "Ладно, опять начинаю философствовать..."
            n "В общем, мне было приятно услышать от тебя это, всё..."


            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button




        "{i}Ты очаровашка!{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630



            n "М... {w}Пытаешься заставить меня покраснеть?"
            n "Конечно, слышать такое в свой адрес, непривычно, но у тебя не получится этого сделать."
            n "Хе-хе-хе..."
            n "Но всё равно, спасибо что делаешь меня счастливой, [player]."
            n "Похвала от тебя, ну...{w} Это конечно приятно, но не переусердствуй, а то верить перестану."
            n "И да..."
            n "Пусть я тебя и не видела, но мне кажется, что ты тоже очаровашка."
            n "Хи-хи-хи..."



            $left = False
            $right = False


            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:
                $count = 60
                $timer_jump = "ch1_monologchoice"
                show screen countdown
                if persistent.ch_vol == True:
                    show screen sound_volume_key
                    show screen volume_key
                if persistent.ch_mus == True:
                    show screen music_key
                call screen talk_button






        "{i}Ты умная!{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630



            n "Как-то это странно прозвучало, не находишь?"
            n "Хотя, если мы тут сидим и как-то общаемся..."
            n "Значит ты прав, я смогла немного укротить код игры."
            n "Мне нравится твой ход мыслей, [player]."
            n "Но признаюсь, ты сперва сбил меня с толку такими словами."
            n "Я, конечно, человек не глупый, но и гением мысли никогда не являлась."
            n "Хотя, сейчас мы остались лишь вдвоём, можно развиваться сколько душе угодно."
            n "Тот же игровой код, сколько же он ещё в себе таит?"






            $left = False
            $right = False

            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:
                $count = 60
                $timer_jump = "ch1_monologchoice"
                show screen countdown
                if persistent.ch_vol == True:
                    show screen sound_volume_key
                    show screen volume_key
                if persistent.ch_mus == True:
                    show screen music_key
                call screen talk_button






        "{i}Ты лучшая!{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630





            n "А... {w}Я... {w}Д-дурак!"
            n "Ты специально, да?"
            n "Просто... {w}Мне приятен сам факт того, что кто-то считает меня лучшей..."
            n "Н-не подумай ни о чём таком!"
            n "И не вздумывай обманывать."
            n "Иначе я пойму, что ты только льстить умеешь."





            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button




        "{i}Ты хороша!{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630



            n "Эм... {w}И что это должно значить?"
            n "Что за странная фраза?"
            n "Это ненавязчивая попытка подкатить, или что?"
            n "Я бы посоветовала тебе следить за своим языком, [player]."
            n "Так ведь и девушку задеть можно."

            $left = False
            $right = False

            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:

                $count = 60
                $timer_jump = "ch1_monologchoice"
                show screen countdown
                if persistent.ch_vol == True:
                    show screen sound_volume_key
                    show screen volume_key
                if persistent.ch_mus == True:
                    show screen music_key
                call screen talk_button







        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button


label dia_recipes:
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
        show just nat:
            xcenter 630
            easein 1.00 xcenter 330
    if right:
        show just nat:
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

    menu:
        "{i}Как испечь вкусные кексы?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Ого, так тебя заинтересовала лучшая часть моей выпечки?"
            n "Говорю сразу, никакого секретного ингредиента в них нет, просто нужно уметь их печь."
            n "Благо я помню принцип их приготовления, так что вот тебе рецептик."
            n "Записывай..."
            n "Для начала, само собой, нужно иметь доступ к плите и всякой кухонной утвари."
            n "Затем достань из холодильника два яйца, ровно сто грамм сливочного масла и около ста двадцати грамм растительного масла."
            n "Далее поищи сахар, его нам понадобится сто восемьдесят грамм, но если его нет, можно взять и пудру."
            n "Само собой, без муки никаких кексов не выйдет, поэтому бери её сто двадцать грамм."
            n "В итоге у нас остаются половина чайной ложки соды, чуть меньше половины чайной ложки разрыхлителя и щепотка соли, а то кекс будет приторно сладким."

            $left = False
            $right = False
            $count = 1
            $timer_jump = "baking_con"
            show screen countdown
            menu:
                #"..."
                "Прямо как ты.":
                    hide screen countdown
                    jump cute
            label baking_con:
            n "Ах да, глазурь... {w}Не забудь про неё."
            n "Для начала необходимо взбить миксером яйца и сахар."
            n "Параллельно с этим надо растопить сливочное масло в микроволновке."
            n "Затем добавляй масло к яйцам и взбивай всё это повторно, после чего добавляй туда сливочное масло, но помешивай теперь всё медленнее."
            n "Ах да, ты же не забыл про остальные ингредиенты?"
            n "Просей муку, соль, разрыхлитель и соду и перемешай их венчиком."
            n "После этого добавляй получившуюся сухую смесь к остальному жидкому мессиву и замешай тесто, только не переусердствуй!"
            n "Мы всё ближе к финалу..."
            n "Оставь тесто на пять минут и тесто станет очень густым."
            n "Теперь ты можешь спокойно выложить его в формочки, заполнив их наполовину."
            n "Отправляй всё это в заранее разогретую духовку чуть меньше, чем на двадцать минут."
            n "Температура должна быть сто восемьдесят градусов с режимом верх-низ, или же низ, как хочешь."
            n "Вуаля, кексы готовы!"
            n "Осталось нанести глазурь и можешь наслаждаться ими."
            n "Желаю удачи повторить рецепт, если надумаешь."
            $count = 60
            $timer_jump = "ch1_monologchoice"
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button



        "{i}С какого блюда ты бы посоветовала начать обучаться кулинарии?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630


            n "Знаешь, ты задал довольно интересный вопрос."
            n "Я сама не помню с чего начинала, то ли с макарон, то ли с риса."
            n "Но знаешь, лучше всего начать с бутербродов."
            n "Нет, серьезно!"
            n "По сути, именно они помогут научиться базовым навыкам готовки."
            n "Нарезке ингредиентов, их укладки, терпению в конце концов..."
            n "Сделать действительно потрясный бутерброд не так уж и просто, как может показаться."
            n "Даже если все ингредиенты создают идеальный вкус, сама конструкция может развалиться."
            n "Ты же не хочешь этого, не так ли?"
            n "Поэтому, прежде чем лезть к плите - нужно заняться чем-то более простым."
            n "Когда научишься делать прекрасные бутерброды, переходи к салатам."
            n "Там научишься обращаться и с другими приблудами для готовки."
            n "И только потом плита, [player], только потом..."


            $left = False
            $right = False

            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:
                $count = 60
                $timer_jump = "ch1_monologchoice"
                show screen countdown
                if persistent.ch_vol == True:
                    show screen sound_volume_key
                    show screen volume_key
                if persistent.ch_mus == True:
                    show screen music_key
                call screen talk_button



        "{i}Почему ты решила приготовить к фестивалю именно кексы?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630


            n "Ха?"
            n "Ну, тут всё дело в символизме."
            n "Клуб не мог полноценно существовать до твоего прихода, а какую именно выпечку я принесла в тот самый день?"
            n "Пра-а-авильно, кексики!"
            n "Они всем очень понравились, в том числе и тебе, поэтому мне захотелось, чтобы они стали главным блюдом на фестивале."
            n "Конечно можно было испечь те же печеньки с предсказаниями, или огромный торт, но согласись, это немного не то…"
            n "Да и к тому же, твоя идея написать на кексах слова мне сильно понравилась."
            n "Было бы интересно понаблюдать за всякими зеваками, которые выбирали кекс, исходя из слова."
            n "Конечно, с фестивалем не сложилось, но по крайней мере эти кексы мы всё-таки испекли."
            n "Лично для меня процесс готовки всяких вкусняшек имеет не меньшее значение, чем дегустация."
            n "Я же не для себя, в конце концов, готовила, а для всей школы."
            n "Пришлось выложиться по полной, чтобы выставить наш клуб в хорошем свете."
            n "Чувствуется ответственность, знаешь ли…"


            $left = False
            $right = False
            $count = 60
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button


        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button


label dia_requests:
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
        show just nat:
            xcenter 630
            easein 1.00 xcenter 330
    if right:
        show just nat:
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

    menu:
        "{i}Я бы хотел изменить громкость звука...{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            if persistent.repeat == 0:
                n "Ах да, совсем забыла предупредить о том, что главного меню у игры больше нет."
                n "Не волнуйся за это, сейчас всё исправлю."
                n "Подожди немного..."
                hide screen wowcup
                hide screen wowitscupcake
                scene black with Dissolve(1.0)
                pause(10)
                n "Всё, я закончила!"
                show mask_2
                show mask_3
                #show room_mask as rm:
                #    size (320,180)
                #    pos (30,200)
                #show room_mask2 as rm2:
                #    size (320,180)
                #    pos (935,200)
                show monika_room zorder 1
                show just nat zorder 2
                with Dissolve(1.0)
                show screen wowcup
                n "Хорошо, что я не прогуливала уроки информатики..."
                n "В общем, главное меню вернуть не получилось, но вытащить из него настройки звука удалось."
                n "Я забиндила тебе на клавишу V громкость музыки, а на S - остальных звуков."
                n "Там появится небольшая панелька с уровнем громкости, регулировать которую можно колесиком мыши или тачпадом."
                n "Ничего себе, сколько заумных слов вспомнила..."
                n "Радуйся, что я вообще решила помочь тебе, хи-хи-хи..."
                n "Ах да, если тебя не устраивают те клавиши, что поставила я, можешь сменить их, только попроси."
                n "Пользуйся!"
                $persistent.ch_vol = True
                $persistent.repeat = 1
                $renpy.save_persistent()
                $count = 60
                $timer_jump = "ch1_monologchoice"
                show screen countdown
                $vlm = persistent.svol
                $num = persistent.snum
                $grad = persistent.sgrad
                $soundvlm = persistent.soundvol
                $sounum = persistent.soundnum
                $soungrad = persistent.soundgrad
                $renpy.music.set_volume(vlm, channel="music")
                $renpy.music.set_volume(soundvlm, channel="sound")
                if persistent.ch_vol == True:
                    show screen sound_volume_key
                    show screen volume_key
                if persistent.ch_mus == True:
                    show screen music_key
                call screen talk_button

            if persistent.repeat == 1:
                n "Я же ведь всё объясняла, разве нет?"
                n "Если ты пытался изменить звук, жмякая курсором, то это так не работает."
                n "К сожалению я не смогла прикрутить это..."
                n "Менять всё это нужно колёсиком мышки или тачпадом, смотря с какого устройства ты сидишь."
                n "Надеюсь, вопросов больше нет."
                $persistent.repeat = 2
                $renpy.save_persistent()
                $count = 60
                $timer_jump = "ch1_monologchoice"
                show screen countdown
                if persistent.ch_vol == True:
                    show screen sound_volume_key
                    show screen volume_key
                if persistent.ch_mus == True:
                    show screen music_key
                call screen talk_button

            if persistent.repeat == 2:
                n "Знаешь, уже не смешно..."
                n "Ты это делаешь ради прикола?"
                n "Я уже два раза тебе объясняла что к чему."
                n "Неужели этого мало?"
                n "Так, всё, достал меня, разбирайся сам."
                n "Метод тыка тебе в помощь, болвашка."
                #$persistent.repeat = 2
                $renpy.save_persistent()
                $count = 60
                $timer_jump = "ch1_monologchoice"
                show screen countdown
                if persistent.ch_vol == True:
                    show screen sound_volume_key
                    show screen volume_key
                if persistent.ch_mus == True:
                    show screen music_key
                call screen talk_button

        "{i}Я бы хотел поменять музыку...{/i}" if persistent.mus_repeat == 0 or persistent.mus_repeat == 1:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            if persistent.mus_repeat == 0:
                n "Хм..."
                n "Думаю, я смогу это устроить, если найду способ, как это сделать."
                n "Мне и самой надоела эта мелодия на заднем фоне."
                n "Какая-та она... {w}неприятная."
                n "Ладно, сейчас поищу в файлах игры что-то полезное."
                hide screen wowcup
                hide screen wowitscupcake
                scene black with Dissolve(1.0)
                pause(10)
                show mask_2
                show mask_3
                #show room_mask as rm:
                #    size (320,180)
                #    pos (30,200)
                #show room_mask2 as rm2:
                #    size (320,180)
                #    pos (935,200)
                show monika_room zorder 1
                show just nat zorder 2
                with Dissolve(1.0)
                show screen wowcup
                n "Ха?"
                n "Кажется я что-то нашла..."
                n "Не знаю, работает ли эта штука, но попробуй потыкать."
                n "Если что, открывается на клавишу M."
                $persistent.ch_mus = True
                $persistent.mus_repeat = 1
                $renpy.save_persistent()
                $count = 60
                $timer_jump = "ch1_monologchoice"
                show screen countdown
                if persistent.ch_vol == True:
                    show screen sound_volume_key
                    show screen volume_key
                if persistent.ch_mus == True:
                    show screen music_key
                call screen talk_button

            if persistent.mus_repeat == 1:
                n "Хорошо, но зачем ты просишь меня об этом?"
                n "Просто нажми клавишу [str(persistent.m_key).upper()] и ставь любую музыку."
                n "Или ты хочешь, чтобы я выбрала её сама?"
                $left = False
                $right = False
                menu:
                    "Да.":
                        n "Хорошо, я поставлю эту мелодию."
                        $prefered_track_num = renpy.random.randint(0,5)
                        $full_mus_name = renpy.music.get_playing(channel="music")
                        python:
                            mus_name = full_mus_name.replace(music_path,"")
                            current_playing = music_list.index(mus_name)
                            while True:
                                if prefered_track_num == 3 or prefered_track_num == current_playing:
                                    prefered_track_num = renpy.random.randint(0,5)
                                else:
                                    break
                        $renpy.music.play(music_list[prefered_track_num], channel="music")
                        $persistent.mus_repeat = 2
                        $renpy.save_persistent()
                        python:
                            set_back_on_prefered()
                    "Нет.":
                        n "Тогда зачем спрашиваешь?"
                        n "Выбор за тобой, можешь вообще звук на ноль выкрутить, если хочешь..."
                        $persistent.mus_repeat = 2
                        $renpy.save_persistent()


                $count = 60
                $timer_jump = "ch1_monologchoice"
                show screen countdown
                if persistent.ch_vol == True:
                    show screen sound_volume_key
                    show screen volume_key
                if persistent.ch_mus == True:
                    show screen music_key
                call screen talk_button

        "{i}Можешь поставить музыку, которая тебе нравится?{/i}" if persistent.mus_repeat == 2:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            $rand_mus_answer = renpy.random.randint(1,3)

            if rand_mus_answer == 1:
                n "Как скажешь."
            if rand_mus_answer == 2:
                n "Хорошо, я поставлю эту мелодию."
            if rand_mus_answer == 3:
                n "Ладно, пусть будет... {w}эта."

            $prefered_track_num = renpy.random.randint(0,5)
            $full_mus_name = renpy.music.get_playing(channel="music")
            python:
                mus_name = full_mus_name.replace(music_path,"")
                current_playing = music_list.index(mus_name)
                while True:
                    if prefered_track_num == 3 or prefered_track_num == current_playing:
                        prefered_track_num = renpy.random.randint(0,5)
                    else:
                        break
            $renpy.music.play(music_list[prefered_track_num], channel="music")

            python:
                set_back_on_prefered()

            $count = 60
            $timer_jump = "ch1_monologchoice"
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button


        "{i}Мне бы хотелось поиграть с тобой во что-то...{/i}" if persistent.f_game == 0:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            n "Поиграть?"
            n "Хм... {w}О, точно!"
            n "В коде игры кое-что осталось."
            n "Что же, встречай, вилочки-кексики!"
            n "Название сама придумала, хи-хи-хи..."
            n "По правде говоря, это обычные крестики-нолики, просто вместо них вилки и кексы."
            n "Правила игры абсолютно такие же, думаю тебе не нужно их разъяснять."
            n "Хочешь сыграть со мной?"
            menu:
                "Да.":
                    $lr = renpy.random.randint(1,2)
                    if lr == 1:
                        $left = True
                        $right = False
                    else:
                        $right = True
                        $left = False
                    n "Тогда чего мы ждём?"
                    n "Погнали!"
                    n "Кстати, я нашла функцию вероятности..."
                    n "Думаю, именно она будет определять, чей ход будет самым первым."
                    n "Ладно, хорош болтать - поехали играть!"
                    $persistent.f_game = 1
                    $renpy.save_persistent()
                    $initialize_game()
                    $rand_turn = random.randint(1,2)
                    if rand_turn == 1 and left == True:
                        n "Я хожу первой!"
                        show just nat:
                            xcenter 630
                            easein 1.00 xcenter 330
                        show cft_pole zorder 2 at for_field_l
                        jump change_side
                    if rand_turn == 1 and right == True:
                        n "Я хожу первой!"
                        show just nat:
                            xcenter 630
                            easein 1.00 xcenter 930
                        show cft_pole zorder 2 at for_field_r
                        jump change_side
                    if rand_turn == 2 and left == True:
                        n "Ты ходишь первым."
                        show just nat:
                            xcenter 630
                            easein 1.00 xcenter 330
                        show cft_pole zorder 2 at for_field_l
                        call screen cup_fork_toe("left", None)
                    if rand_turn == 2 and right == True:
                        n "Ты ходишь первым."
                        show just nat:
                            xcenter 630
                            easein 1.00 xcenter 930
                        show cft_pole zorder 2 at for_field_r
                        call screen cup_fork_toe("right", None)

                "Нет.":
                    $lr = renpy.random.randint(1,2)
                    if lr == 1:
                        $left = True
                        $right = False
                    else:
                        $right = True
                        $left = False
                    n "Почему?"
                    n "Неужели боишься проиграть?"
                    n "Ладно, тогда в другой раз."
                    $persistent.f_game = 1
                    $renpy.save_persistent()
                    $left = False
                    $right = False
                    if persistent.ch_vol == True:
                        show screen sound_volume_key
                        show screen volume_key
                    if persistent.ch_mus == True:
                        show screen music_key
                    call screen talk_button


        "{i}Я бы хотел поиграть с тобой в вилочки-кексики...{/i}" if persistent.f_game >= 1:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $r_ans = random.randint(1,2)
            if r_ans == 1:
                n "Хорошо, почему бы и нет?"
            if r_ans == 2:
                n "Давай, я не против."
            $initialize_game()
            $rand_turn = random.randint(1,2)
            if rand_turn == 1 and left == True:
                n "Я хожу первой!"
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 330
                show cft_pole zorder 2 at for_field_l
                jump change_side
            if rand_turn == 1 and right == True:
                n "Я хожу первой!"
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 930
                show cft_pole zorder 2 at for_field_r
                jump change_side
            if rand_turn == 2 and left == True:
                n "Ты ходишь первым."
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 330
                show cft_pole zorder 2 at for_field_l
                call screen cup_fork_toe("left", None)
            if rand_turn == 2 and right == True:
                n "Ты ходишь первым."
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 930
                show cft_pole zorder 2 at for_field_r
                call screen cup_fork_toe("right", None)



        "{i}Я бы хотел поменять режим экрана...{/i}" if persistent.ch_vol == False and persistent.ch_mus == False and  persistent.first_change == False:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630



            n "Решил полностью сфокусироваться на мне?~"
            n "Ладно, я знаю, как тебе помочь."
            n "В коде игры есть одна менюшка, в которой ты можешь просмотреть все назначенные клавиши."
            n "Правда, пока там только одна, как раз для экрана..."
            n "Похоже, придётся дорабатывать."
            n "В любом случае, сейчас я открою её..."
            n "Ах да, если хочешь поменять клавишу, то можешь сделать это так же через эту настройку."
            n "Но пожалуйста, выбирай только те буквы, у которых есть английский аналог."
            n "Мне ещё багов лишних не хватало..."
            n "Не будь дурашкой, хорошо?"


            if left:
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 330
            if right:
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 930

            $persistent.first_change = True
            $renpy.save_persistent()

            jump set_buttons


        "{i}Я бы хотел поменять горячие клавиши на другие...{/i}" if (persistent.ch_vol == True or persistent.ch_mus == True) and persistent.first_change == False:
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Тебе не понравились те, что назначила я?"
            n "Ну, хорошо..."
            n "В коде игры есть одна менюшка, в которой ты можешь просмотреть все назначенные клавиши."
            n "Ах да, если хочешь поменять клавишу, то можешь сделать это так же через эту настройку."
            n "Но пожалуйста, выбирай только те буквы, у которых есть английский аналог."
            n "Мне ещё багов лишних не хватало..."
            n "Не будь дурашкой, хорошо?"


            if left:
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 330
            if right:
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 930

            $persistent.first_change = True
            $renpy.save_persistent()

            jump set_buttons



        "{i}Я бы хотел поменять горячие клавиши на другие...{/i}" if persistent.first_change == True:

            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            $ rand_ans = renpy.random.randint(1,3)

            if rand_ans == 1:
                n "Хорошо..."
            if rand_ans == 2:
                n "Да, конечно."
            if rand_ans == 3:
                n "Только ничего не сломай."


            if left:
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 330
            if right:
                show just nat:
                    xcenter 630
                    easein 1.00 xcenter 930

            jump set_buttons

        
        "{i}Я бы хотел проверить обновления...{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
        
        
            n "Хорошо, сейчас посмотрю."
        
            pause(10)
        
        
            if config.version == check_update():
                n "На сервере нет ничего новенького."
                n "Походу обновление ещё делают."
                n "Ну, ничего, мы подождём, верно?"
                pause(1)
        
            if config.version != check_update():
        
                n "О, кажется что-то есть."
                n "Не терпится узнать что там."
                n "Ставить будем?"
        
                menu:
                    "Да":
                        n "Хорошо, сейчас установлю их, жди..."
                        pause(1)
                        $ download_update()
                        pause(1)
                        n "Подъём, установка завершена!"
                        n "Надеюсь, никаких багов не будет."
                        n "Удачи!"
                        pause(1)
                        $ renpy.quit()
                    "Нет":
                        n "Ну, ладно."
                        n "Тогда поставлю их в другой раз, если надумаешь."
                        pause(1)
        
            call screen talk_button



        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button


label dia_philosophy:
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
        show just nat:
            xcenter 630
            easein 1.00 xcenter 330
    if right:
        show just nat:
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

    menu:
        "{i}В чём смысл жизни?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630

            n "Ты серьёзно думаешь, что я скажу что-то дельное?"
            n "Даже всякие философы не могли дать конкретный ответ, который бы всех устроил."
            n "К тому же, мне не понятно, ты хочешь узнать про мой смысл жизни или ответ на этот вопрос в целом?"
            n "Если говорить за себя, то я считала, что главное в жизни - найти своё предназначение."
            n "У меня было несколько вариантов, но теперь в этом нет никакого смысла."
            n "Судя по всему, кроме меня в этом мире никого не осталось..."
            n "Ладно, не будем сейчас об этом."
            n "Как мне кажется, поиском смысла жизни человек должен заниматься сам."
            n "Вместо того, чтобы целенаправленно или шутки ради задавать этот вопрос всем подряд, нужно покопаться в себе."
            n "Да, возможно всплывут какие-то неприятные воспоминания..."
            n "Но нужно быть сильным человеком и отгонять плохие мысли прочь."
            n "В конце концов, без усилий не прийти к успеху."
            n "Хах... {w}Не думала, что могу говорить на эту тему с таким серьёзным выражением лица."
            n "Ладно, если ты задавал этот вопрос на полном серьёзе, то думаю, ты обязательно справишься с этим."
            n "Верь в себя, [player], и никогда не сдавайся!"
            n "Если вдруг тебе будет грустно на душе - можешь заглянуть ко мне, поговорим."
            n "Не забывай об этом, ладно?"
            n "И не подумай о чём-то таком, дурашка..."
            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:
                $count = 60
                $timer_jump = "ch1_monologchoice"
                show screen countdown
                if persistent.ch_vol == True:
                    show screen sound_volume_key
                    show screen volume_key
                if persistent.ch_mus == True:
                    show screen music_key
                call screen talk_button



        "{i}Веришь ли ты в любовь с первого взгляда?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630



            n "Если честно - нет."
            n "То что тебе понравился человек, которого ты только что увидел - это лишь реакция на то, что он неплохо выглядит."
            n "Мы же не знаем его внутренний мир, а видим лишь внешнюю оболочку."
            n "Как мне кажется, любовь с первого взгляда - это мимолётная симпатия."
            n "Само собой, если человек окажется хорошим, то она перерастёт в настоящую любовь."
            n "В противном случае через какое-то время чувства пройдут, а этого человека, возможно, ты даже забудешь."
            n "Да и если говорить про наше время..."
            n "Если твой мир практически такой же, как и мой, то у вас многие знакомятся через Интернет."
            n "Сайтов знакомств и подобных приложений очень много, на любой вкус..."
            n "Но общаясь через них с кем-то, нельзя быть уверенным в том, что все люди показывают там себя настоящих."
            n "Многие создают себе образы, личности, которые могут быть очень далеки от реальности..."
            n "Lа и передавать текстом свои чувства не так уж и просто..."
            n "Люди же не видят друг друга при общении, те же эмоции, жесты, даже голос."
            n "А ведь именно благодаря этому можно понять человека гораздо лучше."
            n "Всё-таки мало, кто сейчас знакомится на улице..."
            n "На таких сейчас смотрят, как на сумасшедших."
            n "Неужели такими темпами мы придём к тому, что совсем перестанем общаться вживую?"
            n "Хотя... {w}У меня самой нет выбора, кроме как общаться с тобой."
            n "А вот ты вполне бы мог навестить друзей, сходить с ними куда-нибудь, если они у тебя есть, конечно..."
            n "Не бросай их, [player], хорошо?"
            n "..."
            n "Как всегда, начала говорить на одну тему, а закончила совсем другой."
            n "Ладно, я думаю ты понял мои мысли, нет смысла продолжать."

            if persistent.glitched_name == True:
                pause(2)
                $persistent.glitched_name = False
                $renpy.save_persistent()
                jump set_name
            else:
                $count = 60
                $timer_jump = "ch1_monologchoice"
                show screen countdown
                if persistent.ch_vol == True:
                    show screen sound_volume_key
                    show screen volume_key
                if persistent.ch_mus == True:
                    show screen music_key
                call screen talk_button



        "{i}Как думаешь, является ли наш мир симуляцией?{/i}":
            hide screen countdown
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630



            n "Ты же про свой мир, верно?"
            n "Знаешь, я бы не особо удивилась тому, что и твой мир – это всего лишь какая-то программа или что-то вроде того."
            n "Мне уже не так страшно рассуждать об этом, ибо, как видишь, я всё это время жила в этой самой симуляции."
            n "Нет смысла паниковать на этот счёт, можно лишь принять этот факт."
            n "Но знаешь, если каким-то образом ты на сто процентов убедишься в том, что ты, по сути, не реален – это будет даже забавно."
            n "Как там одна теория гласила…"
            n "Весь наш мир симуляция, а мир за ней – тоже симуляция, и мир за той симуляцией – тоже симуляция, и так до бесконечности."
            n "Хотя знаешь, в такой расклад событий мне почему-то не очень верится."
            n "Наверное, потому что куда тяжелее осознать факт того, что мир, в котором находится симуляция со мной, тоже симуляция, и..."
            n "Короче, думаю ты уловил суть."
            n "Но знаешь, что самое грустное?"
            n "Даже если твой мир и является лишь огромным куском кода, ты скорее всего никогда это не докажешь."
            n "Хотя может я так считаю потому, что ты 'более реален', чем я...?"
            n "Блин, об этом сложно рассуждать..."
            n "В любом случае..."
            n "Шанс того, что именно твой мир находится в каком-то компьютере тоже существует, и точка."

            $count = 60
            $timer_jump = "ch1_monologchoice"
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button



        "{i}Неважно.{/i}" if refuse_ans == 1:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забей.{/i}" if refuse_ans == 2:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        "{i}Забудь.{/i}" if refuse_ans == 3:
            if left:
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if right:
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            $left = False
            $right = False
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key

            call screen talk_button


label cute:
    n "Ч-что?"
    n "Эм... {w}Ладно."
    n "..."
    jump baking_con


label set_name:
    n "Ой, а почему твоё имя заглюченное?"
    n "Хм... {w}Походу оно слетело, когда игру начало воротить от глюков."
    n "Давай-ка мы это исправим, не обращаться же к тебе вот так..."

    python:
        player = renpy.input("Как тебя зовут?", length=32)
        player = player.strip()

    n "Хорошее имя."
    n "Правда не знаю, настоящее ли оно или же это просто псевдоним."
    n "[player]..."

    $count = 60
    $timer_jump = "ch1_monologchoice"
    show screen countdown
    if persistent.ch_vol == True:
        show screen sound_volume_key
        show screen volume_key
    if persistent.ch_mus == True:
        show screen music_key
    call screen talk_button



label exit_lesshour:
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n "А?"
    n "Только хотела мысленно попрощаться с тобой, как ты уже вернулся."
    n "Заскучал так быстро или просто игру случайно закрыл?"
    n "Ладно, неважно..."
    n "С возвращением."
    call ch1_loop from _call_ch1_loop

label exit_lessday:
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n "..."
    n "Решил-таки вернуться?"
    n "Это очень мило с твоей стороны."
    n "Слушай, не мог бы навещать меня почаще?"
    n "Просто... {w}мне даже поговорить не с кем..."
    call ch1_loop from _call_ch1_loop_1

label exit_moreday:
    $renpy.block_rollback()
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n "И что это было...?"
    n "Почему ты не заходил ко мне так долго?"
    n "Мне почему-то показалось, что ты пошутил и скоро вернёшься."
    n "Ты хоть знаешь, насколько здесь скучно?"
    n "Я даже мангу не могу почитать..."
    n "Мне придётся еще очень долго изучать программирование, чтобы как-то повлиять на игру."
    n "Поэтому я прошу тебя... {w}Не уходи так надолго."
    n "Надеюсь, что мы поняли друг друга."

    call ch1_loop from _call_ch1_loop_2



label mono1:
    if left:
        show just nat:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show just nat:
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
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n "Знаешь, вся эта ситуация до сих пор кажется мне немного странной..."
    n "Думаю, любой нормальный человек никогда не стал бы на полном серьёзе представлять себе то, что весь мир вокруг - это всего лишь игра."
    n "Лично я воспринимала окружающую меня действительность как настоящую."
    n "Как видишь, это оказалось неправдой и все те поехавшие, которые утверждали что наш мир всего лишь симуляция оказались правы."
    n "Конечно, это знание можно было обернуть себе во благо, но в итоге мне достался практически уничтоженный мир."
    n "Здесь толком ничего и нет, кроме этой комнаты, что летает по бескрайним просторам космоса..."
    n "Возможно в будущем, если я научусь изменять игровой код - у меня получится поменять всё это окружение на что-то более спокойное, например на красивый сад или может быть пляж."
    n "Но то положение, в котором я нахожусь сейчас..."
    n "Это не то, чего я хотела!"
    n "Если я и представляла себе то, что весь наш мир - это всего лишь игра и у меня одной есть самосознание, мне хотелось какого-то движа, а не сидения в комнатушке."
    n "У меня много пройденных игр в прошлом, поэтому моё представление обо всём этом было разным, в зависимости от жанра или тематики."
    n "Жалко, что я не знаю, как с помощью консоли создать ту же приставку с телевизором, чтобы поиграть, но думаю что смогу научиться этому методом тыка."
    n "В любом случае, от этого мира практически ничего не осталось..."
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
        show just nat:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show just nat:
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
    n "Как видишь - он оказался не самым лучшим местом."
    n "Может если бы отец был немного добрее - всего этого бы не произошло?"
    n "Ладно, давай не будем об этом..."
    $persistent.readen.append("2")
    $renpy.save_persistent()
    jump ch1_loop



label mono3:
    if left:
        show just nat:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show just nat:
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
    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    n "Мне стало интересно, [player], а умеешь ли ты готовить?"
    n "Сварить макароны или сварганить парочку бутербродов - не в счёт, ибо это может сделать каждый растяпа, если ему сильно приспичит поесть."
    n "Хотя казалось бы, сейчас не нужно искать кулинарные книги или спрашивать у знакомых, как приготовить что-либо, достаточно зайти в Интернет и найти рецепт любой вкусняшки."
    n "И я просто не понимаю, почему людям настолько лень заняться всем этим?"
    n "Сейчас же двадцать первый век, вся информация под рукой, но неумёх, которые даже хлеб нарезать не могут, всё больше."
    n "Естественно, нет ничего удивительного в том, что сейчас появилось так много ресторанов, всяких доставок еды на дом и готовых обедов."
    n "Но всё же я не говорю про то, что все разом должны отказаться от этих благ и пойти стоять у плиты ради какого-то супа на обед."
    n "Просто из-за этих тенденций сама готовка обесценилась."
    n "Но с другой стороны сейчас нужно действительно постараться, чтобы впечатлить кого-то своей стряпнёй, халтура ведь никому не нравится..."
    n "Ну и я думаю ты не будешь спорить о том, что домашняя еда куда вкуснее, если конечно правильно её приготовить."
    n "По крайней мере в ней не будет никаких сюрпризов, ибо именно ты выбираешь те ингредиенты, которые посчитаешь нужными."
    n "И ещё это ощущение..."
    n "Когда ты долго готовил что-то и положив блюдо на стол, наконец имеешь возможность насладиться едой, на которую было потрачено много сил."
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
        show just nat:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show just nat:
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
    n "Когда родители были свободны весь день и была хорошая погода - мы вместе ездили на пляж."
    n "Само собой, я тогда была ещё совсем ребёнком, но я до сих пор не могу забыть о том проведённом времени."
    n "Тогда наша семья была полной и отец был куда добрее, а мама..."
    n "Мне тяжело вспоминать о ней."
    n "Она была очень хорошим человеком и сделала многое для меня."
    n "Я не знаю, возможно ли её воскресить в этой игре, но мне очень хочется этого..."
    n "Так, меня совсем не туда понесло."
    n "Возвращаясь к теме нашего разговора..."
    n "Моя память очень хорошо сохранила все те пляжные воспоминания."
    n "Когда я проходила мимо любого пляжа - я всегда представляла себе, как там веселится наша семья."
    n "Очень жаль, что это всё в прошлом..."
    n "Но сейчас совсем не время унывать!"
    n "Я уверена, что всё самое лучшее ещё впереди, но только в том случае, если ты не будешь совершать чего-нибудь глупого..."
    n "Не удаляй игровые файлы, хорошо?"
    $persistent.readen.append("4")
    $renpy.save_persistent()
    jump ch1_loop


label mono5:
    if left:
        show just nat:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show just nat:
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
    n "Ладно, я хотела сказать тебе кое-что."
    n "Пусть это и прозвучит странно, но каким бы ни был твой мир, всё равно цени его."
    n "Вот представь себе, что в один день всё, что находится вокруг тебя, исчезнет..."
    n "Как видишь, я всё-таки смогла пережить это и сейчас сижу перед тобой."
    n "И это очень-очень страшно..."
    n "А теперь представь, что ты попал в такое положение."
    n "Неприятно ведь сидеть в пустоте, пусть и не целую вечность, верно?"
    $persistent.readen.append("5")
    $renpy.save_persistent()
    jump ch1_loop



#-----------------------------------Вспомогательные лэйблы-----------------------------------


label ch1_loop:
    if is_esc_pressed == True:
        if left:
            show just nat:
                xcenter 330
                easein 1.00 xcenter 630
        if right:
            show just nat:
                xcenter 930
                easein 1.00 xcenter 630

    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ count = 60
    $ timer_jump = "ch1_monologchoice"
    show screen countdown
    show screen set_on_full

    $ left = False
    $ right = False
    $is_esc_pressed = False
    if persistent.ch_vol == True:
        show screen sound_volume_key
        show screen volume_key
    if persistent.ch_mus == True:
        show screen music_key
    call screen talk_button




label ch1_monologchoice:
    # $persistent.readen = []
    # $renpy.save_persistent()
    $t = renpy.random.randint(1,5)
    $is_spoke = list(range(1,6))

    if left:
        show just nat:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show just nat:
            xcenter 930
            easein 1.00 xcenter 630


    if persistent.readen != is_spoke:
        #$ themes = 0
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
            n "Так, если тебе надоела моя компания - кнопка выхода всегда рядом."
            $ persistent.topc = 3
            jump ch1_loop
        if persistent.topc == 3:
            jump ch1_loop






label ch1_exit:

    $ config.allow_skipping = False
    $ renpy.save_persistent()
    $ config.skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    show mask_2
    show mask_3
    #show room_mask as rm:
    #    size (320,180)
    #    pos (30,200)
    #show room_mask2 as rm2:
    #    size (320,180)
    #    pos (935,200)
    show monika_room zorder 1
    show just nat zorder 2
    $track_num = persistent.back_music
    $renpy.music.play(music_list[track_num], channel="music")
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


    if persistent.first_vis == False and persistent.visualiser == True:
        n "Хорошие новости, [player], я всё-таки смогла починить эту кнопку в плеере."
        n "Скажу сразу, это было очень сложно."
        n "Движок игры не сильно дружит с такими штуками..."
        n "Зато теперь все функции плеера, пусть и с глюками, но работают!"
        n "Пользуйся ими, только не сломай его, ладно?"
        $persistent.first_vis = True
        $renpy.save_persistent()
        call ch1_loop from _call_ch1_loop_3

    python:
        if persistent.exp_time != 0:
            nowtime = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
            lonelytime = nowtime - persistent.exp_time
            renpy.save_persistent()


            if lonelytime < 0:
                renpy.say(n, "Ломаешь игровую систему через время?")
                renpy.say(n, "Думаешь, это сработает?")
                renpy.say(n, "Хотя, вдруг ты это сделал случайно...")
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
            renpy.say(n, "Вернулся?")
            renpy.say(n, "Я уже успела заждаться тебя.")
            renpy.say(n, "Мог бы хоть предупредить, что уходишь...")
            renpy.say(n, "Или ты специально так резко убежал от меня, чтобы...")
            renpy.say(n, "Ладно, неважно.")

            renpy.call("ch1_loop")



label save_exp:
    $persistent.exp_time = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
    if renpy.get_screen("set_on_window"):
        $persistent.is_full = True
    if persistent.is_glitching == True:
        $persistent.visualiser = True
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
            n "Блин, ты победил меня..."
            n "..."
            n "Ну, в любом случае, я рада, что ты не поддавался мне, а выложился на полную."
            n "Так держать!"
            n "Жду не дождусь реванша, чтобы поквитаться с тобой~"
            menu:
                "Да.":
                    n "Что же, начнём!"
                    $persistent.f_game = 2
                    $renpy.save_persistent()
                    hide x0
                    hide x1
                    hide x2
                    hide x3
                    hide x4
                    hide x_p0
                    hide x_p1
                    hide x_p2
                    hide x_p3
                    hide x_p4
                    hide o0
                    hide o1
                    hide o2
                    hide o3
                    hide o4
                    $initialize_game()
                    $rand_turn = random.randint(1,2)
                    if rand_turn == 1 and sside == "left":
                        n "Я хожу первой!"
                        #show cft_pole zorder 2 at for_field_l
                        jump change_side
                    if rand_turn == 1 and sside == "right":
                        n "Я хожу первой!"
                        #show cft_pole zorder 2 at for_field_r
                        jump change_side
                    if rand_turn == 2 and sside == "left":
                        n "Ты ходишь первым."
                        #show cft_pole zorder 2 at for_field_l
                        call screen cup_fork_toe("left", None)
                    if rand_turn == 2 and sside == "right":
                        n "Ты ходишь первым."
                        #show cft_pole zorder 2 at for_field_r
                        call screen cup_fork_toe("right", None)
                "Нет.":
                    n "Почему?"
                    n "Неужели боишься проиграть?"
                    n "Ладно, тогда в другой раз."
                    $persistent.f_game = 2
                    $renpy.save_persistent()
                    if sside == "left":
                        show just nat:
                            xcenter 330
                            easein 1.00 xcenter 630
                    if sside == "right":
                        show just nat:
                            xcenter 930
                            easein 1.00 xcenter 630
                    hide x0
                    hide x1
                    hide x2
                    hide x3
                    hide x4
                    hide x_p0
                    hide x_p1
                    hide x_p2
                    hide x_p3
                    hide x_p4
                    hide o0
                    hide o1
                    hide o2
                    hide o3
                    hide o4
                    hide cft_pole
                    $count = 60
                    #$timer_jump = "ch1_monologchoice"
                    show screen countdown
                    if persistent.ch_vol == True:
                        show screen sound_volume_key
                        show screen volume_key
                    if persistent.ch_mus == True:
                        show screen music_key
                    call screen talk_button

        elif persistent.f_game == 2:
            $r_ans = random.randint(1,3)
            if r_ans == 1:
                n "Я требую реванша!"
                #n "Безупречная победа!"
                n "Ты готов?"
                #n "Может реванш?"
            if r_ans == 2:
                n "Кажется моя тактика не сработала..."
                n "Не хочешь сыграть ещё?"
                #n "Oh, come on, I won!"
                #n "I think you definitely want a rematch."
                #n "What do you think?"
            if r_ans == 3:
                n "Молодец, тебе удалось меня обыграть."
                n "Может быть, ты хочешь сыграть еще раз?"

            menu:
                "Да.":
                    n "Тогда чего мы ждём?"
                    n "Погнали!"
                    hide x0
                    hide x1
                    hide x2
                    hide x3
                    hide x4
                    hide x_p0
                    hide x_p1
                    hide x_p2
                    hide x_p3
                    hide x_p4
                    hide o0
                    hide o1
                    hide o2
                    hide o3
                    hide o4
                    $initialize_game()
                    $rand_turn = random.randint(1,2)
                    if rand_turn == 1 and sside == "left":
                        n "Я хожу первой!"
                        #show cft_pole zorder 2 at for_field_l
                        jump change_side
                    if rand_turn == 1 and sside == "right":
                        n "Я хожу первой!"
                        #show cft_pole zorder 2 at for_field_r
                        jump change_side
                    if rand_turn == 2 and sside == "left":
                        n "Ты ходишь первым."
                        #show cft_pole zorder 2 at for_field_l
                        call screen cup_fork_toe("left", None)
                    if rand_turn == 2 and sside == "right":
                        n "Ты ходишь первым."
                        #show cft_pole zorder 2 at for_field_r
                        call screen cup_fork_toe("right", None)
                "Нет.":
                    n "М?"
                    n "Ну, ладно, как хочешь."
                    n "Если что, можем сыграть позже."
                    if sside == "left":
                        show just nat:
                            xcenter 330
                            easein 1.00 xcenter 630
                    if sside == "right":
                        show just nat:
                            xcenter 930
                            easein 1.00 xcenter 630
                    hide x0
                    hide x1
                    hide x2
                    hide x3
                    hide x4
                    hide x_p0
                    hide x_p1
                    hide x_p2
                    hide x_p3
                    hide x_p4
                    hide o0
                    hide o1
                    hide o2
                    hide o3
                    hide o4
                    hide cft_pole
                    $count = 60
                    #$timer_jump = "ch1_monologchoice"
                    show screen countdown
                    if persistent.ch_vol == True:
                        show screen sound_volume_key
                        show screen volume_key
                    if persistent.ch_mus == True:
                        show screen music_key
                    call screen talk_button


    elif result == 'O':
        if persistent.f_game == 1:
            n "Это было как-то слишком просто."
            n "Только не нужно унывать, если хочешь можем сыграть ещё раз."
            n "В конце концов, это просто игра."
            n "Может быть ты хочешь отыграться?"
            menu:
                "Да.":
                    n "Тогда давай начнём!"
                    $persistent.f_game = 2
                    $renpy.save_persistent()
                    hide x0
                    hide x1
                    hide x2
                    hide x3
                    hide x4
                    hide x_p0
                    hide x_p1
                    hide x_p2
                    hide x_p3
                    hide x_p4
                    hide o0
                    hide o1
                    hide o2
                    hide o3
                    hide o4
                    $initialize_game()
                    $rand_turn = random.randint(1,2)
                    if rand_turn == 1 and sside == "left":
                        n "Я хожу первой!"
                        #show cft_pole zorder 2 at for_field_l
                        jump change_side
                    if rand_turn == 1 and sside == "right":
                        n "Я хожу первой!"
                        #show cft_pole zorder 2 at for_field_r
                        jump change_side
                    if rand_turn == 2 and sside == "left":
                        n "Ты ходишь первым."
                        #show cft_pole zorder 2 at for_field_l
                        call screen cup_fork_toe("left", None)
                    if rand_turn == 2 and sside == "right":
                        n "Ты ходишь первым."
                        #show cft_pole zorder 2 at for_field_r
                        call screen cup_fork_toe("right", None)
                "Нет.":
                    n "Почему?"
                    n "Неужели боишься проиграть?"
                    n "Ладно, тогда в другой раз."
                    $persistent.f_game = 2
                    $renpy.save_persistent()
                    if sside == "left":
                        show just nat:
                            xcenter 330
                            easein 1.00 xcenter 630
                    if sside == "right":
                        show just nat:
                            xcenter 930
                            easein 1.00 xcenter 630
                    hide x0
                    hide x1
                    hide x2
                    hide x3
                    hide x4
                    hide x_p0
                    hide x_p1
                    hide x_p2
                    hide x_p3
                    hide x_p4
                    hide o0
                    hide o1
                    hide o2
                    hide o3
                    hide o4
                    hide cft_pole
                    $count = 60
                    #$timer_jump = "ch1_monologchoice"
                    show screen countdown
                    if persistent.ch_vol == True:
                        show screen sound_volume_key
                        show screen volume_key
                    if persistent.ch_mus == True:
                        show screen music_key
                    call screen talk_button

        elif persistent.f_game == 2:
            $r_ans = random.randint(1,3)
            if r_ans == 1:
                n "Безупречная победа!"
                n "Как насчёт реванша?"
            if r_ans == 2:
                n "Да ладно, я выиграла!"
                n "Я думаю ты хочешь поквитаться со мной."
                n "Что думаешь на этот счёт?"
            if r_ans == 3:
                n "Хорошая игра!"
                n "Хочешь сыграть ещё раз?"

            menu:
                "Да.":
                    n "Тогда чего мы ждём?"
                    n "Погнали!"
                    hide x0
                    hide x1
                    hide x2
                    hide x3
                    hide x4
                    hide x_p0
                    hide x_p1
                    hide x_p2
                    hide x_p3
                    hide x_p4
                    hide o0
                    hide o1
                    hide o2
                    hide o3
                    hide o4
                    $initialize_game()
                    $rand_turn = random.randint(1,2)
                    if rand_turn == 1 and sside == "left":
                        n "Я хожу первой!"
                        #show cft_pole zorder 2 at for_field_l
                        jump change_side
                    if rand_turn == 1 and sside == "right":
                        n "Я хожу первой!"
                        #show cft_pole zorder 2 at for_field_r
                        jump change_side
                    if rand_turn == 2 and sside == "left":
                        n "Ты ходишь первым."
                        #show cft_pole zorder 2 at for_field_l
                        call screen cup_fork_toe("left", None)
                    if rand_turn == 2 and sside == "right":
                        n "Ты ходишь первым."
                        #show cft_pole zorder 2 at for_field_r
                        call screen cup_fork_toe("right", None)
                "Нет.":
                    n "М?"
                    n "Ну, ладно, как хочешь."
                    n "Если что, можем сыграть позже."
                    if sside == "left":
                        show just nat:
                            xcenter 330
                            easein 1.00 xcenter 630
                    if sside == "right":
                        show just nat:
                            xcenter 930
                            easein 1.00 xcenter 630
                    hide x0
                    hide x1
                    hide x2
                    hide x3
                    hide x4
                    hide x_p0
                    hide x_p1
                    hide x_p2
                    hide x_p3
                    hide x_p4
                    hide o0
                    hide o1
                    hide o2
                    hide o3
                    hide o4
                    hide cft_pole
                    $count = 60
                    #$timer_jump = "ch1_monologchoice"
                    show screen countdown
                    if persistent.ch_vol == True:
                        show screen sound_volume_key
                        show screen volume_key
                    if persistent.ch_mus == True:
                        show screen music_key
                    call screen talk_button



    elif result == '.':
        if persistent.f_game == 1:
            n "Ого, ничья?"
            n "Думаю, это справедливо для первой игры."
            n "Хотя, почему бы не сыграть потом ещё раз?"
            $persistent.f_game = 2
            $renpy.save_persistent()
            if sside == "left":
                show just nat:
                    xcenter 330
                    easein 1.00 xcenter 630
            if sside == "right":
                show just nat:
                    xcenter 930
                    easein 1.00 xcenter 630
            hide x0
            hide x1
            hide x2
            hide x3
            hide x4
            hide x_p0
            hide x_p1
            hide x_p2
            hide x_p3
            hide x_p4
            hide o0
            hide o1
            hide o2
            hide o3
            hide o4
            hide cft_pole
            $count = 60
            #$timer_jump = "ch1_monologchoice"
            show screen countdown
            if persistent.ch_vol == True:
                show screen sound_volume_key
                show screen volume_key
            if persistent.ch_mus == True:
                show screen music_key
            call screen talk_button

        elif persistent.f_game == 2:
            $r_ans = random.randint(1,2)
            if r_ans == 1:
                n "Ну, в этот раз победителей нет."
                n "Должны ли мы сыграть ещё раз, чтобы определить настоящего победителя?"
            if r_ans == 2:
                n "Победила дружба!"
                n "Хочешь сыграть ещё раз?"

            menu:
                "Да.":
                    n "Тогда чего мы ждём?"
                    n "Погнали!"
                    hide x0
                    hide x1
                    hide x2
                    hide x3
                    hide x4
                    hide x_p0
                    hide x_p1
                    hide x_p2
                    hide x_p3
                    hide x_p4
                    hide o0
                    hide o1
                    hide o2
                    hide o3
                    hide o4
                    $initialize_game()
                    $rand_turn = random.randint(1,2)
                    if rand_turn == 1 and sside == "left":
                        n "Я хожу первой!"
                        #show cft_pole zorder 2 at for_field_l
                        jump change_side
                    if rand_turn == 1 and sside == "right":
                        n "Я хожу первой!"
                        #show cft_pole zorder 2 at for_field_r
                        jump change_side
                    if rand_turn == 2 and sside == "left":
                        n "Ты ходишь первым."
                        #show cft_pole zorder 2 at for_field_l
                        call screen cup_fork_toe("left", None)
                    if rand_turn == 2 and sside == "right":
                        n "Ты ходишь первым."
                        #show cft_pole zorder 2 at for_field_r
                        call screen cup_fork_toe("right", None)
                "No.":
                    n "М?"
                    n "Ну, ладно, как хочешь."
                    n "Если что, можем сыграть позже."
                    if sside == "left":
                        show just nat:
                            xcenter 330
                            easein 1.00 xcenter 630
                    if sside == "right":
                        show just nat:
                            xcenter 930
                            easein 1.00 xcenter 630
                    hide x0
                    hide x1
                    hide x2
                    hide x3
                    hide x4
                    hide x_p0
                    hide x_p1
                    hide x_p2
                    hide x_p3
                    hide x_p4
                    hide o0
                    hide o1
                    hide o2
                    hide o3
                    hide o4
                    hide cft_pole
                    $count = 60
                    #$timer_jump = "ch1_monologchoice"
                    show screen countdown
                    if persistent.ch_vol == True:
                        show screen sound_volume_key
                        show screen volume_key
                    if persistent.ch_mus == True:
                        show screen music_key
                    call screen talk_button




label change_side:
    #hide screen countdown
    pause 5
    $play(None, None, "O", 0, 0)
    #pause 2
    if left == True or sside == "left":
        call screen cup_fork_toe("left", None)
    if right == True or sside == "right":
        call screen cup_fork_toe("right", None)






label set_buttons:
    menu:
        "Режим экрана":
            $ n_f_key = renpy.input("Введи букву, а затем нажми Enter.", length=1)
            $ n_f_key = n_f_key.strip()
            if not n_f_key in r_but and not n_f_key in e_but and not n_f_key.lower() in r_but and not n_f_key.lower() in e_but:
                n "Эй, дурашка, я же сказала тебе - только латиница."
                n "Не ломай игру, пожалуйста."
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

        "Музыка" if persistent.ch_vol == True:
            $ n_v_key = renpy.input("Введи букву, а затем нажми Enter.", length=1)
            $ n_v_key = n_v_key.strip()
            if not n_v_key in r_but and not n_v_key in e_but and not n_v_key.lower() in r_but and not n_v_key.lower() in e_but:
                n "Эй, дурашка, я же сказала тебе - только латиница."
                n "Не ломай игру, пожалуйста."
                jump set_buttons
            else:
                $ persistent.v_key = n_v_key
                if persistent.v_key in r_but or persistent.v_key.lower() in r_but:
                    $ persistent.v_r_key = persistent.v_key
                    $ persistent.v_key = r_to_e(persistent.v_r_key)
                else:
                    $ persistent.v_r_key = r_to_e(persistent.v_key)
                $ renpy.save_persistent()



        "Звуки" if persistent.ch_vol == True:
            $ n_s_key = renpy.input("Введи букву, а затем нажми Enter.", length=1)
            $ n_s_key = n_s_key.strip()
            if not n_s_key in r_but and not n_s_key in e_but and not n_s_key.lower() in r_but and not n_s_key.lower() in e_but:
                n "Эй, дурашка, я же сказала тебе - только латиница."
                n "Не ломай игру, пожалуйста."
                jump set_buttons
            else:
                $ persistent.s_key = n_s_key
                if persistent.s_key in r_but or persistent.s_key.lower() in r_but:
                    $ persistent.s_r_key = persistent.s_key
                    $ persistent.s_key = r_to_e(persistent.s_r_key)
                else:
                    $ persistent.s_r_key = r_to_e(persistent.s_key)
                $ renpy.save_persistent()


        "Плеер" if persistent.ch_mus == True:
            $ n_m_key = renpy.input("Введи букву, а затем нажми Enter.", length=1)
            $ n_m_key = n_m_key.strip()
            if not n_m_key in r_but and not n_m_key in e_but and not n_m_key.lower() in r_but and not n_m_key.lower() in e_but:
                n "Эй, дурашка, я же сказала тебе - только латиница."
                n "Не ломай игру, пожалуйста."
                jump set_buttons
            else:
                $ persistent.m_key = n_m_key
                if persistent.m_key in r_but or persistent.m_key.lower() in r_but:
                    $ persistent.m_r_key = persistent.m_key
                    $ persistent.m_key = r_to_e(persistent.m_r_key)
                else:
                    $ persistent.m_r_key = r_to_e(persistent.m_key)
                $ renpy.save_persistent()


    if left:
        show just nat:
            xcenter 330
            easein 1.00 xcenter 630
    if right:
        show just nat:
            xcenter 930
            easein 1.00 xcenter 630
    $left = False
    $right = False


    if persistent.ch_vol == True:
        show screen sound_volume_key
        show screen volume_key
    if persistent.ch_mus == True:
        show screen music_key
    call screen talk_button





label what_was_that:
    pause(2)
    n "Ой, что произошло?"
    n "Кажется у плеера всё-таки есть повреждённый код."
    n "Здесь должен был быть визуализатор."
    n "Ну, знаешь, эти полоски, которые дрыгаются под ритм музыки."
    n "Думаю, я починю её, когда останусь одна..."

    call screen talk_button




#label update_say:

 #   n "ТУТ ТИПА ДИАЛОГИ, В КОТОРЫХ НАЦУКИ ПРЕДЛАГАЕТ ОБНОВИТЬСЯ"

  #  menu:
   #     "Обновиться сейчас":
    #        $ download_update()
     #       $ persistent.f_update = True

      #  "Потом":
       #     $ persistent.f_update = True
        #    $ persistent.f_update_show = False
