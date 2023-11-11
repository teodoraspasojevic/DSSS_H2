import unittest
from math_quiz import generate_random_int, generate_random_operator, calculate_math_operation


class TestMathGame(unittest.TestCase):

    def test_generate_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if random operator is from the given list of operations
        operators = ['+', '-', '*']
        for _ in range(10):
            rand_operator = generate_random_operator()
            self.assertTrue(rand_operator in operators)

    def test_compute_math_operation(self):
        # Test if compute_math_operation works in all cases
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (5, 0, '+', '5 + 0', 5),
                (5, 0, '-', '5 - 0', 5),
                (5, 0, '*', '5 * 0', 0),
                (-5, 2, '+', '-5 + 2', -3),
                (5, -2, '-', '5 - -2', 7),
                (5, -5, '*', '5 * -5', -25)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                computed_problem, computed_answer = calculate_math_operation(num1, num2, operator)
                self.assertTrue(expected_problem == computed_problem)
                self.assertTrue(expected_answer == computed_answer)


if __name__ == "__main__":
    unittest.main()
