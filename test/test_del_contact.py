from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count()==0:
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
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index-1:index] = []
    assert old_contacts == new_contacts