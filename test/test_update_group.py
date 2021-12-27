from model.group import Group


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first_group(Group(name="ytfguyh", header="lkmjmlk", footer="kmlkmkl"))
    app.session.logout()