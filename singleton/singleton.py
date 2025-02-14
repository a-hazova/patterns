from threading import Lock, Thread


class SingletionMeta(type):
    __instance = None
    __lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls.__lock: 
            if not cls.__instance:
                cls.__instance = super().__call__(*args, *kwargs)
        return cls.__instance

class Singleton(metaclass=SingletionMeta):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            raise ValueError('value can only be of type string')
    
    

def test_singleton(value):
    instance = Singleton(value)
    print(instance.value)

if __name__ == "__main__":
    process1 = Thread(target=test_singleton, args ='Первый')
    process2 = Thread(target=test_singleton, args = 'Второй')
    process3 = Thread(target=test_singleton, args = 112)
    process1.start()
    process2.start()
    process3.start()