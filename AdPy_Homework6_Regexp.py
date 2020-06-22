from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

def opening_file():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    # pprint(contacts_list)
    return contacts_list
opening_file()

def forming_correct_file_format():
    new_contact_list = []
    new_contact_list.append(opening_file()[0])
    # print (new_contact_list)
    for contact in opening_file():
        # print (contact)
        F_I_O = ' '.join([contact[0], contact[1], contact[2]])
        # print (F_I_O)
        contacts = re.findall("\w+", F_I_O)
        while len(contacts) < 3:
            contacts.append('')
        contact[0], contact[1], contact[2] = contacts
        # print (contacts)

        pattern_number = re.compile("(\+7|8)\s*\(?(\d{3})[\)\-]?\s*(\d{3})\-?(\d{2})\-?(\d{2})(\s*\(?(доб\.\s*\d{4})\)?)?")
        sub_pattern_phone = r"+7(\2)\3-\4-\5 \7"
        contact[5] = pattern_number.sub(sub_pattern_phone, contact[5]).rstrip()
        final_number=contact[5]

        for new_contact in new_contact_list:
            # print (new_contact)
            if new_contact[0] == contact[0] and \
                    new_contact[1] == contact[1] and \
                    (new_contact[2] == contact[2] or
                         new_contact[2] == ''
                         or contact[2] == ''):
                for i in range(7):
                    new_contact[i] = max(new_contact[i], contact[i])
                break
        else:
            new_contact_list.append(contact)
    return new_contact_list

# pprint (forming_correct_file_format())

def writing_new_file():
    # код для записи файла в формате CSV
    with open("new_formated_phonebook.csv", "w",  newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(forming_correct_file_format())

writing_new_file()