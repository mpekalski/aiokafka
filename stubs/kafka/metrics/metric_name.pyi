from typing import Any, Optional

class MetricName:
    def __init__(self, name: Any, group: Any, description: Optional[Any] = ..., tags: Optional[Any] = ...) -> None: ...
    @property
    def name(self): ...
    @property
    def group(self): ...
    @property
    def description(self): ...
    @property
    def tags(self): ...
    def __hash__(self) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
