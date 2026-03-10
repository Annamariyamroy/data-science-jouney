def bmi_calculator(weight,height):

    if weight<=0 or height<=0:
        raise ValueError("Height and weight must be positive numbers")
    height= height/100
    bmi= round(weight/height**2,2)
    return bmi
def display(bmi):
    print("-.-.-.-.BMI.-.-.-.-.")
    print("BMI: " ,bmi)
    if bmi<18.5:
        print(" Category: Underweight")
        print("Tip: Eat nutrient-dense foods, increase protein intake, and do strength training to gain healthy weight.")
    elif bmi>=18.5 and bmi<=24.9:
        print("Category: Normal Weight")
        print("Tip: Maintain balanced meals, regular exercise, and consistent sleep to stay healthy.")
    elif bmi>=25.0 and bmi<=29.9:
        print("Category: Over Weight")
        print("Tip: Reduce processed foods, increase physical activity, and focus on portion control.")
    else:
        print("Category: Obesity")
        print("Tip:Follow a structured diet, increase daily activity, and consult a healthcare professional for weight management.")



try:
    print("Welcome to BMI Calculator")
    weight=float(input("Enter your weight in Kg: "))
    height=float(input("Enter your height in cm:  "))
    result=bmi_calculator(weight,height)
    display(result)

except ValueError as e:
    print(f'Error : {e}')






