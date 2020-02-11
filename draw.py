from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x0,y0,x1,y1 = int(x0),int(y0),int(x1),int(y1)

    if x0 == x1: #vertical line
        if y1 < y0:
            y0,y1 = y1, y0
        while y0 <= y1:
            plot(screen, color, x0, y0)
            y0 += 1
    elif y0 == y1: #horizonatal
        if x1 < x0:
            x0,x1 = x1,x0
        while x0 <= x1:
            plot(screen, color, x0, y0)
            x0 += 1
    else:
        if x1 < x0:
            x0, y0 , x1, y1 = x1, y1, x0, y0

        A = dXY(y0,y1)
        B = dXY(x1,x0) #dx
        m = dXY(y0,y1)/dXY(x0,x1)

        if (m >= 0 and m <= 1):
            d = 2 * A + B
            A,B = 2*A, 2*B
            while x0 <= x1:
                plot(screen, color, x0, y0)
                if d > 0:
                    y0 += 1
                    d += B
                x0 += 1
                d += A

        elif (m > 1):
            d = A + 2*B
            A,B = 2*A, 2*B
            while y0 <= y1:
                plot(screen, color, x0, y0)
                if d < 0:
                    x0 += 1
                    d += A
                y0 += 1
                d += B

        elif (m < -1):
            d = A - 2*B
            A,B = 2*A, 2*B
            while y0 >= y1:
                plot(screen, color, x0, y0)
                if d > 0:
                    x0 += 1
                    d += A
                y0 -= 1
                d -= B

        elif (m >= -1 and m < 0):
            d = 2*A + B
            A,B = 2*A, 2*B
            while x0 <= x1:
                plot(screen, color, x0, y0)
                if d < 0:
                    y0 -= 1
                    d -= B
                x0 += 1
                d += A


def dXY(p1, p2):
    return int(p2 - p1)
