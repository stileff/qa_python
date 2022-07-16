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

    #Проверяем, что get_books_with_specific_rating() правильно получает список
    def test_get_books_with_specific_rating_filter_rating_list_length_is_correct(self):
        #Создаем список из книг
        dict_with_books = {
            'Золотой ключик или приключения Буратино': 4,
            'Властелин Колец': 10,
            'Чума': 10,
            'Алые паруса': 7
        }
        specific_rating = 10

        collector = BooksCollector()

        #Добавляем список книг в объект BooksCollector
        for key, value in dict_with_books.items():
            collector.add_new_book(key)
            collector.set_book_rating(key, value)

        #Получаем список книг соответствующих specific_rating
        lst_filtred_books_by_specific_rating = collector.get_books_with_specific_rating(specific_rating)

        assert len(lst_filtred_books_by_specific_rating) == 2

    #Проверяем добавление книги в favorities методом add_book_in_favorites
    def test_add_book_in_favorites_name_is_added_to_favorite(self):
        book_name = 'Пришвин. Кладовая солнца'

        collector = BooksCollector()
        collector.add_new_book(book_name)

        assert collector.books_rating[book_name]

    #Проверяем, что метод get_list_of_favorites_books() правильно возвращает список книг
    def test_get_list_of_favorites_books_list_length_is_correct(self):
        # Создаем список из книг
        collector = BooksCollector()

        lst_of_books = ['Зеленая Миля', 'Дон Кихот', 'Гроза', 'Ромео и джульетта', 'Снеговик']
        for book in lst_of_books:
            collector.add_new_book(book)

        collector.add_book_in_favorites(lst_of_books[1])
        collector.add_book_in_favorites(lst_of_books[3])

        assert len(collector.get_list_of_favorites_books()) == 2
