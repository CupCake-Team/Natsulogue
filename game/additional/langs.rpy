# Mod language functions
init -10 python:
    from collections import OrderedDict

    class GameLang:
        def __init__(self, code, name = None, unicode = True,  unix_code = None, wip = False):
            self.code = code #Stands for the language's ISO 639-3 code (excepting English, whose value is None) and the Ren'py language name
            self.name = name or code #Full language name (should be translatable)
            self.unicode = unicode #Does language use non-ASCII characters? (Then we replace all ASCII fonts with their Unicode analogs)
            self.unix_code = unix_code or code[:2] # Unix locale code's 2 first letters
            self.wip = wip #the language pack is not complete, so it's available only for developers

    lang_dict = dict()#OrderedDict() #Language list
    lang_dict["rus"] = GameLang(None, _("Russian"), False, "ru")
    lang_dict["eng"] = GameLang("eng", _("English"), True, "en")

    def cur_lang():
        lang = lang_dict.get(_preferences.language) or lang_dict["rus"]
        if type(lang) == tuple:
            lang = lang[0]
        return lang

    lang = None

    if renpy.windows:
        import locale
        #lang = list(locale.getlocale())[0].split("_")[0].lower()[:3]   
    else:
        import os
        lang = os.environ.get("LANG") or 'rus'
        lang = lang[:3]

    #lang = "eng"

    if lang in list(lang_dict.keys()):
        config.language = lang_dict[lang].code
    else:
        config.language = None
