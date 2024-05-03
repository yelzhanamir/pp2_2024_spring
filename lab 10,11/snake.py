import pygame
import time
import random
import psycopg2
from config import load_config

# Инициализация базы данных
conn = None
cur = None

# Подключение к базе данных
def connect_db():
    global conn, cur
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()
        print("Подключение к базе данных успешно.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Создание таблицы пользователей
def create_user_table():
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS "user" (
                user_id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL
            )
        """)
        conn.commit()
        print("Таблица пользователей успешно создана.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Создание таблицы результатов пользователей
def create_user_score_table():
    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user_score (
                score_id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES "user"(user_id),
                score INTEGER NOT NULL,
                level INTEGER NOT NULL
            )
        """)
        conn.commit()
        print("Таблица результатов пользователей успешно создана.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Вставка нового пользователя в базу данных
def insert_user(username):
    try:
        cur.execute("INSERT INTO \"user\" (username) VALUES (%s) ON CONFLICT DO NOTHING RETURNING user_id;", (username,))
        conn.commit()
        user_id = cur.fetchone()[0]
        print("Пользователь успешно добавлен.")
        return user_id
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Вставка результатов игры в базу данных
def insert_score(user_id, score, level):
    try:
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s);", (user_id, score, level))
        conn.commit()
        print("Результаты успешно сохранены.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Отображение таблицы результатов
def show_scores():
    try:
        cur.execute("SELECT u.username, s.score, s.level FROM user_score s JOIN \"user\" u ON s.user_id = u.user_id ORDER BY s.score DESC;")
        scores = cur.fetchall()
        print("Таблица результатов:")
        print("Имя пользователя\tОчки\tУровень")
        for row in scores:
            print("\t".join(str(col) for col in row))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# Основной игровой цикл
def gameLoop(snake_speed):
    global conn, cur

    pygame.init()

    # Инициализация экрана
    dis_width = 800
    dis_height = 600
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake')

    # Initialize clock
    clock = pygame.time.Clock()

    # Colors
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    # Snake block size and speed
    snake_block = 10

    # Fonts
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    class Food:
        def __init__(self, x, y, weight, time):
            self.x = x
            self.y = y
            self.weight = weight
            self.time = time

    def generate_food():
        # Generate food items randomly with different weights
        x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        weight = random.randint(1, 4)  # Random weight between 1 and 4
        return Food(x, y, weight, time.time())

    def draw_food(food):
        # Draw food item on the screen
        size = snake_block + food.weight * 5  # Increase size based on weight
        pygame.draw.rect(dis, green, [food.x, food.y, size, size])

    def Your_score(score, level):
        # Display score and level
        score_level = score_font.render("Score: " + str(score) + "   Level: " + str(level), True, yellow)
        dis.blit(score_level, [0, 0])

    def our_snake(snake_block, snake_list):
        # Display the snake
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    food = generate_food()

    # Game level
    level = 1

    # Counter for the number of foods eaten
    food_eaten = 0

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lost", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_p:
                    pause_game()

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(red)  # Red background

        draw_food(food)

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1, level)

        pygame.display.update()

        # Check if snake eats the food
        if x1 <= food.x + food.weight * 5 and x1 >= food.x and y1 <= food.y + food.weight * 5 and y1 >= food.y:
            Length_of_snake += food.weight
            food = generate_food()  # Generate new food item
            food_eaten += 1  # Increase the food eaten count

        # Check if food disappears after some time
        if time.time() - food.time > 5:  # Change 5 to the desired time in seconds
            food = generate_food()  # Generate new food item

        # Increase level when the player eats 2 foods
        if food_eaten == 3:
            level += 1
            snake_speed +=2.5 
            food_eaten = 0  # Reset the food eaten count

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def message(msg, color):
    # Display message at the center of the screen
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2 - mesg.get_width() / 2, dis_height / 2 - mesg.get_height() / 2])

def pause_game():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
        show_scores()  # Отображение таблицы результатов

if __name__ == "__main__":
    connect_db()
    create_user_table()
    create_user_score_table()

    username = input("Введите ваше имя: ")
    user_id = insert_user(username)
    gameLoop(15)  # Устанавливаем скорость змейки
    insert_score(user_id, 0, 0)  # Вставляем результаты в базу данных
