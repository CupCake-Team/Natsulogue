default persistent.is_theme_default = True
default persistent.theme_choice_color = "#fa9"
default persistent.theme = [0, 0, 0]

init python:
    class SetColorTheme():

        def blue(self):
            print(persistent.theme)
            persistent.theme = [0.5, 0.7, 1.0]
            persistent.theme_choice_color = "#346d94"
            persistent.is_theme_default = False
            print(persistent.theme)
            return
        
        def default(self):
            persistent.is_theme_default = True
            print(persistent.theme)
            return