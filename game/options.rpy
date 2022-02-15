## Это шаблон версии 3.0.0. Если у вас спросят версию использованного шаблона,
## назовите им этот номер версии.
### НЕ УДАЛЯЙТЕ И НЕ ИЗМЕНЯЙТЕ ВЫШЕПРИВЕДЁННЫЙ КОММЕНТАРИЙ. ###

## options.rpy

# Этот файл настраивает то, чем является ваша модификация, а также то, как она запускается и собирается!

# Указывает название вашей модификации.
define config.name = "Natsulogue"

# Указывает, хотите ли вы, чтобы название вашей модификации отображалось в главном меню.
# Если название длинное, эту надстройку лучше отключить.
define gui.show_name = True

# Указывает номер версии вашей модификации.
define config.version = "0.3.0"

# Добавляет информацию о вашей модификации на экран «Об игре».
# В DDLC нет возможности перехода на экран «Об игре», так что можете оставить это пустым.
define gui.about = _("")

# Указывает название дистрибутива вашей модификации во время упаковки оного
# в Лаунчере Ren'Py или DDMM (Doki Doki Mod Maker).
# Примечание:
# Название сборки поддерживает только символы ASCII, т.е. числа, пробелы и точки с запятой должны быть удалены.
# Пример: было «Doki Doki Yuri Time», стало - «DokiDokiYuriTime»
define build.name = "Natsulogue"

# Указывает, есть ли в вашей модификации звуковые эффекты.
define config.has_sound = True

# Указывает, есть ли в вашей модификации музыка.
define config.has_music = True

# Указывает, есть ли в вашей модификации озвучка.
define config.has_voice = False

# Указывает, какую музыку играть при запуске модификации и в главном меню.
define config.main_menu_music = audio.t1

# Эти переменные управляют эффектами переходов в DDLC, когда игрок входит и
# выходит из меню.
# config.enter_transition указывает эффект, которым сопровождается вход в игровое меню.
# config.exit_transition указывает эффект, которым сопровождается возврат в игру.
# Dissolve(X) «растворяет» меню или последний экран в течение X секунд.
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# Указывает эффект перехода в DDLC после загрузки сохранения.
define config.after_load_transition = None

# Указывает эффект перехода, когда сюжет в вашей модификации подошёл к своему финалу.
define config.end_game_transition = Dissolve(.5)

# Указывает поведение диалогового окна, которое персонажи используют для проговаривания своих фраз.
# "auto" - диалоговое окно будет скрываться во время смены сцен и показываться, когда персонаж говорит;
# "show" - диалоговое окно будет отображаться постоянно;
# "hide" - диалоговое окно будет показываться только тогда, когда персонаж говорит.
define config.window = "auto"

# Указывает эффекты переходов диалогового окна.
# config.window_show_transition указывает эффект, которым сопровождается появление диалогового окна.
# config.window_hide_transition указывает эффект, которым сопровождается скрытие диалогового окна.
# Dissolve(X) «растворяет» меню или последний экран в течение X секунд.
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# Указывает скорость вывода текста в вашей модификации.
default preferences.text_cps = 50

# Указывает задержку при включённом режиме авточтения в вашей модификации.
default preferences.afm_time = 15

# Указывает уровни громкости микшеров по умолчанию в вашей модификации.
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

# Указывает название папки сохранённых данных вашей модификации.
# Сохранения можно найти здесь:
# Windows: %AppData%/RenPy/
# macOS: $HOME/Library/RenPy/ (включите показ папки «Библиотеки» в Настройках Finder)
# Linux: $HOME/.renpy/
define config.save_directory = "Natsulogue"

# Указывает логотип окна вашей модификации.
define config.window_icon = "gui/window_icon.png"

# Указывает, разрешено ли игроку пропускать диалоги.
define config.allow_skipping = True

# Указывает, может ли модификация автоматически сохраняться.
define config.has_autosave = False

# Указывает, может ли модификация автоматически сохраняться во время выхода из игры.
define config.autosave_on_quit = False

# Указывает количество слотов, которые автосохранение может использовать для сохранения игры.
define config.autosave_slots = 0

# Указывает, может ли игрок откатываться назад по сюжету игры.
define config.rollback_enabled = config.developer

