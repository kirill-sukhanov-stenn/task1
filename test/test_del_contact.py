from model.contact import Contact

def test_delete_first_contact(app):
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
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)