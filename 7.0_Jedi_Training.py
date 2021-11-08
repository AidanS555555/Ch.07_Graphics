#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
SW=600
SH=400
arcade.open_window(600,400,"Ch.7 Jedi Training",True)
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()
arcade.draw_point(560,10,arcade.color.RED,5)
for y in range(0,SH,20):
    arcade.draw_line(0,y,SW,y,arcade.color.BLACK)
for x in range(0,SW,20):
    arcade.draw_line(x,0,x,SH,arcade.color.BLACK)
arcade.draw_circle_filled(300,200,40,arcade.color.WISTERIA)
arcade.draw_rectangle_filled(50,370,60,20,arcade.color.PHLOX)
arcade.draw_rectangle_filled(240,260,40,20,arcade.color.BLUSH,315)
arcade.draw_rectangle_filled(100,40,60,1,arcade.color.BLUE,315)
arcade.draw_ellipse_filled(100,100,120,40,arcade.color.AMBER)
arcade.draw_text("I love you. I know.",120,155,arcade.color.BRICK_RED,20,400,"center","Arial",True,False,"center")
arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW,30,330)
arcade.finish_render()
arcade.run()