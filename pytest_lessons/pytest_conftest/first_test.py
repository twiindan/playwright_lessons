class TestClass:
    def test_first_class_check(self, setup_class, setup_function, setup_module, setup_session):
        print("\nThis is my first class test")

    def test_second_class_check(self, setup_class, setup_function, setup_module, setup_session):
        print("\nThis is my second class test")


def test_initial_check(setup_function, setup_module, setup_session):
    print("\nThis is my first test")