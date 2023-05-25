import sys
import unittest
from io import StringIO
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)  # Ajoutez le répertoire parent au sys.path
from main import main


class MainTestCase(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """

    def test_output(self):
        # Créez un objet StringIO pour capturer la sortie standard
        captured_output = StringIO()
        sys.stdout = captured_output
        # Appelez la fonction main
        main()
        # Récupérez la sortie capturée
        output = captured_output.getvalue().strip()
        print(1)
        # Assert la sortie attendue
        self.assertEqual(output, "Hello, World!")


if __name__ == "__main__":
    unittest.main()
