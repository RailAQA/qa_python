import pytest


class TestBooksCollector:

    def test_add_new_book_successful_addition(self, collector):
        book_name = 'Гарри Поттер'
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    @pytest.mark.parametrize(
                            'name', 
                             [
                                 'Гаррри Поттер и Принц Полукровка 1 частьь', 
                                 'Гаррри Поттер и Принц Полукровка 1 частььь', 
                                 ''
                                 ]
                             )
    def test_add_new_book_false_when_book_have_not_valid_values(self, name, collector):
        book_name = name
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_add_new_book_new_book_have_empty_genre(self, collector):
        book_name = 'Гарри Поттер'
        collector.add_new_book(book_name)
        assert collector.books_genre.get(book_name) == ''

    def test_add_new_book_duplicate_book_not_added(self, collector):
        book_name = 'Гарри Поттер'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1

    def test_set_book_genre_existing_name_and_existing_genre(self, collector):
        book_name = 'Гарри Поттер'
        collector.add_new_book(book_name)
        genre = 'Комедии'
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre.get(book_name) == genre

    def test_get_book_genre_get_correct_genre(self, collector):
        book_name = 'Гарри Поттер'
        genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_when_genre_added_book_non_existing(self, collector):
        first_book_name = 'Гарри Поттер'
        second_book_name = 'Букины'
        existing_genre = 'Комедии'
        non_existing_genre = 'Дорамы'

        collector.add_new_book(first_book_name)
        collector.set_book_genre(first_book_name, non_existing_genre)

        collector.add_new_book(second_book_name)
        collector.set_book_genre(second_book_name, existing_genre)

        assert collector.get_books_with_specific_genre(non_existing_genre) == []

    def test_get_books_genre_list_is_correct(self, collector):
        book_name = 'Гарри Поттер'
        genre = 'Комедии'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert book_name in collector.get_books_genre().keys() and genre in collector.get_books_genre().values()

    def test_get_books_for_children_books_with_age_rating_not_in_children_books(self, collector):
        book_name = 'Гарри Поттер'
        genre = 'Ужасы'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert book_name not in collector.get_books_for_children()

    def test_add_book_in_favorites_add_book_that_not_exist_in_favourite_list(self, collector):
        book_name = 'Гарри Поттер'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books() and len(collector.get_list_of_favorites_books())

    def test_delete_book_from_favorites_book_delete_existing_book(self, collector):
        book_name = 'Гарри Поттер'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_default_list_is_empty(self, collector):
        assert len(collector.get_list_of_favorites_books()) == 0
    