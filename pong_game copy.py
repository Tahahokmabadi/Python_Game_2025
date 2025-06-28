import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Pong Game!"

class PongGame(arcade.Window):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.OUTER_SPACE)

# arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    def on_draw(self):
        # arcade.start_render()
        self.clear()

        arcade.draw_line(100, 100, 300, 400, arcade.color.RED, 100)

    def on_update(self, delta_time):
            pass

if __name__ == "__main__":
    pong = PongGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.run()

