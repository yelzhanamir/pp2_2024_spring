import pygame
import random

SQUARE = 'SQUARE'
CIRCLE = 'CIRCLE'
TRIANGLE = 'TRIANGLE'
RHOMBUS = 'RHOMBUS'

dis_width = 640
dis_height = 480
main_screen_size = (dis_width, dis_height)
elements_to_draw = []

icon_top_bar_height = 50
icon_top_bar_width = 50
icon_rectangle_start_x = 0
icon_rectangle_end_x = 50
icon_circle_start_x = 50
icon_circle_end_x = 100
icon_triangle_start_x = 100
icon_triangle_end_x = 150
icon_rhombus_start_x = 150
icon_rhombus_end_x = 200

icon_red_color_start_y = 50
icon_red_color_end_y = 75
icon_blue_color_start_y = 100
icon_blue_color_end_y = 125
icon_black_color_start_y = 150
icon_black_color_end_y = 175
icon_green_color_start_y = 200
icon_green_color_end_y = 225
icon_yellow_color_start_y = 250
icon_yellow_color_end_y = 275
icon_purple_color_start_y = 300
icon_purple_color_end_y = 325
icon_pink_color_start_y = 350
icon_pink_color_end_y = 375
icon_gray_color_start_y = 400
icon_gray_color_end_y = 425


icon_color_shape_width = 40
icon_color_shape_height = 30

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)
pink = (255, 105, 180)
gray = (128, 128, 128)


top_tab_color = (100, 100, 100)
right_tab_color = (80, 80, 80)


def draw_all_shapes(screen):
    for element in elements_to_draw:
        if element['shape'] == SQUARE:
            pygame.draw.rect(screen, element['color'],
                             [element['x'], element['y'], 50, 50])
        elif element['shape'] == CIRCLE:
            pygame.draw.circle(screen, element['color'],
                               (element['x'], element['y']), element['radius'])
        elif element['shape'] == TRIANGLE:
            draw_triangle(screen, element['x'], element['y'], element['color'])
        elif element['shape'] == RHOMBUS:
            draw_rhombus(screen, element['x'], element['y'], element['color'])


def draw_triangle(screen, x, y, color):
    points = [(x, y - 25), (x + 25, y + 25), (x - 25, y + 25)]
    pygame.draw.polygon(screen, color, points)


def draw_rhombus(screen, x, y, color):
    points = [(x, y - 25), (x + 25, y), (x, y + 25), (x - 25, y)]
    pygame.draw.polygon(screen, color, points)


def add_element_rectangle(x, y, color):
    elements_to_draw.append({'shape': SQUARE, 'x': x, 'y': y, 'color': color})


def add_element_circle(x, y, color, radius):
    elements_to_draw.append({
        'shape': CIRCLE,
        'x': x,
        'y': y,
        'color': color,
        'radius': radius
    })


def add_element_triangle(x, y, color):
    elements_to_draw.append({
        'shape': TRIANGLE,
        'x': x,
        'y': y,
        'color': color
    })


def add_element_rhombus(x, y, color):
    elements_to_draw.append({
        'shape': RHOMBUS,
        'x': x,
        'y': y,
        'color': color
    })


