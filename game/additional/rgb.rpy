default persistent.is_theme_default = True
default persistent.theme = 0.0

init python:

    def set_t_b(st, at):
        return  im.MatrixColor(
            "gui/textbox.png",
            im.matrix.hue(persistent.theme)
        ), None

    def set_n_b(st, at):
        return im.MatrixColor(
            "gui/namebox.png",
            im.matrix.hue(persistent.theme)
        ), None

    def inactive_but(num):
        if num == "vis":
            return At(im.Scale(im.MatrixColor("mod_assets/button/custom/round_inactive.png", im.matrix.hue(persistent.theme)), 120, 214), v_but)
        if num == "prev":
            return At(im.Scale(im.MatrixColor("mod_assets/button/custom/round_inactive.png", im.matrix.hue(persistent.theme)), 120, 214), p_but)
        if num == "next":
            return At(im.Scale(im.MatrixColor("mod_assets/button/custom/round_inactive.png", im.matrix.hue(persistent.theme)), 120, 214), n_but)
        if num == "back":
            return At(im.Scale(im.MatrixColor("mod_assets/button/custom/round_inactive.png", im.matrix.hue(persistent.theme)), 120, 214), b_but)

    def vol_cir():
        return im.MatrixColor("mod_assets/button/custom/volume_circle_level.png", im.matrix.hue(persistent.theme))

    def place_but():
        return LiveComposite((100,100), (0,0), im.MatrixColor(im.Scale("mod_assets/button/custom/cup_button_back.png", 100, 100), im.matrix.hue(persistent.theme)), (0,0), im.Scale("mod_assets/button/custom/cup_button_nat.png", 100, 100))

    def place_hover_but():
        return LiveComposite((100,100), (0,0), im.MatrixColor(im.Scale("mod_assets/button/custom/cup_button_hover_back.png", 100, 100), im.matrix.hue(persistent.theme)), (0,0), im.Scale("mod_assets/button/custom/cup_button_hover_nat.png", 100, 100))

    class ColorTheme(object):
        def blue(self):
            # 90
            persistent.theme = -90
            print(persistent.theme)
            persistent.is_theme_default = False
            renpy.save_persistent()
            return

        def yellow(self):
            #75
            persistent.theme = 75.0
            print(persistent.theme)
            persistent.is_theme_default = False
            renpy.save_persistent()
            return

        def green(self):
            # 180
            persistent.theme = -180.0
            print(persistent.theme)
            persistent.is_theme_default = False
            renpy.save_persistent()
            return

        def orange(self):
            # 45
            persistent.theme = 45.0
            print(persistent.theme)
            persistent.is_theme_default = False
            renpy.save_persistent()
            return

        def default(self):
            # 0 or 360
            persistent.theme = 0.0
            persistent.is_theme_default = True
            renpy.save_persistent()
            return
