# Copyright (c) 2025, krushit.dudhat@redsoftware.in and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Project(Document):
	def validate(self):
			total_cost = 0
			for task in frappe.get_all('Task', filters={'project': self.name}, fields=['cost']):
					if 'cost' in task:
							total_cost += task['cost']
			if total_cost > self.budget:
					frappe.throw(f"Total task cost ({total_cost}) exceeds the budget ({self.budget}).")
