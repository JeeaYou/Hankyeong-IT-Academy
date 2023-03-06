from





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




# from tkinter import *   미완성
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