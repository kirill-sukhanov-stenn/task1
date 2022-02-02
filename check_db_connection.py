from model.group import Group
from fixture.orm import ORMFixture


db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    l = db.get_address_in_groups()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()
