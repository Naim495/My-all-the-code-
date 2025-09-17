import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 3D Figure
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

# ---------- Black Hole (center sphere = black) ----------
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)
x = 0.3 * np.outer(np.cos(u), np.sin(v))
y = 0.3 * np.outer(np.sin(u), np.sin(v))
z = 0.3 * np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(x, y, z, color="black")

# ---------- Photon Ring (thin glowing torus) ----------
theta = np.linspace(0, 2 * np.pi, 200)
phi = np.linspace(0, 2 * np.pi, 200)
theta, phi = np.meshgrid(theta, phi)

R, r = 0.6, 0.05  # Torus major/minor radius
X = (R + r * np.cos(phi)) * np.cos(theta)
Y = (R + r * np.cos(phi)) * np.sin(theta)
Z = r * np.sin(phi)

ax.plot_surface(X, Y, Z, color="yellow", alpha=0.9, linewidth=0)

# ---------- Accretion Disk (wider glowing band) ----------
R, r = 1.2, 0.3
X = (R + r * np.cos(phi)) * np.cos(theta)
Y = (R + r * np.cos(phi)) * np.sin(theta)
Z = 0.15 * np.sin(phi)  # Flatten for disk effect

ax.plot_surface(X, Y, Z, color="orange", alpha=0.5, linewidth=0)

# ---------- A 3D Star (sphere) ----------
xs = 2.0 * np.outer(np.cos(u), np.sin(v))
ys = 2.0 * np.outer(np.sin(u), np.sin(v))
zs = 2.0 * np.outer(np.ones_like(u), np.cos(v))
ax.plot_surface(xs, ys, zs, color="white", alpha=0.9)

# ---------- Settings ----------
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)
ax.set_facecolor("black")
ax.axis("off")

plt.title("3D Black Hole with Photon Ring, Accretion Disk & Star", color="white")
plt.show()


# Camera
yaw, pitch = 0.0, 0.0
distance = 8.0
lastX, lastY = 400, 300
left_mouse_pressed = False

def mouse_button_callback(window, button, action, mods):
    global left_mouse_pressed
    if button == glfw.MOUSE_BUTTON_LEFT:
        if action == glfw.PRESS:
            left_mouse_pressed = True
        elif action == glfw.RELEASE:
            left_mouse_pressed = False

def cursor_position_callback(window, xpos, ypos):
    global yaw, pitch, lastX, lastY, left_mouse_pressed
    if left_mouse_pressed:
        dx = xpos - lastX
        dy = ypos - lastY
        yaw += dx * 0.3
        pitch += dy * 0.3
    lastX, lastY = xpos, ypos

def scroll_callback(window, xoffset, yoffset):
    global distance
    distance -= yoffset * 0.5
    if distance < 2.0:
        distance = 2.0
    if distance > 30.0:
        distance = 30.0

def init_gl(width, height):
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND)                # blending চালু
    glBlendFunc(GL_SRC_ALPHA, GL_ONE) # additive blending (glow এর জন্য)
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, width / height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_black_hole():
    glColor3f(0.0, 0.0, 0.0)  # ব্ল্যাক হোল আসল কালো
    quad = gluNewQuadric()
    gluSphere(quad, 2.0, 64, 64)

def draw_photon_ring():
    glBegin(GL_TRIANGLE_STRIP)
    segments = 200
    inner_radius = 2.1
    outer_radius = 2.6
    for i in range(segments + 1):
        angle = 2 * math.pi * i / segments
        x = math.cos(angle)
        y = math.sin(angle)

        # Outer edge (glowing, transparent)
        glColor4f(1.0, 0.8, 0.0, 0.0)  # বাইরের প্রান্ত ফেড আউট
        glVertex3f(x * outer_radius, y * outer_radius, 0.0)

        # Inner edge (bright)
        glColor4f(1.0, 0.8, 0.0, 1.0)  # ভেতরের রিং উজ্জ্বল
        glVertex3f(x * inner_radius, y * inner_radius, 0.0)
    glEnd()

def draw_stars():
    np.random.seed(0)
    glBegin(GL_POINTS)
    for _ in range(1000):
        x, y, z = np.random.uniform(-50, 50, 3)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f(x, y, z)
    glEnd()

def main():
    if not glfw.init():
        return
    window = glfw.create_window(800, 600, "Black Hole with Photon Ring", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_cursor_pos_callback(window, cursor_position_callback)
    glfw.set_scroll_callback(window, scroll_callback)

    width, height = glfw.get_framebuffer_size(window)
    init_gl(width, height)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Camera
        glLoadIdentity()
        eyex = distance * math.sin(math.radians(yaw)) * math.cos(math.radians(pitch))
        eyey = distance * math.sin(math.radians(pitch))
        eyez = distance * math.cos(math.radians(yaw)) * math.cos(math.radians(pitch))
        gluLookAt(eyex, eyey, eyez, 0, 0, 0, 0, 1, 0)

        # Scene
        draw_stars()
        draw_black_hole()
        draw_photon_ring()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
