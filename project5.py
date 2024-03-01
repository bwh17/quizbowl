import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('FridayProj5.db')
cursor = connection.cursor()

# Find the table name in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_name = cursor.fetchone()[0]

# Fetch questions and answers from the table
cursor.execute(f"SELECT question, answer FROM {table_name};")
questions_and_answers = cursor.fetchall()

# Close the database connection
connection.close()

# Create a variable to store the score
correct_answers = 0

# Use a for loop to ask questions
for question, correct_answer in questions_and_answers:
    print(question)

    # Ask the user to enter their answer
    user_answer = input("Your answer: ")

    # Verify if the answer the user entered was correct or not, and use the .lower() method
    correct = user_answer.lower() == correct_answer.lower()

    # Display for the user if their answer was correct or not
    if correct:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")

# Display the results
print("Quiz ended.")
print(f"You scored {correct_answers}/{len(questions_and_answers)}.")