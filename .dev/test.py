import matplotlib.pyplot as plt
import tkinter as tk

plt.switch_backend("TkAgg")

print(plt.__file__)

plt.figure(figsize=(2, 2))
plt.plot(range(50))

# print(canvas.size(tk.Canvas))
plt.show()
