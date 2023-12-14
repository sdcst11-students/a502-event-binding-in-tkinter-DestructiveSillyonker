"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""

import tkinter as tk

def display_information():
    name = name_entry.get()
    student_number = student_number_entry.get()
    grade = grade_entry.get()


    result_entry.delete(0, tk.END)
    result_entry.insert(0, f"Name: {name}, Student Number: {student_number}, Grade: {grade}")


app = tk.Tk()
app.title("Student Information Entry")


name_label = tk.Label(app, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1, padx=10, pady=10)

student_number_label = tk.Label(app, text="Student Number:")
student_number_label.grid(row=1, column=0, padx=10, pady=10)
student_number_entry = tk.Entry(app)
student_number_entry.grid(row=1, column=1, padx=10, pady=10)

grade_label = tk.Label(app, text="Grade:")
grade_label.grid(row=2, column=0, padx=10, pady=10)
grade_entry = tk.Entry(app)
grade_entry.grid(row=2, column=1, padx=10, pady=10)


display_button = tk.Button(app, text="Display Information", command=display_information)
display_button.grid(row=3, column=0, columnspan=2, pady=10)


result_entry = tk.Entry(app, width=40)
result_entry.grid(row=4, column=0, columnspan=2, pady=10)


app.mainloop()
