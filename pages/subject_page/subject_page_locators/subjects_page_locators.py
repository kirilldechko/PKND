# Поиск полей для ввода данных в левом меню
def find_fild_path_in_left_menu_by_name(fild_name):
    fild_path = f"//*[contains(@class, 'sidebar-category')]//*[contains(text(), '{fild_name}')]"
    return fild_path

def find_search_fild_path(placeholder_name):
    search_fild = f"//*[contains(@placeholder, '{placeholder_name}')]"
    return search_fild

def find_subject_by_name_path(subject_name):
    subject_path = f"//*[contains(text(), '{subject_name}')]"
    return subject_path

def find_subject_check_box_path(subject_name):
    check_box_path = f"//*[contains(@class, 'checkbox')]/following-sibling::*[contains(@class, 'list-item')]//*[contains(@class, 'text-bold') and contains(text(),'{subject_name}')]"
    return check_box_path