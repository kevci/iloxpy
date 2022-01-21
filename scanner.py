from imp import source_from_cache
import tokentype

class Scanner:
    def __init__(self, source: str) -> None:
        self.source = source 
        self.tokens = []
