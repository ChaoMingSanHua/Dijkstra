import cv2
import matplotlib.pyplot as plt
from AStar.a_star import AStarPlanner


def main():
    maze = cv2.imread("./maze.png", 0) / 255

    rows, cols = maze.shape
    ox, oy = [], []
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] < 1:
                ox.append(j)
                oy.append(i)

    sx = 1.0
    sy = 45.0
    gx = 254.0
    gy = 212.0
    grid_size = 1.0
    robot_radius = 2.5

    show_animation = True

    if show_animation:
        plt.plot(ox, oy, ".k")
        plt.plot(sx, sy, "or")
        plt.plot(gx, gy, "xr")
        plt.grid(True)
        plt.axis("equal")

    a_star = AStarPlanner(ox, oy, grid_size, robot_radius)
    rx, ry = a_star.planning(sx, sy, gx, gy)

    if show_animation:
        plt.plot(rx, ry, "-r")
        plt.pause(0.001)
        plt.show()


if __name__ == '__main__':
    main()
