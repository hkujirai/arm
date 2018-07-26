# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import math

# 順運動学の計算
#def fk(L, th):
class Arm1:
    def msgs(self, l1,l2,th1,th2):
        self.l1 = l1
        self.l2 = l2
        self.th1 = th1
        self.th2 = th2
        self.th3 = np.radians(self.th1)
        self.th4 = np.radians(self.th2)
        self.x1 = self.l1 * math.cos(self.th3)
        self.y1 = self.l1 * math.sin(self.th3)
        self.x2 = self.x1 + self.l2 * math.cos(self.th3 + self.th4)
        self.y2 = self.y1 + self.l2 * math.sin(self.th3 + self.th4)
        print ("check_python")
#        print (self.l1)
#        print (self.l2)
#        print (self.th1)
#        print (self.th2)
#        print (float(self.x1))
#        print (float(self.y1))
#        print (self.x2)
#        print (self.y2)
#        print (self.th3)
#        print (self.th4)
                        
    
def plot(x, y):
    fn = "Times New Roman"
    # グラフ表示の設定
    fig = plt.figure()
    ax = fig.add_subplot(111, axisbg="w")
    ax.tick_params(labelsize=13)          # 軸のフォントサイズ
    plt.xlabel("$x [m]$", fontsize=20, fontname=fn)
    plt.ylabel("$y [m]$", fontsize=20, fontname=fn)
    plt.plot(x, y,"-g",lw=5,label="link")           # リンクの描画
    plt.plot(x, y,"or",lw=5, ms=10,label="joint")   # 関節の描画
    plt.xlim(-3.0,3.0)
    plt.ylim(-3.0,3.0)
    plt.grid()
    plt.legend(fontsize=20) # 凡例
    plt.show()



def main():
    test1 = Arm1()
    test1.msgs(1.4 ,1.4 ,45 ,-30)

    a1=test1.x1
    a2=test1.x2
    b1=test1.y1
    b2=test1.y2
    x = (0, a1, a2)
    y = (0, b1, b2)

    plot(x, y)


if __name__ == '__main__':
    main()        
