from tkinter import *
import shutil

root = Tk()
root.title("Flipping Tiles Game Maker")
root.geometry("400x330")
root.resizable(False, False)

# 차시 입력 프레임
lecture_num_frame = Frame(root)
lecture_num_frame.pack()

Label(lecture_num_frame, text="차시", padx=10).pack(side="left")
lecture_num = Entry(lecture_num_frame, width=20)
lecture_num.pack(side="right")


# 라벨 프레임
labelframe = Frame(root)
labelframe.pack()

Label(labelframe, text="단어", padx=80, pady=20).pack(side="left")
Label(labelframe, text="이미지 URL", padx=80, pady=20).pack(side="left")


# 입력 프레임
entryframe = Frame(root)
entryframe.pack(expand="true", fill="both", side="bottom")

# 그리드
t1 = Entry(entryframe, width=28)
t1.grid(column=0, row=0, ipady=3)
t2 = Entry(entryframe, width=28)
t2.grid(column=0, row=1, ipady=3)
t3 = Entry(entryframe, width=28)
t3.grid(column=0, row=2, ipady=3)
t4 = Entry(entryframe, width=28)
t4.grid(column=0, row=3, ipady=3)
t5 = Entry(entryframe, width=28)
t5.grid(column=0, row=4, ipady=3)
t6 = Entry(entryframe, width=28)
t6.grid(column=0, row=5, ipady=3)
t7 = Entry(entryframe, width=28)
t7.grid(column=0, row=6, ipady=3)
t8 = Entry(entryframe, width=28)
t8.grid(column=0, row=7, ipady=3)

i1 = Entry(entryframe, width=28)
i1.grid(column=1, row=0, ipady=3)
i2 = Entry(entryframe, width=28)
i2.grid(column=1, row=1, ipady=3)
i3 = Entry(entryframe, width=28)
i3.grid(column=1, row=2, ipady=3)
i4 = Entry(entryframe, width=28)
i4.grid(column=1, row=3, ipady=3)
i5 = Entry(entryframe, width=28)
i5.grid(column=1, row=4, ipady=3)
i6 = Entry(entryframe, width=28)
i6.grid(column=1, row=5, ipady=3)
i7 = Entry(entryframe, width=28)
i7.grid(column=1, row=6, ipady=3)
i8 = Entry(entryframe, width=28)
i8.grid(column=1, row=7, ipady=3)

    
# HTML 파일 생성
def make():
    shutil.copyfile("base.html", "1-{}.html".format(lecture_num.get()))
    i = []
    for item in [i1, i2, i3, i4, i5, i6, i7, i8]:
        i.append(item.get())
    t = []
    for item in [t1, t2, t3, t4, t5, t6, t7, t8]:
        t.append(item.get())

    with open("1-{}.html".format(lecture_num.get()), "a", encoding="utf8") as f:
        print("<script>", file=f)
        idx = 1
        for img in i:
            print("document.getElementById(\"i{0}\").src = \"{1}\";".format(idx, img), file=f)
            idx += 1
        idx = 1
        for text in t:
            print("document.getElementById(\"t{0}\").innerText = \"{1}\";".format(idx, text), file=f)
            idx += 1
        print("document.getElementById(\"title\").innerText = \"사회통합 1단계 {0}과 단어게임\";".format(lecture_num.get()), file=f)
        print("document.getElementById(\"h1\").innerText = \"{0}과 단어게임\";".format(lecture_num.get()), file=f)
        print("</script>", file=f)

make_button = Button(entryframe, text="만들기", pady=16, command=make)
make_button.grid(column=0, row=8, columnspan=2, sticky=N+W+E+S)
root.mainloop()