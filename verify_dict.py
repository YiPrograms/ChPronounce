import logging
import os
import pickle

from chpronounce import ChPronounce

CHEWINGS = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒ	ㄓㄔㄕㄖㄗㄘㄙㄧㄨㄩㄚㄛㄜㄝ	ㄞㄟㄠㄡㄢㄣㄤㄥㄦ'
IGNORE_LIST = "({[(IslamicStateofAfghanistan "


def main():
    replace_table = {
        b'\xc3\xbc'.decode("utf8"): 'u'
    }
    with open("replace_table.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            a, b, tone = line.split(" ")
            replace_table[a] = b  # replace a with b

    chp = ChPronounce()
    dic = chp.dic
    to_pop = []

    if "呣" in dic[1]:
        dic[1].pop("呣")
    py_err = set()
    n_diff = 0
    for word_len, val in dic.items():
        ignore_flag = False
        for word, lis in val.items():
            for ignore_test in IGNORE_LIST:
                if ignore_test in word:
                    # logging.warning(f"ignore {word} ({ignore_test})")
                    ignore_flag = True
                    break
            if ignore_flag:
                continue

            if not isinstance(lis, list):
                lis = [lis]
            for iol, l in enumerate(lis):
                if len(l) == 2:
                    (pys, cys, tones), pos = l
                elif len(l) == 3:
                    pys, cys, tones = l
                    pos = ""
                else:
                    print(l)
                    raise
                if not isinstance(pys, list):
                    pys = [pys]
                if not isinstance(cys, list):
                    cys = [cys]
                if not isinstance(tones, list):
                    tones = [tones]

                pys = [x.replace("(讀音)", "") for x in pys]
                cys = [x.replace("(讀音)", "") for x in cys]
                cys = [x.replace("ˇ", "") for x in cys]

                for i, py in enumerate(pys):
                    for p_chr in py:
                        if p_chr in CHEWINGS:
                            pys[i], cys[i] = cys[i], pys[i]
                            break

                for i, py in enumerate(pys):
                    for p_chr in py:
                        if not (ord('a') <= ord(p_chr) <= ord('z')):
                            if p_chr in replace_table:
                                py = py.replace(p_chr, replace_table[p_chr])
                                pys[i] = py
                            else:
                                py_err.add(p_chr.encode("utf8"))
                                print("w |", "\t ".join(map(str, word)))
                                print("p |", "\t ".join(map(str, pys)))
                                print("c |", "\t ".join(map(str, cys)))
                                print("t |", "\t ".join(map(str, tones)))
                                print("+++++++++++++++-----------------------------")

                if len(cys) != word_len or len(tones) != word_len:
                    to_pop.append((word_len, word, iol))
                    logging.warning(f"{word}[{iol}] is invalid.")
                    continue

                for i, x in enumerate(cys):
                    xx = x
                    x = [y for y in x if y in CHEWINGS]
                    x = "".join(x)
                    if xx != x:

                        logging.warning(f"[{word}] {xx} ---> {x}")
                    cys[i] = x

                ori = dic[word_len][word]
                if word_len == 1:
                    pys, cys, tones = pys[0], cys[0], tones[0]
                if isinstance(dic[word_len][word], list):
                    dic[word_len][word][iol] = ((pys, cys, tones), pos) if pos != '' else (pys, cys, tones)
                else:
                    dic[word_len][word] = ((pys, cys, tones), pos) if pos != '' else (pys, cys, tones)

                if ori != dic[word_len][word]:
                    n_diff += 1
                    # print(ori)
                    # print(dic[word_len][word])
                    # print()
                # input()

    for word_len, word, iol in to_pop:
        dic[word_len].pop(word)

    # summary
    total = 0
    for word_len, val in dic.items():
        count = len(val)
        print(f"\t{word_len}\t字詞：{count}\t個")
        total += count
    print(f"總計：{total}個詞。")
    print(f"removed {len(to_pop)} words. modified {n_diff} words.")
    with open(os.path.join(os.path.dirname(__file__), "chpronounce/xdic.pkl"), "wb") as f:
        pickle.dump(dic, f, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    main()
