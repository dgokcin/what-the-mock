import unittest
from unittest import mock
import main


def overridden_print():
    return 'you got overridden'


class TestModule(unittest.TestCase):

    def setUp(self):
        pass


    @unittest.mock.patch.object(main.TestClass, 'poorly_written_nested_function')
    def test_function_which_uses_print_to_screen(self, mock_poorly_written_function):
        mock_poorly_written_function.return_value = 'overridden return value'

        object = main.TestClass('Called in Test')
        result = object.function_which_uses_print_to_screen()


        self.assertEqual(result ,'overridden return value')

if __name__ == '__main__':
    unittest.main()
