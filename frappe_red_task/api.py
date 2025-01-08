import frappe

# API should fetch fetch the tasks, it should support status open, close, and no status as well.
@frappe.whitelist(allow_guest=True)
def get_tasks(status=None):
    filters = {}
    if status:
        filters['status'] = status

    tasks = frappe.get_all('Task', filters=filters, fields=['name', 'due_date'])
    return tasks


# update status of tasks (bulk api)
# TODO: optimise
@frappe.whitelist()
def update_task_status(task_ids, status):
    
    for task_id in task_ids:
        task = frappe.get_doc('Task', task_id)
        task.status = status
        task.save()

    frappe.db.commit()  
