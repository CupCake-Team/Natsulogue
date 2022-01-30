default persistent.is_theme_default = True
default persistent.theme = [0, 0, 0]   

init python:  

    def set_t_b(st, at):
        return im.MatrixColor(
                "gui/textbox.png",
                im.matrix.tint(persistent.theme[0],persistent.theme[1],persistent.theme[2])
                #im.matrix.tint(0.5, 0.1, 0.9)
        ), None

    def set_n_b(st, at):
        return im.MatrixColor(
            "gui/namebox.png",
            im.matrix.tint(persistent.theme[0],persistent.theme[1],persistent.theme[2])
        ), None

    class ColorTheme(object):
        def blue(self):
            #persistent.theme = [0.5, 0.7, 1.0]
            persistent.theme = [0.1, 0.5, 1.0]
            print(persistent.theme)
            persistent.is_theme_default = False
            return
        
        def yellow(self):
            persistent.theme = [1.0, 0.5, -0.5]
            print(persistent.theme)
            persistent.is_theme_default = False
            return

        def green(self):
            persistent.theme = [-1.0, 1.0, -1.0]
            print(persistent.theme)
            persistent.is_theme_default = False
            return

        def red(self):
            persistent.theme = [1.0, 0.4, 0.4]
            print(persistent.theme)
            persistent.is_theme_default = False
            return

        def purple(self):
            persistent.theme = [0.7, 0.4, 0.8]
            print(persistent.theme)
            persistent.is_theme_default = False
            return
            
        def default(self):
            persistent.theme = [1.0, 1.0, 1.0]
            persistent.is_theme_default = True
            return
