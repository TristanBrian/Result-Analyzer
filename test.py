def calculate_additional_marks(current_average, completed_units, total_units, desired_average):
    # Calculate current total marks
    current_total_marks = current_average * completed_units
    
    # Calculate total marks required for the desired average across all units
    required_total_marks = desired_average * total_units
    
    # Calculate additional marks needed
    additional_marks_needed = required_total_marks - current_total_marks
    
    return additional_marks_needed

def main():
    # Get user values
    try:
        current_average = float(input("Enter your Average: "))
        completed_units = int(input("Enter the number of completed units: "))
        total_units = int(input("Enter the total number of units: "))
        desired_average = float(input("Enter desired average: "))

        # Calculate additional marks needed
        additional_marks = calculate_additional_marks(current_average, completed_units, total_units, desired_average)

        if additional_marks > 0:
            remaining_units = total_units - completed_units
            min_average_per_unit = additional_marks / remaining_units
            
            print(f"You need to score at least {additional_marks:.2f} marks in the remaining units to achieve an average of {desired_average}.")
            print(f"This means you need to score at least an average of {min_average_per_unit:.2f} in each of the remaining {remaining_units} units.")
        else:
            print("You are already on track to achieve the desired average with your current scores.")
    
    except ValueError:
        print("Enter valid numeric values.")

if __name__ == "__main__":
    main()