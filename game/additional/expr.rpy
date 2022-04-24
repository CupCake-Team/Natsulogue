image desk = "mod_assets/natsuki/table/desk.png"
init -10 python:

    import store
    import store.sayo_utilities as sayo_utilities

    sayo_zorder = 3
    sayo_zoom = 0.5

    pose = "/sitting/"


    _NATSUKI_IMAGES_PATH = "mod_assets/natsuki/"


    #EYEBROW DEFS
    class Eyebrows():
        normal = "a"
        frown = "b"
        angry = "c"
        lfrn = "d"
        smug = "e"
        furrowed = "f"
        numb = "n"

        def __str__(self):
            return self.name

    class Backarms():
        unknown = "a"
        empty = "b"

        def __str__(self):
            return self.name

    #LEFT OR BOTH ARMS ONLY! NO RIGHT ARMS STUFF
    
    class Arms():
        cookiebite = "cb"
        cookie = "cookie"
        doublepoint = "double-point"
        folded = "folded"
        lefttouch = "left-fingers-touching"
        leftindex = "left-index-point"
        leftrest = "left-table-rest"
        none = "empty"

        def __str__(self):
            return self.name
    
    
    # RIGHT ARM DEFS
    class Arms2():

        folded = "folded"
        rtr = "right-table-rest"
        rf = "right-fist"
        rfpe = "right-finger-pup-ext"
        dp = "double-point"
        hrt = "hand-restingtop"
        none = "empty"

        def __str__(self):
            return self.name
    
    #EYE DEFS
    class Eyes():
        normal = "a"
        lookleft = "b"
        closed = "c"
        wink = "d"
        eyaa = "e"
        sad = "f"
        crazy = "g"
        wide = "h"
        smug = "i"
        unk = "j"
        
        def __str__(self):
            return self.name
    #HAIR DEFS
    class Hair():
        no_bow = "n"
        bow = "b"
        
        def __str__(self):
            return self.name
    #MOUTH DEFS
    class Mouth():
        a = "a"
        b = "b"
        c = "c"
        d = "d"
        e = "e"
        f = "f"
        g = "g"
        h = "h"
        i = "i"
        j = "j"
        k = "k"
        l = "big_frown"
        m = "drool"
        n = "drool_frown"
        o = "open"
        p = "pout"
        
        
        def __str__(self):
            return self.name


    class Tears():
        d_tears = "d_tears"
        happy_d_tears = "happy_d_tears"
        pooled_tears = "pooled_tears"
        sad_d_tears = "sad_d_tears"
        crumbs = "crumbs"
        sweat_drop = "sweat-drop"
        none = None

        def __str__(self):
            return self.name

    class Blush():
        blushing = "blushing"
        default_cheeks = "default_cheeks"
        red_eyes = "eye-redness"
        gloomy = "gloomy"
        none = None

        def __str__(self):
            return self.name

    def realgen(
        backarm,
        arms,
        arms2,
        hair,
        eyes,
        eyebrows,
        mouth,
        blush=None,
        tears=None
    ):
        """
        """
        ad_hoc = [
            (1280, 720),
            (0, 0), "{0}{1}/backarms/{2}.png".format(_NATSUKI_IMAGES_PATH, pose, backarm),
            (0, 0), "{0}{1}/arms/uniform/back-sleeve.png".format(_NATSUKI_IMAGES_PATH, pose),
            (0, 0), "{0}{1}/body/1.png".format(_NATSUKI_IMAGES_PATH, pose),
            ]

        ad_hoc.extend([
            (0, 0), "{0}{1}/arms/uniform/{2}.png".format(_NATSUKI_IMAGES_PATH, pose, arms),
            (0, 0), "{0}{1}/arms/uniform/{2}.png".format(_NATSUKI_IMAGES_PATH, pose, arms2),
            (0, 0), "{0}{1}/hair/{2}.png".format(_NATSUKI_IMAGES_PATH, pose, hair),
        ])

        if blush:
            ad_hoc.extend([
                (0, 0), "{0}{1}/body/blush/{2}.png".format(_NATSUKI_IMAGES_PATH, pose, blush),
            ])
        
        ad_hoc.extend([
            (0, 0), "{0}{1}/eyes/{2}.png".format(_NATSUKI_IMAGES_PATH, pose, eyes),
            (0, 0), "{0}{1}/mouth/{2}.png".format(_NATSUKI_IMAGES_PATH, pose, mouth),
            ])

        if tears:
            ad_hoc.extend([
                (0, 0), "{0}{1}/eyes/{2}.png".format(_NATSUKI_IMAGES_PATH, pose, tears),
            ])
        
        ad_hoc.extend([
              
            (0, 0), "{0}{1}/eyebrows/{2}.png".format(_NATSUKI_IMAGES_PATH, pose, eyebrows)
            
        ])
       
        return renpy.display.layout.LiveComposite(
            *ad_hoc
            )

