
def pytest_configure(config):
    import src.generators
    import src.context_manager
    import src.iterators
    import src.decorators

    import sys
    sys.modules['generators'] = sys.modules['src.generators']
    sys.modules['context_manager'] = sys.modules['src.context_manager']
    sys.modules['iterators'] = sys.modules['src.iterators']
    sys.modules['decorators'] = sys.modules['src.decorators']
