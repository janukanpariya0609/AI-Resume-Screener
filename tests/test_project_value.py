import unittest

from utils import create_profile_summary, normalize_project_count


class ProjectValueTests(unittest.TestCase):
    def test_normalize_project_count_handles_strings_and_lists(self):
        self.assertEqual(normalize_project_count("Projects: 3"), 3)
        self.assertEqual(normalize_project_count(["A", "B", "C"]), 3)
        self.assertEqual(normalize_project_count("No projects listed"), 0)

    def test_profile_summary_uses_plain_numeric_projects(self):
        candidate = {"Projects": "Projects: 4"}
        summary = create_profile_summary(candidate)
        self.assertEqual(summary["Projects"], "4")


if __name__ == "__main__":
    unittest.main()
