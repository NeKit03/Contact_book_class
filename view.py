import text
from model import Contact, PhoneBook
def main_menu()->int:
    for n, item in enumerate(text.main_menu):
        if n==0:
            print(item)
        else:
            print(f'\t{n}.{item}')
          
    while True:
        choice=input(text.main_menu_choice) 
        print(choice)  
        if choice.isdigit() and 0<int(choice)<len(text.main_menu):
            return int(choice)
        print(f'введите пункт меню от 1 до {len(text.main_menu)-1}')
        
def show_contacts(p_book: PhoneBook,error_massege:str):
    max_size=p_book.max_len()
    #print(max_size)
    #print(p_book.phone_book)
    if p_book.phone_book:
        print('\n'+'='*(sum(max_size)+7))
        for n, contact in p_book.phone_book.items():
            print(f'{n:>3}. {contact.name:<{max_size[0]}} {contact.phone:<{max_size[1]}} {contact.comment:<{max_size[2]}}')
        print('='*(sum(max_size)+7)+'\n')  
        return 1  
    else:
        print_massege(error_massege)
        return 0  


def print_massege(massege: str):
    print('\n'+'='*len(massege))  
    print(massege)       
    print('='*len(massege)+'\n')


def add_contact(massege: list[str],contact:list[str]= None):
    contact=contact if contact else['','','']
    print(contact)
    for n,mes in enumerate(massege):
        #contact.append(input(mes))
    
        field=input(mes)
        contact[n]=field if field else contact[n]
    return contact


def input_data(massege: str)-> str:
    return input(massege)