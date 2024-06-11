import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    bg_ing2 = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.flip(kk_img, True, False)
    bg_ing2 = pg.transform.flip(bg_ing2, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_ing2, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])
        screen.blit(bg_ing2, [-x + 4800, 0])        
        kk_rect = kk_img.get_rect()#こうかとんRectの抽出
        kk_rect.center = 300, 200
        screen.blit(kk_img, kk_rect)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()