init 1 python:
    #EYEBROWS
    EYEBROWS_DEF = {
        "a": Eyebrows.normal,
        "b": Eyebrows.frown,
        "c": Eyebrows.angry,
        "d": Eyebrows.lfrn,
        "e": Eyebrows.smug,
        "f": Eyebrows.furrowed,
        "g": Eyebrows.numb
    }

    BACKARM_DEF = {
        "a": Backarms.unknown,
        "b": Backarms.empty
    }

    #Arms with BOTH or ONLY LEFT NO RIGHT
    ARMS_DEF = {
        "a": Arms.folded,
        "b": Arms.leftindex,
        "c": Arms.cookie,
        "d": Arms.cookiebite,
        "e": Arms.doublepoint,
        #"f": Arms.leftindex,
        "f": Arms.leftrest,
        "g": Arms.lefttouch,
        "h": Arms.none
    }
    ARMS2_DEF = {
        "a": Arms2.folded,
        "b": Arms2.rtr,
        "c": Arms2.rf,
        "d": Arms2.rfpe,
        "e": Arms2.dp,
        "f": Arms2.hrt,
        "g": Arms2.none
    }
    #EYES ONLY
    EYES_DEF = {
        "a": Eyes.normal,
        "b": Eyes.lookleft,
        "c": Eyes.closed,
        "d": Eyes.wink,
        "e": Eyes.eyaa,
        "f": Eyes.sad,
        "g": Eyes.crazy,
        "h": Eyes.wide,
        "i": Eyes.smug,
        "j": Eyes.unk
    }
    #HAIR
    HAIR_DEF = {
        "b": Hair.bow,
        "n": Hair.no_bow
    }
    #MOUTH
    MOUTH_DEF = {
        "a": Mouth.a,
        "b": Mouth.b,
        "c": Mouth.c,
        "d": Mouth.d,
        "e": Mouth.e,
        "f": Mouth.f,
        "g": Mouth.g,
        "h": Mouth.h,
        "i": Mouth.i,
        "j": Mouth.j,
        "k": Mouth.k,
        "l": Mouth.l,
        "m": Mouth.m,
        "n": Mouth.n,
        "o": Mouth.o,
        "p": Mouth.p
    }
    
    BLUSH_DEF = {
        "a": Blush.default_cheeks,
        "b": Blush.blushing,
        "c": Blush.gloomy,
        "d": Blush.red_eyes,
        "": Blush.none
    }

    TEARS_DEF = {
        "e": Tears.d_tears,
        "f": Tears.happy_d_tears,
        "g": Tears.pooled_tears,
        "h": Tears.sad_d_tears,
        "i": Tears.crumbs,
        "j": Tears.sweat_drop,
        "": Tears.none
    }

    

    def _exp_renderer(exp_code):
        if len(exp_code) < 7:
            raise ValueError("Invalid expression code: {0}".format(exp_code))
        

        eyebrows = exp_code[0]
        exp_code = exp_code[1:]

        backarm = exp_code[0]
        exp_code = exp_code[1:]

        arms = exp_code[0]
        exp_code = exp_code[1:]

        arms2 = exp_code[0]
        exp_code = exp_code[1:]

        hair = exp_code[0]
        exp_code = exp_code[1:]

        eyes = exp_code[0]
        exp_code = exp_code[1:]

        mouth = exp_code[0]
        exp_code = exp_code[1:]
        
        blush = None
        tears = None
        


        while exp_code:
            exp_part = exp_code[0]
            exp_code = exp_code[1:]

            if exp_part in BLUSH_DEF:
                blush = exp_part
            #Check if part is a tear
            if exp_part in TEARS_DEF:
                tears = exp_part

            #Otherwise it might be a blush
            

        return {

            "eyebrows": EYEBROWS_DEF[eyebrows],
            "backarm": BACKARM_DEF[backarm],
            "arms": ARMS_DEF[arms],
            "arms2": ARMS2_DEF[arms2],
            "hair": HAIR_DEF[hair],
            "eyes": EYES_DEF[eyes],
            "mouth": MOUTH_DEF[mouth],
            "blush": BLUSH_DEF.get(blush),
            "tears": TEARS_DEF.get(tears)
            
        }

        



    def _auto_gen(exp_code):
        

        disp = realgen(**_exp_renderer(exp_code))

        _existing_attr_list = renpy.display.image.image_attributes["natsuki"]

        renpy.display.image.images[("natsuki", exp_code)] = disp

        #if exp_code not in _existing_attr_list:
        #    _existing_attr_list.append(exp_code)

    def _find_target_override(self):
        
        name = self.name

        if isinstance(name, renpy.display.core.Displayable):
            self.target = name
            return True

        if not isinstance(name, tuple):
            name = tuple(name.split())

        def error(msg):
            self.target = renpy.text.text.Text(msg, color=(255, 0, 0, 255), xanchor=0, xpos=0, yanchor=0, ypos=0)

            if renpy.config.debug:
                raise Exception(msg)

        args = [ ]

        while name:
            target = renpy.display.image.images.get(name, None)

            if target is not None:
                break

            args.insert(0, name[-1])
            name = name[:-1]

        if not name:
            if (
                isinstance(self.name, tuple)
                and len(self.name) == 2
                and self.name[0] == "natsuki"
            ):
                #Reset name
                name = self.name
                #Generate
                _auto_gen(name[1])
                #Try to get the img again
                target = renpy.display.image.images[name]

            else:
                error("Image '%s' not found." % ' '.join(self.name))
                return False

        try:
            a = self._args.copy(name=name, args=args)
            self.target = target._duplicate(a)

        except Exception as e:
            if renpy.config.debug:
                raise

            error(str(e))

        #Copy the old transform over.
        new_transform = self.target._target()

        if isinstance(new_transform, renpy.display.transform.Transform):
            if self.old_transform is not None:
                new_transform.take_state(self.old_transform)

            self.old_transform = new_transform

        else:
            self.old_transform = None

        return True

    renpy.display.image.ImageReference.find_target = _find_target_override


image natsuki idle:

    "natsuki abaabaa"
    zoom 0.17
    xpos 0.30
    ypos 0.122
