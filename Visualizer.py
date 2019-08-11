import pygame
import random
import time
from Vehicle import Vehicle
from typing import List, Tuple, Optional
from PowerUp import PowerUp

black = (0, 0, 0)
white = (255, 255, 255)
display_width = 800
display_height = 600

PLAYER_ONE_CONTROLS = [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s,
                       pygame.K_e]
PLAYER_TWO_CONTROLS = [pygame.K_LEFT, pygame.K_RIGHT,
                       pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE]


class Visualizer:

    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((display_width,
                                                     display_height))
        pygame.display.set_caption("Tron")
        self.clock = pygame.time.Clock()

    def game_loop(self):
        player_width = 10
        player_height = 10
        player_speed = 400
        power_up_height = 15
        power_up_width = 15
        power_up_time = 2000
        curr_power_up = 0

        player = Vehicle(display_width * 0.2, display_height * 0.5,
                         player_width, player_height,
                         (255, 22, 255), PLAYER_ONE_CONTROLS, "pink")
        player2 = Vehicle(display_width * 0.8, display_height * 0.5,
                          player_width, player_height, (51, 255, 51),
                          PLAYER_TWO_CONTROLS, "green")

        players = [player, player2]
        trails = []
        loser = []
        power_ups = []

        play = True

        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                trails = []
                for p in players:
                    trails.append(p.get_trail().get_locations())
                    p.set_change(self.user_controls
                                 (pygame.key.get_pressed(), p))

            self.game_display.fill(white)

            for p in range(len(players)):
                if players[p].get_is_boost():
                    for i in range(players[p].get_boost().get_boost_length()):
                        players[p].change_pos()
                        self.check_boundaries(players[p])
                        if self.check_crash(trails, players[p], p):
                            play = False
                            break
                    players[p].set_is_boost(False)
                else:
                    self.check_boundaries(players[p])
                    players[p].change_pos()
                players[p].get_boost().add_charge(1)
                self.draw_lines()
                self.draw_user(players[p])
                self.draw_boost(players)
                self.display_message("TRON", int(display_width * 0.6),
                                     int(display_height * 0.07), 50)
                if len(power_ups) < 3:
                    curr_power_up += 1
                    if curr_power_up > power_up_time:
                        curr_power_up = 0
                        power_up = self.generate_power_ups\
                            (power_up_width, power_up_height)
                        if power_up:
                            power_ups.append(power_up)
                for pup in power_ups:
                    self.draw_power_up(pup, (109, 165, 255))
                    if self.check_power_up(players[p], pup):
                        pup.activate(1, players[p])
                        power_ups.remove(pup)
                if self.check_crash(trails, players[p], p):
                    loser.append(players[p])
                    if (players[0].get_x() == players[1].get_x()) and \
                            (players[0].get_y() == players[1].get_y()):
                        loser = []
                        for player in players:
                            loser.append(player)

            if len(loser) > 0:
                pygame.display.update()
                self.display_loser(loser)
                play = False

            pygame.display.update()
            self.clock.tick(player_speed)

    def game_intro(self) -> None:

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.game_display.fill(white)
            self.display_message("TRON", int(display_width/2),
                                 int(display_height/2), 75)
            self.create_button("BEGIN", int(display_width * 0.25),
                               int(display_height * 0.6), 100, 50,
                               (51, 255, 51), (20, 200, 20), "Play")
            self.create_button("HELP", int(display_width * 0.75) - 100,
                               int(display_height * 0.6), 100, 50,
                               (255, 22, 255), (200, 0, 200), "Help")
            pygame.display.update()
            self.clock.tick(15)

    def game_ending(self, message: str) -> None:

        cont = True

        while cont:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.game_display.fill(white)
            self.display_message(message,
                                 int(display_width/2),
                                 int(display_height/2), 75)
            self.create_button("PLAY AGAIN", int(display_width * 0.25),
                               int(display_height * 0.6), 150, 50,
                               (51, 255, 51), (20, 200, 20), "Play")
            self.create_button("QUIT", int(display_width * 0.75) - 100,
                               int(display_height * 0.6), 100, 50,
                               (255, 22, 255), (200, 0, 200), "Quit")
            pygame.display.update()
            self.clock.tick(15)

    def help(self) -> None:
        cont = True
        space = 25
        while cont:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.game_display.fill(white)
            self.display_message("Instructions:",
                                 int(display_width / 2),
                                 int(display_height / 9), 20)
            self.display_message("Players ride their vehicles around the "
                                 "screen trying to get the other player to "
                                 "crash into their trail. Players can also ",
                                 int(display_width / 2),
                                 int(display_height / 8) + space, 10)
            self.display_message("boost while they are moving, where they get "
                                 "a temporary speed boost. Each player has a "
                                 "maximum of 3 speed boosts, that recharge ",
                                 int(display_width / 2),
                                 int(display_height / 8) + 2 * space, 10)
            self.display_message("over time and if a player picks up a boost "
                                 "item that randomly spawn on the map.",
                                 int(display_width / 2),
                                 int(display_height / 8) + 3 * space, 10)
            self.display_message("Player 1",
                                 int(display_width / 2),
                                 int(display_height / 8) + 4 * space, 14)
            self.display_message("Up: W    "
                                 "Left: A    "
                                 "Down: S    "
                                 "Right: D    "
                                 "Boost: E    ",
                                 int(display_width / 2),
                                 int(display_height / 8) + 5 * space, 14)
            self.display_message("Player 2",
                                 int(display_width / 2),
                                 int(display_height / 8) + 6 * space, 14)
            self.display_message("Up: Up Arrow    "
                                 "Left: Left Arrow    "
                                 "Down: Down Arrow    "
                                 "Right: Right Arrow    "
                                 "Boost: Space Bar    ",
                                 int(display_width / 2),
                                 int(display_height / 8) + 7 * space, 14)
            self.display_message("Thanks for playing!",
                                 int(display_width / 2),
                                 int(display_height / 8) + 8 * space, 14)
            self.create_button("PLAY", int(display_width * 0.5) - 50,
                               int(display_height * 0.5), 100, 50,
                               (51, 255, 51), (20, 200, 20), "Play")
            self.display_message("Game made by Alexander Shih, Student "
                                 "attending University of Toronto",
                                 int(display_width / 2),
                                 int(display_height / 8) + 12 * space, 14)
            pygame.display.update()
            self.clock.tick(15)

    def create_button(self, text: str, x: int, y: int, width: int, height: int,
                      off_color: Tuple, on_color: Tuple, action) -> None:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x <= mouse[0] <= x + width and y <= mouse[1] <= y + height:
            pygame.draw.rect(self.game_display, on_color,
                             [x, y, width, height])
            if click[0] == 1 and action != None:
                if action == "Play":
                    self.game_loop()
                elif action == "Help":
                    self.help()
                elif action == "Quit":
                    pygame.quit()
                    quit()
        else:
            pygame.draw.rect(self.game_display, off_color,
                             [x, y, width, height])
        text_surface = pygame.font.Font("SourceCodePro-Regular.ttf", 20) \
            .render(text, True, black)
        surface, rectangle = text_surface, text_surface.get_rect()
        rectangle.center = (x + width / 2, y + height / 2)
        self.game_display.blit(surface, rectangle)

    def user_controls(self, keys_pressed, player) -> tuple:
        """
        :param keys_pressed: boolean values representing state of keys
        :return: int, int
        :return: int, int
        """
        x_change = 0
        y_change = 0
        controls = player.get_controls()

        if keys_pressed[controls[0]]:
            x_change -= 1
        if keys_pressed[controls[1]]:
            x_change += 1
        if keys_pressed[controls[2]]:
            y_change -= 1
        if keys_pressed[controls[3]]:
            y_change += 1

        if keys_pressed[controls[4]]:
            boost = player.get_boost()
            if boost.curr_boost > 0:
                player.set_is_boost(True)
                boost.change_boost(-1)

        return x_change, y_change

    def draw_user(self, player: Vehicle):
        """
        draws player as a rectangle
        :param player: Vehicle object
        :return: None
        """
        pygame.draw.rect(self.game_display, player.get_color(),
                         [player.get_x(), player.get_y(), player.get_width(),
                          player.get_height()])
        trail = player.get_trail()
        trail_locations = trail.get_locations()
        for i in range(1, len(trail_locations)):
            pygame.draw.line(self.game_display, player.get_color(),
                             list(trail_locations[i]),
                             list(trail_locations[i]), trail.get_width())

    def draw_lines(self) -> None:
        pygame.draw.line(self.game_display, black, (0, display_height * 0.15),
                         (display_width, display_height * 0.15), 2)

    def check_boundaries(self, player: Vehicle):
        if player.get_x() + player.get_width() > display_width:
            player.set_pos((0, player.get_y()))
        elif player.get_x() < 0:
            player.set_pos((display_width - player.get_width(), player.get_y()))
        elif player.get_y() + player.get_height() > display_height:
            player.set_pos((player.get_x(), int(display_height * 0.15)))
        elif player.get_y() < display_height * 0.15:
            player.set_pos((player.get_x(),
                            display_height - player.get_height()))

    def check_crash(self, positions: List[List[Tuple]], player: Vehicle,
                    player_num: int) -> bool:
        curr_location = player.get_x(), player.get_y() + player.get_width()/2
        for position in range(len(positions)):
            if position != player_num:
                if curr_location in positions[position]:
                    return True
        return False

    def draw_boost(self, players: List[Vehicle]) -> None:
        height = 0
        bar_length = 100
        for p in players:
            boost = p.get_boost()
            for i in range(boost.get_curr()):
                pygame.draw.circle(self.game_display, p.get_color(),
                                   [(int(display_width * 0.05)) + 20 * i,
                                    (int(display_height * 0.05)) + height],
                                   5, 5)
            pygame.draw.rect(self.game_display, p.get_color(),
                             ((int(display_width * 0.05)) + 20 *
                              boost.get_max(),
                              (int(display_height * 0.05)) + height - 5,
                              int(boost.get_charge() * bar_length /
                                  boost.get_max_charge())
                              , 10), 0)
            pygame.draw.rect(self.game_display, (0, 0, 0),
                             ((int(display_width * 0.05)) + 20 *
                              boost.get_max(),
                              (int(display_height * 0.05)) + height - 5,
                              bar_length, 10), 1)
            height += 20

    def display_loser(self, players: List) -> None:
        time.sleep(1)
        if len(players) == 1:
            self.game_ending(players[0].get_name() + " loses!")
        else:
            self.game_ending("It's a tie!")

    def display_message(self, message: str, width: int, height: int,
                        font_size: int) -> None:
        text = pygame.font.Font('SourceCodePro-Regular.ttf', font_size)
        surf, text_box = self.text_objects(message, text)
        text_box.center = (width, height)
        self.game_display.blit(surf, text_box)

    def text_objects(self, text, font):
        surface = font.render(text, True, black)
        return surface, surface.get_rect()

    def generate_power_ups(self, height, width) -> Optional[PowerUp]:
        power_up = PowerUp(height, width, random.randint(0, display_width),
                           random.randint(display_height * 0.15, display_height), 1)
        return power_up

    def draw_power_up(self, power_up: PowerUp, color):
        pygame.draw.rect(self.game_display, color,
                         [power_up.get_x(), power_up.get_y(),
                          power_up.get_width(), power_up.get_height()])

    def check_power_up(self, user: Vehicle, pup: PowerUp) -> bool:
        if (((pup.get_x() <= user.get_x() <= pup.get_x() +
            pup.get_height())
            or (pup.get_x() <= user.get_x() + user.get_height()
            <= pup.get_x() + pup.get_height()))
            and ((pup.get_y() <= user.get_y() <= pup.get_y() +
                  pup.get_width())
            or (pup.get_y() <= user.get_y() + user.get_width() <=
                pup.get_y() + pup.get_width()))):
            return True
        return False


if __name__ == '__main__':
    game = Visualizer()
    game.game_intro()
    game.game_loop()
    pygame.quit()
    quit()
