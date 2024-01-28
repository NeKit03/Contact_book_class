main_menu=['главное меню',
           'Открыть файл',
           'Сохранить файл',
           'Показать контакты',
           'Создать контакт',
           'Найти контакт',
           'Изменить контакт',
           'Удалить контакт',
           'Выход',
           ]
main_menu_choice='Выберите пункт меню: '
emty_phone_book='Телефонная книга пуста или не открыта!'
load_successful='Телефонная книга успешно загружена!'
save_successful='Телефонная книга успешно сохранена!'
new_contact=['Введите имя:',
             'Введите номер телефона:',
             'Введиете комментарий:']
input_search_word='Введите слово для поиска'
change_contact=["Введите новое имя или ENTER, чтобы оставить без изменений:",
              "Введите новый номер телефона или ENTER, чтобы оставить без изменений:",
              "Введите новый комментарий или ENTER, чтобы оставить без изменений:"]

input_id_chance_contact='Введите ID контакта, который хотите изменить:'


def contacts_not_found(word:str)->str:
    return f'Контакты содержащие {word} не найдены!' 

def new_contact_added_successful(name:str)->str:
    return f'Контакт {name} успешно добавлен!'


def contact_changed_successful(name: str)->str:
    return f'Контакт {name} успешно изменен'


input_id_delete_contact='Введите ID контакта, который хотите удалить: '


def contact_deleted_successful(name: str)->str:
    return f'Контакт {name} успешно удален'

good_bay='До новых встреч!'

error_key_del='Не верный ID !!!'


