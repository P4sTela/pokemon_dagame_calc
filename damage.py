import math
import csv
from pprint import pp, pprint

csv_file = open("./ポケモンデータシート.csv", "r", encoding="utf_8", errors="", newline="")
r = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
rlist = list(r)
# ['ぜんこくNo.', 'ガラルNo.', 'ヨロイ島No.', 'カンムリNo.', '名前', 'フォルム', '名前(フォルム)', '英語名', 'タイプ1', 'タイプ2', 'HP', '攻撃', '防御', '特攻', '特防', '素早さ', 'とくせい1', 'とくせい2', '夢特性']

csvmove_file = open("./技データリスト.csv", "r", encoding="utf_8", errors="", newline="")
m = csv.reader(csvmove_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
movelist = list(m)
# ['', '名前', 'タイプ', '分類', '威力', 'ダイマックス', '命中', 'PP', '直接', '守る', '対象', '説明']

def search(word):
    for i in rlist:
        if word == i[6]:
            result = True
            break
        else:
            result = False

    if result:
        return i
    else:
        return -1


def searchmove(word):
    for m in movelist:
        if word == m[1]:
            mresult = True
            break
        else:
            mresult = False

    if mresult:
        return m
    else:
        return -1


def typecal(type1, type2):
    table = {
        '':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':1.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':1.0,'フェアリー':1.0},
        'ノーマル':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':1.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':0.5,'ゴースト':0.0,'ドラゴン':1.0,'あく':1.0,'はがね':0.5,'フェアリー':1.0},
        'ほのお':{'':1.0,'ノーマル':1.0,'ほのお':0.5,'みず':0.5,'でんき':1.0,'くさ':2.0,'こおり':2.0,'かくとう':1.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':2.0,'いわ':0.5,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':2.0,'フェアリー':1.0},
        'みず':{'':1.0,'ノーマル':1.0,'ほのお':2.0,'みず':0.5,'でんき':1.0,'くさ':0.5,'こおり':1.0,'かくとう':1.0,'どく':1.0,'じめん':2.0,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':2.0,'ゴースト':1.0,'ドラゴン':0.5,'あく':1.0,'はがね':1.0,'フェアリー':1.0},
        'でんき':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':2.0,'でんき':0.5,'くさ':0.5,'こおり':1.0,'かくとう':1.0,'どく':1.0,'じめん':0.0,'ひこう':2.0,'エスパー':1.0,'むし':1.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':0.5,'あく':1.0,'はがね':1.0,'フェアリー':1.0},
        'くさ':{'':1.0,'ノーマル':1.0,'ほのお':0.5,'みず':2.0,'でんき':1.0,'くさ':0.5,'こおり':1.0,'かくとう':1.0,'どく':0.5,'じめん':2.0,'ひこう':0.5,'エスパー':1.0,'むし':0.5,'いわ':2.0,'ゴースト':1.0,'ドラゴン':0.5,'あく':1.0,'はがね':0.5,'フェアリー':1.0},
        'こおり':{'':1.0,'ノーマル':1.0,'ほのお':0.5,'みず':0.5,'でんき':1.0,'くさ':2.0,'こおり':0.5,'かくとう':1.0,'どく':1.0,'じめん':2.0,'ひこう':2.0,'エスパー':1.0,'むし':1.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':2.0,'あく':1.0,'はがね':0.5,'フェアリー':1.0},
        'かくとう':{'':1.0,'ノーマル':2.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':2.0,'かくとう':1.0,'どく':0.5,'じめん':1.0,'ひこう':0.5,'エスパー':0.5,'むし':0.5,'いわ':2.0,'ゴースト':0.0,'ドラゴン':1.0,'あく':2.0,'はがね':2.0,'フェアリー':0.5},
        'どく':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':2.0,'こおり':1.0,'かくとう':1.0,'どく':0.5,'じめん':0.5,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':0.5,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':0.0,'フェアリー':2.0},
        'じめん':{'':1.0,'ノーマル':1.0,'ほのお':2.0,'みず':1.0,'でんき':2.0,'くさ':0.5,'こおり':1.0,'かくとう':1.0,'どく':2.0,'じめん':1.0,'ひこう':0.0,'エスパー':1.0,'むし':0.5,'いわ':2.0,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':2.0,'フェアリー':1.0},
        'ひこう':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':0.5,'くさ':2.0,'こおり':1.0,'かくとう':2.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':2.0,'いわ':0.5,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':0.5,'フェアリー':1.0},
        'エスパー':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':2.0,'どく':2.0,'じめん':1.0,'ひこう':1.0,'エスパー':0.5,'むし':1.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':1.0,'あく':0.0,'はがね':0.5,'フェアリー':1.0},
        'むし':{'':1.0,'ノーマル':1.0,'ほのお':0.5,'みず':1.0,'でんき':1.0,'くさ':2.0,'こおり':1.0,'かくとう':0.5,'どく':0.5,'じめん':1.0,'ひこう':0.5,'エスパー':2.0,'むし':1.0,'いわ':1.0,'ゴースト':0.5,'ドラゴン':1.0,'あく':2.0,'はがね':0.5,'フェアリー':0.5},
        'いわ':{'':1.0,'ノーマル':1.0,'ほのお':2.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':2.0,'かくとう':0.5,'どく':1.0,'じめん':0.5,'ひこう':2.0,'エスパー':1.0,'むし':2.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':0.5,'フェアリー':1.0},
        'ゴースト':{'':1.0,'ノーマル':0.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':1.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':2.0,'むし':1.0,'いわ':1.0,'ゴースト':2.0,'ドラゴン':1.0,'あく':0.5,'はがね':1.0,'フェアリー':1.0},
        'ドラゴン':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':1.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':2.0,'あく':1.0,'はがね':0.5,'フェアリー':0.0},
        'あく':{'':1.0,'ノーマル':1.0,'ほのお':1.0,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':0.5,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':2.0,'むし':1.0,'いわ':1.0,'ゴースト':2.0,'ドラゴン':1.0,'あく':0.5,'はがね':1.0,'フェアリー':0.5},
        'はがね':{'':1.0,'ノーマル':1.0,'ほのお':0.5,'みず':0.5,'でんき':0.5,'くさ':1.0,'こおり':2.0,'かくとう':1.0,'どく':1.0,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':2.0,'ゴースト':1.0,'ドラゴン':1.0,'あく':1.0,'はがね':0.5,'フェアリー':2.0},
        'フェアリー':{'':1.0,'ノーマル':1.0,'ほのお':0.5,'みず':1.0,'でんき':1.0,'くさ':1.0,'こおり':1.0,'かくとう':2.0,'どく':0.5,'じめん':1.0,'ひこう':1.0,'エスパー':1.0,'むし':1.0,'いわ':1.0,'ゴースト':1.0,'ドラゴン':2.0,'あく':2.0,'はがね':0.5,'フェアリー':1.0}
        }
    return table[type1][type2]


def damagecal(poke1, move, poke2):
    st1 = search(poke1)
    mov = searchmove(move)
    st2 = search(poke2)

    # エラー時の例外処理
    if st1 == -1 or mov == -1 or st2 == -1:
        return -1
    
    T11 = st1[8]
    T12 = st1[9]
    HP1 = int(st1[10])
    A1 = int(st1[11])
    B1 = int(st1[12])
    C1 = int(st1[13])
    D1 = int(st1[14])

    MT = mov[2]
    MB = mov[3]
    MD = int(mov[4])

    T21 = st2[8]
    T22 = st2[9]
    HP2 = int(st2[10])
    A2 = int(st2[11])
    B2 = int(st2[12])
    C2 = int(st2[13])
    D2 = int(st2[14])

    if T11 == MT or T12 == MT:
        typex = 1.5
    else:
        typex = 1.0
    
    if MB == "物理":
        result1 = int(int(int(22 * MD * (A1 + 52) / (B2 + 20)) / 50 + 2) * typex * typecal(MT, T21) * typecal(MT, T22))
        result2 = int(int(int(22 * MD * (A1 + 52) / (B2 + 52)) / 50 + 2) * typex * typecal(MT, T21) * typecal(MT, T22))
    elif MB == "特殊":
        result1 = int(int(int(22 * MD * (C1 + 52) / (D2 + 20)) / 50 + 2) * typex * typecal(MT, T21) * typecal(MT, T22))
        result2 = int(int(int(22 * MD * (C1 + 52) / (D2 + 52)) / 50 + 2) * typex * typecal(MT, T21) * typecal(MT, T22))
    else:
        return "この技は変化技です"
    
    # none HP+75
    print(result1)
    print('{:.1%}'.format(math.floor(result1/(HP2+75) * 10 ** 3) / (10 ** 3)))

    # HP HP+107
    print(result1)
    print('{:.1%}'.format(math.floor(result1/(HP2+107) * 10 ** 3) / (10 ** 3)))

    # B or D HP+75
    print(result2)
    print('{:.1%}'.format(math.floor(result2/(HP2+75) * 10 ** 3) / (10 ** 3)))

    # HP and B or D HP+107
    print(result2)
    print('{:.1%}'.format(math.floor(result2/(HP2+107) * 10 ** 3) / (10 ** 3)))    


damagecal("カミツルギ", "リーフブレード", "ムゲンダイナ")
