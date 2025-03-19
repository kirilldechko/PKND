def find_page_name(page_name):
    organisation_page_name_loc = f"//*[@class='header' and normalize-space(text())='{page_name}']"
    return organisation_page_name_loc

def find_organisation_name(organisation_name):
    organisation = f"//*[normalize-space(text())='{organisation_name}']"
    return organisation
