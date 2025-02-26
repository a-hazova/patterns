from abc import ABC, abstractmethod


class Translator(ABC):
    @abstractmethod
    def translate(self, text: str) -> str:
        pass


class TranslatorFactory(ABC):
    @abstractmethod
    def create_translator(self, language: str) -> Translator:
        pass


class GermanTranslator(Translator):
    def __init__(self):
        self.dictionary = {
            'hello': 'hallo',
            'world': 'der Welt',
            'cat': 'die Katze',
            'dog': 'der Hund'
        }

    def translate(self, text: str) -> str:
        try:
            return self.dictionary[text]
        except KeyError:
            return f'Translation not found for "{text}"'


class RussianTranslator(Translator):
    def __init__(self):
        self.dictionary = {
            'hello': 'привет',
            'world': 'мир',
            'cat': 'кошка',
            'dog': 'собака'
        }

    def translate(self, text: str) -> str:
        try:
            return self.dictionary[text]
        except KeyError:
            return f'Translation not found for "{text}"'


class TranslatorFactoryImpl(TranslatorFactory):
    def create_translator(self, language: str) -> Translator:
        if language == 'german':
            return GermanTranslator()
        elif language == 'russian':
            return RussianTranslator()
        else:
            raise ValueError(f'Unsupported language: {language}')

if __name__ == '__main__':
    factory = TranslatorFactoryImpl()
    text = ["cat", "dog", "world"]
    german = factory.create_translator('german')
    russian = factory.create_translator('russian')
    german_translation = ', '.join([german.translate(word) for word in text])
    russian_translation = ', '.join([russian.translate(word) for word in text])
    print(f'German Translation: {german_translation}')
    print(f'Russian Translation: {russian_translation}')
    