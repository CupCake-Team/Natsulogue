# Mod language functions
init -10 python:
    from collections import OrderedDict
    
    class GameLang:
        def __init__(self, code, name = None, unicode = True, unix_code = None, wip = False):
            self.code = code #Stands for the language's ISO 639-3 code (excepting English, whose value is None) and the Ren'py language name
            self.name = name or code #Full language name (should be translatable)
            self.unicode = unicode #Does language use non-ASCII characters? (Then we replace all ASCII fonts with their Unicode analogs)
            self.wip = False if (wip is None) else wip #the language pack is not complete, so it's available only for developers
    
    lang_dict = OrderedDict() #Language list
    lang_dict["rus"] = GameLang(None, _("Русский"), False)
    lang_dict["eng"] = GameLang("eng", _("Английский"), True, "en")
    def cur_lang():
        lang = lang_dict.get(_preferences.language) or lang_dict["eng"]
        if type(lang) == tuple:
            lang = lang[0]
        return lang
    
    try:
        lang = None
        
        if renpy.windows:
            import locale, subprocess
            
            lang = subprocess.check_output("wmic os get Locale", shell=True)
            lang = int(lang.split('\n')[1], 16)
            lang = locale.windows_locale.get(lang) or "en"
            lang = lang[:2]
            
        else:
            import os
            
            lang = os.environ.get("LANG") or 'en'
            lang = lang[:2]
            
        for l in lang_dict.values():
            if type(l) == tuple:
                l = l[0]
            if l.unix_code == lang:
                config.default_language = l.code
                break
    except:
        pass
