import tkinter as tk
from tkinter import ttk
import win32api
from win32api import GetSystemMetrics
from tkinter import font

main = tk.Tk()
main.title("Tution payment Calculator")
main.iconbitmap("logo.ico")
screen_width = GetSystemMetrics(0)  #/screen_width = root.winfo_screenwidth()
screen_height = GetSystemMetrics(1) #screen_height = root.winfo_screenwidth()
window_width = 400
window_height = 500
x_position = (screen_width/2 ) - (window_width/2)
y_position = (screen_height/2) - (window_height/2)

#print(screen_height)
#print(screen_width)
main.geometry(f'{window_width}x{window_height}+{int(x_position)}+{int(y_position)}')
main.resizable(False,False)
#var
label_font = font.Font(weight="bold")
Sinhala_var = tk.StringVar()
Mathematics_var = tk.StringVar()
English_var = tk.StringVar()
History_var = tk.StringVar()
admission_var = tk.StringVar()
#weiget
frame_1=tk.LabelFrame(main,text="payment",padx=30, pady=10)
admission_pay =  ttk.Checkbutton(frame_1,text="Addmission", onvalue=1000 ,variable=admission_var)
Sinhala = ttk.Checkbutton(frame_1,text="Sinhala", onvalue=1500 ,variable=Sinhala_var)
Mathematics = ttk.Checkbutton(frame_1,text="Mathematics",onvalue=2000, variable=Mathematics_var)
English = ttk.Checkbutton(frame_1,text="English",onvalue=2000, variable=English_var)
History = ttk.Checkbutton(frame_1,text="History",onvalue=1500,variable=History_var)
 
#data
student_names = ("sanuthi","anuthi","tharindu","thamesh","shayan")
grade =("8","8","8","8","8")
student_ID = ("2301","2302","2303","2304","2305")
admission = [1,0,1,1,0]
pay = ("want admission","admission payed")
classes =[ ["Sinhala", "Mathematics", "English" ],
            ["History","Mathematics"],
            ["Sinhala"],
            ["Sinhala","History","Mathematics"],
            ["English"]
           ]

