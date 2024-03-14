import sys
import pygame


class AlienInvasion:
    ''' Класс для управленя ресурсами и поведением игры'''
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        # Назначаем новы цвет фона
        self.bg_color = (90, 177, 200)

    def run_game(self):
        '''Запуск основного цикла игры'''
        while True:
            # Отслеживание событий клавы и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #При каждом проходе цикла перерисовывается экран
            self.screen.fill(self.bg_color)
            # Отображение последнего прорисованного экрана
            pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()