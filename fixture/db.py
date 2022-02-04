import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    #def get_address_in_groups(self):
    #    list = []
    #    cursor = self.connection.cursor()
    #    try:
     #       cursor.execute("select id, group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
      #      for row in cursor:
     #           (id, group_id) = row
    #            list.append(Contact(id=str(id))) and (Group(id=str(group_id)))
    #    finally:
     #       cursor.close()
     #   return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id,  firstname, middlename, lastname,  address, home, mobile, work, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(Contact(id=str(id), first_name=firstname, middle_name=middlename, last_name=lastname, contact_address=address,
                                    home_contact=home,
                                  mobile_phone=mobile, work_phone=work, phone_2=phone2, email_com=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

