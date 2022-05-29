import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()

root.title("파이썬 컴파일 프로그램")
root.geometry("300x200")

# list_file = []
def selectfile():
    root.filename = filedialog.askopenfilename(initialdir='', title='파일 선택', filetypes=(
        ("파이썬 파일(*.py)", "*.py"), ('All Files', '*.*')))
    if root.filename == '':
        messagebox.showerror("파일이 선택되지 않음!", "파일이 선택되어야 합니다!")
    l1.configure(text=f"파일 이름:{root.filename}")

l1 = Label(root, text="파일 선택 ->")
l1.pack(side=LEFT)


def startcompile():
    if root.filename == '':
        messagebox.showerror("파일이 선택되지 않음!", "파일이 선택되어야 합니다!")
    else:
        os.system(f"Scripts\pyinstaller.exe -w -F {root.filename}")
        messagebox.showinfo("컴파일 완료!", "컴파일된 파일은 파이썬 컴파일러가 설치된 경로(dist폴더 안)에 있습니다!")


b1 = Button(root, text="파일 선택", command=selectfile)
b1.pack(side=RIGHT)

b2 = Button(root, text="컴파일 시작", command=startcompile)
b2.pack()

root.mainloop()
