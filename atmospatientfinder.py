from tkinter import *
import sqlite3
from tkinter import messagebox






root = Tk()

#connecting to database
connect = sqlite3.connect('patients.db')


cursor = connect.cursor()

#dealling with frame work
root.title("Patient Finder")
root.geometry("1500x700")
left = Frame(root, width=900, height=720, bg='lightblue')
left.pack(side =LEFT)

left = Frame(root, width=500, height=720, bg='lightgreen')
left.pack(side =RIGHT)

#creating menu bar
#file menu
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File   ", menu=filemenu)
filemenu.add_command (label = "New", command=" ")
filemenu.add_command (label = "Recent", command=" ")
filemenu.add_command (label = "exit", command=" ")

#data base for all admited patients
def ADP():
    global top
    top = Toplevel()
    top.title('RECORD PATIENT DETAILS')
    top.geometry("1500x700")

    left = Frame(top, width=1500, height=720, bg='lightblue')
    left.pack(side=LEFT)

    # creating a header label
    header = Label(top, text="ALL PATIENTS ADMITTED \nPATIENTS IN THE HOSPITAL", font=('Arial 30  underline '), bg="lightblue")
    header.place(relx=0.1, rely=0.005)
    #headerline = Label(top,text="******************************************************************************************************************",bg="light blue")
    #headerline.place(relx=0.1, rely=0.14)
    sql = "SELECT * from details "
    result = connect.execute(sql)
    print_result = ''
    for name in result:
        print_result += str(name[0]) + "  " + str(name[1]) + "\t " + str(name[2]) + "\t    " + str(
            name[3]) + "\t    " + str(name[4]) + "\t    " + str(name[5]) + "\t    " + str(name[6]) + "\t    " + str(
            name[7]) + "\t    " + str(name[8]) + "\t    " + str(name[9]) + "\t   " + str(name[10]) + "    " + str(
            name[11]) + "    " + str(name[12]) + "    " + str(name[13]) + " \n"
        # box.insert(END, print_records)
        box_label = Label(top, text=print_result, font=('arial 11 '), bg="white", fg="black", justify=LEFT, pady=4)
        box_label.place(relx=0.0, rely=0.2)


    #box = Text(top, width=160, height=40)
    #box.place(relx=0.03, rely=0.2)
    #FUNTION FOR PATIENT IN SURGICAL WARD
def surgical():
    global top
    top = Toplevel()
    top.title('RECORD PATIENT DETAILS')
    top.geometry("1500x700")

    left = Frame(top, width=1500, height=720, bg='lightblue')
    left.pack(side=LEFT)
    head_label = Label(top, text="PATIENTS ADMITTED IN SURGICAL WARD", font=('Arial 30  underline '), bg="lightblue")
    head_label.place(relx = 0.25, rely=0.05)

    #
    sql_sur = "SELECT * from details WHERE ward LIKE 'SURGICAL%'"
    result_sur = connect.execute(sql_sur)
    print_surgical = ''
    for name3 in result_sur:
        print_surgical += str(name3[0]) + "  " + str(name3[1]) + "\t " + str(name3[2]) + "\t    " + str(
            name3[3]) + "\t    " + str(name3[4]) + "\t    " + str(name3[5]) + "\t    " + str(name3[6]) + "\t    " + str(
            name3[7]) + "\t    " + str(name3[8]) + "\t    " + str(name3[9]) + "\t   " + str(name3[10]) + "    " + str(
            name3[11]) + "    " + str(name3[12]) + "    " + str(name3[13]) + " \n"
        # box.insert(END, print_records)
        box_label = Label(top, text=print_surgical, font=('arial 11 '), bg="white", fg="black", justify=LEFT, pady=4)
        box_label.place(relx=0.0, rely=0.2)
        print(print_surgical)
        #FUNCTIOIN FOR PATIENT IN MEDICAL WARD
