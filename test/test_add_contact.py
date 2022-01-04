# -*- coding: utf-8 -*-
from model.contact import Contact



def test_task1_add_contact(app):
    app.contact.create(Contact(first_name="trrdytfyuhgjkbhk", middle_name="gvjhbkjbnjknlk", last_name="hvbjbkjnlknm",
                               nick="gfuhbkhjbkljnlm", title_contact="hfuygujhkl",
                               company_contact="giuhjnllk", contact_address="uyfuyighklnmlknkjbn",
                               home_contact="gfhgghjkh",
                               mobile_phone="456778789789", work_phone="645768", fax_phone="46756879890",
                               email_com="lvcgjhbjkbnm,n@bvhfgh.com", email2="yghjhjklk@gvhjbhj.com",
                               home_page="gfjhbgkjnkjln",
                               b_day="14", b_month="October",
                               b_year="1234", a_day="17", a_month="November", a_year="1989",
                               address_2="tdcghvbkhjbnkjn",
                               phone_2="jjgjhknkjnm,", notes_contact="fduygihjhbjlnljknmn"))


def test_task1_add_empty_contact(app):
    app.contact.create(Contact(first_name="", middle_name="", last_name="",
                               nick="", title_contact="",
                               company_contact="", contact_address="",
                               home_contact="",
                               mobile_phone="", work_phone="", fax_phone="",
                               email_com="", email2="",
                               home_page="",
                               b_day="12", b_month="October",
                               b_year="1989", a_day="12", a_month="March", a_year="1999", address_2="",
                               phone_2=",", notes_contact=""))

