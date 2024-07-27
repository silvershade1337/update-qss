import re

class st:
    def __init__(self):
        self.ssht = """\
        font-size: 20px;
        font-weight: Bold;
        """

    def setStyleSheet(self, stylesheet: str):
        self.ssht = stylesheet

    def styleSheet(self):
        return self.ssht

def updateStyleSheet(stylable, style: str):
    prop, val = map(lambda strg: strg.strip(), style.split(":"))
    val = val[:-1] if val.endswith(";") else val
    s = stylable.styleSheet()
    print(stylable.styleSheet(), end="\n")
    stylable.setStyleSheet(re.sub(f"{prop} *: *[^;\n]*;?", f"{prop}: {val};", s))
    print(stylable.styleSheet(), end="\n")

def behappy():
    print("habibi")

updateStyleSheet(st(), "font-weight: 40px;")