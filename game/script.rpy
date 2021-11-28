


label start:

    $ _dismiss_pause = config.developer

    $ s_name = "Сайори"
    $ m_name = "Моника"
    $ n_name = "Нацуки"
    $ y_name = "Юри"

    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True


    if persistent.autoload != "ch1_main":
        call ch0_main from _call_ch0_main



# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
