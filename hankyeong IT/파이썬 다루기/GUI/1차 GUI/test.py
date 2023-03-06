from tkinter import *

def btn_act( btn_pressed):
    if btn_pressed == '=':
        value = output.cget('text')
        try:
            result = eval(value)
            if result != '':
                output.config(text=result)
        except:
            output.config(text=value)
    elif btn_pressed == 'C':
        output.config(text='')
    else:
        value = output.cget('text')
        output.config(text=str(value) + btn_pressed)

root=Tk()
root.title('계산기')
root.configure(bg='pink')

output = Label(width=25,height=5, relief=FLAT, bd=1, justify=RIGHT,bg='pink')
output.grid(columnspan=4, row=0)

btn_e=Button(root, text='=')
btn_e.config(command=lambda button='=': btn_act(button))
btn_e.grid(row=5,column=2,columnspan=2,sticky=N+E+W+S, padx=3, pady=3)

btn_c=Button(root, text='C')
btn_c.config(command=lambda button='C': btn_act(button))
btn_c.grid(row=5,column=0,columnspan=2,sticky=N+E+W+S, padx=3, pady=3)

dit = [['7', '8', '9', '/'],
       ['4', '5', '6', '*'],
       ['1', '2', '3', '-'],
       ['0', '.', '<', '+']]

