from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass

class Publisher(ABC):
    def __init__(self):
        self._subscribers = []

    @abstractmethod
    def subscribe(self, subscriber: Subscriber) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, subscriber: Subscriber) -> None:
        pass

    @abstractmethod    
    def notify_subscribers(self, message) -> None:
        pass

class PostPublisher(Publisher):
    def __init__(self):
        super().__init__()
    
    def subscribe(self, subscriber):
        return self._subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber):
        return self._subscribers.remove(subscriber)
    
    def notify_subscribers(self, message: str) -> None:
        for subscriber in self._subscribers:
            subscriber.update(message)

class PostSubscriber(Subscriber):
    def __init__(self, name: str):
        self.name = name
    
    def update(self, message: str) -> None:
        print(f'{self.name} received new post: {message}')

if __name__ == "__main__":
    publisher = PostPublisher()
    subscriber1 = PostSubscriber('John Doe')
    subscriber2 = PostSubscriber('Jane Smith')

    publisher.subscribe(subscriber1)
    publisher.subscribe(subscriber2)

    publisher.notify_subscribers('New article: The Evolution of Technology')