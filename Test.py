import unittest
from main import Student

class StudentTest(unittest.TestCase):
    def test_walk(self):
        student = Student('Вася')
        for i in range(10):
            student.walk()
        result = student.distance
        self.assertEqual(result, 50, f'Дистанции не равны {result}! = 50')

    def test_run(self):
        student = Student('Вася')
        for i in range(10):
            student.run()
        result_2 = student.distance
        self.assertEqual(result_2, 100, f'Дистанции не равны {result_2}! = 100')

    def test_equal(self):
        student = Student('Вася')
        for i in range(10):
            student.walk()
        result = student.distance
        student_2 = Student('Коля')
        for i in range(10):
            student.run()
        result_2 = student.distance
        self.assertLess(result, result_2, f'{result} Должен преодолеть дистанцию больше, чем {result_2}')



if __name__ == '__main':
    unittest.main()