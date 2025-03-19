def find_fild_by_name(fild_name):
    """Поиск поля по названию"""
    code_fild_path = f"//*[contains(@class, 'category-title')]/*[contains(normalize-space(text()), '{fild_name}')]//../following-sibling::div//input"
    return code_fild_path

def find_filtered_service(st_num, st_full_name):
    """Поиск стандарта по номеру и названию"""
    filtered_service_path = f"//*[contains(@class, 'full-width')][.//*[text()='{st_full_name}']][.//*[contains(text(), '{st_num}')]]"
    return filtered_service_path

def find_create_button(create_button_name):
    """Кнопка Создать"""
    add_button_path = f"//button[contains(@class, '20') and contains(text(), '{create_button_name}')]"
    return add_button_path