# Эти переменные контролируют расположение слоёв экранов, изображений и прочего. 
# Настоятельно рекомендуется не трогать их.
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
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

    # Эта функция сохраняет логотип вашей модификации как файл иконки («.ico») для сборки Windows-дистрибутива
    # с собственной иконкой.
    def saveIco(filepath):
        import pygame_sdl2
        
        bmp = os.path.join(renpy.config.basedir, "icon.bmp").replace("\\", "/")
        ico = os.path.join(renpy.config.basedir, "icon.ico").replace("\\", "/")

        surf = pygame_sdl2.image.load(os.path.join(
                renpy.config.gamedir, filepath
                ).replace("\\", "/")
            )
        trans = pygame_sdl2.transform.scale(surf, (64, 64))
        pygame_sdl2.image.save(trans, bmp)

        if os.path.exists(ico):
            os.remove(ico)

        os.rename(os.path.join(renpy.config.basedir, "icon.bmp").replace("\\", "/"), 
            os.path.join(renpy.config.basedir, "icon.ico").replace("\\", "/"))
        
        renpy.show_screen("dialog", message="Экспорт логотипа вашей модификации в иконку прошёл успешно.", ok_action=Hide("dialog"))

## Настройка дистрибуции #########################################################
##
## Этот раздел контролирует, как Ren'Py строит файлы дистрибутива из вашего проекта.

init python:
    ## Следующие функции берут образцы файлов. Образцы файлов не учитывают
    ## регистр и соответствующе зависят от директории проекта (base), с или без
    ## учёта /, задающей директорию. Если обнаруживается множество одноимённых
    ## файлов, то используется только первый.
    ##
    ## Внутри образца:
    ## * включает в себя все символы, исключая разделитель директорий.
    ## ** включает в себя все символы, включая разделитель директорий.
    ##
    ## Примеры:
    ## "*.txt" берёт все файлы формата «.txt» из директории проекта.
    ## "game/**.ogg" берёт все файлы ogg из директории game и 
    ## всех поддиректорий.
    ## "**.psd" берёт все файлы psd из любого места проекта.

    # Эти функции объявляют пакеты для сборки вашей модификации, которые соответствуют условиям
    # Руководства по ИС Team Salvato. Ни в коем случае не изменяйте эти переменные.
    build.package(build.directory_name + "Mod","zip","mod",description="DDLC-совместимый мод на Ren'Py 6")
    build.package(build.directory_name + "Renpy7Mod","zip","windows linux mac renpy mod",description="DDLC-совместимый мод на Ren'Py 7")

    # Эти функции объявляют архивы, которые будут сделаны для упаковки вашей модификации.
    # Чтобы добавить ещё один архив, пропишите отдельный «build.archive», взяв в качестве примера одну из уже имеющихся функций:
    build.archive("scripts", "mod renpy")
    build.archive("game-parameters/mod_assets", "mod renpy")

    # Не трогайте эти строчки. Это нужно для того, чтобы Ren'Py добавил файл формата «.py» вашей модификации
    # и специальный лаунчер для систем Linux и macOS, необходимый для запуска.
    try: 
        build.renpy_patterns.remove(("renpy.py", ["all"]))
        build.classify_renpy("renpy.py", "renpy")
    except: pass
    
    try:
        build.early_base_patterns.remove(("*.sh", None))
        build.classify("LinuxLauncher.sh", "linux") ## Скрипт лаунчера для Linux
        build.classify("*.sh", None)
    except: pass
    
    #############################################################
    # Эти функции классифицируют пакеты для настольных (PC, Linux, macOS) и мобильных (Android) платформ.
    # Примечание переводчика: категорически не рекомендую прописывать добавление файлов «наголо» вместе с архивами,
    # в которые они уже упакованы, а аффтару советую выпить йаду за «рекомендацию», которую он написал в оригинальном скрипте.
    # Поэтому здесь, в тех местах, где это наиболее уместно, вместо «all» будет написано «android».
    
    build.classify("game/game-parameters/mod_assets/**", "game-parameters/mod_assets android")
    build.classify("game/**.rpyc", "scripts android")
    build.classify("game/README.md", None)
    build.classify("game/**.txt", "scripts android")
    build.classify("game/**.chr", "scripts android")
    build.classify("game/advanced_scripts/**","scripts android") ## Обратная совместимость
    build.classify("game/**.rpymc", "scripts android") ## Папка с переводами

    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("**.rpy", None)
    build.classify('**.rpym', None)
    build.classify("**.psd", None)
    build.classify("**.sublime-project", None)
    build.classify("**.sublime-workspace", None)
    build.classify("/music/*.*", None)
    build.classify("script-regex.txt", None)
    build.classify("/game/10", None)
    build.classify("/game/cache/*.*", None)
    build.classify("**/.DS_Store", None) # Удаление кэша Finder из дистрибутива - прим. пер.
    build.classify("**/__MACOSX/**", None) # Удаление из дистрибутива папки __MACOSX с кэшированными миниатюрами, которую Finder так же любит генерировать - прим. пер.
    build.classify("**/.vscode/**", None) # Удаление папки .vscode с конфигом VS Code из дистрибутива - прим. пер.
    build.classify("**.rpa", None)
    build.classify("README.html","mod")
    build.classify("README.linux", "linux")
   
    # Это указывает файл README.html как файл документации
    build.documentation("README.html")

    build.include_old_themes = False
