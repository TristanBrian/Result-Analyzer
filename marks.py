def get_marks(num_subjects):
    """Get marks from the user for the specified number of subjects."""
    marks = []
    for i in range(num_subjects):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i + 1}: "))
                if mark < 0:
                    print("Please enter a non-negative value.")
                else:
                    marks.append(mark)
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return marks

def calculate_average(marks):
    """Calculate the average of the given marks."""
    if marks:
        return sum(marks) / len(marks)
    return 0

def display_results(marks, average):
    """Display the marks and the average."""
    print("\nMarks entered:")
    for i, mark in enumerate(marks, start=1):
        print(f"Subject {i}: {mark:.2f}")
    print(f"\nAverage marks: {average:.2f}")

def main():
    """Main function to execute the program."""
    while True:
        try:
            num_subjects = int(input("Enter the number of subjects: "))
            if num_subjects <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    marks = get_marks(num_subjects)
    average = calculate_average(marks)
    display_results(marks, average)

if __name__ == "__main__":
    main()