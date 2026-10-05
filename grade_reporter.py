# List of student scores
scores = [72, 45, 90, 61, 38]

# Track passes, fails, and total score sum
passed_count = 0
failed_count = 0
total_score = 0

# Loop through each score to assign grades
for score in scores:
    total_score += score

    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"

    print(f"Score: {score} - Grade: {grade}")

    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

# Calculate average score
average_score = round(total_score / len(scores), 1)

# Display summary statistics
print("\n--- Summary ---")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
print(f"Average score: {average_score}")