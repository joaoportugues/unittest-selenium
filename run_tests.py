import unittest
from html_reporter import HTMLTestRunner

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    tests = loader.discover(start_dir="tests", pattern="test_*.py")
    suite.addTests(tests)

    runner = HTMLTestRunner(
        report_filepath="my_report.html",
        title="My unit test",
        description="This demonstrates the report output by HTMLTestRunner.",
        open_in_browser=True
    )

    runner.run(suite)

