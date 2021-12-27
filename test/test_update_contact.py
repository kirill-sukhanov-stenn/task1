from model.contact import Contact


def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first_contact(Contact(first_name="trrdytfyuhgjkbhk", middle_name="gvjhbkjbnjknlk", last_name="hvbjbkjnlknm",
                               nick="gfuhbkhjbkljnlm", title_contact="hfuygujhkl",
                               company_contact="giuhjnllk", contact_address="uyfuyighklnmlknkjbn",
                               home_contact="gfhgghjkh",
                               mobile_phone="456778789789", work_phone="645768", fax_phone="46756879890",
                               email_com="lvcgjhbjkbnm,n@bvhfgh.com", email2="yghjhjklk@gvhjbhj.com",
                               home_page="gfjhbgkjnkjln",
                               b_day="14", b_month="October",
                               b_year="1234", a_day="17", a_month="November", a_year="1989",
                               address_2="tdcghvbkhjbnkjn",
                               phone_2="jjgjhknkjnm,", notes_contact="fduygihjhbjlnljk"))
    app.session.logout()