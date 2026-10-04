import unittest

from ats import calculate_experience_score


class ATSExperienceScoreTests(unittest.TestCase):
    def test_numeric_years_return_different_scores(self):
        self.assertEqual(calculate_experience_score(0), 0)
        self.assertEqual(calculate_experience_score(0.5), 20)
        self.assertEqual(calculate_experience_score(2), 60)
        self.assertEqual(calculate_experience_score(4), 80)
        self.assertEqual(calculate_experience_score(6), 100)

    def test_string_years_are_parsed(self):
        self.assertEqual(calculate_experience_score("2 years"), 60)
        self.assertEqual(calculate_experience_score("3+ yrs"), 80)
        self.assertEqual(calculate_experience_score("6 year"), 100)


if __name__ == "__main__":
    unittest.main()
