# Function to calculate grade based on average marks
def calculate_percentage(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


print("Enter the marks of four subjects:")
subject_1 = float(input("Subject 1: "))
subject_2 = float(input("Subject 2: "))
subject_3 = float(input("Subject 3: "))
subject_4 = float(input("Subject 4: "))



total = subject_1 + subject_2 + subject_3 + subject_4 
average = total / 4
percentage = (total / 400) * 100

# Determine grade
grade = calculate_percentage(average)

# Display results
print("\nResults:")
print(f"Total Marks: {total} / 400")
print(f"Average Marks: {average}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
