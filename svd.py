
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button


def generate_matrix(n):
    while True:
        A = np.random.rand(n, n)
        if np.linalg.det(A) != 0:
            return A


def plot_svd_2d(U):
    circle = plt.Circle((0, 0), 1, color='blue', fill=False)
    fig, ax = plt.subplots()
    ax.add_artist(circle)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)

    angles = np.linspace(0, 2*np.pi, 100)
    x = np.cos(angles)
    y = np.sin(angles)
    unit_circle = np.vstack((x, y))

    transformed_points = np.dot(U, unit_circle)

    plt.scatter(transformed_points[0], transformed_points[1], color='red')
    plt.show()


def plot_svd_3d(U):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    sphere = ax.plot_wireframe(x, y, z, color='blue')

    phi = np.linspace(0, np.pi, 100)
    theta = np.linspace(0, 2*np.pi, 100)
    x = np.outer(np.sin(theta), np.cos(phi))
    y = np.outer(np.sin(theta), np.sin(phi))
    z = np.outer(np.cos(theta), np.ones_like(phi))
    unit_sphere = np.vstack((x.flatten(), y.flatten(), z.flatten()))

    transformed_points = np.dot(U, unit_sphere)

    ax.scatter(transformed_points[0], transformed_points[1], transformed_points[2], color='red')
    plt.show()


def plot_svd(n, U):
    if n == 2:
        plot_svd_2d(U)
    elif n == 3:
        plot_svd_3d(U)


def show_gui():
    def on_generate_matrix_click():
        n = int(matrix_size_entry.get())
        A = generate_matrix(n)
        U, _, _ = np.linalg.svd(A)
        plot_svd(n, U)

    root = Tk()
    root.title("SVD Geometry")
    root.geometry("300x150")

    matrix_size_label = Label(root, text="Dimensiunea matricii:")
    matrix_size_label.pack()

    matrix_size_entry = Entry(root)
    matrix_size_entry.pack()

    generate_matrix_button = Button(root, text="Generare matrice", command=on_generate_matrix_click)
    generate_matrix_button.pack()

    root.mainloop()


if __name__ == '__main__':
    show_gui()
