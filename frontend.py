from tkinter import*
import mysql.connector
def result():
   con=mysql.connector.connect(host="localhost",user="root",password="Balu@123",database="AKNU MSN CAMPUS")
   cur=con.cursor()
   htno= int(t2.get())
   name= t3.get()
   telugu= int(t4.get())
   hindi= int(t5.get())
   english= int(t6.get())
   maths= int(t7.get())
   physics = int(t8.get())
   chemistry= int(t9.get())
   social= int(t10.get())
   total=telugu+hindi+english+maths+physics+chemistry+social
   avg = total//7
   if avg>=90:
      grade="A+"

   elif avg >= 80:
      grade = "A"

   elif avg >= 70:
      grade = "B+"
   sql="insert into result( htno,name ,telugu ,hindi,english ,maths,physics ,chemistry,social ,total ,avg ,grade)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
   val=(htno, name, telugu, hindi, english, maths, physics, chemistry, social, total, avg, grade)
   cur.execute(sql, val)
   con.commit()
   l11.config(text="Result submitted successfully")

   
sem=Tk()
sem.geometry("500x500")
sem.title("PG Third Sem Result Database")
l1=Label(sem,text="student  database",font=("Times New Roman",20),fg="red")
l2=Label(sem,text="Enter HALL TICKET:",font=("Times New Roman",18))
t2=Entry(sem)
l3=Label(sem,text="Enter NAME:",font=("Times New Roman",18))
t3=Entry(sem)
l4=Label(sem,text="Enter TELUGU:",font=("Times New Roman",18))
t4=Entry(sem)
l5=Label(sem,text="Enter HINDI:",font=("Times New Roman",18))
t5=Entry(sem)
l6=Label(sem,text="Enter ENGLISH:",font=("Times New Roman",18))
t6=Entry(sem)
l7=Label(sem,text="Enter HALL MATHS:",font=("Times New Roman",18))
t7=Entry(sem)
l8=Label(sem,text="Enter HALL PHYSICS:",font=("Times New Roman",18))
t8=Entry(sem)
l9=Label(sem,text="CHEMISTRY:",font=("Times New Roman",18))
t9=Entry(sem)
l10=Label(sem,text="SOCIAL:",font=("Times New Roman",18))
t10=Entry(sem)
b=Button(sem, text="SUBMIT",font=("Times New Roman",18),command=result)
l11=Label(sem, text="",font=("Times New Roman",16),fg="green")

l1.grid(row=0,column=1)
l2.grid(row=1,column=0)
t2.grid(row=1, column=1)
l3.grid(row=2, column=0)
t3.grid(row=2, column=1)
l4.grid(row=3, column=0)
t4.grid(row=3, column=1)
l5.grid(row=4, column=0)
t5.grid(row=4, column=1)
l6.grid(row=5, column=0)
t6.grid(row=5, column=1)
l7.grid(row=6, column=0)
t7.grid(row=6, column=1)
l8.grid(row=7, column=0)
t8.grid(row=7, column=1)
l9.grid(row=8, column=0)
t9.grid(row=8, column=1)
l10.grid(row=9, column=0)
t10.grid(row=9, column=1)
b.grid(row=10, column=1)
l11.grid(row=11, column=1)
mainloop()



