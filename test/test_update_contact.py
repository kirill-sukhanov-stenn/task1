from model.contact import Contact
from random import randrange


def test_update_first_contact(app, json_contacts):
    contact = json_contacts
    if app.contact.count() == 0:
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
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

