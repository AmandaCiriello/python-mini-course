"""
Celsius to Fahrenheit Temperature Converter

Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is as follows:
  F = (9/5)C + 32
The program should ask the user to enter a temperature in Celsius, then display the temperature converted to Fahrenheit.
"""
Celsius = input("Enter degree in Celsius: ")
Celsius = float(Celsius)
F = (9/5) * Celsius + 32
print(f"Degree in Fahrenheit is {F} degree")