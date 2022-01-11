from model.contact import Contact


def test_update_first_contact(app):
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
    contact = Contact(first_name="trrdytfyuhgjkbhk", middle_name="gvjhbkjbnjknlk", last_name="hvbjbkjnlknm",
                nick="gfuhbkhjbkljnlm", title_contact="hfuygujhkl",
                company_contact="giuhjnllk", contact_address="uyfuyighklnmlknkjbn",
                home_contact="gfhgghjkh",
                mobile_phone="456778789789", work_phone="645768", fax_phone="46756879890",
                email_com="lvcgjhbjkbnm,n@bvhfgh.com", email2="yghjhjklk@gvhjbhj.com",
                home_page="gfjhbgkjnkjln",
                b_day="14", b_month="October",
                b_year="1234", a_day="17", a_month="November", a_year="1989",
                address_2="tdcghvbkhjbnkjn",
                phone_2="jjgjhknkjnm,", notes_contact="fduygihjhbjlnljk")
    contact.id = old_contacts[0].id
    app.contact.update_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

