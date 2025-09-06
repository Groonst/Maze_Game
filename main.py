# Complete your game here
import pygame

class Level:
    """Level class to have the level settings separated from the app (normally would be a file)."""
    def __init__(self, level_number):
        self.level_number = level_number
        self.load_level()
    
    
    def load_level(self):
        if self.level_number == 1:
                        #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
            self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 0
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 1
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 2
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 3
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1], # 4
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], # 5
                        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], # 6
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], # 7
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], # 8
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], # 9
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] # 10
                        
            self.robot_position = (50, 400-18)
            self.monsters = [(50, 50, "ccv", "down"), 
                             (550, 250, "ccv", "down"), 
                             (350, 50, "ccv", "down")]
            self.coins = [(150 + 5 , 150 + 5), (650 + 5, 350 + 5)]
            self.doors = (750, 100 - 10)
        
        if self.level_number == 2:
                        #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
            self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 0
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], # 1
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], # 2
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 3
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 4
                        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], # 5
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 6
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 7
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], # 8
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], # 9
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] # 10
                        
            self.robot_position = (400, 450-36)
            self.monsters = [(50, 50, "ccv", "down"), 
                             (50, 430, "ccv", "left"), 
                             (750, 50, "ccv", "right"), 
                             (750, 430, "ccv", "up")]
            self.coins = [(150 + 5 , 125 + 5), (150 + 5 , 375 + 5), (650 + 5 , 125 + 5), (650 + 5, 375 + 5)]
            self.doors = (400, 50)    

        if self.level_number == 3:
                        #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
            self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 0
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 1
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 2
                        [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 3
                        [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1], # 4
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1], # 5
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1], # 6
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1], # 7
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 8
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 9
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] # 10
                        
            self.robot_position = (50, 50)
            self.monsters = [(175, 50, "vertical", "down"), 
                             (250, 300, "ccv", "left"), 
                             (550, 200, "horizontal", "right"), 
                             (500, 270, "horizontal", "right"), 
                             (450, 340, "horizontal", "right")]
            self.coins = [(50 + 5 , 200 + 5), (300 + 5, 250 + 5), (750 + 5, 425 + 5)]
            self.doors = (750, 100 - 10)

        if self.level_number == 4:
                        #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
            self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 0
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 1
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 2
                        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], # 3
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 4
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 5
                        [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1], # 6
                        [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1], # 7
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 8
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 9
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] # 10
                        
            self.robot_position = (50, 50)
            self.monsters = [(75, 200, "vertical", "down"), 
                             (225, 200, "vertical", "down"), 
                             (575, 200, "vertical", "down"), 
                             (725, 200, "vertical", "down"), 
                             (375, 200, "ccv", "left")]
            self.coins = [(75 + 5 , 225 + 5), (75 + 5, 425 + 5), (725 + 5, 225 + 5), (725 + 5, 425 + 5)]
            self.doors = (750, 50 + 10)

        if self.level_number == 5:
                        #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
            self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], # 0
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], # 1
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], # 2
                        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1], # 3
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], # 4
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], # 5
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 6
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 7
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], # 8
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], # 9
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]] # 10
                        
            self.robot_position = (50, 50 + 7)
            self.monsters = [(50, 315, "horizontal", "right"), 
                             (50, 350, "ccv", "down"), 
                             (750, 430, "ccv", "up"), 
                             (225, 50, "vertical", "down"), 
                             (625, 50, "vertical", "down")]
            self.coins = [(50 + 5 , 200 + 5), 
                          (50 + 5 , 450 + 5), 
                          (400 + 5 , 200 + 5), 
                          (400 + 5, 450 + 5), 
                          (500 + 5 , 50 + 5), 
                          (500 + 5 , 450 + 5), 
                          (750 + 5 , 50 + 5), 
                          (750 + 5, 450 + 5)]
            self.doors = (400, 50 + 10)  


