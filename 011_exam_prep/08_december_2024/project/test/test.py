import unittest
from project_1.senior_student import SeniorStudent


class TestSeniorStudent(unittest.TestCase):

    def setUp(self):
        self.test_student = SeniorStudent(student_id="1234", name="Valid Name", student_gpa=3.5)

    def test_correct_init(self):
        self.assertEqual(self.test_student.student_id, "1234")
        self.assertEqual(self.test_student.name, "Valid Name")
        self.assertEqual(self.test_student.student_gpa, 3.5)
        self.assertEqual(len(self.test_student.colleges), 0)

    def test_student_id_too_short(self):
        with self.assertRaises(ValueError) as context:
            self.test_student.student_id = "123"
        self.assertEqual(str(context.exception), "Student ID must be at least 4 digits long!")

        with self.assertRaises(ValueError) as context:
            self.test_student.student_id = " 123 "
        self.assertEqual(str(context.exception), "Student ID must be at least 4 digits long!")

    def test_student_id_with_spaces__strip(self):
        self.test_student.student_id = " 1234 "
        self.assertEqual(self.test_student.student_id, "1234")

    def test_name_valid(self):
        self.test_student.name = "Bozhko Kamen"
        self.assertEqual(self.test_student.name, "Bozhko Kamen")

        self.test_student.name = "Bozhko Kamen"
        self.assertEqual(self.test_student.name, "Bozhko Kamen")

    def test_name_empty(self):
        with self.assertRaises(ValueError) as context:
            self.test_student.name = ""
        self.assertEqual(str(context.exception), "Student name cannot be null or empty!")

        with self.assertRaises(ValueError) as context:
            self.test_student.name = "  "
        self.assertEqual(str(context.exception), "Student name cannot be null or empty!")

    def test_gpa_valid(self):
        self.test_student.student_gpa = 1.001
        self.assertEqual(self.test_student.student_gpa, 1.001)

    def test_gpa_exact_boundary(self):
        with self.assertRaises(ValueError) as context:
            self.test_student.student_gpa = 1.0
        self.assertEqual(str(context.exception), "Student GPA must be more than 1.0!")

    def test_gpa_below_boundary(self):
        with self.assertRaises(ValueError) as context:
            self.test_student.student_gpa = 0.99
        self.assertEqual(str(context.exception), "Student GPA must be more than 1.0!")

    def test_gpa_valid_above_boundary(self):
        self.test_student.student_gpa = 1.11
        self.assertEqual(self.test_student.student_gpa, 1.11)

    def test_apply_to_college__success(self):
        result = self.test_student.apply_to_college(gpa_required=3.0, college_name="Harvard")
        self.assertEqual(result, 'Valid Name successfully applied to Harvard.')
        self.assertIn("HARVARD", self.test_student.colleges)
        self.assertEqual(len(self.test_student.colleges), 1)

    def test_apply_to_college_failure__gpa_too_low(self):
        result = self.test_student.apply_to_college(gpa_required=3.51, college_name="MIT")
        self.assertEqual(result, 'Application failed!')
        self.assertNotIn("MIT", self.test_student.colleges)
        self.assertEqual(len(self.test_student.colleges), 0)

    def test_apply_to_college_exact_gpa(self):
        result = self.test_student.apply_to_college(gpa_required=3.5, college_name="Stanford")
        self.assertEqual(result, 'Valid Name successfully applied to Stanford.')
        self.assertIn("STANFORD", self.test_student.colleges)
        self.assertEqual(len(self.test_student.colleges), 1)

    def test_apply_to_college_duplicate_application(self):
        self.test_student.apply_to_college(gpa_required=3.0, college_name="Harvard")
        self.test_student.apply_to_college(gpa_required=3.0, college_name="Harvard")
        self.assertEqual(len(self.test_student.colleges), 1)

    def test_apply_to_college__case_check(self):
        self.test_student.apply_to_college(gpa_required=3.0, college_name="Harvard")
        self.test_student.apply_to_college(gpa_required=3.0, college_name="harvarD")
        self.assertEqual(len(self.test_student.colleges), 1)

    def test_apply_to_college__multiple(self):
        self.test_student.apply_to_college(gpa_required=3.0, college_name="Harvard")
        self.test_student.apply_to_college(gpa_required=3.0, college_name="MIT")
        self.assertEqual(len(self.test_student.colleges), 2)
        self.assertIn("HARVARD", self.test_student.colleges)
        self.assertIn("MIT", self.test_student.colleges)

    def test_update_gpa_success(self):
        result = self.test_student.update_gpa(3.51)
        self.assertEqual(result, "Student GPA was successfully updated.")
        self.assertEqual(self.test_student.student_gpa, 3.51)

    def test_update_gpa_failure(self):
        result = self.test_student.update_gpa(1.0)
        self.assertEqual(result, "The GPA has not been changed!")
        self.assertEqual(self.test_student.student_gpa, 3.5)

        result = self.test_student.update_gpa(0.0)
        self.assertEqual(result, "The GPA has not been changed!")
        self.assertEqual(self.test_student.student_gpa, 3.5)

    def test_update_gpa_boundary(self):
        result = self.test_student.update_gpa(1.01)
        self.assertEqual(result, "Student GPA was successfully updated.")
        self.assertEqual(self.test_student.student_gpa, 1.01)

    def test_update_gpa_no_change(self):
        result = self.test_student.update_gpa(3.5)
        self.assertEqual(result, "Student GPA was successfully updated.")
        self.assertEqual(self.test_student.student_gpa, 3.5)  # No actual change

    def test_equality_same_gpa(self):
        student2 = SeniorStudent(student_id="5678", name="Jane Smith", student_gpa=3.5)
        self.assertTrue(self.test_student == student2)

    def test_equality_different_gpa__greater(self):
        student2 = SeniorStudent(student_id="5678", name="Jane Smith", student_gpa=3.8)
        self.assertFalse(self.test_student == student2)

    def test_equality_different_gpa__smaller(self):
        student2 = SeniorStudent(student_id="5678", name="Jane Smith", student_gpa=1.001)
        self.assertFalse(self.test_student == student2)


if __name__ == "__main__":
    unittest.main()