def medical():
    global top
    top = Toplevel()
    top.title('RECORD PATIENT DETAILS')
    top.geometry("1500x700")

    left = Frame(top, width=1500, height=720, bg='lightblue')
    left.pack(side=LEFT)
    head_label = Label(top, text="PATIENTS ADMITTED IN MEDICAL WARD", font=('Arial 30  underline '), bg="lightblue")
    head_label.place(relx=0.25, rely=0.05)

    #
    sql_mer = "SELECT * from details WHERE ward LIKE 'MEDICAL%'"
    result_mer = connect.execute(sql_mer)
    print_medical = ''
    for name4 in result_mer:
        print_medical += str(name4[0]) + "  " + str(name4[1]) + "\t " + str(name4[2]) + "\t    " + str(
            name4[3]) + "\t    " + str(name4[4]) + "\t    " + str(name4[5]) + "\t    " + str(name4[6]) + "\t    " + str(
            name4[7]) + "\t    " + str(name4[8]) + "\t    " + str(name4[9]) + "\t   " + str(name4[10]) + "    " + str(
            name4[11]) + "    " + str(name4[12]) + "    " + str(name4[13]) + " \n"
        # box.insert(END, print_records)
        box_label = Label(top, text=print_medical, font=('arial 11 '), bg="white", fg="black", justify=LEFT, pady=4)
        box_label.place(relx=0.0, rely=0.2)
        print(print_medical)
#patient in emergency ward
def emergency ():
    global top
    top = Toplevel()
    top.title('RECORD PATIENT DETAILS')
    top.geometry("1500x700")

    left = Frame(top, width=1500, height=720, bg='lightblue')
    left.pack(side=LEFT)
    head_label = Label(top, text="PATIENTS ADMITTED IN EMERGENCY WARD", font=('Arial 30  underline '), bg="lightblue")
    head_label.place(relx=0.25, rely=0.05)

    #
    sql_emer = "SELECT * from details WHERE ward LIKE 'EMERGENCY%'"
    result_emer = connect.execute(sql_emer)
    print_emer = ''
    for name4 in result_emer:
        print_emer += str(name4[0]) + "  " + str(name4[1]) + "\t " + str(name4[2]) + "\t    " + str(
            name4[3]) + "\t    " + str(name4[4]) + "\t    " + str(name4[5]) + "\t    " + str(name4[6]) + "\t    " + str(
            name4[7]) + "\t    " + str(name4[8]) + "\t    " + str(name4[9]) + "\t   " + str(name4[10]) + "    " + str(
            name4[11]) + "    " + str(name4[12]) + "    " + str(name4[13]) + " \n"
        # box.insert(END, print_records)
        box_label = Label(top, text=print_emer, font=('arial 11 '), bg="white", fg="black", justify=LEFT, pady=4)
        box_label.place(relx=0.0, rely=0.2)
        print(print_emer)
def children():
    global top
    top = Toplevel()
    top.title('RECORD PATIENT DETAILS')
    top.geometry("1500x700")

    left = Frame(top, width=1500, height=720, bg='lightblue')
    left.pack(side=LEFT)

    head_label = Label(top, text="PATIENTS ADMITTED IN CHILDREN\'S WARD", font=('Arial 30  underline '), bg="lightblue")
    head_label.place(relx=0.25, rely=0.05)

    #
    sql_child = "SELECT * from details WHERE ward LIKE 'CHILD%'"
    result_child = connect.execute(sql_child)
    print_child = ''
    for name5 in result_child:
        print_child += str(name5[0]) + "  " + str(name5[1]) + "\t " + str(name5[2]) + "\t    " + str(
            name5[3]) + "\t    " + str(name5[4]) + "\t    " + str(name5[5]) + "\t    " + str(name5[6]) + "\t    " + str(
            name5[7]) + "\t    " + str(name5[8]) + "\t    " + str(name5[9]) + "\t   " + str(name5[10]) + "    " + str(
            name5[11]) + "    " + str(name5[12]) + "    " + str(name5[13]) + " \n"
        # box.insert(END, print_records)
        box_label = Label(top, text=print_child, font=('arial 11 '), bg="white", fg="black", justify=LEFT, pady=4)
        box_label.place(relx=0.0, rely=0.2)
        print(print_child)
