'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''

import arcade
arcade.open_window(600,600,"In Darkest Knight",True)
arcade.set_background_color(arcade.color.GO_GREEN)
arcade.start_render()
arcade.draw_rectangle_filled(150,300,300,100,arcade.color.BLACK,45)
arcade.draw_rectangle_filled(450,300,300,100,arcade.color.BLACK,315)
arcade.draw_rectangle_filled(300,175,135,135,arcade.color.BLACK,45)
arcade.draw_circle_filled(30,320,50,arcade.color.GO_GREEN)
arcade.draw_circle_filled(570,320,50,arcade.color.GO_GREEN)
arcade.draw_circle_filled(70,242,75,arcade.color.GO_GREEN)
arcade.draw_circle_filled(530,242,75,arcade.color.GO_GREEN)
arcade.draw_circle_filled(145,190,50,arcade.color.GO_GREEN)
arcade.draw_circle_filled(455,190,50,arcade.color.GO_GREEN)
arcade.draw_arc_filled(50,400,125,100,arcade.color.BLACK,0,180,45)
arcade.draw_arc_filled(550,400,125,100,arcade.color.BLACK,0,180,315)
arcade.draw_triangle_filled(100,375,300,425,300,200,arcade.color.BLACK)
arcade.draw_triangle_filled(500,375,300,425,300,200,arcade.color.BLACK)
arcade.draw_triangle_filled(250,550,250,300,150,350,arcade.color.BLACK)
arcade.draw_triangle_filled(350,550,350,300,450,350,arcade.color.BLACK)
arcade.draw_circle_filled(300,200,100,arcade.color.BOTTLE_GREEN)
arcade.draw_circle_filled(300,200,50,arcade.color.BLACK)
arcade.draw_rectangle_filled(300,300,200,60,arcade.color.BOTTLE_GREEN)
arcade.draw_rectangle_filled(300,100,200,60,arcade.color.BOTTLE_GREEN)




arcade.finish_render()
arcade.run()




