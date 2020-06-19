def pytest_collection_modifyitems(items):
    for item in items:
        if "integration" in str(item.module):
            item.add_marker('integration')


