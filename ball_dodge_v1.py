from livewires import games, color
import random

games.init(screen_width = 640, screen_height = 480, fps = 60)

class Ball(games.Sprite):
    
    size_of_ball = ["/icns/ball1.bmp", "/icns/ball2.bmp", "/icns/ball3.bmp", "/icns/ball4.bmp", "/icns/ball5.bmp", "/icns/ball6.bmp"]

    def __init__(self):
        file_name = random.choice(Ball.size_of_ball)
        image = games.load_image(file_name)

        super(Ball, self).__init__(image = image, x = random.randrange(0, games.screen.width), y = 0, dy = random.randrange(1, 7))

    def update(self):
        """ Check if bottom edge has reached screen bottom. """
        if self.bottom > games.screen.height:
            self.destroy()
        super(Ball, self).update()


class Ball_Launcher:
    """Methods for repeating a single ball launch"""
    def __init__(self):
        self.time_till_drop = 0
        self.speed = 30
 
    def update(self):
        """Launches another ball"""
        if self.time_till_drop == 0:
            games.screen.add(Ball())
            self.time_till_drop = random.randrange(self.speed)
        else:
            self.time_till_drop -= 1

class Player_Character(games.Sprite):
    """Loads User-controlled player character"""
    x_coord = 25
    run_speed = 2
    
    def __init__(self):
        image = games.load_image("/icns/stickman.bmp")
        super(Player_Character, self).__init__(image = image, x = Player_Character.x_coord, bottom = games.screen.height)
        self.ball_launcher = Ball_Launcher()
        self.lives = 3
        
        self.num_lives = games.Text(value = self.lives, size = 25, color = color.red,
                                    top = 5, right = games.screen.width - 10)
        self.msg = games.Text(value = "Lives: ", size = 25, color = color.black,
                                    top = 6, right = games.screen.width - 20)

        games.screen.add(self.num_lives)
        games.screen.add(self.msg)



    def update(self):
        self.ball_launcher.update()
        
        """ Moves character according to L & R arrow keys"""

        if games.keyboard.is_pressed(games.K_LEFT):
            self.x -= Player_Character.run_speed
            if self.left < 0:
                self.left = 0

        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x += Player_Character.run_speed
            if self.right > games.screen.width:
                self.right = games.screen.width
    
        for ball in self.overlapping_sprites:
            ball.destroy()
            self.num_lives.value -= 1
            if self.num_lives.value == 0:
                self.destroy()
                end()
                _quit()

def end():

    end_message = games.Message(value = "Game Over",
                                size = 90,
                                color = color.red,
                                x = games.screen.width/2,
                                y = games.screen.height/2,
                                lifetime = 5000 * games.screen.fps,
                                is_collideable = False)
    games.screen.add(end_message)

def _quit():

    games.screen.quit()

def add_Objects():

    background_image = games.load_image("/icns/background.jpg", transparent = False)

    games.screen.add(Player_Character())
    

def main():

    background_image = games.load_image("/icns/background.jpg", transparent = False)
    games.screen.background = background_image

    time_to_read_msg = 5 * games.screen.fps
    x_location_of_start_msg = 300
    y_location_of_start_msg = 50
    size_of_msg = 35

    line_one = games.Message(value = "Reign of Terror v1",
                             size = size_of_msg,
                             color = color.red,
                             x = x_location_of_start_msg,
                             y = y_location_of_start_msg,
                             lifetime = time_to_read_msg)
    line_two = games.Message(value = "Dodge the falling balls with the arrow keys",
                             size = size_of_msg,
                             color = color.red,
                             x = x_location_of_start_msg,
                             y = y_location_of_start_msg + 50,
                             lifetime = time_to_read_msg)
    line_three = games.Message(value = "If you die more than three times, game over!",
                             size = size_of_msg,
                             color = color.red,
                             x = x_location_of_start_msg,
                             y = y_location_of_start_msg + 100,
                             lifetime = time_to_read_msg)
    line_four = games.Message(value = "Written by: Matt Wall",
                             size = int(size_of_msg * (3/2)),
                             color = color.blue,
                             x = x_location_of_start_msg,
                             y = y_location_of_start_msg + 200,
                             lifetime = time_to_read_msg,
                               after_death = add_Objects)

    games.screen.add(line_one)
    games.screen.add(line_two)
    games.screen.add(line_three)
    games.screen.add(line_four)

    games.screen.mainloop()


    """Play the Game!"""

main()
