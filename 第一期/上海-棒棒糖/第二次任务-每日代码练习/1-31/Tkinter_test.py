from tkinter import *
import tkinter.messagebox as messagebox
#从Frame派生一个Application 类,这是所有 Widget 的父容器
#在 GUI 中，每个 Button、 Label、输入框等，都是一个 Widget,Frame则是可以容纳其他 Widget 的 Widget，所有的 Widget 组合起来就是一棵树
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        # pack()方法把 Widget 加入到父容器中，并实现布局。 pack()是最简单的布局， grid()可以实现更复杂的布局
        self.pack()
        self.createWidgets()
        #在 createWidgets()方法中，我们创建一个 Label 和一个 Button，当 Button被点击时，触发 self.quit()使程序退出
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello',command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)
#实例化 Application，并启动消息循环
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()