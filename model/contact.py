from sys import maxsize

class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nick=None, title_contact=None,
                 company_contact=None, contact_address=None,
                 home_contact=None, mobile_phone=None, work_phone=None, fax_phone=None, email_com=None, email2=None,
                 email3 = None, home_page=None, all_phones_from_home_page= None, all_emails_from_home_page=None,
                 b_day=None, b_month=None, b_year=None, a_day=None, a_month=None, a_year=None, address_2=None,
                 phone_2=None, notes_contact=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick = nick
        self.title_contact = title_contact
        self.company_contact = company_contact
        self.contact_address = contact_address
        self.home_contact = home_contact
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.email_com = email_com
        self.email2 = email2
        self.email3 = email3
        self.home_page = home_page
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.a_day = a_day
        self.a_month = a_month
        self.a_year = a_year
        self.address_2 = address_2
        self.phone_2 = phone_2
        self.notes_contact = notes_contact
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s %s %s %s " % (self.id, self.first_name, self.middle_name,
                                                                          self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.first_name is None or
                        other.first_name is None or self.first_name == other.first_name) and (
                       self.last_name is None or
                       other.last_name is None or self.last_name == other.last_name)


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize




