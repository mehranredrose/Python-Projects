class singleton:
    """
    Singleton is a creational design pattern that lets you ensure that 
    a class has only one instance, 
    while providing a global access point to this instance.
    """
    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(*args, **kwargs)
        return cls.instance
