#クラスの定義
class CharaTest:
    def __init__(self):
        self.name = "俺"
    def fight(self):
        print("戦うぞ！")

#クラスの使用
chara1 = CharaTest()
print(chara1.name)
chara1.fight()