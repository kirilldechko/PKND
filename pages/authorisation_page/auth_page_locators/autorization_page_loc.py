def find_page_name(page_name):
    page_name_loc = f"//*[@class='caption' and normalize-space(text())='{page_name}']"
    return page_name_loc

def find_enter_button(enter_button_name):
    enter_button_loc = f"//*[@class='submit ng-star-inserted' and contains(text(), '{enter_button_name}')]"
    return enter_button_loc

def find_login_fild(placeholder_name):
    login_fild_loc = f"//*[@placeholder='{placeholder_name}']"
    return login_fild_loc

def find_password_fild(placeholder_name):
    password_fild_loc = f"//*[@placeholder='{placeholder_name}']"
    return password_fild_loc

def find_check_box_by_name(check_box_name):
    check_box_loc = f"//*[contains(@class, 'checkbox')]//label[contains(text(),'{check_box_name}')]"
    return check_box_loc