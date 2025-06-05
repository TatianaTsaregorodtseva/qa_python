#qa_python_4_sprint

Реализованы фикстуры:
  1. books_collection: возвращает объект класса BooksCollector

Сценарии, которые покрыты тестами:
  1. test_add_new_book_add_two_books: проверка добавления двух книг
  2. test_add_new_book_name_out_of_range: негативная проверка на добавление книги с невалидным значением (названием)
  3. test_get_book_genre_by_name: проверка на вывод жанра по имени книги
  4. test_add_book_in_favorites_not_added_in_favorites_book: проверка на добавление книги в избранное
  5. test_delete_book_from_favorites: проверка на удаление книги из избранного
  6. test_get_list_of_favorites_books: проверка на получение списка избранных книг
  7. test_set_book_genre_to_existing_book: проверка на добавление жанра из genre для книги из books_genre
  8. test_set_book_genre_to_not_existing_book: негативная проверка на добавление жанра из genre для книги не из books_genre
  9. test_get_books_with_specific_genre_by_genre: проверка на вывод книг по жанру
  10. test_get_books_with_specific_genre_by_wrong_genre: негативная проверка на вывод книг по жанру не из genre