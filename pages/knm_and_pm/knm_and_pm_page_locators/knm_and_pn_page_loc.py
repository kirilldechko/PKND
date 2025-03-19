def find_add_case_button(button_name):
    """Добавить дело"""
    add_button_path = f"//button[contains(@class, 'btn') and normalize-space(text()) = '{button_name}']"
    return add_button_path

def find_text_fild_by_placeholder(fild_name):
    """Найти текстовое поле по тексту в плейсхолдере"""
    code_field_path = f"//input[@type='text' and contains(@placeholder, '{fild_name}')]"
    return code_field_path

# def find_filtered_st(st_num, st_full_name):
#     """Выбрать стандарт по номеру и названию"""
#     filtered_st_path = f"//*[contains(@class, 'full-width')][.//*[text()='{st_full_name}']][.//*[contains(text(), '{st_num}')]]"
#     return filtered_st_path

def find_create_button(button_name):
    """Кнопка Создать"""
    add_button_path = f"//button[contains(@class, '20') and contains(text(), '{button_name}')]"
    return add_button_path

def find_create_page_name(page_name):
    """Проверить имя страницы"""
    create_page_name_path = f"//*[contains(@class, 'text-slate') and normalize-space(text())='{page_name}']"
    return create_page_name_path

def find_directory_by_name(name):
    """Найти поле с выпадающим списком по имени"""
    directory_path = f"//label[contains(normalize-space(text()), '{name}')]//following-sibling::*//*//*//input"
    return directory_path

def find_directory_value(value):
    """Найти значение выпадающего списка"""
    value_path = f"//span[contains(normalize-space(text()), '{value}')]"
    return value_path

def find_text_fild_by_name(name):
    """Найти текстовое поле по имени"""
    text_fild_path = f"//label[contains(normalize-space(text()), '{name}')]/following-sibling::*//*"
    return text_fild_path

def find_date_fild(fild_name):
    """Найти поле Дата"""
    date_fild_path = f"//*[contains(@class, 'ng-star-inserted') and contains(text(), '{fild_name}')]/following-sibling::*//input[@type='text']"
    return date_fild_path

def find_time_fild(fild_name):
    """Найти поле Время"""
    time_fild_path = f"//*[contains(text(), '{fild_name}')]/following-sibling::*//input"
    return time_fild_path

def find_delete_element(fild_name):
    """Найти кнопку удалить в поле(крестик)"""
    delete_elem_path = f"//*[contains(normalize-space(text()), '{fild_name}')]/following-sibling::*//*[contains(@class, 'icon-cross')]"
    return delete_elem_path

def find_save_button(button_name):
    """Найти кнопку Сохранить"""
    save_button_path = f"//button[contains(@type, 'button') and contains(text(), '{button_name}')]"
    return save_button_path

def find_reg_button(button_name):
    """Найти кнопку Регистрация"""
    registration_button_path = f"//button[contains(text(), '{button_name}')]"
    return registration_button_path

def find_add_button(button_name):
    """Найти кнопку Добавить(не Объект, Субъект)"""
    add_button_path = f"//button[contains(@class, 'btn-labeled') and normalize-space(text()) = '{button_name}']"
    return add_button_path

def find_left_menu_button(button_name):
    """Поиск элемента по названию, в левом меню"""
    left_menu_button_path = f"//*[contains(@class, 'category-title') and .//text()[normalize-space()='{button_name}']]"
    return left_menu_button_path

def find_type_of_control_subject(subject_name):
    """Поиск чекбокса контролируемого субъекта по его наименованию"""
    control_subject_path = f"//*[contains(@class, 'radio-inline')]/*[text()='{subject_name}']"
    return control_subject_path

def find_new_subject_type_name(subject_name):
    """Поиск наименования выбранного типа субъекта, после выбора его типа"""
    new_subject_type_path = f"//*[contains(@class, 'badge text') and text()='{subject_name}']"
    return new_subject_type_path

def find_button_choose_subject_from_registry(button_name):
    choose_subject_from_registry_path = f"//*[text()='{button_name}']"
    return choose_subject_from_registry_path