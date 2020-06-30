from typing import Callable, Any


class Action:
    def __init__(self, function: Callable, *args: Any, **kwargs: Any):
        self.function = function
        self.args = [*args]
        self.kwargs = {**kwargs}

    def __call__(self):
        return self.function(*self.args, **self.kwargs)

