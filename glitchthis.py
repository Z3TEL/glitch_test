from PIL import Image
from glitch_this import ImageGlitcher
import random


# For GIFs

img = Image.open(r'/home/hello/Desktop/tests/glitch_this/media/video_cat.gif')
glitcher = ImageGlitcher()
glitch_img, src_gif_duration, src_gif_frames = glitcher.glitch_gif(img, 2, color_offset=True)


DURATION = 200
LOOP = 0



glitch_img[0].save(
    
    r'/home/hello/Desktop/tests/glitch_this/output/glitched_obj.gif',
    
    format = 'GIF',
    
    append_images=glitch_img[1:],

    save_all = True,
    
    duration = DURATION,

    loop = LOOP
    )









# For images

glitcher = ImageGlitcher()

random.seed(random.randint(1,20000000))

x = random.random()

img = Image.open(r'/home/hello/Desktop/tests/glitch_this/media/ugly.jpg')

glitch_img = glitcher.glitch_image(img, 5, color_offset=True, seed=x)

glitch_img.save(r'/home/hello/Desktop/tests/glitch_this/output/glitched_obj2.jpg',)