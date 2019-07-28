class TestClass:
    def __init__(self, name):
        self.object_name = name

    def poorly_written_nested_function(self):
        return 1

    def poorly_written_other_nested_function(self):
        return 2

    def function_which_uses_poorly_written_nested_functions(self):
        k = self.poorly_written_nested_function()
        l = self.poorly_written_other_nested_function()
        return k + l



