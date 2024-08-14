from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

ct = ColorThief("./Images/109.jpg")
# colot = (ct.get_color(quality=1))

# plt.imshow([[colot]])
# plt.show()


palette = ct.get_palette(color_count=5)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()

for color in palette:
    print(color)
    print(f"#{color[0]:02X}{color[1]:02X}{color[2]:02X}")