import pygame
from dino_runner.components.Dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

FONT_STYLE = "freesansbold.ttf"

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.playing = True
        self.points =0
        while self.playing:
            self.events()
            self.update()
            self.draw()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                

    def update(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        self.player.check_invicibility()
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self, self.points)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"Points: {self.points}", True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 22)
        self.screen.blit(text, text_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                self.run()

    def draw_message_component(self, message: str, pos_y = 0):
        half_screen_width = SCREEN_WIDTH//2
        half_screen_height = SCREEN_HEIGHT//2
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(message, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (half_screen_width, half_screen_height + pos_y)
        self.screen.blit(text, text_rect)



    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT//2
        half_screen_width = SCREEN_WIDTH//2

        if  self.death_count == 0:
            
            self.draw_message_component("Press any key to start")

        else:

            self.draw_message_component("Press any key to restart")
        self.draw_message_component(f"Your Score: {self.points}", 50)
        self.draw_message_component(f"Death Count: {self.death_count}", 100)
        
        self.screen.blit(RUNNING[0], (half_screen_width -50, half_screen_height -120))

        pygame.display.update()
        self.handle_key_events_on_menu()