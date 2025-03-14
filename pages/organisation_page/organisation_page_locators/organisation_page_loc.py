organisation_page_name_loc = "//*[@class='header' and normalize-space(text())='Выберите организацию']"


def find_organisation_name(organisation_name):
    organisation = f"//*[normalize-space(text())='{organisation_name}']"
    return organisation
