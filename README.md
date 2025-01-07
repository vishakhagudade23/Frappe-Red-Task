## Frappe Red Task

# Frappe Red Task Application

## **Overview**
The **Frappe Red Task** application is designed to manage **Projects** and their associated **Tasks**. It provides features such as task tracking, budget validation, and reporting. The app includes APIs for task management and bulk status updates, along with role-based access for reports.

---

## **Key Features**

1. **Task Management**:
   - Define tasks with details such as subject, description, due date, status, project association, and cost.
   - Link tasks to projects for better organization and tracking.

2. **Project Management**:
   - Manage projects with a name and budget.
   - Validate project budgets against the total cost of associated tasks.

3. **Dynamic Reporting**:
   - Generate a report listing all projects with their respective budgets.
   - Role-based access ensures only authorized users can view reports.

4. **APIs**:
   - Fetch tasks based on status.
   - Bulk update the status of multiple tasks for efficient management.

---

## **Requirements**

### **Task**
- A **Task** represents a unit of work with the following attributes:
  - **Subject**: (Required) A short description of the task.
  - **Description**: Additional details about the task.
  - **Due Date**: (Required) The deadline for the task.
  - **Status**: Indicates whether the task is `Open` or `Closed`.
  - **Project**: A link to the associated project.
  - **Cost**: The monetary value associated with the task.

### **Project**
- A **Project** is a container for multiple tasks, with the following attributes:
  - **Project Name**: (Required) A unique name for the project.
  - **Budget**: (Required) The total allowable cost for the project.

#### **Validation Logic**:
- A project's total task cost cannot exceed its budget. This is checked whenever the project is saved.

### **Project Report**
- A report listing all projects along with their budgets.

#### **Role Requirements**:
- Only users with the `Project Manager` role can view this report.

---

## **API Endpoints**

### 1. **Fetch Tasks**
- **Endpoint**: `/api/method/task_manager.api.get_tasks`
- **Parameters**:
  - `status`: (Optional) Filter tasks by their status (`Open` or `Closed`).
- **Response**:
  - Returns a list of tasks with their name and due date.

### 2. **Bulk Update Task Status**
- **Endpoint**: `/api/method/task_manager.api.update_task_status`
- **Parameters**:
  - `task_ids`: A list of task IDs to update.
  - `status`: The new status to apply to the tasks.
- **Response**:
  - Updates the status of the specified tasks.

---

## **Hooks**

- **Task Validation**:
  - A hook is set up to validate tasks before they are saved.
  - Logic for validation is implemented in `task_manager.utils.validate_task`.

---

## **Setup and Installation**

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd task_manager
    ```
2. install app
3. migrate app

## **Usage Instructions**

### **Project and Task Management**
1. Create a project and specify its budget.
2. Add tasks to the project and assign costs.
3. Ensure the total task cost does not exceed the project budget.

### **Reports**
1. Access the project report via the Reports section.
2. Ensure the user has the `Project Manager` role to view the report.

### **Tasks**
1. A user with the `Task Employee` role can:
   - View only tasks they created or tasks assigned to them.
   - Manage the progress and details of their tasks.
2. Tasks assigned to a specific employee will appear in their task list automatically.

### **APIs**
- Use the provided APIs to manage tasks programmatically.

---

## **Roles and Permissions**

- **System Manager**:
  - Full access to all features, including creating, editing, and deleting projects and tasks.

- **Project Manager**:
  - Access to the project report.
  - Manage projects and all associated tasks.

- **Task Employee**:
  - Access only to tasks they created or tasks assigned to them.
  - Cannot access project-level data or reports.

---

## **Notes**

- The app assumes proper configuration of roles and permissions for optimal functionality.
- Developers are encouraged to review the API logic for enhancements and optimizations.


#### License

mit