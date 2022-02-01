import re
from random import randrange
from model.contact import Contact


def test_random_contact_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.contact_address == contact_from_edit_page.contact_address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home_contact,
                                                            contact.mobile_phone, contact.work_phone,
                                                            contact.phone_2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email_com,
                                                                                contact.email2, contact.email3])))


def test_all_contact_home_page_db(app, db, check_ui):
    db_contacts = db.get_contact_list()
    db_contacts = sorted(db_contacts, key=Contact.id_or_max)
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(db_contacts) == len(contacts_from_home_page)
    assert db_contacts == contacts_from_home_page
    for number in db_contacts:
        number.all_emails_from_home_page = merge_emails_like_on_home_page(number)
        number.all_phones_from_home_page = merge_phones_like_on_home_page(number)
    for i in range(len(db_contacts)):
        assert db_contacts[i].id == contacts_from_home_page[i].id
        assert db_contacts[i].first_name == contacts_from_home_page[i].first_name
        assert db_contacts[i].last_name == contacts_from_home_page[i].last_name
        assert db_contacts[i].contact_address == contacts_from_home_page[i].contact_address
        assert db_contacts[i].all_phones_from_home_page == contacts_from_home_page[i].all_phones_from_home_page
        assert db_contacts[i].all_emails_from_home_page == contacts_from_home_page[i].all_emails_from_home_page
        print(str(i))
        print(db_contacts[i])
        print(contacts_from_home_page[i])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home_contact,
                                                            contact.mobile_phone, contact.work_phone,
                                                            contact.phone_2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email_com,
                                                                                contact.email2, contact.email3])))