'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red:#BF0A30 and blue:#002868
Title the window, "The Stars and Stripes"
I used a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
'''
SW=494
BH=140
import arcade
arcade.open_window(494,260,"The Stars and Stripes",True)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
arcade.draw_rectangle_filled(99,190,198,140,(00,40,104))
arcade.draw_rectangle_filled(247,10,SW,20,(191,10,48))
arcade.draw_rectangle_filled(247,50,SW,20,(191,10,48))
arcade.draw_rectangle_filled(247,90,SW,20,(191,10,48))
arcade.draw_rectangle_filled(347.5,130,300,20,(191,10,48))
arcade.draw_rectangle_filled(347.5,170,300,20,(191,10,48))
arcade.draw_rectangle_filled(347.5,210,300,20,(191,10,48))
arcade.draw_rectangle_filled(347.5,250,300,20,(191,10,48))
for y in range(120,250,25):
    arcade.draw_text("*", 10, y, arcade.color.WHITE, 20)
for b in range(130,237,27):
    arcade.draw_text("*",31,b,arcade.color.WHITE,20)
for r in range(120,250,25):
    arcade.draw_text("*", 52, r, arcade.color.WHITE, 20)
for w in range(130,237,27):
    arcade.draw_text("*",73,w,arcade.color.WHITE,20)
for t in range(120,250,25):
    arcade.draw_text("*", 94, t, arcade.color.WHITE, 20)
for u in range(130,237,27):
    arcade.draw_text("*",115,u,arcade.color.WHITE,20)
for o in range(120,250,25):
    arcade.draw_text("*", 136, o, arcade.color.WHITE, 20)
for h in range(130,237,27):
    arcade.draw_text("*",157,h,arcade.color.WHITE,20)
for f in range(120,250,25):
    arcade.draw_text("*",178 , f, arcade.color.WHITE, 20)




arcade.finish_render()
arcade.run()