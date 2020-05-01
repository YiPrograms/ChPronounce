# Ch-Pronounce

A tool that uses [pkuseg](https://github.com/lancopku/pkuseg-python), a text segmentation tool,  and dictionaries to convert Chinese sentences to zhuyin (a.k.a bopomofo) or pinyin


## Usage

```python
from chpronounce import ChPronounce

chp = ChPronounce()

# To print out segmentation result from pkuseg, use:
# chp = ChPronounce(print_seg=True)

# Convert to both pinyin and zhuyin
print(chp.get_duyin("吃飽了沒？"))

# Convert to zhuyin
print(chp.get_zhuyin("吃飽了"))

# Convert to pinyin
print(chp.get_pinyin("我能吃玻璃而不傷身體"))


print(chp.get_duyin("我睡著了"))

# Output:
# [('chi', 'ㄔ', 1), ('bao', 'ㄅㄠ', 3), ('le', 'ㄌㄜ', 5), ('mei', 'ㄇㄟ', 2), ('？', '？', 0)]
# [('ㄔ', 1), ('ㄅㄠ', 3), ('ㄌㄜ', 5)]
# [('wo', 3), ('neng', 2), ('chi', 1), ('bo', 1), ('li', 5), ('er', 2), ('bu', 4), ('shang', 1), ('shen', 1), ('ti', 3)]
# [('wo', 'ㄨㄛ', 3), ('shui', 'ㄕㄨㄟ', 4), ('zhao', 'ㄓㄠ', 2), ('le', 'ㄌㄜ', 5)]
```

## Edit dictionary
```python
from chpronounce import ChPronounce
ChPronounce().inspect_dict()
```

```python
To access or modify dictionary, use 'dic'
To save, use save()
Python 3.7.7 (default, Apr 24 2020, 09:08:39) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> dic[1]["好"] # Check the word "好"
[(('hao', 'ㄏㄠ', 3), '形副助叹动'), (('hao', 'ㄏㄠ', 4), '动名')]
>>> dic[1]["好"] = [(('hao', 'ㄏㄠ', 3), '形副助叹动')] # Modify the word
>>> dic[2]["你好"] # Check a phrase
(['ni', 'hao'], ['ㄋㄧ', 'ㄏㄠ'], [3, 3])
>>> dic[3]["好棒棒"] = (['hao', 'bang', 'bang'], ['ㄏㄠ', 'ㄅㄤ', 'ㄅㄤ'], [3, 4, 4]) # Create a phrase
>>> save() # Write changes
```
> Press `Ctrl+D` to exit the shell

Dictionary structure:
```python
 dic
  ├── 1: (dict)
  │   ├── "數": [ (list)
  │   │          (('shu', 'ㄕㄨ', 4), '名形'),
  │   │          (('shu', 'ㄕㄨ', 3), '动副')
  │   │         ]
  │   ├── ...
  │   
  ├── 2: (dict)
  │   ├── "你好": (['ni', 'hao'], ['ㄋㄧ', 'ㄏㄠ'], [3, 3])
  │   ├── ...
  │   
  ├── 3: (dict)
  │   ├── "計算機": (['ji', 'suan', 'ji'], ['ㄐㄧ', 'ㄙㄨㄢ', 'ㄐㄧ'], [4, 4, 1])
  │   ├── ...
  │   
  ├── 4: ...
  ├── ...
  
dic = ["", { "X": [(...), (...)] }, { "XX": (...), "YY": (...) }]
```

## References

- Dictionary
    - [zdic.net](http://www.zdic.net)
    - [moedict.tw](https://www.moedict.tw)

- Text segmentation tool
    - [pkuseg](https://github.com/lancopku/pkuseg-python)

- Chinese Traditional to Simplified conversion
    - [OpenCC](https://github.com/yichen0831/opencc-python)
