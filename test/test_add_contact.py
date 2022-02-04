# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random



def test_task1_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact_in_group(app, orm, db):

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
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    groups = db.get_group_list()
    group = random.choice(groups)
    app.contact.add_contact_in_group(contact.id, group.name)
    contacts_in_group = orm.get_contacts_in_group(group)
    print(contacts_in_group)
    assert contact in contacts_in_group



