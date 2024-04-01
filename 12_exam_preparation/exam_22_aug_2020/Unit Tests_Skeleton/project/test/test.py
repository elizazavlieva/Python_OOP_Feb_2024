from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTest(TestCase):
    def setUp(self) -> None:
        self.student = StudentReportCard("Ivan", 1)

    def test_init(self):
        self.assertEqual("Ivan", self.student.student_name)
        self.assertEqual(1, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

        self.student.school_year = 12
        self.assertEqual(12, self.student.school_year)

    def test_invalid_student_name(self):

        with self.assertRaises(ValueError) as ve:
            StudentReportCard("", 5)

        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_invalid_school_year(self):
        with self.assertRaises(ValueError) as ve:
            StudentReportCard("Ivan", 0)

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            StudentReportCard("Ivan", 15)

        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_add_grade(self):
        self.student.add_grade("Math", 5)
        self.assertEqual({"Math": [5]}, self.student.grades_by_subject)

        self.student.add_grade("Music", 6)
        self.assertEqual({"Math": [5], "Music": [6]}, self.student.grades_by_subject)

        self.student.add_grade("Math", 5)
        self.assertEqual({"Math": [5, 5], "Music": [6]}, self.student.grades_by_subject)

    def test_avg_grade_by_subjects(self):
        self.student.grades_by_subject = {"Math": [6, 5], "Music": [6, 4], "History": [6, 5, 5]}
        message = "Math: 5.50\nMusic: 5.00\nHistory: 5.33"
        self.assertEqual(message, self.student.average_grade_by_subject())

    def test_avg_grade_for_all_subjects(self):
        self.student.grades_by_subject = {"Math": [6, 5], "Music": [6, 4], "History": [6, 5, 5]}
        message = "Average Grade: 5.29"

        self.assertEqual(message, self.student.average_grade_for_all_subjects())

    def test_repr(self):
        self.student.grades_by_subject = {"Math": [6, 5], "Music": [6, 4], "History": [6, 5, 5]}
        message = "Name: Ivan\n" \
                  "Year: 1\n" \
                  "----------\n" \
                  "Math: 5.50\n" \
                  "Music: 5.00\n" \
                  "History: 5.33\n" \
                  "----------\n" \
                  "Average Grade: 5.29"

        self.assertEqual(message, repr(self.student))

if __name__ == "__main__":
    main()
