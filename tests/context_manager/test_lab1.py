from context_manager.lab1 import MyContextManager


def test_my_context_manager():
    with MyContextManager():
        print('Run')