def check_info():
    st_name = entry_name.get()
    print(st_name)
    st_ID = entry_id.get()
    x = 0
    while True:
        if str(st_ID) == student_ID[x]:
            if st_name == student_names[x]:
                print("done")
                if admission[x] == 1:
                    print("admission payed")
                    student_info = tk.Toplevel(main)  
                    window_1_width = 300
                    window_1_height = 400
                    x_1_position = (screen_width/2 ) - (window_1_width/2)
                    y_1_position = (screen_height/2) - (window_1_height/2)
                    student_info.geometry(f'{window_1_width}x{window_1_height}+{int(x_1_position)}+{int(y_1_position)}')
                    student_info.iconbitmap("logo.ico")
                    student_info.title("submission faild ")
                    student_info.resizable(False,False)
                    label_4 = ttk.Label(student_info, text="- Student Details -",background="yellow" , font=label_font)
                    label_4.pack(pady=10)
                    label_5 = ttk.Label(student_info, text="- Student name :- "+student_names[x])
                    label_5.pack(anchor="w",padx=(10,5), pady=5)
                    label_6 = ttk.Label(student_info, text="- Student ID :- "+student_ID[x])
                    label_6.pack(anchor="w",padx=(10,5), pady=5)
                    label_6_1 = ttk.Label(student_info, text="- Grade :- "+grade[x])
                    label_6_1.pack(anchor="w",padx=(10,5), pady=5)
                    label_7 = ttk.Label(student_info, text="- admission:- "+pay[1])
                    label_7.pack(anchor="w",padx=(10,5), pady=5)
                    y=0
                    cls_val=""
                    while y < len(classes[x]):
                        cls_val = str(cls_val) + classes[x][y] +" , "
                        y=y+1
                    print(cls_val)

                    label_7_1 = ttk.Label(student_info, text="- classes:- "+str(cls_val))
                    label_7_1.pack(anchor="w",padx=(10,5), pady=5)
                    frame_1.pack(pady=(5,0))
                    z = 0
                    while z < len(classes[x]):
                        globals()[classes[x][z]].pack(anchor="w",padx=(10,150), pady=5)
                        z=z+1
                    def payment_pro():
                        payment_info = tk.Toplevel(main)  
                        window_1_width = 300
                        window_1_height = 400
                        x_1_position = (screen_width/2 ) - (window_1_width/2)
                        y_1_position = (screen_height/2) - (window_1_height/2)
                        payment_info.geometry(f'{window_1_width}x{window_1_height}+{int(x_1_position)}+{int(y_1_position)}')
                        payment_info.iconbitmap("logo.ico")
                        payment_info.title("submission faild ")
                        payment_info.resizable(False,False)
                        label_8 = ttk.Label(payment_info, text="- Payment Details -",background="yellow" , font=label_font)
                        label_8.pack(pady=10)
                        frame_2=tk.LabelFrame(payment_info,text="payment",padx=30, pady=10)
                        frame_2.pack()
                        total = 0
                        z = 0
                        while z < len(classes[x]):
                          labels = str("lebel_pay"+str(z))
                          labels_1 = str(classes[x][z]+"_var")
                          value_1 = globals()[labels_1].get()
                          total = total + int(value_1)
                          globals()[labels] = ttk.Label(frame_2,text="- "+classes[x][z]+" :- Rs."+value_1)
                          globals()[labels].pack(anchor="w", pady=5, padx=(0,20))
                          z=z+1
                        label_9 = ttk.Label(frame_2, text="Total = Rs."+str(total),font=label_font)
                        label_9.pack(anchor="w", pady=5)
                    Calculate = ttk.Button(frame_1,text="proceed to payment", padding=(10,5,10,5), command=payment_pro)
                    Calculate.pack(pady=(15,10))
                   
    
                    break
                else:
                    print("admission payed")
                    student_info = tk.Toplevel(main)  
                    window_1_width = 300
                    window_1_height = 400
                    x_1_position = (screen_width/2 ) - (window_1_width/2)
                    y_1_position = (screen_height/2) - (window_1_height/2)
                    student_info.geometry(f'{window_1_width}x{window_1_height}+{int(x_1_position)}+{int(y_1_position)}')
                    student_info.iconbitmap("logo.ico")
                    student_info.title("submission faild ")
                    student_info.resizable(False,False)
                    label_4 = ttk.Label(student_info, text="- Student Details -",background="yellow" , font=label_font)
                    label_4.pack(pady=10)
                    label_5 = ttk.Label(student_info, text="- Student name :- "+student_names[x])
                    label_5.pack(anchor="w",padx=(10,5), pady=5)
                    label_6 = ttk.Label(student_info, text="- Student ID :- "+student_ID[x])
                    label_6.pack(anchor="w",padx=(10,5), pady=5)
                    label_6_1 = ttk.Label(student_info, text="- Grade :- "+grade[x])
                    label_6_1.pack(anchor="w",padx=(10,5), pady=5)
                    label_7 = ttk.Label(student_info, text="- admission:- "+pay[0])
                    label_7.pack(anchor="w",padx=(10,5), pady=5)
                    y=0
                    cls_val=""
                    while y < len(classes[x]):
                        cls_val = str(cls_val) + classes[x][y] +" , "
                        y=y+1
                    print(cls_val)

                    label_7_1 = ttk.Label(student_info, text="- classes:- "+str(cls_val))
                    label_7_1.pack(anchor="w",padx=(10,5), pady=5)
                    frame_1.pack(pady=(5,0))
                    admission_pay.pack(anchor="w",padx=(10,150), pady=5)
                    z = 0
                    while z < len(classes[x]):
                        globals()[classes[x][z]].pack(anchor="w",padx=(10,150), pady=5)
                        z=z+1
                    def payment_pro():
                        payment_info = tk.Toplevel(main)  
                        window_1_width = 300
                        window_1_height = 400
                        x_1_position = (screen_width/2 ) - (window_1_width/2)
                        y_1_position = (screen_height/2) - (window_1_height/2)
                        payment_info.geometry(f'{window_1_width}x{window_1_height}+{int(x_1_position)}+{int(y_1_position)}')
                        payment_info.iconbitmap("logo.ico")
                        payment_info.title("submission faild ")
                        payment_info.resizable(False,False)
                        label_8 = ttk.Label(payment_info, text="- Payment Details -",background="yellow" , font=label_font)
                        label_8.pack(pady=10)
                        frame_2=tk.LabelFrame(payment_info,text="payment",padx=30, pady=10)
                        frame_2.pack()
                        label_10 = ttk.Label(frame_2, text="- Addmission :- 1000")
                        label_10.pack(anchor="w", pady=5, padx=(0,20))
                        total = 0
                        z = 0
                        while z < len(classes[x]):
                          labels = str("lebel_pay"+str(z))
                          labels_1 = str(classes[x][z]+"_var")
                          value_1 = globals()[labels_1].get()
                          total = total + int(value_1)
                          globals()[labels] = ttk.Label(frame_2,text="- "+classes[x][z]+" :- Rs."+value_1)
                          globals()[labels].pack(anchor="w", pady=5, padx=(0,20))
                          z=z+1
                        
                        label_9 = ttk.Label(frame_2, text="Total = Rs."+str(total+1000),font=label_font)
                        label_9.pack(anchor="w", pady=5)
                        
                    Calculate = ttk.Button(frame_1,text="proceed to payment", padding=(10,5,10,5), command=payment_pro)
                    Calculate.pack(pady=(15,10))
                    break
            else:
               root_fail = tk.Toplevel(main)  
               window_1_width = 300
               window_1_height = 100
               x_1_position = (screen_width/2 ) - (window_1_width/2)
               y_1_position = (screen_height/2) - (window_1_height/2)
               root_fail.geometry(f'{window_1_width}x{window_1_height}+{int(x_1_position)}+{int(y_1_position)}')
               root_fail.iconbitmap("wrong.ico")
               root_fail.title("Invalid Details")
               root_fail.resizable(False,False)
               label_3 = ttk.Label(root_fail, text="Invalid Details",background="red" , font=label_font, foreground="white",padding=(10,5,10,5) )
               label_3.pack(pady=15)
               break
            
        else:
            x = x+1


#weiget

label_1 =ttk.Label(main,text="- Payment Calculator -",font=label_font,background="yellow",padding=5)
label_1.pack(pady=10)

frame=tk.LabelFrame(main,text="student's Details",padx=30, pady=10, foreground="gray")
frame.pack(pady=(5,0))

label_2 = ttk.Label(frame,text="student's name :-")
label_2.pack(anchor="w")

entry_name = ttk.Entry(frame, width="40")
entry_name.pack()

label_3 = ttk.Label(frame,text="student's ID :-")
label_3.pack(anchor="w", pady=(5,0))

entry_id = ttk.Entry(frame, width="40")
entry_id.pack()

val_btn = ttk.Button(frame, text="check", command=check_info)
val_btn.pack(pady=(15,10))
tk.mainloop()





