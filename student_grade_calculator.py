#Global Scope
MIN_PASS_MARK = 50
def process_student_report():
    #Local 
    print("--- New Student Entry ---")
    #Only dashes are printed all is needed is to fill in
    Student_name = input("Enter the student's name: ")
    Student_name = Student_name.title()
    #Check for cheating
    Cheated = input("Did the student have identical test answers? (yes/no): ")
    if Cheated == "yes":
        print(f"\nFinal Report for {Student_name} : CHEATED")
        return
    try:
        Math = float(input("Enter Math score (0-100): "))
        Science = float(input("Enter Science score (0-100): "))
        History = float(input("Enter History score (0-100): "))
    except ValueError:
        print("Invalid input. Please enter numeric values only")
        return
    #Sort marks from highest to lowest
    marks = [Math,Science,History]
    marks.sort(reverse=True)
    #Separate best and average scores
    best_scores = marks[0:2]
    lower_score = marks[2]
    #Calculate average 
    Final_average = sum(best_scores) + lower_score / 3
    def determine_letter_grade(average_score):
        if average_score >= 90:
            return "A"
        elif average_score >= 80:
            return "B"
        elif average_score >= 70:
            return "C"
        elif average_score >= 50:
            return "D"
        else:
            return "F"
    def determine_status(average_score):
        if average_score >= MIN_PASS_MARK:
            return "PASS"
        else:
            return "FAIL"
    #Calling the functions
    letter_grade = determine_letter_grade(Final_average)
    status = determine_status(Final_average)

    print("\n" + "=" * 30)
    print(f"Student report for {Student_name}")
    print(f"Final Average: {Final_average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"Status: {status}")
    print("=" *30)
    #The "=" *30 is a string multiplication that creates a line of 30 equal signs for formatting the report.
    # Just for order after calculations

if __name__ == "__main__":
    process_student_report()






              