#!/usr/bin/env python3

#   -------------------------------------------------------------
#   Rhyne-Wise
#   - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Project:        Nasqueron
#   Description:    Pywikibot configuration
#   License:        BSD-2-Clause
#   Site:           Nasqueron Agora
#   -------------------------------------------------------------


from pywikibot import family


class Family(family.Family):  # noqa: D101

    name = "agora"
    langs = {
        "agora": "agora.nasqueron.org",
    }

    def scriptpath(self, code):
        return {
            "agora": "",
        }[code]

    def protocol(self, code):
        return {
            "agora": "https",
        }[code]
