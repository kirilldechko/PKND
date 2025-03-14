from datetime import datetime

# Получаем текущую дату и время
current_date = datetime.now().strftime('%d.%m.%Y')
current_time = datetime.now().strftime('%H:%M')

code_fild_name = "Код"
add_case_button_name = "Добавить дело"
standard_full_name = "Внеплановая контрольная закупка (Кастомизированный)_ПС"
create_button_name = "Создать"
create_page_name = "Создание дела"
save_button_name = "Сохранить"
reg_button_name = "Регистрация"
directory = ["Вид государственного контроля (надзора)", "Основание КНМ (ЕРВК)"]
type_of_state_control_value = ["Региональный государственный контроль (надзор) на автомобильном транспорте, городском наземном электрическом транспорте и в дорожном хозяйстве", ]
knm_foundation_value = ["(336-ПП) По истечении срока исполнения предписания, выданного после 1 марта 2023 года"]
text_fild_name =["Ссылка на другой паспорт КНМ"]
beginning_knm_date_fild_name = "Дата начала КНМ"
beginning_knm_time_fild_name= "Время начала КНМ"
ending_knm_date_fild_name = "Дата окончания КНМ"
ending_knm_date_time_name = "Время окончания КНМ"
knm_date_period_fild_name = "Срок проведения (дней)"
knm_time_period_fild_name = "Срок непосредственного взаимодействия (часов)"
knm_date_period = '1'
knm_time_period = '1'
need_for_coordination_fild_name = "Необходимость согласования"
need_for_coordination_values = ["Требует согласования", "Не требует согласования"]
post_fild_name = "Должность"
post = ["Начальник Объединения административно-технических инспекций города Москвы"]
left_menu_buttons = ["Общие данные", "Контролируемые лица", "Объекты"]
add_button_name = "Добавить"
