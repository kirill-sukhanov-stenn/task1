# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

calendar_date = str(random.randrange(1, 31))
calendar_year = str(random.randrange(1900, 2022))
calendar_month = random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September",
                                "October", "November", "December"])

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", middle_name="", last_name="",
                       nick="", title_contact="",
                       company_contact="", contact_address="",
                       home_contact="",
                       mobile_phone="", work_phone="", fax_phone="",
                       email_com="", email2="",
                       home_page="",
                       b_day="-", b_month="-",
                       b_year="", a_day="-", a_month="-", a_year="", address_2="",
                       phone_2=" ", notes_contact="")] + [
    Contact(first_name=random_string("firstname", 15), middle_name=random_string("middlename", 20), last_name=random_string("lastname", 15),
            nick=random_string("nick", 25), title_contact=random_string("title", 15),
            company_contact=random_string("company", 15), contact_address=random_string("address", 20),
            home_contact=random_string("phone", 15),
            mobile_phone=random_string("mobile", 15), work_phone=random_string("work", 15), fax_phone=random_string("fax", 15),
            email_com=random_string("email", 20), email2=random_string("email2", 25), email3=random_string("email3", 15),
            home_page=random_string("page", 15),
            b_day=calendar_date, b_month=calendar_month,
            b_year=calendar_year, a_day=calendar_date, a_month=calendar_month, a_year=calendar_year,
            address_2=random_string("address2", 15),
            phone_2=random_string("phone2", 15), notes_contact=random_string("notes", 45))
    for i in range(1)


]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_task1_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



