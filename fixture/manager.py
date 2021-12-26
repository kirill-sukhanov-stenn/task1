from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper


class Manager:

    def __init__(self, app):
        self.app = app
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
