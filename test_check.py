from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_new_book(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    def test_add_new_book_add_duplicate_book(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1

    def test_set_book_genre_set_with_existing_name_and_existing_genre(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        collector.add_new_book(book_name)
        genre = 'Комедии'
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre.get(book_name) == genre

    def test_set_book_genre_set_with_existing_name_and_non_existing_genre(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер'
        collector.add_new_book(book_name)
        non_existing_genre = 'Дорама'
        collector.set_book_genre(book_name, non_existing_genre)
        assert collector.books_genre.get(book_name) != non_existing_genre