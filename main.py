from display import *
from draw import *

s = new_screen()
#outline
r = 240
g = 1
b = 1
c = [r , g , b]
for i in range (15):
    c = [r , g , b]
    g += 15
    b += 15
    draw_line(XRES / 2 + i, 100 + i, XRES/2 + i, YRES/2 + i , s, c)
    draw_line(XRES / 2 + i, 100 + i, XRES / 2 + 125 + i, 150 + i ,  s, c)
    draw_line(XRES/2 + i , YRES/2 + i , XRES/2 + 125 + i , YRES/2 + 50 +i  , s, c)
    draw_line(XRES / 2 + 125 + i , 150 + i , XRES/2 + 125 + i , YRES/2 + 50 + i, s, c)
    draw_line(XRES / 2 + i , 100 + i , XRES / 2 - 125 + i , 150 + i, s, c)
    draw_line(XRES/2 - 125 + i , YRES/2 + 50 + i, XRES / 2 - 125 + i, 150 + i, s, c )
    draw_line(XRES/2 - 125 + i, YRES/2 + 50 + i, XRES/2 +i , YRES/2 + i , s, c )
    draw_line(XRES/2 + 125 + i , YRES/2 + 50 + i, XRES/2 + i  , YRES/2 + 100 + i, s, c)
    draw_line(XRES/2 + i, YRES/2 + 100 + i , XRES / 2 - 125 + i , YRES/2 + 50 +i , s, c)






display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
