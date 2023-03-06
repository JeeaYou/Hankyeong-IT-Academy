import tkinter
windows = tkinter.Tk()
windows.title('text')
windows.geometry('640x480')

photo=tkinter.PhotoImage(file='./')
lbl=tkinter.Label(windows,image=)

windows.mainloop()




# import tkinter
# windows=tkinter.Tk()
# windows.title('test')
# windows.geometry('640x480')
#
# lbl=tkinter.Label(windows,text='안녕하세요!')
# lbl.pack()
#
# windows.mainloop()



# import tkinter
# windows= tkinter.Tk()
# windows.title('지금은 연습중')
# windows.geometry('640x480')
# # windows.resizable(False,True)   #크기조정 고정유무
#
# windows.mainloop()




'''
# -----------------------------------------------------------
# Tkinter GUI
# https://076923.github.io/posts/Python-tkinter-1/
# -----------------------------------------------------------

import tkinter

window=tkinter.Tk()

window.title('test')
window.geometry('640x640')
window.resizable(True,False)

label=tkinter.Label(window,text='안녕하세요')
label.pack()

window.mainloop()
'''