def discharge():
    global top
    top = Toplevel()
    top.title('RECORD PATIENT DETAILS')
    top.geometry("1500x700")

    left = Frame(top, width=1500, height=720, bg='lightblue')
    left.pack(side=LEFT)

    head_label = Label(top, text="PATIENTS DISCHARGE", font=('Arial 30  underline '), bg="lightblue")
    head_label.place(relx=0.25, rely=0.05)

    #patients discharge
    sql_dis = "SELECT * from details WHERE ward LIKE 'DISCH%'"
    result_dis = connect.execute(sql_dis)
    print_dis = ''
    for name6 in result_dis:
        print_dis += str(name6[0]) + "  " + str(name6[1]) + "\t " + str(name6[2]) + "\t    " + str(
            name6[3]) + "\t    " + str(name6[4]) + "\t    " + str(name6[5]) + "\t    " + str(name6[6]) + "\t    " + str(
            name6[7]) + "\t    " + str(name6[8]) + "\t    " + str(name6[9]) + "\t   " + str(name6[10]) + "    " + str(
            name6[11]) + "    " + str(name6[12]) + "    " + str(name6[13]) + " \n"
        # box.insert(END, print_records)
        box_label = Label(top, text=print_dis, font=('arial 11 '), bg="white", fg="black", justify=LEFT, pady=4)
        box_label.place(relx=0.0, rely=0.2)
        print(print_dis)
def death():
    global top
    top = Toplevel()
    top.title('RECORD PATIENT DETAILS')
    top.geometry("1500x700")

    left = Frame(top, width=1500, height=720, bg='lightblue')
    left.pack(side=LEFT)

    head_label = Label(top, text="PATIENTS DEAD", font=('Arial 30  underline '), bg="lightblue")
    head_label.place(relx=0.25, rely=0.05)

    # patients discharge
    sql_dead = "SELECT * from details WHERE ward LIKE 'DEA%'"
    result_dead = connect.execute(sql_dead)
    print_dead = ''
    for name7 in result_dead:
        print_dead += str(name7[0]) + "  " + str(name7[1]) + "\t " + str(name7[2]) + "\t    " + str(
            name7[3]) + "\t    " + str(name7[4]) + "\t    " + str(name7[5]) + "\t    " + str(name7[6]) + "\t    " + str(
            name7[7]) + "\t    " + str(name7[8]) + "\t    " + str(name7[9]) + "\t   " + str(name7[10]) + "    " + str(
            name7[11]) + "    " + str(name7[12]) + "    " + str(name7[13]) + " \n"
        # box.insert(END, print_records)
        box_label = Label(top, text=print_dead, font=('arial 11 '), bg="white", fg="black", justify=LEFT, pady=4)
        box_label.place(relx=0.0, rely=0.2)
        print(print_dead)


# full number of patient admited
database = Menu(menu)
menu.add_cascade(label="Admitted Patients", menu=database)
database.add_command (label = "Admitted Patients", command=ADP)

#patient in a particular ward
PIPW = Menu(menu)
menu.add_cascade(label="Patients ward", menu=PIPW)
PIPW.add_command (label = "Surgical ward", command=surgical)
PIPW.add_command (label = "Medical ward", command=medical)
PIPW.add_command (label = "Emergency ward", command=emergency)
PIPW.add_command (label = "Children\'s ward", command=children)

#all dead patients
ADP = Menu(menu)
menu.add_cascade(label="Dead Patients", menu=ADP)
ADP.add_command (label = "Dead Patients", command= death)

#all discharge patients
DP = Menu(menu)
menu.add_cascade(label="Discharge patients", menu=DP)
DP.add_command (label = "Discharge patients", command=discharge)

#creating a header label
header = Label(root, text="PATIENT\'S FINDER", font= ('arial 40 bold') ,bg="lightblue")
header.place(relx = 0.258, rely = 0.005)
headerline=Label(root, text="**************************************************************************************************", bg = "light blue")
headerline.place(relx=0.258, rely = 0.080)

#creating the labels
id_num_lab = Label(root, text="ID NO.",font= ('arial 20 bold'), bg="light blue", fg= "red")
id_num_lab.place(relx=0.01, rely=0.050)
firstname_lab = Label(root, text="First Name", font=("Times New Roman" ,20))
firstname_lab.place(relx=0.003, rely=0.2)
lastname_lab = Label(root, text="Last Name", font= ("Times New Roman", 20))
lastname_lab.place(relx=0.003, rely=0.3)
location_lab = Label(root, text="Location", font= ("Times New Roman", 20))
location_lab.place(relx=0.003, rely=0.4)

