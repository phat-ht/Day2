import random

def multiply(questions=10):
    correct = 0
    for i in range(1, questions + 1):
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        answer = int(input(f"{num1} x {num2} = "))
        if answer == num1 * num2:
            correct += 1
            print("Correct!")
        else:
            print(f"Incorrect. The answer is {num1 * num2}.")
    print(f"\nYou got {correct} out of {questions} questions correct.")

if __name__ == "__main__":
    multiply()
