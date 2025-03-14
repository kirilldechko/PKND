def find_add_case_button(button_name):
    add_button_path = f"//button[contains(@class, 'btn') and normalize-space(text()) = '{button_name}']"
    return add_button_path

def find_text_fild_by_placeholder(fild_name):
    code_field_path = f"//input[@type='text' and contains(@placeholder, '{fild_name}')]"
    return code_field_path

def find_filtered_st(st_num, st_full_name):
    filtered_st_path = f"//*[contains(@class, 'full-width')][.//*[text()='{st_full_name}']][.//*[contains(text(), '{st_num}')]]"
    return filtered_st_path

def find_create_button(button_name):
    add_button_path = f"//button[contains(@class, 'mr-20') and contains(text(), '{button_name}')]"
    return add_button_path

def find_create_page_name(page_name):
    create_page_name_path = f"//*[contains(@class, 'text-slate') and normalize-space(text())='{page_name}']"
    return create_page_name_path

def find_directory_by_name(name):
    directory_path = f"//label[contains(normalize-space(text()), '{name}')]//following-sibling::*//*//*//input"
    return directory_path

def find_directory_value(value):
    value_path = f"//span[contains(normalize-space(text()), '{value}')]"
    return value_path

def find_text_fild_by_name(name):
    text_fild_path = f"//label[contains(normalize-space(text()), '{name}')]/following-sibling::*//*"
    return text_fild_path

def find_date_fild(fild_name):
    date_fild_path = f"//*[contains(@class, 'ng-star-inserted') and contains(text(), '{fild_name}')]/following-sibling::*//input[@type='text']"
    return date_fild_path

def find_time_fild(fild_name):
    time_fild_path = f"//*[contains(text(), '{fild_name}')]/following-sibling::*//input"
    return time_fild_path

def find_delete_element(fild_name):
    delete_elem_path = f"//*[contains(normalize-space(text()), '{fild_name}')]/following-sibling::*//*[contains(@class, 'icon-cross')]"
    return delete_elem_path

def find_save_button(button_name):
    save_button_path = f"//button[contains(@type, 'button') and contains(text(), '{button_name}')]"
    return save_button_path

def find_reg_button(button_name):
    registration_button_path = f"//button[contains(text(), '{button_name}')]"
    return registration_button_path

def find_add_button(button_name):
    add_button_path = f"//button[contains(@class, 'btn-labeled') and normalize-space(text()) = '{button_name}']"
    return add_button_path

def find_left_menu_button(button_name):
    """Поиск элемента по названию, в левом меню"""
    left_menu_button_path = f"//*[contains(@class, 'category-title') and .//text()[normalize-space()='{button_name}']]"
    return left_menu_button_path