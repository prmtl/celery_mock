from collections import defaultdict

import mock


_celery_mock_history = defaultdict(mock.Mock)


class MockedTaskMixin(object):

    def apply_async(self, *args, **kwargs):
        task_name = self.name
        # Mock.__call__ records calls to object
        _celery_mock_history[task_name].__call__(*args, **kwargs)

    @property
    def mock(self):
        return _celery_mock_history[self.name]


def mock_celery_task(celery_app):
    celery_app.Task = type('Task', (MockedTaskMixin, celery_app.Task), {})


def reset_celery_mocks():
    for mock_obj in _celery_mock_history.values():
        mock_obj.reset_mock()
