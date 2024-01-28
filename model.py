phone_book={}
#path='C:\codes\gb\Python_table_data\phones.txt'
#SEPARATOR=';'
import text
class Contact:
    def __init__(self,name:str,phone:str, comment:str):
        self.name=name
        self.phone=phone
        self.comment=comment

    def to_str(self,sep:str=' '):
        return f'{self.name}{sep}{self.phone}{sep}{self.comment }'    

    def field_len(self,field:str):
        if field =='name':
            return len(self.name)
        elif field =='phone':
            return len(self.phone)
        elif field =='comment':
            return len(self.comment)

class PhoneBook:
    def __init__(self,path: str='C:\codes\gb\Python_table_data2\phones.txt',separator: str=';'):
        self.phone_book={}
        self.path=path
        self.separator=separator
        
    def open_file(self):
         
        with open(self.path,'r', encoding='UTF-8') as file:
            for c_id,contact in enumerate(file.readlines(),1):
                contact=contact.strip().split(self.separator)
                self.phone_book[c_id]=Contact(*contact)
           

    

    def next_id(self):
        return max(self.phone_book)+1 if self.phone_book else 1


    def new_contact(self,contact: list[str]):
        self.phone_book[self.next_id()]=Contact(*contact)


    def find_contact(self,word: str)-> 'PhoneBook':
        result=PhoneBook()
        for u_id, contact in self.phone_book.items():
            print((contact.to_str(self.separator)).split(';'))
            if word.lower() in str(contact.to_str( )).lower():
                result.phone_book[u_id]=Contact(*(contact.to_str(self.separator)).split(';'))
        return result        

    def change_contact(self,c_id: int,c_contact: list[str]):
        self.phone_book[c_id]=Contact(*c_contact)

    def delete_contact(self,c_id: int)->list[str]:
        if c_id in self.phone_book:
            return self.phone_book.pop(c_id).to_str(';').split(';')
        else:
            return ['1','','']

    def save_file(self):
        data=[]
        for contact in self.phone_book.values():
            data.append(contact.to_str(self.separator))
        data='\n'.join(data)   
        with open(self.path,'w',encoding='UTF-8',) as file:
            file.write(data)

    def max_len(self):
        max_field_lens=[0,0,0]
        for contact in self.phone_book.values():
            for n,field in enumerate(['name','phone','comment']):
                if max_field_lens[n]<contact.field_len(field):
                    max_field_lens[n]=contact.field_len(field)
        return max_field_lens            
