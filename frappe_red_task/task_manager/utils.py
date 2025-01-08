import frappe

def validate_task(doc, method):
  
    if doc.due_date and doc.due_date < frappe.utils.nowdate():
        frappe.throw("Due date cannot be in the past.")