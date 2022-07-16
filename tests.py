from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    #Тест 1: Книга добавляется в словарь
    def test_add_new_book_name_book_is_added(self):
        collector = BooksCollector()
        book_name = 'Д.Карризи. Девушка в тумане'
        collector.add_new_book(book_name)

        assert book_name in collector.books_rating

    #Тест 2: Книге при добавлении присваивается рейтинг 1
    def test_add_new_book_rating_is_one(self):
        # Создаем объект и добавляем книгу
        collector = BooksCollector()
        book_name = 'Трое из Простоквашино'
        collector.add_new_book(book_name)

        assert collector.books_rating[book_name] == 1

    #Тест 3: Установка рейтинга книги set_book_rating()
    def test_set_book_rating_name_rating_for_consist_book_is_set(self):

        #Создаем объект и добавляем книгу
        collector = BooksCollector()
        collector.add_new_book('Братья Карамазовы')

        #Устанавливаем рейтинг книге
        collector.set_book_rating('Братья Карамазовы', 7)

        assert collector.books_rating['Братья Карамазовы'] == 7

    #Тест 4: Нет возможности установить рейтинг вне диапазона от 1 до 10
    def test_set_book_rating_name_rating_not_set_incorrect_rating(self):
        # Создаем объект и добавляем книгу
        collector = BooksCollector()
        collector.add_new_book('Ф. Фицджеральд. Великий Гэтсби')

        #Пытаемся установить рейтинг вне диапазона
        collector.set_book_rating('Ф. Фицджеральд. Великий Гэтсби', 11)

        assert collector.books_rating['Ф. Фицджеральд. Великий Гэтсби'] == 1

    #Тест 5: На корректность получения рейтинга по названию книги get_book_rating()
    def test_get_book_rating_name_book_is_correct_rating(self):
        #Создаем объект, добавляем книгу, устанавливаем рейтинг
        collector = BooksCollector()
        book_name = 'Война и мир'
        rate = 10

        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, rate)

        #Вызываем метод get_books_rating() и проверяем соответствие
        assert collector.get_book_rating(book_name) == rate

    #Тест 6: Проверяем, что get_books_with_specific_rating() правильно получает список
    def test_get_books_with_specific_rating_filter_rating_list_length_is_correct(self):
        #Создаем объект и список из книг
        collector = BooksCollector()
        dict_with_books = {
            'Золотой ключик или приключения Буратино': 4,
            'Властелин Колец': 10,
            'Чума': 10,
            'Алые паруса': 7
        }
        specific_rating = 10

        #Добавляем список книг в объект BooksCollector
        for key, value in dict_with_books.items():
            collector.add_new_book(key)
            collector.set_book_rating(key, value)

        #Получаем список книг соответствующих specific_rating
        lst_filtred_books_by_specific_rating = collector.get_books_with_specific_rating(specific_rating)

        assert len(lst_filtred_books_by_specific_rating) == 2

    #Тест 7: Проверяем, что метод get_books_rating() возвращает корректно
    def test_get_books_rating_return_correct_dict_books_rating(self):
        # Создаем объект и добавляем книгу
        collector = BooksCollector()
        collector.add_new_book('Стендаль. Красное и черное')

        #Устанавливаем рейтинг
        collector.set_book_rating('Стендаль. Красное и черное', 8)

        #Пытаемся получить ранее добавленную книгу с рейтингом
        result = collector.get_books_rating().get('Стендаль. Красное и черное')

        assert result == 8

    #Тест 8: Проверяем добавление книги в favorities методом add_book_in_favorites
    def test_add_book_in_favorites_name_is_added_to_favorite(self):
        # Создаем объект и добавляем книгу
        collector = BooksCollector()
        book_name = 'Пришвин. Кладовая солнца'
        collector.add_new_book(book_name)

        assert collector.books_rating[book_name]

    #Тест 9: Проверяем, что второй раз не добавить книгу в favorities
    def test_add_book_in_favorites_name_not_added_twice(self):
        # Создаем объект и добавляем книги
        collector = BooksCollector()
        lst_of_books = ['Ж.Верн. Дети капитана Гранта', 'Ф.Кафка. Процесс', 'М. Булгаков. Мастер и маргарита']
        for book in lst_of_books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        #Делаем попытку добавить еще раз книгу
        collector.add_book_in_favorites(lst_of_books[0])

        #Считаем кол-во совпадений в списке
        count = 0
        for book in collector.favorites:
            if book == lst_of_books[0]:
                count += 1

        assert count == 1

    #Тест 10: Проверяем, что метод get_list_of_favorites_books() правильно возвращает список книг
    def test_get_list_of_favorites_books_list_length_is_correct(self):
        # Создаем список из книг
        collector = BooksCollector()
        lst_of_books = ['Зеленая Миля', 'Дон Кихот', 'Гроза', 'Ромео и джульетта', 'Снеговик']
        for book in lst_of_books:
            collector.add_new_book(book)

        #Добавляем 2 книги в список избранных
        collector.add_book_in_favorites(lst_of_books[1])
        collector.add_book_in_favorites(lst_of_books[3])

        assert len(collector.get_list_of_favorites_books()) == 2

    #Тест 11: Проверяем удаление из списка favorities
    def test_delete_book_from_favorites_name_is_deleted(self):
        #Создаем объект и добавляем книги в список и избранное
        collector = BooksCollector()
        lst_books_name = ['Братья Стругацкие. Понедельник начинается в субботу', 'Джордж Оруэлл.1984']
        for book in lst_books_name:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        #Удаляем книгу из избранного
        collector.delete_book_from_favorites('Братья Стругацкие. Понедельник начинается в субботу')

        assert 'Братья Стругацкие. Понедельник начинается в субботу' not in collector.favorites