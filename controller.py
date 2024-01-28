import text
import view
import model
def find_contact(phones: model.PhoneBook):
    word= view.input_data(text.input_search_word)
    result=phones.find_contact(word)
    return view.show_contacts(result,text.contacts_not_found(word))
        
def strart_app():
    pb=model.PhoneBook()
    while True:
        choice=view.main_menu()
        match choice:
            case 1:
                pb.open_file()
                view.print_massege(text.load_successful)
            case 2:
                print(pb.phone_book)
                pb.save_file()
                view.print_massege(text.save_successful)
            case 3:
                view.show_contacts(pb,text.emty_phone_book)
            case 4:
                contact=view.add_contact(text.new_contact)
                pb.new_contact(contact)
                view.print_massege(text.new_contact_added_successful(contact[0]))
            case 5:
                find_contact(pb)
            case 6:
                if find_contact(pb):
                    c_id=int(view.input_data(text.input_id_chance_contact))
                    print(pb.phone_book[c_id].to_str(';').split(';'))
                    c_contact=view.add_contact(text.change_contact,pb.phone_book[c_id].to_str(';').split(';'))
                    #c_contact=view.add_contact(text.change_contact,pb.phone_book[c_id])
                    pb.change_contact(c_id,c_contact)
                    view.print_massege(text.contact_changed_successful(c_contact[0]))
            case 7:
                if find_contact(pb):
                    c_id=int(view.input_data(text.input_id_delete_contact))
                    name=pb.delete_contact(c_id)[0]
                    print(name.split())
                    if name.split()=='1':
                        view.print_massege(text.contact_deleted_successful(name))
                    else:
                        view.print_massege(text.error_key_del)

            case 8:
                view.print_massege(text.good_bay)
                break
                  

