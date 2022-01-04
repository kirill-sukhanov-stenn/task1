
def test_sorters_contacts(app):
    app.contact.test_sorters_last_name()
    app.contact.test_sorters_first_name()
    app.contact.test_sorters_address()
    app.contact.test_sorters_mail()
    app.contact.test_sorters_phones()



