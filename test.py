from chpronounce import ChPronounce

chp = ChPronounce()
print(chp.get_duyin("吃飽了沒？"))
print(chp.get_zhuyin("吃飽了"))
print(chp.get_pinyin("我能吃玻璃而不傷身體"))
print(chp.get_duyin("我睡著了"))
print(chp.get_duyin("一句話"))

# Output:
# [('chi', 'ㄔ', 1), ('bao', 'ㄅㄠ', 3), ('le', 'ㄌㄜ', 5), ('mei', 'ㄇㄟ', 2), ('？', '？', 0)]
# [('ㄔ', 1), ('ㄅㄠ', 3), ('ㄌㄜ', 5)]
# [('wo', 3), ('neng', 2), ('chi', 1), ('bo', 1), ('li', 5), ('er', 2), ('bu', 4), ('shang', 1), ('shen', 1), ('ti', 3)]
# [('wo', 'ㄨㄛ', 3), ('shui', 'ㄕㄨㄟ', 4), ('zhao', 'ㄓㄠ', 2), ('le', 'ㄌㄜ', 5)]