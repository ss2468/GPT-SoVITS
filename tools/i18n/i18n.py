import json
import os

import locale

# todo 切换-路径
def switch_path(path: str):
    if "UntitledProjects" in os.getcwd():
        return path.replace("./i18n", "C:/Users/Administrator/UntitledProjects/GPT-SoVITS/tools/i18n")
    else:
        return path

def load_language_list(language):
    with open(switch_path(f"./i18n/locale/{language}.json"), "r", encoding="utf-8") as f:
        language_list = json.load(f)
    return language_list

class I18nAuto:
    def __init__(self, language=None):
        if language in ["Auto", None]:
            language = locale.getdefaultlocale()[
                0
            ]  # getlocale can't identify the system's language ((None, None))
        if not os.path.exists(switch_path(f"./i18n/locale/{language}.json")):
            language = "en_US"
        self.language = language
        self.language_map = load_language_list(language)

    def __call__(self, key):
        return self.language_map.get(key, key)

    def __repr__(self):
        return "Use Language: " + self.language
