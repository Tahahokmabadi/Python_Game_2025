import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Pong Game!"


class PongGame(arcade.Window):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.HUNTER_GREEN)
        self.ball_x = 400
        self.ball_y = 200

# arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    def on_draw(self):
        # arcade.start_render()


        # arcade.draw_rectangle_filled()
        # arcade.draw_lbwh_rectangle_filled()
        # arcade.draw_lrbt_rectangle_filled()

        

        self.clear()
        # self.ball.draw()
        # self.paddle_left.draw()
        # self.paddle_right.draw()
        # arcade.clear()
        
        arcade.draw_line(SCREEN_WIDTH / 2, 0, SCREEN_WIDTH / 2, SCREEN_HEIGHT, arcade.color.WHITE)
        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.CYBER_YELLOW, 0. -1)
    # def make_objects(self):
    #     self.ball = arcade.Sprite("Assignment_1 (Pong Game)/ball_sprite.png", 1)
    #     self.ball.center_x = SCREEN_WIDTH / 2
    #     self.ball.center_y = SCREEN_HEIGHT / 2

    #     self.paddle_left = arcade.SpriteSolidColor(10, 60, arcade.color.BLUE_YONDER)
    #     self.paddle_left.center_x = 25
    #     self.paddle_left.center_y = SCREEN_HEIGHT / 2

    #     self.paddle_right = arcade.SpriteSolidColor(10, 60, arcade.color.CRIMSON_GLORY)
    #     self.paddle_right.center_x = SCREEN_WIDTH - 25
    #     self.paddle_right.center_y = SCREEN_HEIGHT / 2
# arcade.draw_lrbt_rectangle_filled(40, 60, 165, 245, arcade.color.BLUE_YONDER)
    
    def on_update(self, delta_time):
        self.ball_x += 5
if __name__ == "__main__":
    pong = PongGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # pong.make_objects()
    arcade.run()

