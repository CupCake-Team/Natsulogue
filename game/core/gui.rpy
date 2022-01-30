init offset = -2









init python:
    gui.init(1280, 720)







define gui.hover_sound = "gui/sfx/hover.ogg"
define gui.activate_sound = "gui/sfx/select.ogg"
define gui.activate_sound_glitch = "gui/sfx/select_glitch.ogg"




define gui.window_background = Image("gui/textbox.png", xalign=0.5, yalign=1.0)


define gui.accent_color = '#ffffff'


define gui.idle_color = '#140f0b'



define gui.idle_small_color = '#333'


define gui.hover_color = '#703752'



define gui.selected_color = '#302d2e'


define gui.insensitive_color = '#aaaaaa7f'



define gui.muted_color = '#6666a3'
define gui.hover_muted_color = '#9999c1'


define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'





define gui.default_font = "gui/font/comic.ttf"


define gui.name_font = "gui/font/Rotonda.ttf"


define gui.interface_font = "gui/font/DejaVuSans.ttf"


define gui.splash_text_size = 26


define gui.text_size = 20


define gui.name_text_size = 22


define gui.interface_text_size = 22


define gui.label_text_size = 24


define gui.notify_text_size = 16


define gui.title_text_size = 38

define gui.check_button_text_size = 22

define gui.pref_label_text_size = 24

define gui.poemgame_text_size = 26

define gui.main_menu_background = "menu_bg"
define gui.game_menu_background = "game_menu_bg"


define gui.show_name = True








define gui.textbox_height = 182



define gui.textbox_yalign = 0.99




define gui.name_xpos = 350
define gui.name_ypos = -3



define gui.name_xalign = 0.5



define gui.namebox_width = 200
define gui.namebox_height = 39



define gui.namebox_borders = Borders(5, 5, 5, 2)



define gui.namebox_tile = False





define gui.text_xpos = 260
define gui.text_ypos = 58


define gui.text_width = 760
define gui.ctc_xalign = 0.81
define gui.ctc_ease_x = 0.75
define gui.ctc_ease_yoffset = 0
define gui.ctc_ease_zoom = 1.0


define gui.text_xalign = 0.0








define gui.button_width = None
define gui.button_height = 36


define gui.button_borders = Borders(4, 4, 4, 4)



define gui.button_tile = False


define gui.button_text_font = gui.interface_font


define gui.button_text_size = gui.interface_text_size


define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color



define gui.button_text_xalign = 0.0





define gui.poem_viewport_xsize = 720
define gui.poem_viewport_xpos = 280
define gui.poem_vbar_xpos = 1000
define gui.poem_child_size = 710




define gui.radio_button_borders = Borders(28, 4, 4, 4)

define gui.check_button_borders = Borders(28, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5
define gui.confirm_frame_yalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)


define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = "#522"
define gui.quick_button_text_hover_color = "#fcc"
define gui.quick_button_text_selected_color = gui.accent_color
define gui.quick_button_text_insensitive_color = "#884d4d"
define gui.quick_button_text_outlines = []












define gui.choice_button_width = 420
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.default_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#000"
if !persistent.is_theme_default:
    define gui.choice_button_text_hover_color = persistent.theme_choice_color
else:
    define gui.choice_button_text_hover_color = "#fa9"    




define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_hover_color = gui.hover_color


define config.thumbnail_width = 256
define config.thumbnail_height = 144


define gui.file_slot_cols = 3
define gui.file_slot_rows = 2

define gui.game_menu_label_xpos = 50
define gui.navigation_xpos = 80
define gui.navigation_button_text_size = 24
define gui.navigation_spacing = 6


define gui.skip_ypos = 10


define gui.notify_ypos = 45


define gui.choice_spacing = 22


define gui.pref_spacing = 10


define gui.pref_button_spacing = 0


define gui.page_button_text_size = 24

define gui.page_spacing = 0

define gui.slot_spacing = 10








define gui.frame_borders = Borders(4, 4, 4, 4)


define gui.confirm_frame_borders = Borders(40, 40, 40, 40)


define gui.skip_frame_borders = Borders(16, 5, 50, 5)


define gui.notify_frame_borders = Borders(16, 5, 40, 5)


define gui.frame_tile = False











define gui.bar_size = 36
define gui.scrollbar_size = 12
define gui.slider_size = 30


define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False


define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)


define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)



define gui.unscrollable = "hide"







define config.history_length = 50



define gui.history_height = None



define gui.history_name_xpos = 0
define gui.history_name_ypos = 0
define gui.history_name_width = 170
define gui.history_name_xalign = 0.0


define gui.history_text_xpos = 200
define gui.history_text_ypos = 5
define gui.history_text_width = 710
define gui.history_text_xalign = 0.0







define gui.nvl_borders = Borders(0, 10, 0, 20)



define gui.nvl_height = 115



define gui.nvl_spacing = 10



define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0


define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0



define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0


define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0







init python:









    layout.ARE_YOU_SURE = _("Вы уверены?")
    layout.DELETE_SAVE = _("Вы уверены, что хотите удалить сохранение?")
    layout.OVERWRITE_SAVE = _("Вы уверены, что хотите перезаписать сохранение?")
    layout.LOADING = _("Загрузка приведёт к потере прогресса.\nВы уверены, что хотите это сделать?")
    layout.QUIT = _("Вы уверены, что хотите выйти?")
    layout.MAIN_MENU = _("Вы уверены, что хотите вернуться в главное меню?\nЭто приведёт к потере прогресса.")
    layout.END_REPLAY = _("Вы уверены, что хотите остановить повтор?")
    layout.SLOW_SKIP = _("Вы уверены, что хотите начать пропуск текста?")
    layout.FAST_SKIP_UNSEEN = _("Вы уверены, что хотите пропустить непрочитанный текст до следующего выбора?")
    layout.FAST_SKIP_SEEN = _("Вы уверены, что хотите перейти к следующему выбору?")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
