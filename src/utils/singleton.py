class SingletonMeta(type):
    """Implements singleton class interface"""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call method"""
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
