from model.contact import Contact
from model.group import Group
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test", middle_name="", last_name="",
                                   nick="", title_contact="",
                                   company_contact="", contact_address="",
                                   home_contact="",
                                   mobile_phone="", work_phone="", fax_phone="",
                                   email_com="", email2="",
                                   home_page="",
                                   b_day="12", b_month="October",
                                   b_year="1989", a_day="12", a_month="March", a_year="1999", address_2="",
                                   phone_2=",", notes_contact=""))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)


def test_delete_some_contact_in_groups(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="test", middle_name="", last_name="",
                               nick="", title_contact="",
                               company_contact="", contact_address="",
                               home_contact="",
                               mobile_phone="", work_phone="", fax_phone="",
                               email_com="", email2="",
                               home_page="",
                               b_day="12", b_month="October",
                               b_year="1989", a_day="12", a_month="March"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts_in_group = db.get_address_in_groups()
    if contacts_in_group == []:
        app.contact.add_contact_in_group(contact.id, group.name)
    app.contact.delete_contact_in_group(contact.id, group.name)
    new_contacts_in_group = db.get_address_in_groups()
    assert contact not in new_contacts_in_group
