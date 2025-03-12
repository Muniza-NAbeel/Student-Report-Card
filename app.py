students = []  # To store data of all students

while True:
    print("\n--- Enter Student Details ---")
    name = input("Enter Your Name: ")
    roll_number = input("Enter Roll Number: ")
    marks = int(input("Enter Maximum Marks: "))
    
    try:
        maths = float(input("Enter Maths Marks: "))
        english = float(input("Enter English Marks: "))
        urdu = float(input("Enter Urdu Marks: "))
        biology = float(input("Enter Biology Marks: "))
        chemistry = float(input("Enter Chemistry Marks: "))
    except ValueError:
        print("Error: Please enter valid numeric marks.")
        continue

    if any(subject > marks for subject in [maths, english, urdu, biology, chemistry]):
        print("Error: Marks must be a number between 0 and the maximum marks.")
        print("Please re-enter the details correctly.")
        continue

    totalmarks = maths + english + urdu + biology + chemistry
    percentage = (totalmarks / (5 * marks)) * 100

    # Grade Calculation
    if percentage >= 80:
        grade = "A+"
    elif percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    # Display Individual Report
    print(f"\n--- Report Card for {name} ---")
    print(f"Roll Number: {roll_number}")
    print(f"Maths: {maths}, English: {english}, Urdu: {urdu}, Biology: {biology}, Chemistry: {chemistry}")
    print(f"Total Marks: {totalmarks} / {5 * marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("\nRecord of", name, "inserted successfully.")

    # Store Student Data
    students.append({
        "name": name,
        "roll_number": roll_number,
        "percentage": percentage,
        "grade": grade,
    })

    # Ask if the user wants to create another report card
    while True:
        choice = input("\nDo you want to create another report card? (Yes/No): ").strip().lower()
        if choice in ["yes", "no"]:
            break
        print("Invalid input! Please enter 'Yes' or 'No'.")

    if choice == "no":
        print("\n--- Summary of All Students ---")
        for student in students:
            print(f" Student Name: {student['name']}, Roll Number: {student['roll_number']}, Percentage: {student['percentage']:.2f}%, Grade: {student['grade']}")
        print("\nThank you for using the Report Card Generator!")
        break
