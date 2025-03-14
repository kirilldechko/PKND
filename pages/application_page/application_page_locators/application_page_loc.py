def application_path(application_name):
    application = f"//*[normalize-space(text())= '{application_name}']"
    return application

def crumbs_application_name(crumbs_name):
    crumb_name = f"//*[contains(@class, 'xng-breadcrumb-link') and normalize-space(text()) = {crumbs_name}]"
    return crumb_name