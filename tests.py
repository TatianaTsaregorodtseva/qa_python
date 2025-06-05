import pytest
from main import BooksCollector



class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': '',
                                               'Что делать, если ваш кот хочет вас убить': ''}

    @pytest.mark.parametrize('name', ['',
                                      'Чук и Гек',
                                      'Чук и Гек на Мальдивах'])
    def test_add_new_book_name_out_of_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert len(books_collection.get_books_genre()) == 0

    @pytest.mark.parametrize('name, genre', [('Гордость и предубеждение и зомби', 'Ужасы'),
                                             ('Что делать, если ваш кот хочет вас убить', 'Комедии')])
    def test_get_book_genre_by_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_add_book_in_favorites_not_added_in_favorites_book(self, books_collection):
        books_collection.add_book_in_favorites('Джэйн Эйр')
        assert 'Джэйн Эйр' in books_collection.get_list_of_favorites_books() and len(books_collection.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self, books_collection):
        books_collection.add_book_in_favorites('Джэйн Эйр')
        books_collection.delete_book_from_favorites('Джэйн Эйр')
        assert len(books_collection.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books(self, books_collection):
        books_collection.add_book_in_favorites('Джэйн Эйр')
        books_collection.add_book_in_favorites('451 градус по Фаренгейту')
        assert books_collection.get_list_of_favorites_books() == ['Джэйн Эйр', '451 градус по Фаренгейту']

    def test_set_book_genre_to_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_books_genre() == {'Гордость и предубеждение': 'Фантастика'}

    def test_set_book_genre_to_not_existing_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize('name, genre', [('Гордость и предубеждение и зомби', 'Ужасы'),
                                             ('Что делать, если ваш кот хочет вас убить', 'Комедии')])
    def test_get_books_with_specific_genre_by_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_with_specific_genre_by_wrong_genre(self, books_collection):
        assert len(books_collection.get_books_with_specific_genre('Роман')) == 0