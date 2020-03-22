import unittest
from pdeffer.generate_pdf import generate_pdf
from pdeffer.utils import setup_logging


class TestGeneratePdf(unittest.TestCase):
    def test__basic_pdf_generation(self):
        """Verify that a PDF is created from the provided HTML"""
        generate_pdf("./data/basic", ".")

        self.assertTrue(False)


if __name__ == "__main__":
    setup_logging()
    unittest.main()
