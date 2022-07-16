from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    #Тест на проверку установки рейтинга книги set_book_rating()
    def test_set_book_rating_add_rating_for_consist_book_is_set(self):

        #Создаем объект и добавляем книгу
        collector = BooksCollector()
        collector.add_new_book('Братья Карамазовы')

        #Устанавливаем рейтинг книге
        collector.set_book_rating('Братья Карамазовы', 7)

        #Проверка на корректность
        assert collector.books_rating['Братья Карамазовы'] == 7

    #Тест на корректность получения рейтинга по названию книги get_book_rating()
    def test_get_book_rating_name_book_is_correct_rating(self):
        #Создаем объект, добавляем книгу, устанавливаем рейтинг
        collector = BooksCollector()
        book_name = 'Война и мир'
        rate = 10

        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, rate)

        #Вызываем метод get_books_rating() и проверяем соответствие
        assert collector.get_book_rating(book_name) == rate

