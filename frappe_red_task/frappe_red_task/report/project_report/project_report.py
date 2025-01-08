import frappe

@frappe.whitelist()
def execute(filters=None):
    columns = [
        {"label": "Project Name", "fieldname": "project_name", "fieldtype": "Data"},
        {"label": "Budget", "fieldname": "budget", "fieldtype": "Currency"},
    ]
    data = frappe.get_all('Project', fields=['project_name', 'budget'])
    return columns, data