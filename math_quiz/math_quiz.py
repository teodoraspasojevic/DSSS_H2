import random


def generate_random_int(min_value, max_value):
    """
    Generate a random int in range from min to max.

    Args:
        min_value (float): Minimum value that can be generated.
        max_value (float): Maximum value that can be generated.

    Returns:
        int: Randomly generated number in range of min_value and max_value.
    """
    # Convert min and max values to ints for function random.randint()
    min_value = int(min_value)
    max_value = int(max_value)
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generate a random math operator from list of operations ['+', '-', '*'].

    Returns:
        str: String representing randomly chosen math operation from list ['+', '-', '*'].
    """
    return random.choice(['+', '-', '*'])


def calculate_math_operation(operator_1, operator_2, operation):
    """
    Calculate the given math operation over two given operands.

    Args:
         operator_1(int): First operand participating in math operation.
         operator_2(int): Second operand participating in math operation.
         operation(str): Math operation that should be performed on operators.
    Returns:
         str: String displaying the performed math operation.
         int: Result of the calculated math operation.
    """
    problem = f"{operator_1} {operation} {operator_2}"
    if operation == '+':
        answer = operator_1 + operator_2
    elif operation == '-':
        answer = operator_1 - operator_2
    else:
        answer = operator_1 * operator_2
    return problem, answer


def math_quiz():
    """
    Perform a math quiz.

    The function generates a randomly chosen math operation. Operation is displayed to the user and user's answer is
    saved. If user's answer is correct, user gets one point.

    User Input:
        - Integer input for the math quiz answers.
    Returns:
        None
    """
    score = 0
    total = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problem, and you need to provide the correct answers.")

    for _ in range(total):
        # Generate random math operation
        operator_1 = generate_random_int(1, 10)
        operator_2 = generate_random_int(1, 5.5)
        operation = generate_random_operator()

        problem, answer = calculate_math_operation(operator_1, operator_2, operation)

        # Display the question and save the user's answer
        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter an int math operation result.")

        # Compare user's answer with correct result of the operation. Catch exception when invalid input.
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
    print(f"\nGame over! Your score is: {score}/{total}")


if __name__ == "__main__":
    math_quiz()
