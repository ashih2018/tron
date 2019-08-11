

class Scene:
    def game_intro(self) -> None:

        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.gameDisplay.fill(white)
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
            self.gameDisplay.fill(white)
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
            self.gameDisplay.fill(white)
            self.display_message("Instructions:",
                                 int(display_width / 2),
                                 int(display_height / 9), 20)
            self.display_message("Players ride their vehicles around the"
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
            pygame.draw.rect(self.gameDisplay, on_color,
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
            pygame.draw.rect(self.gameDisplay, off_color,
                             [x, y, width, height])
        text_surface = pygame.font.Font("SourceCodePro-Regular.ttf", 20) \
            .render(text, True, black)
        surface, rectangle = text_surface, text_surface.get_rect()
        rectangle.center = (x + width / 2, y + height / 2)
        self.gameDisplay.blit(surface, rectangle)
