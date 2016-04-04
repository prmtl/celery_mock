def pytest_sessionstart(session):
    from celery_mock import mock_celery_task
    from my_app import celery_app
    mock_celery_task(celery_app)


def pytest_runtest_teardown(item, nextitem):
    from celery_mock import reset_celery_mocks
    reset_celery_mocks()
