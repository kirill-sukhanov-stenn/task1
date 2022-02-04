import time

from model.contact import Contact
import random


def test_update_first_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
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
    contact_mod = random.choice(old_contacts)
    old_contacts.remove(contact_mod)
    contact.id = contact_mod.id
    app.contact.update_contact_by_id(contact.id, contact)
    time.sleep(2)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)