class TestClass:
    def __init__(self, name):
        self.object_name = name

    def poorly_written_nested_function(self):

        return '1'

    def function_which_uses_print_to_screen(self):
        k = self.poorly_written_nested_function()
        return k



