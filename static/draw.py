from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap

base = Image.open('output.png')
text = 'Di tengah-tengah kesenjangan waktunya, seorang sysadmin menemukan sebuah log trace pada server miliknya. Di sana, ia mengetahui bahwa terdapat upaya pengaksesan dan eksploitasi sebuah web AnimeList pada sebuah private tunnel antara 2 buah region yang berbeda.'
draw = ImageDraw.Draw(base)
font = ImageFont.truetype('Lato-Regular.ttf',20)

tt = wrap(text,70)
font2 = ImageFont.truetype('Raleway-Regular.ttf',35)
font3 = ImageFont.truetype('Raleway-Regular.ttf',35)
draw.text((275,130),'MyAnimeList', (0,0,0), font=font2)
draw.text((350,180),'250', (0,0,0), font=font3)

for i,j in enumerate(tt[:]):
	draw.text((50, 250 + 30*i), j,(0,0,0),font=font)
base.show()
# draw.text((0, 0),"Sample Text",(255,255,255),font=font)
