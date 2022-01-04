from model.group import Group


def test_update_first_group(app):
    if app.group.count()==0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.update_first_group(Group(name="ytfguyh", header="lkmjmlk", footer="kmlkmkl"))