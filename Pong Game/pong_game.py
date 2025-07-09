import arcade
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Pong Game!"


class PongGame(arcade.Window):
    def __init__(self, WIDTH, HEIGHT, TITLE):
        super().__init__(WIDTH, HEIGHT, TITLE)
        arcade.set_background_color(arcade.color.CHARLESTON_GREEN)
        self.time_ali = True
        self.HEIGHT = HEIGHT

        self.ball_x = WIDTH // 2
        self.ball_y = HEIGHT // 2
        self.ball_speed_x = random.choice([-6, 6])
        self.ball_speed_y = random.randint(2, 4) * random.choice([-1, 1])

        self.paddle_1_y = HEIGHT // 2
        self.paddle_2_y = HEIGHT // 2

        self.w_pressed_paddle_1 = False
        self.s_pressed_paddle_1 = False
        self.up_pressed_paddle_2 = False
        self.down_pressed_paddle_2 = False

        # self.paddle_1_y_bottom = SCREEN_HEIGHT // 2 + SCREEN_HEIGHT * 0.1
        # self.paddle_1_y_top = SCREEN_HEIGHT // 2 + SCREEN_HEIGHT * 0.1
        
        # self.paddle_2_y_bottom = SCREEN_HEIGHT // 2 + SCREEN_HEIGHT * 0.1
        # self.paddle_2_y_top = SCREEN_HEIGHT // 2 + SCREEN_HEIGHT * 0.1
        
        # self.paddles_x_left = SCREEN_WIDTH // 20 - SCREEN_WIDTH // 160
        # self.paddles_x_right = SCREEN_WIDTH // 20 + SCREEN_WIDTH // 160
        
        self.paddle_1_score = 0
        self.paddle_2_score = 0

        self.text_score_display = f"Score: "

        # self.text_paddle_1_scores = f"0"
        # self.text_paddle_2_scores = f"0"

        self.paddle_speed = 4
        
        self.winning_score = 20
        self.game_over = False

        self.winner = ""
        
    def on_draw(self):
        # arcade.start_render()
        self.clear()

        if self.game_over:
            # arcade.draw_text("GAME OVER!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.RED, 54, anchor_x = "center", anchor_y = "center")
            if self.winner == "1":
                arcade.draw_text(f"PLAYER {self.winner} WINS!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.SILVER_LAKE_BLUE, 54, font_name = "Comic Sans MS", anchor_x = "center", anchor_y = "center")
                return
            elif self.winner == "2":
                arcade.draw_text(f"PLAYER {self.winner} WINS!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.CRIMSON_GLORY, 54, font_name = "Comic Sans MS", anchor_x = "center", anchor_y = "center")
                return
        # Display of scores
        arcade.draw_text(self.text_score_display + str(self.paddle_1_score), SCREEN_WIDTH // 4, SCREEN_HEIGHT - SCREEN_HEIGHT // 8, arcade.color.DUTCH_WHITE, 24, font_name = "Kenney Mini", anchor_x= "center", bold = True)
        arcade.draw_text(self.text_score_display + str(self.paddle_2_score), SCREEN_WIDTH - SCREEN_WIDTH // 4, SCREEN_HEIGHT - SCREEN_HEIGHT // 8, arcade.color.DUTCH_WHITE, 24, font_name = "Kenney Mini", anchor_x= "center", bold = True)
        
        # # Score +1
        # arcade.draw_text(self.text_paddle_1_scores, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.SILVER_LAKE_BLUE, 48, font_name = "Kenney Mini", anchor_x= "center", bold = True)
        # arcade.draw_text(self.text_paddle_2_scores, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.CRIMSON_GLORY, 48, font_name = "Kenney Mini", anchor_x= "center", bold = True)

        paddle_1_x_left = SCREEN_WIDTH // 20 - SCREEN_WIDTH // 160
        paddle_1_x_right = SCREEN_WIDTH // 20 + SCREEN_WIDTH // 160
        arcade.draw_lrbt_rectangle_filled(
            paddle_1_x_left,
            paddle_1_x_right,
            self.paddle_1_y - 70 // 2,
            self.paddle_1_y + 70 // 2,
            arcade.color.SILVER_LAKE_BLUE)
        
        paddle_2_x_left = SCREEN_WIDTH - (SCREEN_WIDTH // 20 + SCREEN_WIDTH // 160)
        paddle_2_x_right = SCREEN_WIDTH - (SCREEN_WIDTH // 20 - SCREEN_WIDTH // 160)
        arcade.draw_lrbt_rectangle_filled(
            paddle_2_x_left,
            paddle_2_x_right,
            self.paddle_2_y - 70 // 2,
            self.paddle_2_y + 70 // 2,
            arcade.color.CRIMSON_GLORY)
        
        # Paddle 2
        # paddle_2_x_left = SCREEN_WIDTH - (SCREEN_WIDTH // 20 + SCREEN_WIDTH // 160)
        # paddle_2_x_right = SCREEN_WIDTH - (SCREEN_WIDTH // 20 - SCREEN_WIDTH // 160)
        # arcade.draw_lrbt_rectangle_filled(
        #     paddle_2_x_left,
        #     paddle_2_x_right,
        #     self.paddle_2_y_bottom,
        #     self.paddle_2_y_top,
        #     arcade.color.CRIMSON_GLORY)

        # # Paddle 2
        # arcade.draw_lrbt_rectangle_filled(
        #     SCREEN_WIDTH - self.paddles_x_right,
        #     SCREEN_WIDTH - self.paddles_x_left,
        #     self.paddle_1_y_bottom,
        #     self.paddle_1_y_top,
        #     arcade.color.CRIMSON_GLORY)

        arcade.draw_line(SCREEN_WIDTH / 2, 0, SCREEN_WIDTH / 2, SCREEN_HEIGHT, arcade.color.WHITE)

        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.CYBER_YELLOW, 0. -1)

    def on_update(self, delta_time):
        if self.time_ali is True:
            time.sleep(10)
            self.time_ali = False
        # self.ball_x += 5

        if self.paddle_1_score >= self.winning_score:
            self.winner = "1"
            # time.sleep(0.5)            
            self.game_over = True
            if self.game_over:
                return

        elif self.paddle_2_score >= self.winning_score:
            self.winner = "2"
            # time.sleep(0.5)            
            self.game_over = True
            if self.game_over:
                return


        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y

        ball_left = self.ball_x - 15
        ball_right = self.ball_x + 15
        ball_top = self.ball_y + 15
        ball_bottom = self.ball_y - 15

        if self.ball_y - 15 <= 0 or self.ball_y + 15 >= SCREEN_HEIGHT:
            self.ball_speed_y *= -1
        
        if self.ball_x - 15 <= 0:
            self.ball_x = SCREEN_WIDTH // 2
            self.ball_y = SCREEN_HEIGHT // 2
            self.ball_speed_x = random.choice([-8, 8])
            self.ball_speed_y = random.randint(1, 4) * random.choice([-1, 1])
            
            # Recenter Paddles
            self.paddle_1_y = self.HEIGHT // 2
            self.paddle_2_y = self.HEIGHT // 2

            self.paddle_2_score += 1
            # self.text_paddle_1_scores = f"SCORE +1 => {self.paddle_1_score}"
            # self.on_draw()
            time.sleep(0.5)

            # if self.paddle_1_score >= self.winning_score:
            #     self.winner = "1"
            #     time.sleep(1.5)
            #     self.game_over = True

            #     if self.game_over:
            #         return

            # self.text_paddle_1_scores = " "

        elif self.ball_x + 15 >= SCREEN_WIDTH:
            self.ball_x = SCREEN_WIDTH // 2
            self.ball_y = SCREEN_HEIGHT // 2
            self.ball_speed_x = random.choice([-8, 8])
            self.ball_speed_y = random.randint(1, 4) * random.choice([-1, 1])
            
            # Recenter Paddles
            self.paddle_1_y = self.HEIGHT // 2
            self.paddle_2_y = self.HEIGHT // 2

            self.paddle_1_score += 1
            # self.text_paddle_2_scores = f"SCORE +1 => {self.paddle_2_score}"
            # self.on_draw()
            time.sleep(0.5)

            # if self.paddle_2_score >= self.winning_score:
            #     self.winner = "2"
            #     time.sleep(1.5)            
            #     self.game_over = True

            #     if self.game_over:
            #         return
            
            # self.text_paddle_2_scores = " "

        if self.w_pressed_paddle_1 is True:
            self.paddle_1_y += self.paddle_speed
        if self.s_pressed_paddle_1 is True:
            self.paddle_1_y -= self.paddle_speed
        if self.up_pressed_paddle_2 is True:
            self.paddle_2_y += self.paddle_speed
        if self.down_pressed_paddle_2 is True:
            self.paddle_2_y -= self.paddle_speed


        paddle_1_x_left = SCREEN_WIDTH // 20 - SCREEN_WIDTH // 160
        paddle_1_x_right = SCREEN_WIDTH // 20 + SCREEN_WIDTH // 160
        paddle_1_top = self.paddle_1_y + 35
        paddle_1_bottom = self.paddle_1_y - 35

        paddle_2_x_left = SCREEN_WIDTH - (SCREEN_WIDTH // 20 + SCREEN_WIDTH // 160)
        paddle_2_x_right = SCREEN_WIDTH - (SCREEN_WIDTH // 20 - SCREEN_WIDTH // 160)
        paddle_2_top = self.paddle_2_y + 35
        paddle_2_bottom = self.paddle_2_y - 35
        

        if (ball_right >= paddle_1_x_left and ball_left <= paddle_1_x_right and
            ball_top >= paddle_1_bottom and ball_bottom <= paddle_1_top):
            self.ball_x = paddle_1_x_right + 15
            self.ball_speed_x *= -1
        
        if (ball_right >= paddle_2_x_left and ball_left <= paddle_2_x_right and
            ball_top >= paddle_2_bottom and ball_bottom <= paddle_2_top):
            self.ball_x = paddle_2_x_left - 15
            self.ball_speed_x *= -1

        # Paddle 1
        # self.paddle_1_y_bottom = SCREEN_HEIGHT // 2 + SCREEN_HEIGHT * 0.1
        # self.paddle_1_y_top = SCREEN_HEIGHT // 2 + SCREEN_HEIGHT * 0.1
        
        # # Paddle 2
        # self.paddle_2_y_bottom = SCREEN_HEIGHT // 2 + SCREEN_HEIGHT * 0.1
        # self.paddle_2_y_top = SCREEN_HEIGHT // 2 + SCREEN_HEIGHT * 0.1
        # self.paddles_x_left = SCREEN_WIDTH // 20 - SCREEN_WIDTH // 160
        # self.paddles_x_right = SCREEN_WIDTH // 20 + SCREEN_WIDTH // 160
       
        if self.paddle_1_y < 35:
            self.paddle_1_y = 35
        elif self.paddle_1_y > SCREEN_HEIGHT - 35:
            self.paddle_1_y = SCREEN_HEIGHT - 35

        if self.paddle_2_y < 35:
            self.paddle_2_y = 35
        elif self.paddle_2_y > SCREEN_HEIGHT - 35:
            self.paddle_2_y = SCREEN_HEIGHT - 35


    def on_key_press(self, key, modifiers):
        if key == arcade.key.W:
            self.w_pressed_paddle_1 = True
        elif key == arcade.key.S:
            self.s_pressed_paddle_1 = True
        elif key == arcade.key.UP:
            self.up_pressed_paddle_2 = True
        elif key == arcade.key.DOWN:
            self.down_pressed_paddle_2 = True

        # if key == arcade.key.UP:
        #     self.paddle_2_y += 5
        # elif key == arcade.key.DOWN:
        #     self.paddle_2_y -= 5
        # elif key == arcade.key.W:
        #     self.paddle_1_y += 5
        # elif key == arcade.key.S:
        #     self.paddle_1_y -= 5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.w_pressed_paddle_1 = False
        elif key == arcade.key.S:
            self.s_pressed_paddle_1 = False
        elif key == arcade.key.UP:
            self.up_pressed_paddle_2 = False
        elif key == arcade.key.DOWN:
            self.down_pressed_paddle_2 = False

if __name__ == "__main__":
    pong = PongGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