def draw_main_icons(screen):
    pygame.draw.rect(screen, top_tab_color, (0, 0, dis_width, 40))
    pygame.draw.rect(screen, right_tab_color,
                     (dis_width - 80, 0, 80, dis_height))
    pygame.draw.rect(screen, white, (icon_rectangle_start_x + 5, 5, 40, 30))
    pygame.draw.rect(screen, white, (icon_circle_start_x + 5, 5, 40, 30))
    pygame.draw.circle(
        screen, (128, 0, 128), (icon_circle_start_x + 25, 20), 10)
    pygame.draw.polygon(screen, white, [(icon_triangle_start_x + 25, 5), (icon_triangle_start_x + 45, 35), (icon_triangle_start_x + 5, 35)])
    pygame.draw.polygon(screen, white, [(icon_rhombus_start_x + 25, 5), (icon_rhombus_start_x + 50, 20), (icon_rhombus_start_x + 25, 35), (icon_rhombus_start_x, 20)])
    pygame.draw.rect(screen, red,
                     (dis_width - 70, icon_red_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, blue,
                     (dis_width - 70, icon_blue_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, black,
                     (dis_width - 70, icon_black_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, green,
                     (dis_width - 70, icon_green_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, yellow,
                     (dis_width - 70, icon_yellow_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, purple,
                     (dis_width - 70, icon_purple_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, pink,
                     (dis_width - 70, icon_pink_color_start_y, icon_color_shape_width, icon_color_shape_height))
    pygame.draw.rect(screen, gray,
                     (dis_width - 70, icon_gray_color_start_y, icon_color_shape_width, icon_color_shape_height))


def main():
    pygame.init()
    screen = pygame.display.set_mode(main_screen_size)
    clock = pygame.time.Clock()

    x = 0
    y = 0
    mode = 'blue'
    points = []
    is_rectangle_drawer = False
    is_circle_drawer = False
    is_triangle_drawer = False
    is_rhombus_drawer = False

    color = black

    position = (0, 0)

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if position[0] <= icon_rectangle_end_x and position[
                            0] > 0 and position[1] < icon_top_bar_height:
                        is_rectangle_drawer = not is_rectangle_drawer
                        is_circle_drawer = False
                        is_triangle_drawer = False
                        is_rhombus_drawer = False
                        print('is_rectangle_drawer = True')
                    elif position[0] <= icon_circle_end_x and position[
                            0] > icon_circle_start_x and position[1] < icon_top_bar_height:
                        is_circle_drawer = not is_circle_drawer
                        is_rectangle_drawer = False
                        is_triangle_drawer = False
                        is_rhombus_drawer = False
                        print('is_circle_drawer = True')
                    elif position[0] <= icon_triangle_end_x and position[
                            0] > icon_triangle_start_x and position[1] < icon_top_bar_height:
                        is_triangle_drawer = not is_triangle_drawer
                        is_rectangle_drawer = False
                        is_circle_drawer = False
                        is_rhombus_drawer = False
                        print('is_triangle_drawer = True')
                    elif position[0] <= icon_rhombus_end_x and position[
                            0] > icon_rhombus_start_x and position[1] < icon_top_bar_height:
                        is_rhombus_drawer = not is_rhombus_drawer
                        is_rectangle_drawer = False
                        is_circle_drawer = False
                        is_triangle_drawer = False
                        print('is_rhombus_drawer = True')
                    elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_red_color_start_y and position[1] < icon_red_color_end_y:
                        color = red
                        print('color = red')
                    elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_black_color_start_y and position[1] < icon_black_color_end_y:
                        color = black
                        print('color = black')
                    elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_blue_color_start_y and position[1] < icon_blue_color_end_y:
                        color = blue
                        print('color = blue')
                    elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_green_color_start_y and position[1] < icon_green_color_end_y:
                        color = green
                        print('color = green')
                    elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_yellow_color_start_y and position[1] < icon_yellow_color_end_y:
                        color = yellow
                        print('color = yellow')
                    elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_purple_color_start_y and position[1] < icon_purple_color_end_y:
                        color = purple
                        print('color = purple')
                    elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_pink_color_start_y and position[1] < icon_pink_color_end_y:
                        color = pink
                        print('color = pink')
                    elif position[0] >= dis_width - 70 and position[0] < dis_width - 70 + icon_color_shape_width and position[1] > icon_gray_color_start_y and position[1] < icon_gray_color_end_y:
                        color = gray
                        print('color = gray')
                    elif is_rectangle_drawer:
                        add_element_rectangle(
                            position[0], position[1], color)
                    elif is_circle_drawer:
                        add_element_circle(
                            position[0], position[1], color, 20)
                    elif is_triangle_drawer:
                        add_element_triangle(
                            position[0], position[1], color)
                    elif is_rhombus_drawer:
                        add_element_rhombus(
                            position[0], position[1], color)

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                print(position)

        screen.fill((255, 255, 255))

        draw_all_shapes(screen)
        draw_main_icons(screen)

        pygame.display.flip()

        clock.tick(60)


def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'yellow':
        color = (c2, c2, c1)
    elif color_mode == 'purple':
        color = (c2, c1, c2)
    elif color_mode == 'pink':
        color = (c2, c1, c2)
    elif color_mode == 'gray':
        color = (c2, c2, c2)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


main()

