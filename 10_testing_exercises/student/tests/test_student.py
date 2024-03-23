from unittest import TestCase, main

from student.project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        courses = {"OOP": ["new course"]}
        self.student = Student("Student1", courses)

    def test_validating_init(self):
        courses = {"OOP": ["new course"]}
        self.assertEqual(courses, self.student.courses)
        self.assertEqual("Student1", self.student.name)

    def test_validating_courses_if_empty_dict(self):
        self.student = Student("Student1")
        self.assertEqual({}, self.student.courses)

    def test_enroll_already_added_course(self):
        result = self.student.enroll("OOP", ["some text"], 'N')
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_with_notes_and_empty_add_course_notes(self):
        result = self.student.enroll("Advanced", ["previous course"])
        self.assertEqual(["previous course"], self.student.courses["Advanced"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_with_notes_and_add_course_notes(self):
        result = self.student.enroll("Advanced", ["previous course"], "Y")
        self.assertEqual(["previous course"], self.student.courses["Advanced"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_without_notes(self):
        result = self.student.enroll("Advanced", ["some notes"], "N")
        self.assertEqual([], self.student.courses["Advanced"])
        self.assertEqual("Course has been added.", result)

    def test_adding_notes(self):
        courses = {"OOP": ["new course", "some notes"]}
        result = self.student.add_notes("OOP", "some notes")
        self.assertEqual(courses, self.student.courses)
        self.assertEqual("Notes have been updated", result)

    def test_adding_notes_to_non_existent_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Advanced", "some notes")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leaving_existing_course(self):

        result = self.student.leave_course("OOP")
        self.assertEqual({}, self.student.courses)
        self.assertEqual("Course has been removed", result)

    def test_leaving_non_existing_course_and_raising_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Advanced")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
