
character_map = {
    '：': '，',
    '；': '，',
    '！': '。',
    '（': '，',
    '）': '，',
    '【': '，',
    '】': '，',
    '『': '，',
    '』': '，',
    '「': '，',
    '」': '，',
    '《': '，',
    '》': '，',
    '－': '，',
    '‘': '',
    '“': '',
    '’': '',
    '”': '',
    ':': ',',
    ';': ',',
    '!': '.',
    '(': ',',
    ')': ',',
    '[': ',',
    ']': ',',
    '>': ',',
    '<': ',',
    '-': ',',
    '…': '',
    '—': ',',
}

motion_map = {
    '，': '[uv_break]',
    '。': '[lbreak]',
}

class TextUtils:
    def __init__(self,text="",file=""):
        # if text != "":
        #     self.text = text
        # else:
        #     log.info("Reading file: " + file)
        #     if file == "":
        #         # 抛出异常
        #         log.error("File not found")
        #         return
        #     with open(file, 'r', encoding='utf-8') as f:
        #         self.text = f.read()
        self.text = text
        self.out = ""

    def convert_half_width_to_full_width(self):
        """
        将半角字符转换为全角字符
        """
        out = ""
        for char in self.text:
            if ord(char) == 32:
                out += "　"
            elif 33 <= ord(char) <= 126:
                out += chr(ord(char) + 65248)
            else:
                out += char
        self.out = out
        return self.out
    def apply_character_map(self):
        """
        将字符映射到对应的字符
        """
        translation_table = str.maketrans(character_map)
        self.out = self.out.translate(translation_table)
        return self.out
    def apply_motion_map(self):
        """
        将字符映射到对应的动作
        """
        translation_table = str.maketrans(motion_map)
        self.out = self.out.translate(translation_table)
        return self.out