class MazeGame:
    """Main class of the game."""
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.keys = set() 
        self.new_game()

        self.height = len(self.level.map)
        self.width = len(self.level.map[0])
        self.scale = 50

        window_height = self.scale * self.height
        window_width = self.scale * self.width
        self.window = pygame.display.set_mode((window_width, window_height))
        
        pygame.display.set_caption("Maze Game by Michal Filipek")

        self.load_images()
        self.main_loop()

    def check_coin_collision(self):
        """Detects the coin collision with the robot."""
        robot_rect = pygame.Rect(
            self.level.robot_position[0],
            self.level.robot_position[1],
            self.images["robot"].get_width(),
            self.images["robot"].get_height()
        )

        for coin in self.level.coins[:]:
            coin_rect = pygame.Rect(
                coin[0],
                coin[1],
                self.images["coin"].get_width(),
                self.images["coin"].get_height()
            )

            if robot_rect.colliderect(coin_rect):
                self.level.coins.remove(coin)  
                self.score += 500
                self.collected_coins += 1 

    def check_collision(self):
        """Detects the collision between the robot and monsters."""
        robot_rect = pygame.Rect(
            self.level.robot_position[0],
            self.level.robot_position[1],
            self.images["robot"].get_width(),
            self.images["robot"].get_height()
        )

        for monster in self.level.monsters:
            monster_rect = pygame.Rect(
                monster[0],
                monster[1],
                self.images["monster"].get_width(),
                self.images["monster"].get_height()
            )

            if robot_rect.colliderect(monster_rect):
                return True
        return False

    def check_door_collision(self):
        """Detects the collision with the door."""
        if self.collected_coins == len(self.level.coins) + self.collected_coins:
            robot_rect = pygame.Rect(
                self.level.robot_position[0],
                self.level.robot_position[1],
                self.images["robot"].get_width(),
                self.images["robot"].get_height()
            )

            door_rect = pygame.Rect(
                self.level.doors[0],
                self.level.doors[1],
                self.images["door"].get_width(),
                self.images["door"].get_height()
            )

            return robot_rect.colliderect(door_rect) 
        return False


    def reset_level(self):
        """Resets the current level."""
        self.collected_coins = 0
        self.score = self.last_level_score
        self.level = Level(self.level.level_number)

    def draw_congratulations(self):
        """Congratulation screen upon finishing the game."""
        congrats_font = pygame.font.SysFont("Arial", 50)
        score_font = pygame.font.SysFont("Arial", 16)
        restart_font = pygame.font.SysFont("Arial", 24)

        congrats_text = congrats_font.render("CONGRATULATIONS", True, (0, 255, 0))
        score_text = score_font.render(f"YOU HAVE FINISHED THE GAME WITH THE SCORE = {self.score} OUT OF 15500", True, (255, 255, 255))
        restart_text = restart_font.render("Press ENTER to exit", True, (255, 255, 255))

        text_x, text_y = 180, 180
        pygame.draw.rect(self.window, (255, 255, 255), (text_x - 5, text_y - 5, 500 + 10, 180 + 10))
        pygame.draw.rect(self.window, (0, 0, 0), (text_x, text_y, 500, 180))

        self.window.blit(congrats_text, (text_x + 50, text_y + 20))
        self.window.blit(score_text, (text_x + 15, text_y + 90))
        self.window.blit(restart_text, (text_x + 160, text_y + 140))
        pygame.display.flip()

    def draw_coins(self):
        """Draws the coins."""
        for coin in self.level.coins:
            self.window.blit(self.images["coin"], coin)

    def draw_doors(self):
        """Draws the door when all coins are collected."""
        if self.collected_coins == len(self.level.coins) + self.collected_coins:
            self.window.blit(self.images["door"], self.level.doors)

    def draw_collected_coins(self):
        """Will draw the status of collected coins in the top left corner."""
        font = pygame.font.SysFont("Arial", 24)
        coin_text = font.render(f"Collected coins: {self.collected_coins} / {len(self.level.coins) + self.collected_coins}", True, (255, 255, 255))
        self.window.blit(coin_text, (10, 10))
    
    def draw_score(self):
        """Will draw the current score."""
        font = pygame.font.SysFont("Arial", 24)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(score_text, (390, 10))

    def draw_lives(self):
        """Will draw the lifes in top right corner with two circles and a triangle."""
        heart_size = 20
        spacing = 15
        start_x = self.width * self.scale - (self.lives * (heart_size + spacing))
        start_y = 18

        for i in range(self.lives):
            x = start_x + i * (heart_size + spacing)
            y = start_y

            # Left circle
            pygame.draw.circle(self.window, (255, 0, 0), (x + heart_size // 4, y + heart_size // 4), heart_size // 2)
            # Right circle
            pygame.draw.circle(self.window, (255, 0, 0), (x + 3 * heart_size // 4, y + heart_size // 4), heart_size // 2)
            # Triangle
            pygame.draw.polygon(self.window, (255, 0, 0), [
                (x, y + heart_size // 2),
                (x + heart_size, y + heart_size // 2),
                (x + heart_size // 2, y + heart_size)
            ])

    def draw_game_over(self):
        """Will show the GAME OVER screen."""
        go_font = pygame.font.SysFont("Arial", 50)
        restart_font = pygame.font.SysFont("Arial", 24)
        game_over_text = go_font.render("GAME OVER", True, (255, 0, 0))
        restart_text = restart_font.render("Press ENTER to restart the game", True, (255, 255, 255))

        text_x , text_y = 280, 220
        pygame.draw.rect(self.window, (255, 255, 255), (text_x - 5, text_y - 5, 300 + 10, 100 + 10))
        pygame.draw.rect(self.window, (0, 0, 0), (text_x, text_y, 300 , 100))

        self.window.blit(game_over_text, (text_x + 25, text_y + 5))
        self.window.blit(restart_text, (text_x + 5, text_y + 60))
        pygame.display.flip()

    def draw_help(self):
        """Will show the help for keys and the current level."""
        font = pygame.font.SysFont("Arial", 24)
        help_text = font.render(f"SPACE = Restart level | ENTER = Restart game | Current level: {self.level.level_number} / 5", True, (255, 255, 255))
        self.window.blit(help_text, (10, self.height * self.scale - 30))

    def new_game(self):
        """Initial settings for the new game."""
        self.lives = 5
        self.game_over = False
        self.score = 0
        self.last_level_score = 0
        self.collected_coins = 0
        self.level = Level(1)

    def load_images(self):
        """Image loading (i've chosen to invert the monster image to look more like a ghost)."""
        self.images = {}
        for name in ["coin", "door", "monster", "robot"]:
            self.images[name] = pygame.image.load(name + ".png")
            if name == "monster":
                self.images[name] = self.invert_image(self.images[name])

    def invert_image(self, image):
        """This method inverts the ghost colors pixel by pixel."""
        surface = image.copy().convert_alpha()
        for x in range(surface.get_width()):
            for y in range(surface.get_height()):
                r, g, b, a = surface.get_at((x, y))
                surface.set_at((x, y), (255 - r, 255 - g, 255 - b, a))
        return surface

    def update_monsters(self):
        """Will update all the monsters according to their type and direction."""
        speed = 2
        new_monsters = []
        monster_width, monster_height = self.images["monster"].get_width(), self.images["monster"].get_height()

        for x, y, type, direction in self.level.monsters:
            new_x, new_y = x, y

            if type == "ccv":
                if direction == "down":
                    if self.can_move(new_x, new_y + speed, monster_width, monster_height):  
                        new_y += speed
                    else:
                        direction = "right"

                elif direction == "right":
                    if self.can_move(new_x + speed, new_y, monster_width, monster_height):
                        new_x += speed
                    else:
                        direction = "up"

                elif direction == "up":
                    if self.can_move(new_x, new_y - speed, monster_width, monster_height):
                        new_y -= speed
                    else:
                        direction = "left"

                elif direction == "left":
                    if self.can_move(new_x - speed, new_y, monster_width, monster_height):
                        new_x -= speed
                    else:
                        direction = "down"

            elif type == "vertical":
                if direction == "down":
                    if self.can_move(new_x, new_y + speed, monster_width, monster_height):  
                        new_y += speed
                    else:
                        direction = "up"

                elif direction == "up":
                    if self.can_move(new_x, new_y - speed, monster_width, monster_height):
                        new_y -= speed
                    else:
                        direction = "down"

            elif type == "horizontal":
                if direction == "right":
                    if self.can_move(new_x + speed, new_y, monster_width, monster_height):
                        new_x += speed
                    else:
                        direction = "left"
                if direction == "left":
                    if self.can_move(new_x - speed, new_y, monster_width, monster_height):
                        new_x -= speed
                    else:
                        direction = "right"

            new_monsters.append((new_x, new_y, type, direction))

        self.level.monsters = new_monsters

    def can_move(self, x, y, width, height):
        """Will check the monsters for collisions."""
        tile_positions = [
            (int(x / self.scale), int(y / self.scale)),  # Upper left corner
            (int((x + width - 1) / self.scale), int(y / self.scale)),  # Upper right corner
            (int(x / self.scale), int((y + height - 1) / self.scale)),  # Lower left corner
            (int((x + width - 1) / self.scale), int((y + height - 1) / self.scale))  # lower right corner
        ]
        return all(self.level.map[ty][tx] == 0 for tx, ty in tile_positions)

    def main_loop(self):
        """A main loop."""
        while True:
            self.check_events()
            if not self.game_over:
                self.update_player()
                self.update_monsters()
                self.check_coin_collision()

                if self.check_collision():
                    self.score = max(0, (self.score - 500))
                    self.last_level_score = max(0, (self.last_level_score - 500))
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over = True
                    else:
                        self.reset_level()

                if self.check_door_collision():
                    if self.level.level_number == 5:
                        self.score += 1000
                        self.draw_congratulations()
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                    exit()
                                if event.type == pygame.QUIT:
                                    exit()
                            else:
                                continue
                    else:
                        self.collected_coins = 0
                        self.score += 1000
                        self.last_level_score = self.score
                        self.level = Level(self.level.level_number + 1)

                self.draw_window()
            else:
                self.draw_game_over()
                if pygame.K_RETURN in self.keys:
                    self.new_game()

            self.clock.tick(60)

    def move_player(self, dx, dy):
        """Will move the player."""
        new_x, new_y = self.level.robot_position
        robot_width, robot_height = self.images["robot"].get_width(), self.images["robot"].get_height()

        def can_move(x, y):
            """Checks all the corners and line centers for collision with wall."""
            tile_positions = [
                (int(x / self.scale), int(y / self.scale)),  # Upper left corner
                (int((x + robot_width - 1) / self.scale), int(y / self.scale)),  # Upper right corner
                (int(x / self.scale), int((y + robot_height - 1) / self.scale)),  # Lower left corner
                (int((x + robot_width - 1) / self.scale), int((y + robot_height - 1) / self.scale)),  # Lower right corner
                (int((x + robot_width / 2) / self.scale), int(y / self.scale)),  # The center of upper line
                (int((x + robot_width / 2) / self.scale), int((y + robot_height - 1) / self.scale)),  # The center of lower line
                (int(x / self.scale), int((y + robot_height / 2) / self.scale)),  # The center of left line
                (int((x + robot_width - 1) / self.scale), int((y + robot_height / 2) / self.scale))  # The center of right line
            ]
            return all(self.level.map[ty][tx] == 0 for tx, ty in tile_positions)

        if can_move(new_x + dx, new_y):
            new_x += dx

        if can_move(new_x, new_y + dy):
            new_y += dy

        self.level.robot_position = (new_x, new_y)
        
    def update_player(self):
        """Will call for moving the player according to the downed keys."""
        speed = 3

        dx = 0
        dy = 0

        if pygame.K_LEFT in self.keys:
            dx -= speed
        if pygame.K_RIGHT in self.keys:
            dx += speed
        if pygame.K_UP in self.keys:
            dy -= speed
        if pygame.K_DOWN in self.keys:
            dy += speed

        self.move_player(dx, dy)

    def check_events(self):
        """Event check."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.keys.add(event.key)
                if event.key == pygame.K_SPACE:
                    self.reset_level()
                if event.key == pygame.K_RETURN:
                    self.new_game()



            if event.type == pygame.KEYUP:
                self.keys.discard(event.key)

            if event.type == pygame.QUIT:
                exit()

    def draw_window(self):
        """Will call for drawing all the things."""
        self.draw_map()
        self.draw_characters()
        self.draw_coins()
        self.draw_doors()
        self.draw_collected_coins()
        self.draw_score()
        self.draw_lives()
        self.draw_help()
        pygame.display.flip()

    def draw_map(self):
        """Draws the map."""
        self.window.fill((0, 0, 0))
        for y in range(self.height):
            for x in range(self.width):
                if self.level.map[y][x] == 1:
                    self.draw_wall(x * self.scale, y * self.scale)

    def draw_wall(self, wall_x, wall_y):
        """Draws the wall."""
        pygame.draw.rect(self.window, (100, 100, 100), (wall_x, wall_y, self.scale, self.scale))
    
    def draw_characters(self):
        """Draws the characters"""
        self.window.blit(self.images["robot"], self.level.robot_position)
        for monster_position in self.level.monsters:
            self.window.blit(self.images["monster"], (monster_position[0], monster_position[1]))
        

if __name__ == "__main__":
    MazeGame()
