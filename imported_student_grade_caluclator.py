from student_grade_calculator import process_student_report
def run_grading_system():
    running = True
    print("---Welcome to the School Grading System---")
    #This loop continues as long as running is True
    while running:
        #Call imported function from other file
        process_student_report()
        #Ask user if they want to process another report
        choice = input("Do you want to process another student report? (yes/no): ").strip().lower()
        if choice.lower() != "yes":
            running = False
            print("Exiting the grading system. Goodbye!")
if __name__ == "__main__":    
    run_grading_system()