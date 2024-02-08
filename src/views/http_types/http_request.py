from typing import Dict

class HttpRequest: # -> PascalCase
    def __init__(  # -> Constructor method
            self,
            header: Dict = None,
            body: Dict = None,
            query_params: Dict = None
        ) -> None:
        self.header = header  # -> Attributes that saving all elements on entry
        self.body = body
        self.query_params = query_params