#DOB mean date of admittance
DOA_lab = Label(root, text="Date of Admittance", font=("Times New Roman" ,20))
DOA_lab.place(relx=0.3, rely=0.2)
patient_tell_lab = Label(root, text="Patient tell", font= ("Times New Roman", 20))
patient_tell_lab.place(relx=0.3, rely=0.3)
Gurdian_lab = Label(root, text="Gurdian name", font= ("Times New Roman", 20))
Gurdian_lab.place(relx=0.3, rely=0.4)

Gurdian_tell_lab = Label(root, text="Gurdian Tell", font= ("Times New Roman", 20))
Gurdian_tell_lab.place(relx=0.3, rely=0.5)
sickness_lab = Label(root, text="Sickness", font= ("Times New Roman", 20))
sickness_lab.place(relx=0.003, rely=0.5)
ward_lab = Label(root, text="Ward", font= ("Times New Roman", 20))
ward_lab.place(relx=0.003, rely=0.6)
Bed_num_lab = Label(root, text="Bed Number", font= ("Times New Roman", 20))
Bed_num_lab.place(relx=0.3, rely=0.6)
sex_lab = Label(root, text="Sex", font= ("Times New Roman", 20))
sex_lab.place(relx=0.003, rely=0.7)

#Entries
id_num = Entry(root, width=10, font= ("Times New Roman", 20))
id_num.place(relx = 0.080 ,rely =0.047)
Firstname = Entry(root, width=15, font=('arial 20 '))
Firstname.place(relx=0.1, rely=0.20 )
lastname = Entry(root, width=15, font=('arial 20 '))
lastname.place(relx=0.1, rely=0.30 )
location = Entry(root, width=15, font=('arial 20 '))
location.place(relx=0.1, rely=0.40 )
sickness = Entry(root, width=15, font=('arial 20'))
sickness.place(relx=0.1, rely=0.50 )


DOA = Entry(root, width=15, font=('arial 20'))
DOA.insert( 0,"00/00/00")
DOA.place(relx=0.47, rely=0.20)
patient_tell = Entry(root, width=18, font=('arial 20 '))
patient_tell.place(relx=0.40, rely=0.30)
Gurdian_name = Entry(root, width=20, font=('arial 20'))
Gurdian_name.place(relx=0.43, rely=0.405)
Gurdian_tell  = Entry(root, width=18, font=('arial 20 '))
Gurdian_tell.place(relx=0.43, rely=0.51)


#ward lists
option = ["MEDICAL WARD ",
          "MATERNITY WARD",
          "EMERGENCY WARD",
         "CHILDREN WARD"

]


ward = StringVar()
ward.set(option[0])

ward_drop = OptionMenu(root, ward, *option)
ward_drop.place(relx=0.07, rely=0.61)
print(ward.get())

