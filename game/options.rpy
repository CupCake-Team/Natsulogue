

init -1:
   python hide:
      config.developer = True
      config.quit_action = renpy.curried_call_in_new_context("save_exp")






define config.name = "Doki Doki Literature Club?"



define gui.show_name = False




define config.version = "-0.0.5"





define gui.about = _("")






define build.name = "Natsulogue"






define config.has_sound = True
define config.has_music = True
define config.has_voice = False













define config.main_menu_music = audio.t1










define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)




define config.after_load_transition = None




define config.end_game_transition = Dissolve(.5)









define config.hard_rollback_limit = 0






define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 15

default preferences.music_volume = 1.0
default preferences.sfx_volume = 1.0
















define config.save_directory = "DDLC-1454445547"







define config.window_icon = "gui/window_icon.png"



define config.allow_skipping = False
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = False
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"


init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014')
        s = s.replace(' - ', u'\u2014')
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)






init python:
    ## Следующие функции принимают шаблоны файлов. Файловые шаблоны не чувствительны к регистру.
    ## нечувствительны и сопоставляются с путем относительно базового каталога,
    ## с ведущим / и без него. Если совпадает несколько шаблонов, используется первый.
    ## используется.
    ##
    ## В шаблоне:
    ##
    ## / - это разделитель каталогов.
    ##
    ## * соответствует всем символам, кроме разделителя каталогов.
    ##
    ## ** соответствует всем символам, включая разделитель каталогов.
    ##
    ## Например, "*.txt" соответствует файлам txt в базовом каталоге, "game/
    ## **.ogg" соответствует файлам ogg в каталоге игры или любом из его
    ## поддиректории, а "**.psd" соответствует psd-файлам в любом месте проекта.

    # Код для упаковки вашего мода в ZIP в Ren'Py

    build.package(build.directory_name + "Mod",'zip','mod',description="Ren'Py 6 DDLC Compliant Mod")
    build.package(build.directory_name + "Renpy7Mod",'zip','windows linux mac renpy mod',description="Ren'Py 7 DDLC Compliant Mod")

    build.archive("scripts", 'mod all')
    build.archive("mod_assets", 'mod all')

    ## Не трогайте это. Это нужно для того, чтобы Ren'Py мог добавить файл .sh. 
    ## для Linux/Mac, чтобы запустить ваш мод.
    try:
        build.renpy_patterns.remove((u'renpy.py', [u'all']))
    except:
        pass
    build.classify_renpy("renpy.py", "renpy all")
    
    #############################################################

    # Чтобы классифицировать пакеты для pc и android, обязательно добавьте к ним all, как показано ниже.
    
    build.classify("game/mod_assets/**", "mod_assets all")
    build.classify("game/**.rpyc", "scripts all")
    build.classify("game/README.md", None)
    build.classify("game/**.txt", "scripts all")
    build.classify("game/**.chr", "scripts all")
    build.classify("game/advanced_scripts/**","scripts all") ## Обратная совместимость
    build.classify("game/tl/**", "scripts all") ## Папка переводов

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa', None)
    build.classify('README.html','mod all')

    # Установите README.html в качестве документации
    build.documentation('README.html')

    build.include_old_themes = False

define build.itch_project = "teamsalvato/ddlc"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
