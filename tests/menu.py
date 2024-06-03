import pygame
import pygame_menu
from pygame_menu import themes


class Menu(pygame_menu.Menu):
    def __init__(self, root, theme=themes.THEME_GREEN):
        theme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_NONE
        theme.title_font = pygame_menu.font.FONT_COMIC_NEUE
        theme.widget_font = pygame_menu.font.FONT_OPEN_SANS_LIGHT
        theme.title_font_color = "green"
        theme.selection_color = 'black'
        super().__init__(pygame.display.get_caption()[0], root.get_width(), root.get_height(), theme=theme)
        self.root = root
        self.set_title('Menu')

    def flip(self, events):
        if self.is_enabled():
            self.update(events)
        if self.is_enabled():
            self.draw(self.root)
