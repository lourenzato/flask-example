import unittest
from flask_example import hello_world


class ExampleFlaskTestCase(unittest.TestCase):

    def test_hello_world(self):
        """ Testando o retorno de hello world """
        self.assertEqual(hello_world(), '<p>Hello, world!</p>')


if __name__ == "__main__":
    unittest.main()