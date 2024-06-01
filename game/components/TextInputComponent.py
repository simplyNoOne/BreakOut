import pygame
from engine import Engine, EntityComponent, ResourceManager
from game.GameManager import GameManager



class TextInputComponent(EntityComponent):
    def __init__(self):
        super().__init__()
        self._player_name : list[str] = [""]
        self._pass : list[str] = [""]
        self._text : list[str] = self._player_name
        self._box_w = 400
        self._box_h = 60
        self._box_x = 0
        self._box_y1 = 0
        self._box_y2 = 0
        self._label_color = (220, 220, 220)
        self._active_color = (200, 200, 200)
        self._inactive_color = (100, 100, 100)
        self._col_1 = self._active_color
        self._col_2 = self._inactive_color
        self._focused = True
        self._focused_el = 0
        self._just_returned = False
        self._on_give_up_focus = []
        self._on_credentials_collected = []
        self._shift = 15
        self._up_shift = 100
        self._len_limit = 15


    def load(self):
        super().load()
        self._font = pygame.font.Font(None, 50)
        self._player_name[0] = GameManager.get().get_player_name()
        if self._player_name[0] == "Anonymous":
            self._player_name[0] = ""
        self._pass[0] = GameManager.get().get_player_password()
        self._label_x = self._owner.x - 300
        self._label_name_surface = self._font.render("Name: ", True, self._label_color)
        self._label_pass_surface = self._font.render("Password: ", True, self._label_color)
        w = self._label_pass_surface.get_width()
        self._box_x = self._label_x + w + 20
        self._box_y1 = self._owner.y - self._up_shift
        self._box_y2 = self._owner.y - self._up_shift + self._box_h + 20


    def update(self, dt):
        super().update(dt)
        if not self._focused:
            return
        
        events = Engine.get().get_events()
        if self._just_returned:
            self._just_returned = False
            return

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self._text[0] = self._text[0][:-1]
                elif event.key == pygame.K_UP:
                    self.focus_up()
                elif event.key == pygame.K_DOWN:
                    self.focus_down()
                elif event.unicode.isalnum() or event.unicode == '_':
                    if len(self._text[0]) < self._len_limit:
                        self._text[0] += event.unicode
                

    def forward_credentials(self):
        for func in self._on_credentials_collected:
            func(self._player_name[0], self._pass[0])
        if GameManager.get().get_player_name() == "":
            self._pass[0] = ""
        

    def draw(self, window):
        super().draw(window)
        window.blit(self._label_name_surface, (self._label_x, self._box_y1 + self._shift))
        window.blit(self._label_pass_surface, (self._label_x, self._box_y2 + self._shift))
        name_surface = self._font.render(self._player_name[0], True, (250,250,250))
        window.blit(name_surface, (self._box_x + self._shift, self._box_y1 + self._shift))
        pass_surface = self._font.render(self._pass[0], True, (250,250,250))
        window.blit(pass_surface, (self._box_x + self._shift, self._box_y2 + self._shift))
        pygame.draw.rect(window, self._col_1, (self._box_x, self._box_y1, self._box_w, self._box_h), 2)
        pygame.draw.rect(window, self._col_2, (self._box_x, self._box_y2, self._box_w, self._box_h), 2)


    def focus_down(self):
        self._col_1 = self._inactive_color
        self._col_2 = self._active_color
        self._text = self._pass
        self._focused_el += 1
        if self._focused_el > 1:
            self.give_up_focus()
            
    def focus_up(self):
        self._col_1 = self._active_color
        self._col_2 = self._inactive_color
        self._text = self._player_name
        self._focused_el = 0
        print("hark")


    def bind_to_give_up_focus(self, func):
        self._on_give_up_focus.append(func)
    
    def bind_to_credentials_collected(self, func):
        self._on_credentials_collected.append(func)

    def give_up_focus(self):
        self._focused = False
        self._col_2 = self._inactive_color
        for func in self._on_give_up_focus:
            func()

    def get_focus(self):
        self._focused_el = 1
        self._col_1 = self._inactive_color
        self._col_2 = self._active_color
        self._text = self._pass
        self._just_returned = True
        self._focused = True
