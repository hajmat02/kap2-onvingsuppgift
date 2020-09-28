svar = input('Hur många grader Fahrenheit?') 
f = float(svar) # f varibeln innerhåller konverterat grader Fahrenheit till float
c = (f-32)*5/9 # c variabeln är <ntalet grader Celsius
print(f'Det är {c:.2f} grader Celsius')