bed_num = IntVar()
bed_num.set(1)
bed_num1 = OptionMenu(root, bed_num, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
bed_num1.place(relx=0.43, rely=0.61)
print(bed_num.get())

sex = StringVar()
sex.set("Male")
sex1 = OptionMenu(root, sex,  "Male","Female")
sex1.place(relx=0.07, rely=0.71)

out_label = Label(root,text="Out",font=('arial 15'))
out_label.place(relx=0.52, rely=0.60)
out = Entry(root, width=20, font=('arial 10') )
out.place(relx=0.55, rely=0.61)
age_label = Label(root, text = "Age", font=('arial 15'))
age_label.place(relx=0.52, rely=0.65)
age = Entry(root, width=5, font=('arial 20') )
age.place(relx=0.55, rely=0.65)



#creating function for save details
def savedetails():
    global input1
    global input2
    global input3
    global input4
    global input5
    global input6
    global input7
    global input8
    global input9
    global input10
    global input11
    global input12
    global input13
    global input14

    input1 = id_num.get()
    input2 = Firstname.get()
    input3 = lastname.get()
    input4 = location.get()
    input5 = DOA.get()
    input6 = patient_tell.get()
    input7 = Gurdian_name.get()
    input8 = Gurdian_tell.get()
    input9 = sickness.get()
    input10 = ward.get()
    input11 = bed_num.get()
    input12 = sex.get()
    input13 = out.get()
    input14 = age.get()




    if   input2 == '' or input3=='' or input4=='' or input5==''or input6=='' or input7=='' or input8=='' or  input9=='' or  input10=='' or input11=='' or input12=='' or input13 == '' or input14 == ''  :
        messagebox.showinfo("Warning", "Please fill up all empty spaces")

    else:
        sql = "INSERT INTO 'details' (first_name, last_name, location,DOA,pat_tell,gurdian_name,gurdian_tell,sickness,ward,bed_num,sex,out,age) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"
        connect.execute(sql,(input2,input3,input4,input5,input6,input7,input8,input9,input10,input11,input12,input13,input14))
        connect.commit()
        print("successfully entered into database")
        messagebox.showinfo("success", input2 +"  detail saved")



    Firstname.delete(0, END)
    lastname.delete(0, END)
    location.delete(0, END)
    sickness.delete(0, END)
    #ward.delete(0, END)
    DOA.delete(0, END)
    patient_tell.delete(0, END)
    Gurdian_name.delete(0, END)
    Gurdian_tell.delete(0, END)
    #bed_num.delete(0, END)
    #sex.delete(0, END)
    out.delete(0, END)
    age.delete(0, END)




def searche():
    global input1
    global input2
    global input3
    global input4
    global input5
    global input6
    global input7
    global input8
    global input9
    global input10
    global input11
    global input12
    global input13
    global input14

    id_num = Entry(root, width=10, font=("Times New Roman", 20))
    id_num.place(relx=0.080, rely=0.047)
    Firstname = Entry(root, width=15, font=('arial 20 '))
    Firstname.place(relx=0.1, rely=0.20)
    lastname = Entry(root, width=15, font=('arial 20 '))
    lastname.place(relx=0.1, rely=0.30)
    location = Entry(root, width=15, font=('arial 20 '))
    location.place(relx=0.1, rely=0.40)
    sickness = Entry(root, width=15, font=('arial 20'))
    sickness.place(relx=0.1, rely=0.50)

    DOA = Entry(root, width=15, font=('arial 20'))
    DOA.insert(0, "00/00/00")
    DOA.place(relx=0.47, rely=0.20)
    patient_tell = Entry(root, width=18, font=('arial 20 '))
    patient_tell.place(relx=0.40, rely=0.30)
    Gurdian_name = Entry(root, width=20, font=('arial 20'))
    Gurdian_name.place(relx=0.43, rely=0.405)
    Gurdian_tell = Entry(root, width=18, font=('arial 20 '))
    Gurdian_tell.place(relx=0.43, rely=0.51)

    input1 = id_num.get()
    input2 = Firstname.get()
    input3 = lastname.get()
    input4 = location.get()
    input5 = DOA.get()
    input6 = patient_tell.get()
    input7 = Gurdian_name.get()
    input8 = Gurdian_tell.get()
    input9 = sickness.get()
    input10 = ward.get()
    input11 = bed_num.get()
    input12 = sex.get()
    input13 = out.get()
    input14 = age.get()


    search = Entry(root, width=22, font=('arial 20 '))
    search.place(relx=0.657, rely=0.1)
    global input15
    input15 = search.get()


    def searchbut1():
        global input15
        input15 = search.get()

        print(input15)

        sql4 = "SELECT * from details"
        result2 = connect.execute(sql4)
        print_records = ''
        for name in result2:


            print_records += str(name[0]) + "  " + str(name[1]) + "\t\t" + str(name[2]) + "\t  " + str(name[3]) + "\t" + str(name[4]) + "\t\t" + str(name[5]) + "\t " + str(name[6]) + "\t \t " + str(name[7]) + "  " + str(name[8]) + " \t\t" + str(name[9]) + "\t\t\t" + str(name[10]) + "\t\t" + str(name[11]) + "\t\t  " + str(name[12]) + "\t" + str(name[13]) + "\n"
            if input15 == '':
                messagebox.showinfo("Warning", "No Patient Name")
                name-=1



            if name[1] == input15 or name[2] == input15:
                print("done")
                askok = messagebox.askokcancel("Match found", "Search " + input15 + " info?")
                if askok==1:
                    #present result from search unit
                    print("work")
                    sql_detail = "SELECT * FROM details WHERE first_name LIKE ? "
                    fetch_result=connect.execute(sql_detail,(input15,))
                    specific_result = ''
                    print(fetch_result)
                    box1 = Text(root, width=30, height=15,font=('arial 15 '), bg="light green", fg="blue")
                    box1.place(relx=0.8, rely=0.2)
                    for name1 in fetch_result:
                        specific_result += str(name1[0]) + "\n" + str(name1[1]) + "\n" + str(name1[2]) + "\n" + str(
                            name1[3]) + "\n" + str(name1[4]) + "\n" + str(name1[5]) + "\n" + str(
                            name1[6]) + "\n " + str(name1[7]) + " \n " + str(name1[8]) + "\n" + str(
                            name1[9]) + "\n" + str(name1[10]) + "\n" + str(name1[11]) + "\n" + str(
                            name1[12]) + "\n" + str(name1[13]) + "\n"
                        print(name1)
                        id_num_lab1 = Label(root, text="ID NO.", font=("Times New Roman", 15), bg="light green", fg="red")
                        id_num_lab1.place(relx=0.67, rely=0.2)
                        firstname_lab1 = Label(root, text="First Name", font=("Times New Roman", 15), bg="light green", fg="red")
                        firstname_lab1.place(relx=0.67, rely=0.23)
                        lastname_lab1 = Label(root, text="Last Name", font=("Times New Roman", 15), bg="light green", fg="red")
                        lastname_lab1.place(relx=0.67, rely=0.26)
                        location_lab1 = Label(root, text="Location", font=("Times New Roman", 15), bg="light green", fg="red")
                        location_lab1.place(relx=0.67, rely=0.29)
                        DOA_lab1 = Label(root, text="Date of Admittance", font=("Times New Roman", 15), bg="light green", fg="red")
                        DOA_lab1.place(relx=0.67, rely=0.32)
                        patient_tell_lab1 = Label(root, text="Patient tell", font=("Times New Roman", 15), bg="light green", fg="red")
                        patient_tell_lab1.place(relx=0.67, rely=0.35)
                        Gurdian_lab1 = Label(root, text="Gurdian name", font=("Times New Roman", 15), bg="light green", fg="red")
                        Gurdian_lab1.place(relx=0.67, rely=0.39)

                        Gurdian_tell_lab1 = Label(root, text="Gurdian Tell", font=("Times New Roman", 15), bg="light green", fg="red")
                        Gurdian_tell_lab1.place(relx=0.67, rely=0.43)
                        sickness_lab1 = Label(root, text="Sickness", font=("Times New Roman", 15), bg="light green", fg="red")
                        sickness_lab1.place(relx=0.67, rely=0.46)
                        ward_lab1 = Label(root, text="Ward", font=("Times New Roman", 15), bg="light green", fg="red")
                        ward_lab1.place(relx=0.67, rely=0.49)
                        Bed_num_lab1 = Label(root, text="Bed Number", font=("Times New Roman", 15), bg="light green", fg ="red")
                        Bed_num_lab1.place(relx=0.67, rely=0.53)
                        sex_lab = Label(root, text="Sex", font=("Times New Roman", 15), bg="light green", fg="red")
                        sex_lab.place(relx=0.67, rely=0.56)

                        out_label1 = Label(root, text="Out", font=("Times New Roman", 15), bg="light green", fg="red")
                        out_label1.place(relx=0.67, rely=0.59)

                        age_label1 = Label(root, text="Age", font=("Times New Roman", 15), bg="light green", fg="red")
                        age_label1.place(relx=0.67, rely=0.62)
                        
                        box1.insert(END,specific_result)











                    break

        if name[1] == input15 or name[2] == input15:
            print("")


        elif name[1] != input15 or name[2] != input15:

                messagebox.showinfo("Warning", "No Match Found")
                print("no match")


        def edit():
            id_num = Entry(root, width=10, font=("Times New Roman", 20))
            id_num.place(relx=0.080, rely=0.047)
            id_num.insert(END, str(name[0]))

            Firstname = Entry(root, width=15, font=('arial 20 '))
            Firstname.place(relx=0.1, rely=0.20)
            Firstname.insert(END,str(name[1]))

            lastname = Entry(root, width=15, font=('arial 20 '))
            lastname.place(relx=0.1, rely=0.30)
            lastname.insert(END,str(name[2]))

            location = Entry(root, width=15, font=('arial 20 '))
            location.place(relx=0.1, rely=0.40)
            location.insert(END,str (name[3]))

            sickness = Entry(root, width=15, font=('arial 20'))
            sickness.place(relx=0.1, rely=0.50)
            sickness.insert(END, str(name[8]))


            DOA = Entry(root, width=15, font=('arial 20'))
            DOA.place(relx=0.47, rely=0.20)
            DOA.insert(END, str(name[4]))


            patient_tell = Entry(root, width=18, font=('arial 20 '))
            patient_tell.place(relx=0.40, rely=0.30)
            patient_tell.insert(END,(name[5]))

            Gurdian_name = Entry(root, width=20, font=('arial 20'))
            Gurdian_name.place(relx=0.43, rely=0.405)
            Gurdian_name.insert(END,(name[6]))

            Gurdian_tell = Entry(root, width=18, font=('arial 20 '))
            Gurdian_tell.place(relx=0.43, rely=0.51)
            Gurdian_tell.insert(END, name[7])

            out = Entry(root, width=20, font=('arial 10'))
            out.place(relx=0.55, rely=0.61)
            out.insert(END,str(name[12]) )
            age = Entry(root, width=5, font=('arial 20'))
            age.place(relx=0.55, rely=0.65)
            age.insert(END, str(name[13]))

            def saveupdate():
                input1 = id_num.get()
                input2 = Firstname.get()
                input3 = lastname.get()
                input4 = location.get()
                input5 = DOA.get()
                input6 = patient_tell.get()
                input7 = Gurdian_name.get()
                input8 = Gurdian_tell.get()
                input9 = sickness.get()
                input10 = ward.get()
                input11 = bed_num.get()
                input12 = sex.get()
                input13 = out.get()
                input14 = age.get()

                sql_update = "UPDATE details SET ID=?, first_name=?, last_name=?, location=?,DOA=?,pat_tell=?,gurdian_name=?,gurdian_tell=?,sickness=?,ward=?,bed_num=?,sex=?,out=?,age=? WHERE first_name LIKE ?"
                connect.execute(sql_update,(input1,input2,input3,input4,input5,input6,input7,input8,input9,input10,input11,input12,input13,input14,input15, ))
                connect.commit()

                Firstname.delete(0, END)
                lastname.delete(0, END)
                location.delete(0, END)
                sickness.delete(0, END)
                # ward.delete(0, END)
                DOA.delete(0, END)
                patient_tell.delete(0, END)
                Gurdian_name.delete(0, END)
                Gurdian_tell.delete(0, END)
                # bed_num.delete(0, END)
                # sex.delete(0, END)
                out.delete(0, END)
                age.delete(0, END)
                print("great")




            update=Button(root, text="UPDATE", command=saveupdate, width=20, height=2, bg='red', fg="black" )
            update.place(relx=0.8, rely=0.80)

        editinfo = Button(root, text="Edit Details", command=edit, width=15, height=1, bg="yellow", fg="red",
                          font=('arial 20 bold'))
        editinfo.place(relx=0.75, rely=0.855)




    searchbut= Button(root, text = "Search", command=searchbut1, width=10, height=2, bg="red",font=("arial", 10))
    searchbut.place(relx=0.92, rely=0.1)





#creating buttons
saveinfo = Button(root, text="SAVE DETAILS", command=savedetails , width=60, height=2, bg="steelblue", fg="black", font=("Bernard MT condensed", 14))
saveinfo.place(relx=0.155, rely=0.8)

findpatients = Button(root, text="Find Patients", command=searche , width=15, height=1, bg="yellow", fg="blue", font=('arial 20 bold'))
findpatients.place(relx=0.75, rely=0.0)




root.mainloop()



