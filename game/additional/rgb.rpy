default persistent.is_theme_default = True
default persistent.theme = 0.0

init python:

    def set_t_b(st, at):
        return  im.MatrixColor(
            "gui/textbox.png",
            im.matrix.hue(persistent.theme)
            #im.matrix.hue(90)
        ), None

    def set_n_b(st, at):
        return im.MatrixColor(
            "gui/namebox.png",
            #im.matrix.tint(persistent.theme[0],persistent.theme[1],persistent.theme[2])
            im.matrix.hue(persistent.theme)
        ), None

    def inactive_but(num):
        if num == "vis":
            return At(im.Scale(im.MatrixColor("gui/button/custom/round_inactive.png", im.matrix.hue(persistent.theme)), 120, 214), v_but)
        if num == "prev":
            return At(im.Scale(im.MatrixColor("gui/button/custom/round_inactive.png", im.matrix.hue(persistent.theme)), 120, 214), p_but)
        if num == "next":
            return At(im.Scale(im.MatrixColor("gui/button/custom/round_inactive.png", im.matrix.hue(persistent.theme)), 120, 214), n_but)
        if num == "back":
            return At(im.Scale(im.MatrixColor("gui/button/custom/round_inactive.png", im.matrix.hue(persistent.theme)), 120, 214), b_but)

    class ColorTheme(object):
        def blue(self):
            # 90
            #persistent.theme = [0.5, 0.7, 1.0]
            #persistent.theme = [0.1, 0.5, 1.0]
            persistent.theme = -90
            print(persistent.theme)
            persistent.is_theme_default = False
            return

        def yellow(self):
            #75
            #persistent.theme = [1.0, 0.5, -0.5]
            persistent.theme = 75.0
            print(persistent.theme)
            persistent.is_theme_default = False
            return

        def green(self):
            # 180
            #persistent.theme = [-1.0, 1.0, -1.0]
            persistent.theme = -180.0
            print(persistent.theme)
            persistent.is_theme_default = False
            return

        def orange(self):
            # 45
            #persistent.theme = [1.0, 0.4, 0.4]
            persistent.theme = 45.0
            print(persistent.theme)
            persistent.is_theme_default = False
            return

        def default(self):
            # 0 or 360
            #persistent.theme = [1.0, 1.0, 1.0]
            persistent.theme = 0.0
            persistent.is_theme_default = True
            return
