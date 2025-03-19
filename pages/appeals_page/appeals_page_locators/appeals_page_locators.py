def find_add_case_button(button_name):
    add_case_button_path = f"//button[contains(text(), '{button_name}')]"
    return add_case_button_path