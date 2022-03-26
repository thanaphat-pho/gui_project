from tkinter import *
from tkinter import messagebox

##################
# STEP 1  ประกาศค่า
#################
#ประกาศ Tk
cake =Tk()
#เปลี่ยน 20 เป็น 0 **จุดที่แก้ล่าสุด**
result = 0
#ประกาศค่า name_list เป็นค่าว่าง
name_list = ""
#ประกาศชื่อโปรแกรม furniture
cake.title('cake')
#ประกาศค่า total ให้อยู่ในรูปแบบข้อความและตั้งค่าให้เป็น "ราคารวม 0 บาท"
total = StringVar()
total.set("ราคารวม 0 บาท")

#ประกาศค่า list_var ให้อยู่ในรูปแบบข้อความ
list_var = StringVar()
list_var.set("")


##################
# STEP 4  ประกาศค่า
#################
#สร้างคำสั่งใน method ที่ชื่อว่า sum เพื่อใช้คำนวณ
def sum(e):
    #ดึงค่าจาก result, name_list
    global result, name_list
    #นำ e
    name = e.widget["text"]


    #สร้างเงื่อนไขโดยให้ name มีค่าเท่ากับ "ชื่อสินค้า" โดยที่ result นั้นมีค่าเป็น Int ที่มีค่าเท่ากับ 0
    #นำมาบวกกับราคาที่ตั้งไว้และใส่ไว้ที่ result
    #นำ result มาใส่ใน total1_st โดยให้อยู่ในรูปแบบ String
    #set total ไว้เป็นราคาที่บวกกับสินค้าอื่น ๆ
    #นำข้อความรายการสินค้ามาใส่ใน name_list
    #set list_var ไว้เป็นรายการที่สั่งซื้อทั้งหมด
    if name == "เค้กเลเยอร์วานิลลา":
        result = int(result + 695)
        total1_st = str(result)
        total.set("ราคารวม " + total1_st + " บาท")
        name_list = name_list + "เค้กเลเยอร์วานิลลา 695 บาท \n"
        list_var.set(name_list)

    elif name == "เค้กแบล็คฟอเรสต์":
        result = int(result + 775)
        total1_st = str(result)
        total.set("ราคารวม " + total1_st + " บาท")
        name_list = name_list + "เค้กแบล็คฟอเรสต์ 775 บาท \n"
        list_var.set(name_list)
    elif name == "เค้กเลเยอร์ใบเตย":
        result = int(result + 695)
        total1_st = str(result)
        total.set("ราคารวม " + total1_st + " บาท")
        name_list = name_list + "เค้กเลเยอร์ใบเตย 695 บาท \n"
        list_var.set(name_list)
    elif name == "เค้กบัทเทอร์วานิลลา":
        result = int(result + 735)
        total1_st = str(result)
        total.set("ราคารวม " + total1_st + " บาท")
        name_list = name_list + "เค้กบัทเทอร์วานิลลา 735 บาท \n"
        list_var.set(name_list)
    elif name == "เค้กช็อกโกแลตฟัดจ์1.5":
        result = int(result + 680)
        total1_st = str(result)
        total.set("ราคารวม " + total1_st + " บาท")
        name_list = name_list + "เค้กช็อกโกแลตฟัดจ์ 1.5 ปอนด์ 680 บาท \n"
        list_var.set(name_list)

    elif name == "ฮอกไกโดมิลด์เค้ก":
        result = int(result + 465)
        total1_st = str(result)
        total.set("ราคารวม " + total1_st + " บาท")
        name_list = name_list + "ฮอกไกโดมิลด์เค้ก 465 บาท \n"
        list_var.set(name_list)
    elif name == "เค้กสปันจ์เนยวานิลลา":
        result = int(result + 435)
        total1_st = str(result)
        total.set("ราคารวม " + total1_st + " บาท")
        name_list = name_list + "เค้กสปันจ์เนยวานิลลา 435 บาท \n"
        list_var.set(name_list)
    elif name == "ฟรุตเค้ก":
        result = int(result + 765)
        total1_st = str(result)
        total.set("ราคารวม " + total1_st + " บาท")
        name_list = name_list + "ฟรุตเค้ก 765 บาท \n"
        list_var.set(name_list)
    elif name == "เค้กช็อกโกแลตฟัดจ์ 1.0":
        result = int(result + 465)
        total1_st = str(result)
        total.set("ราคารวม " + total1_st + " บาท")
        name_list = name_list + "เค้กช็อกโกแลตฟัดจ์ 465 บาท \n"
        list_var.set(name_list)
    elif name == "เค้กชิฟฟ่อนกาแฟ":
        result = int(result + 465)
        total1_st = str(result)
        total.set("ราคารวม " + total1_st + " บาท")
        name_list = name_list + "เค้กชิฟฟ่อนกาแฟ 465 บาท \n"
        list_var.set(name_list)







#คำสั่งใช้ลบรายการสั่งซท้อทั้งหมด
def Clear():
    global btn_clear, name_list, total, result
    result = 0
    name_list = ""
    total1_st = "ราคารวม 0 บาท"
    list_var.set(str(name_list))
    total.set((total1_st))

#คำสั่ง ยืนยัน
def Ok():
    global list_var, lbl_total
    Thank = StringVar()
    money = total.get()
    Thank.set("ขอบคุณสำหรับลูกค้าที่อุดหนุนร้านของ SuperCake")
    Thankyou = Thank.get()
    total_message = "ราคารวมทั้งหมด : " + money
    messagebox.showinfo("ร้าน SuperCake", total_message)
    messagebox.showinfo("ร้าน SuperCake", Thankyou)
