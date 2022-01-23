from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

calendar_date = str(random.randrange(1, 31))
calendar_year = str(random.randrange(1900, 2022))
calendar_month = random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September",
                                "October", "November", "December"])

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))