for i in range(0, len(dit)):
    for j in range(0, len(dit[i])):
        btn_label = dit[i][j]
        btns= Button(root, text=btn_label)
        btns.config(command=lambda button=btn_label: btn_act(button))
        btns.grid(column=j, row=i+1,sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()





# import os
# from tkinter import *
# from tkinter.scrolledtext import ScrolledText
#
# root=Tk()
# root.title('test')
# root.geometry('640x480')
#
# menu=Menu(root)
# root.config(menu=menu)
#
# file_name='mynote.txt'
# def open_file():
#     if os.path.isfile(file_name):
#         with open(file_name,'r',encoding='utf8') as file:
#             text.delete('1.0',END)
#             text.insert(END,file.read())
#
# def save_file():
#     with open(file_name,'w',encoding='utf8') as file:
#         file.write(text.get('1.0',END))
#
#
# menu_file=Menu(menu,tearoff=0)
# menu.add_cascade(label='파일',menu=menu_file)
# menu_file.add_command(label='열기',command=open_file)
# menu_file.add_command(label='저장',command=save_file)
# menu_file.add_separator()
# menu_file.add_command(label='끝내기')
#
#
# menu_edit=Menu(menu, tearoff=0)
# menu.add_cascade(label='편집',menu=menu_file)
#
# menu_temp=Menu(menu, tearoff=0)
# menu.add_cascade(label='서식',menu=menu_file)
#
# menu_view=Menu(menu, tearoff=0)
# menu.add_cascade(label='보기',menu=menu_file)
#
# menu_help=Menu(menu, tearoff=0)
# menu.add_cascade(label='도움말',menu=menu_file)
#
# text=ScrolledText(root,width=50,height=50)
# text.pack(fill=BOTH,side='right',expand=True)
#
# root.mainloop()





# from tkinter import *
#
# root=Tk()
# root.title('test')
# root.geometry('640x480')
#
# # 첫번째줄 만들기
# btn_f16=Button(root,text='F16',width=5,height=2)
# btn_f17=Button(root,text='F17',width=5,height=2)
# btn_f18=Button(root,text='F18',width=5,height=2)
# btn_f19=Button(root,text='F19',width=5,height=2)
#
# btn_f16.grid(row=0,column=0,sticky=N+E+W+S,padx=3,pady=3)
# btn_f17.grid(row=0,column=1,sticky=N+E+W+S,padx=3,pady=3)
# btn_f18.grid(row=0,column=2,sticky=N+E+W+S,padx=3,pady=3)
# btn_f19.grid(row=0,column=3,sticky=N+E+W+S,padx=3,pady=3)
#
# # 두번째 줄 만들기
# btn_7=Button(root,text='7',width=5,height=2)
# btn_8=Button(root,text='8',width=5,height=2)
# btn_9=Button(root,text='9',width=5,height=2)
# btn_plus=Button(root,text='+',width=5,height=2)
#
# btn_7.grid(row=1,column=0,sticky=N+E+W+S,padx=3,pady=3)
# btn_8.grid(row=1,column=1,sticky=N+E+W+S,padx=3,pady=3)
# btn_9.grid(row=1,column=2,sticky=N+E+W+S,padx=3,pady=3)
# btn_plus.grid(row=1,column=3,sticky=N+E+W+S,padx=3,pady=3)
#
# # 세번째 줄 만들기
# btn_4=Button(root,text='4',width=5,height=2)
# btn_5=Button(root,text='5',width=5,height=2)
# btn_6=Button(root,text='6',width=5,height=2)
# btn_minus=Button(root,text='-',width=5,height=2)
#
# btn_4.grid(row=2,column=0,sticky=N+E+W+S,padx=3,pady=3)
# btn_5.grid(row=2,column=1,sticky=N+E+W+S,padx=3,pady=3)
# btn_6.grid(row=2,column=2,sticky=N+E+W+S,padx=3,pady=3)
# btn_minus.grid(row=2,column=3,sticky=N+E+W+S,padx=3,pady=3)
#
# # 네번째 줄 만들기
# btn_1=Button(root,text='1',width=5,height=2)
# btn_2=Button(root,text='2',width=5,height=2)
# btn_3=Button(root,text='3',width=5,height=2)
# btn_enter=Button(root,text='enter',)
#
# btn_1.grid(row=3,column=0,sticky=N+E+W+S,padx=3,pady=3)
# btn_2.grid(row=3,column=1,sticky=N+E+W+S,padx=3,pady=3)
# btn_3.grid(row=3,column=2,sticky=N+E+W+S,padx=3,pady=3)
# btn_enter.grid(row=3,column=3, rowspan=2,sticky=N+E+W+S, padx=3, pady=3)
#
# # 다섯번째 줄 만들기
# btn_0=Button(root,text='0',width=5,height=2)
# btn_point=Button(root,text='.',width=5,height=2)
#
# btn_0.grid(row=4,column=0,columnspan=2,sticky=N+E+W+S,padx=3,pady=3)
# btn_point.grid(row=4,column=2,sticky=N+E+W+S,padx=3,pady=3)
#
# root.mainloop()





# from tkinter import *
# root=Tk()
# root.title('test')
# root.geometry('640x480')
#
# # 프레임 생성
# frame=Frame(root)
# frame.pack()
#
# # 스크롤바 만들기
# scrollbar=Scrollbar(frame)
# scrollbar.pack(side='right',fill='y')
#
# # 리스트 박스 만들기
# listbox=Listbox(frame,selectmode='extended',yscrollcommand=scrollbar.set)
# for i in range(1,32):
#     listbox.insert(END,str(i)+'일')
# listbox.pack(side='left')
# scrollbar.config(command=listbox.yview())
#
# root.mainloop()





# from tkinter import *
# root=Tk()
# root.title('test')
# root.geometry('640x480')
#
# Label(root,text='메뉴를 선택해 주세요').pack(side='top')
# Button(root,text='주문하기').pack(side='bottom')
#
# # 프레임1
# frame1=Frame(root,bd=1,relief='solid')
# frame1.pack(side='left',fill='both',expand=True)
# Button(frame1,text='햄버거').pack()
# Button(frame1,text='불고기버거').pack()
# Button(frame1,text='새우버거').pack()
#
#
# #프레임 2
# frame2=LabelFrame(root,text='음료')
# frame2.pack(side='right',fill='both',expand=True)
# Button(frame2,text='아이스아메리카노').pack()
# Button(frame2,text='콜라').pack()
#
# root.mainloop()





# import tkinter.messagebox as msgbox
# from tkinter import *
#
# root=Tk()
# root.title('test')
# root.geometry('640x480')
#
# def info():
#     msgbox.showinfo('알림','주문이 완료되었습니다')
# def warning():
#     msgbox.showwarning('경고','결재 오류가 발생했습니다')
# def error():
#     msgbox.showerror('오류','결재 오류가 발생했습니다')
# def okcancel():
#     msgbox.askokcancel('확인/취소','대기시간이 10분이상입니다.\n기다리겠습니까?')
# def retrycancel():
#     msgbox.askretrycancel('재시도/취소','일시오류입니다.\n다시 진행하시겠습니까?')
# def yesno():
#     response=msgbox.askyesno(title=None, message='결제 계속 진행할까요?')
#     if response==1:
#         print('감사합니다, 결재 진행합니다')
#     else:
#         print('감사합니다. 결재 취소됬습니다.\n다음에 또 오세요!')
#
# btn1=Button(root,text='알림',command=info).pack()
# btn2=Button(root,text='경고',command=warning).pack()
# btn3=Button(root,text='오류',command=error).pack()
# btn4=Button(root,text='확인/취소',command=okcancel).pack()
# btn5=Button(root,text='재시도/취소',command=retrycancel).pack()
# btn6=Button(root,text='예/아니오',command=yesno).pack()
#
# root.mainloop()






# from tkinter import *
#
# root=Tk()
# root.title('test')
# root.geometry('640x480')
#
# #파일 메뉴탭을 만들기
# def new_cmd():
#     print('새 프로젝트를 선택했습니다')
# menu=Menu(root)
# menu_file=Menu(menu,tearoff=False)
# menu.add_cascade(label='File',menu=menu_file)
# menu_file.add_command(label='New Project..')
# menu_file.add_command(label='New File')
# menu_file.add_command(label='Restart',state='disabled')
# menu_file.add_separator()
# menu_file.add_command(label='End')
#
#
# # 메뉴 편집탭 만들기
# menu_edit=Menu(menu)
# menu.add_cascade(label='edit',menu=menu_edit)
#
# # 메뉴 언어탭 만들기
# menu_lang=Menu(menu,tearoff=0)
# menu.add_cascade(label='language',menu=menu_lang)
# menu_lang.add_radiobutton(label='Java')
# menu_lang.add_radiobutton(label='Python')
# menu_lang.add_radiobutton(label='C++')
#
# root.config(menu=menu)
#
# root.mainloop()





# import tkinter.ttk as ttk
# from tkinter import *
# import time
#
# root=Tk()
# root.title('test')
# root.geometry('640x480')
#
# #프로그래스 바 만들기
# pbar_value=DoubleVar()
# pbar=ttk.Progressbar(root,maximum=100,length=150,mode='determinate',variable=pbar_value)
# pbar.pack()
#
# #중지버튼
# def btncmd():
#     for i in range(1,101):
#         time.sleep(0.01)
#         pbar_value.set(i)
#         pbar.update()
#         print(pbar_value.get())
# btn=Button(root,text='시작',command=btncmd)
# btn.pack()
#
#
# root.mainloop()




# from tkinter import *
# import tkinter.ttk as ttk
#
# root=Tk()
# root.title('test')
# root.geometry('640x480')
#
# cmb1_value=[str(i)+'월' for i in range(1,13)]
# cmb1=ttk.Combobox(root,height=5, values=cmb1_value)
# cmb1.set('월 선택')
# cmb1.pack()
#
# vlue_days=[str(i)+'일' for i in range(1,32)] #1일~31일까지 지정
# combox2=ttk.Combobox(root, height=10, values=vlue_days, state='readonly')
# combox2.set('1일') #기본값 설정
# combox2.pack()
#
# cmb2=ttk.Combobox(root,height=10)
#
# root.mainloop()





# from tkinter import *
#
# root=Tk()
# root.title('text')
# root.geometry('640x480')
# # 메뉴 가격표
# main_menue_list=['햄버거','불고기버거','치킨버거']
# main_menue_price=[4500,5000,6000]
# # label 만들기
# Label(root,text='메뉴를 선택해 주세요').pack()
# # radio 버튼 만들기
# menu_var=IntVar()
# opt1=Radiobutton(root,text='햄버거',value=0,variable=menu_var)
# opt1.pack()
# opt1.select()
# opt2=Radiobutton(root,text='불고기버거',value=1,variable=menu_var)
# opt2.pack()
# opt3=Radiobutton(root,text='치킨버거',value=2,variable=menu_var)
# opt3.pack()
#
# main_menue_list1=['아케리카노','콜라']
# main_menue_price1=[1500,1200]
#
# Label(root,text='음료를 선택해 주세요').pack()
# # radio 버튼 만들기
# menu_var1=IntVar()
# op1=Radiobutton(root,text='아메리카노',value=0,variable=menu_var1)
# op1.pack()
# op1.select()
# op2=Radiobutton(root,text='콜라',value=1,variable=menu_var1)
# op2.pack()
#
# def btncmd():
#     global n
#     n=menu_var.get()
#     m=menu_var1.get()
#     print('선택합 메뉴는: ','메뉴명:',main_menue_list[n],'가격:',main_menue_price[n])
#     print('선택합 음료는: ','메뉴명:',main_menue_list1[m],'가격:',main_menue_price1[m])
#     print('총가격은',main_menue_price[n] + main_menue_price1[m],'원 입니다')
# btn=Button(root,text='주문',command=btncmd)
# btn.pack()
#
# root.mainloop()





# from tkinter import *
#
# root=Tk()
# root.title('text')
# root.geometry('640x480')
#
# chkvar=IntVar()
# chkbox=Checkbutton(root,text='오늘 하루동안 그만보기',variable=chkvar)
# chkbox.pack()
#
# chkvar1=IntVar()
# chkbox=Checkbutton(root,text='일주일 동안 그만보기',variable=chkvar1)
# chkbox.pack()
#
# def btncmd():
#     print(chkvar.get())
#     print(chkvar1.get())
#
# btn=Button(root,text='클릭',command=btncmd)
# btn.pack()
#
# root.mainloop()




# from tkinter import *
#
# class App:
#     def __init__(self):
#         self.items=['국어','영어','수학','과학']
#         self.root=Tk()
#         self.root.title('test')
#         self.root.geometry('300x200')
#
#         #listbox 생성
#         self.listbox=Listbox(self.root,selectmode='extended', height=0)
#         for item in self.items:
#             self.listbox.insert(END,item)
#         #button 생성
#         self.btn=Button(self.root, text='삭제', command=self.delete)
#
#         self.listbox.pack()
#         self.btn.pack()
#
#         self.root.mainloop()
#
#     def delete(self):
#         self.selection =self.listbox.curselection()
#         self.n=self.selection[0]
#         for i in range(len(self.selection)):
#             self.listbox.delete(self.n)
#             self.listbox.update() # for문 동작할때마다 GUI가 업데이트 됨
#
#
# if __name__=='__main__':
#     App()




# import tkinter
#
# window=tkinter.Tk()
# window.title('test')
# window.geometry('640x480')
#
# # list box 만들기
# listbox=tkinter.Listbox(window,selectmode='extended',height=0)
# listbox.pack()
# listbox.insert(0,'항목1')
# listbox.insert(1,'항목2')
# listbox.insert(tkinter.END,'항목3')
# listbox.insert(tkinter.END,'항목4')
# listbox.insert(tkinter.END,'항목5')
#
# def btncmd():
#     print('총 항목 개수:',listbox.size())
#     print('첫번째 항목 명칭:', listbox.get(0))
#     print('1~3번까지 항목 가져오기:',listbox.get(0,2))
#     print('모든 항목 이름은: ',listbox.get(0,tkinter.END))
#     print('사용자가 선택한 항목 index:',listbox.curselection())
#     print('사용자가 선택한 항목이름:',[listbox.get(i) for i in listbox.curselection()])
#
# btn=tkinter.Button(window,text='클릭',command=btncmd)
# btn.pack()
#
#
# window.mainloop()




# import tkinter
# import time
#
# window=tkinter.Tk()
# window.title('test')
# window.geometry('640x480')
#
# # list box 만들기
# listbox=tkinter.Listbox(window,selectmode='extended',height=0)
# listbox.pack()
# listbox.insert(0,'항목1')
# listbox.insert(1,'항목2')
# listbox.insert(tkinter.END,'항목3')
# listbox.insert(tkinter.END,'항목4')
# listbox.insert(tkinter.END,'항목5')
#
# time.sleep(3)  # 창 제체가 늦게 떳씀
# # listbox.delete(0,2)    listbox 0~2를 삭제하기
#
# window.mainloop()



# import tkinter
# # from tkinter import *
# window=tkinter.Tk()
# window.title('text')
# window.geometry('640x480')
#
# #text box 만들기
# text=tkinter.Text(window,width=30,height=5)
# text.pack()
#
# text.insert('current','글자를 입력하세요\n')
# text.insert('current','안녕하세요,홍길동입니다')
#
# e=tkinter.Entry(window,width=30,)
# e.pack()
# e.insert(0,'글자 한줄만 입력해주세요')
#
# def btncmd():
#     print(text.get('1.0',tkinter.END))
#     print(e.get())
#
#
# btn=tkinter.Button(window,text='클릭',command=btncmd)
# btn.pack()
#
# window.mainloop()



# import tkinter
# class App:
#     def __init__(self):
#         self.window = tkinter.Tk()
#         self.window.title('test')
#         self.window.geometry('640x480')
#
#         self.lbl=tkinter.Label(self.window,text='레이블 예제')
#         self.lbl.pack()
#         self.btn=tkinter.Button(self.window,text='레이블 읽기',
#                                 command=self.labeltxt)
#         self.btn.pack()
#
#         self.window.mainloop()
#
#     def labeltxt(self):
#         print(self.lbl['text'])
#
# if __name__ == '__main__':
#     App()





# import tkinter
# window=tkinter.Tk()
# window.title('test')
# window.geometry('640x480')
#
# cnt=0
# def click():
#     global cnt
#     cnt+=1
#     lbl.config(text='버튼 클릭 횟수:'+str(cnt))
#
# def reset():
#     lbl.config(text='리셋되어짐: '+str(0))
#
# lbl=tkinter.Label(window,text='아직 클릭되지 않았음')
# lbl.pack()
# btn1=tkinter.Button(window,text='증가',command=click)
# btn1.pack()
# btn2=tkinter.Button(window,text='리셋',command=reset)
# btn2.pack()
#
# window.mainloop()




# import tkinter
# window=tkinter.Tk()
# window.title('test')
# window.geometry('640x480')
#
# cnt=0
# def change():
#     global cnt
#     cnt += 1
#     lbl.config(text=str(cnt))
#
# lbl=tkinter.Label(window,text='0')
# lbl.pack()
# btn=tkinter.Button(window,text='클릭',command=change, repeatinterval=100)
# btn.pack()
#
#
# window.mainloop()




# import tkinter
# window=tkinter.Tk()
# window.title('test')
# window.geometry('640x480')
#
# photo=tkinter.PhotoImage(file='./img01.png')
# btn=tkinter.Button(window,image=photo).pack()
#
#
# window.mainloop()





# import tkinter
#
# window=tkinter.Tk()
# window.title('test')
# window.geometry('640x480')
#
# photo=tkinter.PhotoImage(file='./img01.png')
#
# btn1=tkinter.Button(window,text='버튼1',padx=10,pady=5).pack()
# btn2=tkinter.Button(window,text='버튼2',padx=5,pady=10).pack()
# btn3=tkinter.Button(window,text='버튼3',padx=10,pady=5,width=10,height=5).pack()
# btn4=tkinter.Button(window,image=photo,width=4,height=5,bg='red',fg='yellow').pack()
#
# window.mainloop()




# import tkinter
# window=tkinter.Tk()
# window.title('test')
# window.geometry('640x480')
#
# def change():
#     lbl1.config(text='또 만나요~')
#     global photo2
#     photo2=tkinter.PhotoImage(file='./img02.png')
#     lbl2.config(image=photo2)
#
# # label1 만들기
# lbl1=tkinter.Label(window,text='안녕하세요')
# lbl1.pack()
#
# # label2 만들기
# photo=tkinter.PhotoImage(file='./img01.png')
# lbl2=tkinter.Label(window,image=photo)
# lbl2.pack()
#
# btn=tkinter.Button(window,text='클릭',command=change)
# btn.pack()
#
# window.mainloop()





# import tkinter
# window=tkinter.Tk()
# window.title('test')
# window.geometry('640x480')
#
# def change():
#     lbl.config(text='클릭했습니다!')
#
# #  레이블 만들기
# lbl=tkinter.Label(window,text='안녕하세요')
# lbl.pack()
#
# btn=tkinter.Button(window,text='클릭',command=change)
# btn.pack()
#
# window.mainloop()