"""
Определить класс Person:

- атрибут fullname - ФИО (тип str)
- атрибут phone - номер телефона (тип str)
- магический метод __init__, который принимает fullname и phone

Описать класс LibraryReader, который наследуется от Person:

- атрибут uid - номер читательского билета (тип int)
- атрибут books - список книг (тип set)
- магический метод __init__, который принимает fullname, phone, uid, а books
  заполняет пустым множеством
- метод take_books(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. взял(а)
  книги: Приключения, Словарь, Энциклопедия", если было взято до 3 книг
  включительно. Если было взято больше книг, то возвращает строку: "Петров В.В.
  взял(а) 4 книги".
- метод return_book(*args), который принимает произвольное количество книг
  (книга - строка с названием книги) и возвращает строку: "Петров В.В. вернул(а)
  книги: Приключения, Словарь, Энциклопедия", если было возвращено до 3 книг
  включительно. Если было возвращено больше книг, то возвращает строку:
  "Петров В.В. вернул(а) 4 книги". Если какой-то книги нет, то бросить исключение
  ValueError с сообщением "Петров В. В. не брал: Рассказы", при этом книги не
  должны быть удалены

Названия книг в сообщениях должны быть отсортированы по алфавиту.
"""


def sort_by_alphabet(input_str):
    return input_str[0]

class Person:
    fullname: str
    phone: str

    def __init__(self, fullname, phone):
        self.fullname = fullname
        self.phone = phone


class LibraryReader(Person):
    uid: str
    books: set

    def __init__(self, fullname, phone, uid):
        super().__init__(fullname, phone)
        self.uid = uid
        self.books = set()

    def take_books(self, *args: str):
        book_list = list(args)
        book_list.sort(key=sort_by_alphabet)
        for book in book_list:
            self.books.add(book)
        if len(book_list) > 3:
            return f'{self.fullname} взял(а) {len(book_list)} книг(и)'
        else:
            return f'{self.fullname} взял(а) книги: {book_list}'

    def return_book(self, *args):
        book_list = list(args)
        book_list.sort(key=sort_by_alphabet)
        for book in book_list:
            if book not in self.books:
                raise ValueError(f'{self.fullname} не брал: {book}')
            else:
                if len(args) > 3:
                    return f'{self.fullname} вернул(а) {len(book_list)} книг(и)'
                else:
                    return f'{self.fullname} вернул(а) {book_list}'
