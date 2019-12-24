import graphics as gr


def main():
    window = gr.GraphWin('My Image', 600, 600)
    draw_image(window)

    window.getMouse()


def draw_background(window):
    earth = gr.Rectangle(
        gr.Point(0, window.height // 2),
        gr.Point(window.width - 1, window.height - 1),
    )
    earth.setFill('green')
    earth.draw(window)
    scy = gr.Rectangle(
        gr.Point(0,0),
        gr.Point(window.width - 1, window.height // 2),
    )
    scy.setFill('cyan')
    scy.draw(window)


def draw_house_foundation(window, foundational_height):
    foundational = gr.Rectangle(
        gr.Point(20, window.height - foundational_height),
        gr.Point(window.width - 20, window.height),
    )
    foundational.setFill('black')
    foundational.draw(window)


def draw_house_walls(window, walls_height, walls_width, foundational_height):
    walls = gr.Rectangle(
        gr.Point(25, window.height - walls_height - foundational_height),
        gr.Point(window.width - 25, window.height - foundational_height),
    )
    walls.setFill('red')
    walls.draw(window)


def draw_house_roof(window, roof_height, walls_width):
    pass


def draw_house(window, x, y, width, height):
    foundational_height = height // 8
    walls_height = height // 2
    walls_width = 7 * width // 8
    roof_height = height - walls_height - foundational_height

    draw_house_foundation(window, foundational_height)
    draw_house_walls(window, walls_height, walls_width, foundational_height)
    draw_house_roof(window, roof_height, walls_width)


def draw_image(window):
    x, y = window.width // 2, window.height * 2 // 3
    width = window.width // 3
    height = window.height * 4 // 3

    draw_background(window)
    draw_house(window, x, y, width, height)

if __name__ == '__main__':
    main()