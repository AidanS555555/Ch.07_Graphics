import arcade
SW=600
SH=400
arcade.open_window(600,400,"Kyle Rayner",True)
arcade.set_background_color((51,123,73))
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(200,400,300,200,arcade.color.BLOND)
arcade.draw_rectangle_filled(300,200,50,50,arcade.color.ANDROID_GREEN,45)
arcade.draw_point(300,300,(0,0,0),5)
arcade.draw_line(20,30,100,200,arcade.color.BRUNSWICK_GREEN,3)
arcade.draw_circle_filled(400,100,20,arcade.color.WHITE)
arcade.draw_text("ALEX NOOOOO",300,200,arcade.color.EERIE_BLACK,20,400,"center","Papyrus",True,False,"center")
for x in range(0,SW,20):
    arcade.draw_rectangle_filled(x,20,10,30,arcade.color.CARIBBEAN_GREEN)
arcade.draw_rectangle_filled(300,25,SW,5,arcade.color.WHITE)
arcade.draw_rectangle_filled(300,10,SW,5,arcade.color.WHITE)
radius=50
arcade.finish_render()
arcade.run()