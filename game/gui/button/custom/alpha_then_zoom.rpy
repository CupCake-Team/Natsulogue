label Test3:
    scene bg club_day

    show monika 1a at t11 zorder 2

    "Elckarow" "you'll see how this shit work"
    "Elckarow" "first, we set alpha to 0, wait 1s, then change the alpha value"

    show monika at zoom_alpha_thing

    "Elckarow" "wait for the alpha changes to be done"
    "Elckarow" "now, the game waits for a certain variable to be True to zoom"
    "Elckarow" "so in the meantime, i can say as much shit as i want"
    "Elckarow" "a"
    "Elckarow" "b"
    "Elckarow" "c"
    "Elckarow" "d"
    "Elckarow" "k stop"
    "Elckarow" "now look into the nuke script line 25"
    "Elckarow" "this is the flag to do the zoom changes"
    "Elckarow" "setting it to True will allow the zoom"
    "Elckarow" "ready?"
    "Elckarow" "3, 2, 1..."

    $ trans_var["monika"][1] = True

    "Elckarow" "tadaaaaaa"
    "Elckarow" "pretty cool huh?"
    "Elckarow" "anyway that's it"
    "Elckarow" "see ya"

    return





init python:
    def transform_function(f):
        """
        Decorator to pass arguments to transform functions

        """
        def arguments_f(*args, **kwargs):
            def renpyfunction_f(trans, st, at):
                return f(trans, st, at, *args, **kwargs)
            return renpyfunction_f
        return arguments_f


    @transform_function
    def alpha_thing(trans, st, at, alpha_value, time_alpha, mode, n):
        global trans_var

        if (st <= time_alpha):

            #is the game skipping?
            if renpy.is_skipping(): #if False: if there's an issue
                #if so, do the changes immediately
                trans.alpha = 1.0
                #get the hell outta here
                return None

            if mode in {easein_pow, ease_pow, easeout_pow}:
                trans.alpha = (alpha_value * mode(st, time_alpha, n))
                return 0.0
            trans.alpha = (alpha_value * mode(st, time_alpha))
            return 0.0

        #get the hell outta here
        return None
        
    @transform_function
    def zoom_thing(trans, st, at, who, zoom_value, time_zoom, mode, n):
        global trans_var

        #are we being told to do the zoom?
        if (not trans_var[who][1]): #comment this shit it renpy won't do the zoom, it'll do it instantly but idk...
            #if not wait for it (check every 0.5s)
            return 0.5
        
        if (st <= time_zoom):
            if mode in {easein_pow, ease_pow, easeout_pow}:
                trans.zoom = 0.8 + (mode(st, time_zoom, n) / zoom_value)
                return 0.0
            trans.zoom = 0.8 + (mode(st, time_zoom) / zoom_value)
            return 0.0
        return None


    #warpers
    def linear(st, time):
        return (st / time)

    def easein(st, time):
        from math import cos, pi
        return cos(((1.0 - (st / time)) * pi) / 2.0)

    def easeout(st, time):
        from math import cos, pi
        return (1.0 - cos(((st / time) * pi) / 2.0))

    def ease(st, time):
        from math import cos, pi
        return (0.5 - (cos(pi * (st / time)) / 2))

    def easeout_pow(st, time, n, from_what=None):
        if not from_what:
            return pow((st / time), n)
        if (from_what == "easein_pow"):
            return pow((1.0 - (st / time)), n) 
        elif (from_what == "ease_pow_1"):
            return pow(((st / time) * 2.0), n)
        elif (from_what == "ease_pow_2"):
            return pow(((1.0 - (st / time)) * 2.0), n)
        return 0.0

    def easein_pow(st, time, n):
        return (1.0 - easeout_pow(st, time, n, from_what="easein_pow"))

    def ease_pow(st, time, n):
        if (st / time) < 0.5:
            return (easeout_pow(st, time, n, from_what="ease_pow_1") / 2.0)
        return (1.0 - (easeout_pow(st, time, n, from_what="ease_pow_2") / 2.0))





transform zoom_alpha_thing(who="monika", alpha_init=0.0, alpha=1.0, zoom=1.5, time_a=0.5, time_z=1.0, mode_a=ease, mode_z=linear, n_a=3, n_z=3):
    subpixel True
    alpha alpha_init
    pause 1.0
    function alpha_thing(alpha_value=alpha, time_alpha=time_a, mode=mode_a, n=n_a)
    function zoom_thing(who=who, zoom_value=zoom, time_zoom=time_z, mode=mode_z, n=n_z)


#thing to store trans variable
# "who": [some value we wanna store, some flags and shit...]
define trans_var = {
    "monika": [0, False, False, False]
}