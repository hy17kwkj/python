# http://vipprog.net/wiki/exercise.html

"""
シェルピンスキーのギャスケット †
フラクタル図形の一種
シェルピンスキーのギャスケット-wikipedia等を参考にし、これを描画する
プログラムを書いてください。
"""
from PIL import Image, ImageDraw
 
im = Image.new('RGB', (500, 500), (255, 255, 255))
draw = ImageDraw.Draw(im)
 
def sierpinski(trig):
    xy1 = trig[0]
    xy2 = trig[1]
    xy3 = trig[2]
    draw.polygon((xy1, xy2, xy3), fill=(0,0,0))
   sierpinski2(trig)
 
def sierpinski2(trig):
    #print(trig)
    xy1 = trig[0]
    xy2 = trig[1]
    xy3 = trig[2]
    xy12 = ((xy1[0] + xy2[0]) / 2, (xy1[1] + xy2[1]) / 2)
    xy23 = ((xy2[0] + xy3[0]) / 2, (xy2[1] + xy3[1]) / 2)
    xy31 = ((xy3[0] + xy1[0]) / 2, (xy3[1] + xy1[1]) / 2)
    dx = xy1[0] - xy12[0]
    dy = xy1[1] - xy12[1]
    if dx * dx + dy * dy < 5:
        return
    draw.polygon((xy12, xy23, xy31), fill=(255,255,255))
    sierpinski2((xy1, xy12, xy31))
    sierpinski2((xy12, xy2, xy23))
    sierpinski2((xy31, xy23, xy3))
 
sierpinski(((250,0), (0,500), (500,500)))
im.show()
