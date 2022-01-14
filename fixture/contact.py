from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_new_contact(self):
        # open new contact creation
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        # fill contact form
        wd = self.app.wd
        self.open_new_contact()
        self.fill_contact(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home()
        self.contact_cache = None

    def fill_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nick)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title_contact)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company_contact)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.contact_address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_contact)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_phone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_com)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.home_page)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.b_day)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.b_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.b_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.a_day)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.a_month)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.a_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone_2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes_contact)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.return_to_home()
        self.contact_cache = None

    def update_first_contact(self, contact):
        self.delete_contact_by_index(0)

    def update_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.return_to_home()
        self.select_contact_by_index(index)
        self.fill_contact(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home()
        self.contact_cache = None

    def test_sorters_last_name(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Last name").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[2]/span").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[2]/span").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[2]/span").click()
        self.return_to_home()

    def test_sorters_first_name(self):
        wd = self.app.wd
        wd.find_element_by_link_text("First name").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[3]/span").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[3]/span").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[3]/span").click()
        self.return_to_home()

    def test_sorters_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Address").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[4]/span").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[4]/span").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[4]/span").click()
        self.return_to_home()

    def test_sorters_mail(self):
        wd = self.app.wd
        wd.find_element_by_link_text("All e-mail").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[5]/span").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[5]/span").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[5]/span").click()
        self.return_to_home()

    def test_sorters_phones(self):
        wd = self.app.wd
        wd.find_element_by_link_text("All phones").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[6]/span").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[6]/span").click()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/th[6]/span").click()
        self.return_to_home()

    def test_details(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        self.return_to_home()

    def test_print_details(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        wd.find_element_by_name("print").click()
        wd.get("http://localhost/addressbook/addressbook/")
        self.return_to_home()

    def test_vCard(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='vCard']").click()
        wd.get("http://localhost/addressbook/addressbook/")
        self.return_to_home()

    def test_details_modify(self):
        wd = self.app.wd
        wd.wd.find_element_by_xpath("//img[@alt='Details']").click()
        wd.find_element_by_name("modifiy").click()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("update").click()
        self.return_to_home()

    def return_to_home(self):
        # return to home page
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_xpath("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first_name=firstname, last_name=lastname, id=id))
        return list(self.contact_cache)
