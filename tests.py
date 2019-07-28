import unittest
from unittest import mock
import main


class TestModule(unittest.TestCase):

    def setUp(self):
        pass


    @unittest.mock.patch.object(main.TestClass, 'poorly_written_other_nested_function')
    @unittest.mock.patch.object(main.TestClass, 'poorly_written_nested_function')
    def test_function_which_uses_print_to_screen(self, mock_poorly_written_function, mock_poorly_written_other_function):
        mock_poorly_written_function.return_value = 2
        mock_poorly_written_other_function.return_value = 3

        object = main.TestClass('Called in Test')
        result = object.function_which_uses_poorly_written_nested_functions()


        self.assertEqual(result , 5)

if __name__ == '__main__':
    unittest.main()