command = Ok

##################
# STEP 2  ประกาศ frame และจัดขนาด Frame
#################
#กำหนด frame ไว้ทั้งหมด 7 frame
frame1 = Frame(cake)
frame2 = Frame(cake)
frame3 = Frame(cake)
frame4 = Frame(cake)
frame5 = Frame(cake)
frame6 = Frame(cake)



frame1.pack(fill="both", side="top", expand="true")
frame2.pack(fill="both", side="top", expand="true")
frame3.pack(fill="both", side="top", expand="true")
frame4.pack(fill="both", side="top", expand="true")
frame5.pack(fill="both", side="top", expand="true")
frame6.pack(fill="both", side="top", expand="true")



#นำไฟล์รูปภาพ cake1-10.png ร้านค้ามาใส่ใน table1 โดยใช้ PhotoImage
photo_cake1 = PhotoImage(file="cake1.png")
photo_cake2 = PhotoImage(file="cake2.png")
photo_cake3 = PhotoImage(file="cake3.png")
photo_cake4 = PhotoImage(file="cake4.png")
photo_cake5 = PhotoImage(file="cake5.png")
photo_cake6 = PhotoImage(file="cake6.png")
photo_cake7 = PhotoImage(file="cake7.png")
photo_cake8 = PhotoImage(file="cake8.png")
photo_cake9 = PhotoImage(file="cake9.png")
photo_cake10 = PhotoImage(file="cake10.png")









#-----------------------------------------------------------------------------------------------------#

#สร้างปุ่มเลือกโต๊ะโดยส่งไปยัง Table1
btn_cake1 = Button(frame2, text="เค้กเลเยอร์วานิลลา", image = photo_cake1,compound="bottom", border="0")
btn_cake2 = Button(frame2, text="เค้กแบล็คฟอเรสต์", image = photo_cake2,compound="bottom", border="0")
btn_cake3 = Button(frame2, text="เค้กเลเยอร์ใบเตย", image = photo_cake3,compound="bottom", border="0")
btn_cake4 = Button(frame2, text="เค้กบัทเทอร์วานิลลา", image = photo_cake4,compound="bottom", border="0")
btn_cake5 = Button(frame2, text="เค้กช็อกโกแลตฟัดจ์1.5", image = photo_cake5,compound="bottom", border="0")
btn_cake6 = Button(frame3, text="ฮอกไกโดมิลด์เค้ก", image=photo_cake6,compound="bottom", border="0")
btn_cake7 = Button(frame3, text="เค้กสปันจ์เนยวานิลลา", image=photo_cake7,compound="bottom", border="0")
btn_cake8 = Button(frame3, text="ฟรุตเค้ก", image=photo_cake8,compound="bottom", border="0")
btn_cake9 = Button(frame3, text="เค้กช็อกโกแลตฟัดจ์ 1.0", image=photo_cake9,compound="bottom", border="0")
btn_cake10 = Button(frame3, text="เค้กชิฟฟ่อนกาแฟ", image=photo_cake10,compound="bottom", border="0")



#-----------------------------------------------------------------------------------------------------#

#แสดงรายการสั่งซื้อทั้งหมด
lbl_a = Label(frame5, text="รายการสั่งซื้อทั้งหมด", bg="white" ,font="consolas 30")
lbl_list = Label(frame6, textvariable=list_var, bg="coral",font="consolas 20")

#สร้างปุ่มกดยืนยันโดยใช้คำสั่ง OK
btn_confirm = Button(frame2,text="ยืนยัน", bg="Spring Green" ,font="consolas 30",command=Ok)

#สร้างปุ่มกดลบประวัติรายการสินค้าโดยใช้คำสั่ง Clear
btn_clear = Button(frame3,text="Clear" , bg="Red" ,font="consolas 30",command=Clear)

#แสดงราคาสั่งซื้อทั้งหมด
lbl_total = Label(frame4, textvariable=total, bg="cyan",font="consolas 30")


#****
btn_cake1.bind("<Button-1>", sum)
btn_cake2.bind("<Button-1>", sum)
btn_cake3.bind("<Button-1>", sum)
btn_cake4.bind("<Button-1>", sum)
btn_cake5.bind("<Button-1>", sum)
btn_cake6.bind("<Button-1>", sum)
btn_cake7.bind("<Button-1>", sum)
btn_cake8.bind("<Button-1>", sum)
btn_cake9.bind("<Button-1>", sum)
btn_cake10.bind("<Button-1>", sum)

#****



#แสดงเค้กทั้งหมด
btn_cake1.pack(side="left")
btn_cake2.pack(side="left")
btn_cake3.pack(side="left")
btn_cake4.pack(side="left")
btn_cake5.pack(side="left")
btn_cake6.pack(side="left")
btn_cake7.pack(side="left")
btn_cake8.pack(side="left")
btn_cake9.pack(side="left")
btn_cake10.pack(side="left")






#แสดง Label รายการสั่งซื้อทั้งหมด
lbl_a.pack()

#แสดงปุ่มกดยืนยัน
btn_confirm.pack()

#แสดงปุ่มกดลบประวัติรายการสินค้าทั้งหมด
btn_clear.pack()

#แสดงรายการสั่งซื้อทั้งหมดและราคารวมทั้งหมด
lbl_list.pack(fill="x")
lbl_total.pack(fill="x")

#
cake.mainloop()