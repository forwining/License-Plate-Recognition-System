import tkinter as tk
from tkinter import filedialog
import method1
from PIL import Image, ImageTk

root = tk.Tk()
root.title('车牌识别')
root.geometry("350x220+550+150")


# 文本框

def open():
    try:
        global file_path
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            y = int(200 * image.height / image.width)
            size = (200, y)
            image1 = image.resize(size)  #照片缩放
            photo = ImageTk.PhotoImage(image1)

            # 清除旧图片
            for widget in root.winfo_children():
                if isinstance(widget, tk.Label):
                    widget.destroy()

            label = tk.Label(root, image=photo)
            label.image = photo
            label.grid(row=0, column=1)
            # 调整窗口大小以适应图片
            # root.geometry("{}x{}".format(image.width, image.height))
    except AttributeError:
        print("No image selected.")


def word():
    try:
        outcome = method1.plt_identify(file_path)
        outcome = '车牌号为：' + outcome
        label = tk.Label(root, text=outcome)
        label.grid(row=1, column=1)
        print(outcome)
    except AttributeError:
        print("No image selected.")


btn1 = tk.Button(root, command=open, padx=10, pady=5)
btn1["text"] = "选择照片"
btn1.grid(row=0, column=0, pady=60, padx=10)
btn2 = tk.Button(root, command=word, padx=10, pady=5)
btn2["text"] = "开始识别"
btn2.grid(row=1, column=0, padx=10)
root.mainloop()
