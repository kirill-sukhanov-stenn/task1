# -*- coding: utf-8 -*-
from model.contact import Contact


def test_task1_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Mikle", middle_name="Ivanovich", last_name="Ivanov",
                      nick="Misha", title_contact="Mick",
                      company_contact="giuhjnllk", contact_address="Moscow 111",
                      home_contact="999 999 9999",
                      mobile_phone="456778789789", work_phone="645768", fax_phone="46756879890",
                      email_com="lvcgjhbjkbnm,n@bvhfgh.com", email2="yghjhjklk@gvhjbhj.com",
                      home_page="gfjhbgkjnkjln",
                      b_day="14", b_month="October",
                      b_year="1234", a_day="17", a_month="November", a_year="1989",
                      address_2="tdcghvbkhjbnkjn",
                      phone_2="123456789 ", notes_contact="fduygihjhbjlnljknmn")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_task1_add_empty_contact(app):
#    old_contacts = app.contact.get_contact_list()
 #   contact = Contact(first_name="", middle_name="", last_name="",
  #                    nick="", title_contact="",
   #                   company_contact="", contact_address="",
    #                  home_contact="",
     #                 mobile_phone="", work_phone="", fax_phone="",
      #                email_com="", email2="",
       #               home_page="",
        #              b_day="12", b_month="October",
         #             b_year="1989", a_day="12", a_month="March", a_year="1999", address_2="",
          #            phone_2=",", notes_contact="")
#    app.contact.create(contact)
 #   new_contacts = app.contact.get_contact_list()
  #  assert len(old_contacts) + 1 == len(new_contacts)
   # old_contacts.append(contact)
   # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
