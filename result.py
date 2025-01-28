from tkinter import *
import mysql.connector

def display_result():
    try:
        # Connect to the database
        con = mysql.connector.connect(host="localhost", user="root", password="Balu@123", database="AKNU MSN CAMPUS")
        cur = con.cursor()
        
        # Execute the query
        htno = t2.get()
        cur.execute("SELECT * FROM result WHERE htno = %s", (htno,))
        student_data = cur.fetchone()
        
        if student_data:
            # Update labels with the fetched data
            l3.config(text=f"NAME: {student_data[1]}")  # Assuming 'name' is the second column
            l8.config(text=student_data[2])  # Telugu marks
            l10.config(text=student_data[3])  # Hindi marks
            l12.config(text=student_data[4])  # English marks
            l14.config(text=student_data[5])  # Maths marks
            l16.config(text=student_data[6])  # Physics marks
            l18.config(text=student_data[7])  # Chemistry marks
            l20.config(text=student_data[8])  # Social marks
            total = sum(student_data[2:9])  # Total marks
            percentage = total / 7  # Assuming 7 subjects
            l22.config(text=total)
            l24.config(text=f"{percentage:.2f}%")
            l26.config(text="PASS" if percentage >= 35 else "FAIL")
        else:
            # No student found
            l3.config(text="NAME: Not Found")
            l8.config(text="")
            l10.config(text="")
            l12.config(text="")
            l14.config(text="")
            l16.config(text="")
            l18.config(text="")
            l20.config(text="")
            l22.config(text="")
            l24.config(text="")
            l26.config(text="")

        con.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Define the main window
stdres = Tk()
stdres.title("Student Result")
stdres.geometry("800x500")

# Labels and Inputs
l1 = Label(stdres, text="Student Result", font=("Times New Roman", 20), fg="red")
l2 = Label(stdres, text="Enter HALL TICKET:", font=("Times New Roman", 18))
t2 = Entry(stdres)
b = Button(stdres, text="SUBMIT", font=("Times New Roman", 18), command=display_result)
l3 = Label(stdres, text="NAME:", font=("Times New Roman", 18))

# Result Labels
l4 = Label(stdres, text="")
l5 = Label(stdres, text="Subject",font=("Times New Roman", 18))
l6 = Label(stdres, text="Marks",font=("Times New Roman", 18))
l7 = Label(stdres, text="Telugu")
l8 = Label(stdres, text="")
l9 = Label(stdres, text="Hindi")
l10 = Label(stdres, text="")
l11 = Label(stdres, text="English")
l12 = Label(stdres, text="")
l13 = Label(stdres, text="Maths")
l14 = Label(stdres, text="")
l15 = Label(stdres, text="Physics")
l16 = Label(stdres, text="")
l17 = Label(stdres, text="Chemistry")
l18 = Label(stdres, text="")
l19 = Label(stdres, text="Social")
l20 = Label(stdres, text="")
l21 = Label(stdres, text="Total")
l22 = Label(stdres, text="")
l23 = Label(stdres, text="Percentage")
l24 = Label(stdres, text="")
l25 = Label(stdres, text="Result")
l26 = Label(stdres, text="")

# Grid Layout
l1.grid(row=0, column=1)
l2.grid(row=1, column=0)
t2.grid(row=1, column=1)
b.grid(row=1, column=2)
l3.grid(row=2, column=1)
l4.grid(row=3, column=1)
l5.grid(row=4, column=0)
l6.grid(row=4, column=1)
l7.grid(row=5, column=0)
l8.grid(row=5, column=1)
l9.grid(row=6, column=0)
l10.grid(row=6, column=1)
l11.grid(row=7, column=0)
l12.grid(row=7, column=1)
l13.grid(row=8, column=0)
l14.grid(row=8, column=1)
l15.grid(row=9, column=0)
l16.grid(row=9, column=1)
l17.grid(row=10, column=0)
l18.grid(row=10, column=1)
l19.grid(row=11, column=0)
l20.grid(row=11, column=1)
l21.grid(row=12, column=0)
l22.grid(row=12, column=1)
l23.grid(row=13, column=0)
l24.grid(row=13, column=1)
l25.grid(row=14, column=0)
l26.grid(row=14, column=1)

# Run the main loop
stdres.mainloop()
