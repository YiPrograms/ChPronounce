import pkuseg
import os
import pickle


class ChPronounce:

    def __init__(self, print_seg=False):
        self.seg = pkuseg.pkuseg(postag=True)
        self.print_seg = print_seg

        with open(os.path.join(os.path.dirname(__file__), "xdic.pkl"), "rb") as f:
            self.dic = pickle.load(f)
        with open(os.path.join(os.path.dirname(__file__), "postag"), "r") as f:
            self.postag = dict((k.split(" ")[0], k.split(" ")[2]) for k in f.read().splitlines())
        with open(os.path.join(os.path.dirname(__file__), "t2s"), "r") as f:
            self.t2s = dict((k.split("\t")[0], k.split("\t")[1]) for k in f.read().splitlines())

    def _append_phrase(self, ph, res):
        pys, zys, tones = self.dic[len(ph)][ph]
        for i in range(len(pys)):
            res.append((pys[i], zys[i], tones[i]))
    
    def _append_word(self, word, pos, res):
        if word in self.dic[1]:
            for dy, poses in self.dic[1][word]:
                if pos in poses:
                    res.append(dy)
                    break
            else:
                res.append(self.dic[1][word][0][0])
    
    def _break_down(self, sub, pos, res):
        if len(sub) == 0:
            return
        for c in sub:
            self._append_word(c, pos, res)


    def get_duyin(self, sentence):
        for i in range(len(sentence)):
            if sentence[i] in self.t2s:
                sentence = sentence[:i] + self.t2s[sentence[i]] + sentence[i+1:]

        sen = self.seg.cut(sentence)
        if self.print_seg:
            print(sen)
        res = []
        for word, pos in sen:
            pos = self.postag[pos]
            if pos == "X":
                res.append((word, word, 0))
                continue
            if len(word) == 1:
                self._append_word(word, pos, res)
            else:
                if word in self.dic[len(word)]:
                    self._append_phrase(word, res)
                else:
                    sub = ""
                    for c in word:
                        if c not in self.dic[1]:
                            self._break_down(sub, pos, res)
                            sub = ""
                        sub += c
                        if len(sub) > 1 and sub in self.dic[len(sub)]:
                            self._append_phrase(sub, res)
                            sub = ""
                    self._break_down(sub, pos, res)
        return res

    def get_zhuyin(self, sentence):
        dy = self.get_duyin(sentence)
        res = []
        for _, zy, tone in dy:
            res.append((zy, tone))
        return res

    def get_pinyin(self, sentence):
        dy = self.get_duyin(sentence)
        res = []
        for py, _, tone in dy:
            res.append((py, tone))
        return res

    def inspect_dict(self):
        print("To access or modify dictionary, use 'dic'")
        print("To save, use save()")

        dic = self.dic
        def save():
            with open(os.path.join(os.path.dirname(__file__), "xdic.pkl"), "wb") as f:
                pickle.dump(dic, f, pickle.HIGHEST_PROTOCOL)

        import code
        code.interact(local=locals())


