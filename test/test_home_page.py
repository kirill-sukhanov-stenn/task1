import re
from random import randrange

def test_phones_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home_contact,
                                                            contact.mobile_phone, contact.work_phone,
                                                            contact.phone_2]))))

def test_firstname_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first_name == firstname_like_on_home_page(contact_from_edit_page)

def firstname_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x is not None, [contact.first_name]))

def test_lastname_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.last_name == lastname_like_on_home_page(contact_from_edit_page)

def lastname_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x is not None, [contact.last_name]))

def test_address_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.contact_address == address_like_on_home_page(contact_from_edit_page)

def address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x is not None, [contact.contact_address]))

def test_emails_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def merge_emails_like_on_home_page(contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: clear(x), filter(lambda x: x is not None,
                                                               [contact.email_com,
                                                                contact.email2, contact.email3]))))


