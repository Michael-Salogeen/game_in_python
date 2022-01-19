# 1. Подключения модулей для работы
# 2. Создание игрового поля
# 3. Создание игровых обЪектов
# 4. Создание логики и управления игрой
# 5. Создание счетчик

# Подключения модулей (pygame, sys, random)
import pygame, sys, random

#-----------------------------------------------------------

def ball_animation():
	# Обращение к глобальным переменным
	global ball_speed_x, ball_speed_y

	ball.x += ball_speed_x # Движение мяча
	ball.y += ball_speed_y # Движение мяча

	# Логика столкновения со стенками
	if ball.top <= 0:
		ball_speed_y *= -1 # Отражение мяча
	if ball.bottom >= screen_height:
		ball_speed_y *= -1 # Отражение мяча
	if ball.left <= 0:
		ball_start() # Возвращать в центр после столкновения
	if ball.right >= screen_width:
		ball_start() # Возвращать в центр после столкновения
	
	# Логика столкновения с игроками
	if ball.colliderect(player):
		ball_speed_x *= -1 # Отражение мяча
	if ball.colliderect(opponent):
		ball_speed_x *= -1 # Отражение мяча


def player_animation():
	player.y += player_speed # Движение игрока

	# Логика столкновения со стенками
	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height


def opponent_animation():
	# Логика движения за мячом когда он выше или ниже игрока
	if opponent.top < ball.y:
		opponent.top += opponent_speed
	if opponent.bottom > ball.y:
		opponent.bottom -= opponent_speed

	# Логика столкновения со стенками
	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height
	

def ball_start():
	# Обращение к глобальным переменным
	global ball_speed_x, ball_speed_y

	# Поместить в центре окна
	ball.center = (screen_width/2, screen_height/2)
	ball_speed_x *= random.choice((1, -1)) # Движение в случайную сторону
	ball_speed_y *= random.choice((1, -1)) # Движение в случайную сторону

#-----------------------------------------------------------

# Инициализация главной модуля pygame
pygame.init()
clock  = pygame.time.Clock()  # Время и частота кадров

screen_width  = int(1280/1.35) # Ширина
screen_height = int(960/1.35)  # Высота
screen = pygame.display.set_mode((screen_width, screen_height)) # Создание игрового окна
pygame.display.set_caption('Pong') # Название игрового окна

#-----------------------------------------------------------

# Создание цвета
bg_color   = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Создание игровых обЪектов (ball, player, opponent)
ball     = pygame.Rect(screen_width/2-12, screen_height/2-12, 25,  25)
player   = pygame.Rect(screen_width - 20, screen_height/2-70, 10, 140)
opponent = pygame.Rect(               20, screen_height/2-70, 10, 140)

# Скорость игровых обЪектов
ball_speed_x = 5.0 * random.choice((1, -1))
ball_speed_y = 5.0 * random.choice((1, -1))

player_speed   = 0.0
opponent_speed = 5.0

#-----------------------------------------------------------

# Главный игровой цикл
while True:

	# Цикл для отслеживание всех событий игры
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Проверка на закрытие окна
			pygame.quit()             # Закрытие из pygame
			sys.exit()                # Системное закрытие окна
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				player_speed -= 5.0
			if event.key == pygame.K_s:
				player_speed += 5.0
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				player_speed += 5.0
			if event.key == pygame.K_s:
				player_speed -= 5.0


	# Функции логики и анимации
	ball_animation()
	player_animation()
	opponent_animation()

	# Установка цвета окна
	screen.fill(bg_color)

	# Отрисовка игровых обЪекты
	pygame.draw.rect(   screen, light_grey, player  )
	pygame.draw.rect(   screen, light_grey, opponent)
	pygame.draw.ellipse(screen, light_grey, ball    )
	pygame.draw.aaline( screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))


	pygame.display.flip() # Обновление содержимое основного окна
	clock.tick(60)        # Частота обновления окна в сек