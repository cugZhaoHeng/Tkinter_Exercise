# 引入tkinter类库
import tkinter

def func():
	print('The button1 is clicked')

# 调用Tk函数创建窗体对象
win = tkinter.Tk()

# 创建标题
win.title('创建窗口')

# 设置窗体大小，同时设置左上角的位置
win.geometry('400x400+200+200')

# 创建标签
'''
Label函数的属性包括：win：父窗体  text：显示的文本内容  
bg：背景色  font：字体  fg：字体颜色  wraplength：指定text文本中多宽之后换行
justify：设置换行后的对齐方式  
'''
label1 = tkinter.Label(win, text='标签1')
label1.pack()

# 创建按钮
button1 = tkinter.Button(win, text='按钮1', command=func)
button1.pack()

button2 = tkinter.Button(win, text='按钮2', command=lambda:print('The button2 is clicked'))
button2.pack()

button3 = tkinter.Button(win, text='按钮3', command=win.quit)
button3.pack()
# 创建一个需要显示的文本
e = tkinter.Variable()
e.set('abcde')

# 创建单行文本框
entry1 = tkinter.Entry(win, textvariable=e)
entry1.pack()
print(e.get())

# 创建密码框
entry2 = tkinter.Entry(win, show='*')
entry2.pack()



# 运行窗体对象
win.mainloop()
