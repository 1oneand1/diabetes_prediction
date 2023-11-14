# This is a app that will predict if a person has diabetes or not

# The app will take in the following inputs:
# 1. Pregnancies, 2. Glucose, 3. BloodPressure, 4. SkinThickness, 5. Insulin, 6. BMI, 7. DiabetesPedigreeFunction, 8. Age

# The app will output a prediction of 0 or 1
# 0 = No diabetes, 1 = Diabetes, 2 = Error, 3 = Invalid Input, 4 = Invalid Input, 5 = Invalid Input, 6 = Invalid Input, 7 = Invalid Input, 8 = Invalid Input

import tkinter as tk
from tkinter import *
import joblib
from tkinter import messagebox

diabetes_prediction_Model = joblib.load('diabetes_prediction_Model.pkl')
#import os 
#print(os.getcwd())

def analyze():
    # get the values from the entries
    preg = float(entry_pregnancies.get())
    gluco = float(entry_glucose.get())
    bp = float(entry_bloodpressure.get())
    stinmm = float(entry_skinthickness.get())
    insulin = float(entry_insulin.get())
    mass = float(entry_bmi.get())
    dpf = float(entry_diabetesfunction.get())
    age = float(entry_age.get())
    # create a 2D array with the values
    values = [[preg, gluco, bp, stinmm, insulin, mass, dpf, age]]
    # model prediction
    prediction = diabetes_prediction_Model.predict(values)
    if prediction[0] == 1:
        messagebox.showinfo("Prediction", "The model predicts: Diabetes ")
    else:
        messagebox.showinfo("Prediction", "The model predicts: No Diabetes")
   

root = tk.Tk()
root.title("Diabetes Prediction App")
root.geometry("600x600")
root.configure(bg='light blue')

# This is a label widget
label0 = tk.Label(root, text="Does this person have diabetes?", bg='light blue', font=('arial', 14, 'bold'))
label0.grid(row=0, column=1)  # This will place label0 at position (0,0)

label_pregnancies = tk.Label(root, text="Pregnancies", bg='light blue')
label_pregnancies.grid(row=1, column=0)  # This will place label_pregnancies at position (0,0)

entry_pregnancies = tk.Entry(root)
entry_pregnancies.grid(row=1, column=1)  # This will place entry_pregnancies at position (0,1)

label_glucose = tk.Label(root, text="Glucose", bg="light blue")
label_glucose.grid(row=2, column=0)  # This will place label_glucose at position (1,0)

entry_glucose = tk.Entry(root)
entry_glucose.grid(row=2, column=1)  # This will place entry_glucose at position (1,1)

label_bloodpressure = tk.Label(root, text="BloodPressure", bg="light blue")
label_bloodpressure.grid(row=3, column=0)  # This will place label_bloodpressure at position (2,0)

entry_bloodpressure = tk.Entry(root)
entry_bloodpressure.grid(row=3, column=1)  # This will place entry_bloodpressure at position (2,1)

label_skinthickness = tk.Label(root, text="SkinThickness", bg="light blue")
label_skinthickness.grid(row=4, column=0)  # This will place label_skinthickness at position (3,0)

entry_skinthickness = tk.Entry(root)
entry_skinthickness.grid(row=4, column=1)  # This will place entry_skinthickness at position (3,1)

label_insulin = tk.Label(root, text="Insulin", bg="light blue")
label_insulin.grid(row=5, column=0)  # This will place label_insulin at position (4,0)

entry_insulin = tk.Entry(root)
entry_insulin.grid(row=5, column=1)  # This will place entry_insulin at position (4,1)

label_bmi = tk.Label(root, text="BMI", bg="light blue")
label_bmi.grid(row=6, column=0)  # This will place label_bmi at position (5,0)

entry_bmi = tk.Entry(root)
entry_bmi.grid(row=6, column=1)  # This will place entry_bmi at position (5,1)

label_diabetesfunction = tk.Label(root, text="DiabetesPedigreeFunction", bg="light blue")
label_diabetesfunction.grid(row=7, column=0)  # This will place label_diabetesfunction at position (6,0)

entry_diabetesfunction = tk.Entry(root)
entry_diabetesfunction.grid(row=7, column=1)  # This will place entry_diabetesfunction at position (6,1)

label_age = tk.Label(root, text="Age", bg="light blue")
label_age.grid(row=9, column=0)  # This will place label_age at position (7,0)

entry_age = tk.Entry(root)
entry_age.grid(row=9, column=1)  # This will place entry_age at position (7,1)

# This is a button to Analyze the data
button1 = tk.Button(root, text="Analyze", bg="blue", foreground="white", command=analyze)
button1.grid(row=10, column=1)  # This will place button1 at position (8,1)

root.mainloop()




