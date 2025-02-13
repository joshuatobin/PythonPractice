import csv
from datetime import datetime, timedelta

class Employee():
    def __init__(self, id, name, department, start_date, salary):
        self.id = id
        self.name = name
        self.department = department
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.salary = float(salary)

    def __repr__(self):
        return f"Employee: {self.name}, salary: {self.salary}, start data: {self.start_date}"
        
class Department():
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
            
    def calc_avg_salary(self):
        if not self.employees:
            return 0

        return self.sum_of_salaries() / len(self.employees)
    
    def sum_of_salaries(self):
        if not self.employees:
           return 0
       
        return sum(emp.salary for emp in self.employees)
   
    # without generators      
    # def calc_avg_salary(self):
    #     total_salary = 0
    #     count = 0
    #     for emp in self.employees:
    #         total_salary += emp.salary
    #         count += 1
    #     if count == 0:
    #         return 0
    #     return total_salary / count

    def get_employees(self):
        return self.employees
    
    def __repr__(self):
        return f"Department: {self.department_name}, Employees: {len(self.employees)}"
    
def write_csv(fileName, data):
    """
    Write the CSV
    """
    with open(fileName, "w", encoding="utf-8") as csv_file:
         csv_file.write(data)

def main():
    """
    Your task is to write Python code that processes this file and answers the following questions:  
       - What is the average salary for each department?  
       - How many employees were hired in the last 5 years?  
       - Which department has the highest total payroll (sum of salaries)?  
    """
    csvData = """EmployeeID,Name,Department,Salary,HireDate
    1,John Doe,Engineering,90000,2016-07-23
    2,Jane Smith,Marketing,60000,2019-03-11
    3,Emily Johnson,Engineering,95000,2014-11-02
    4,Michael Brown,HR,45000,2018-08-05
    5,Linda Taylor,Marketing,62000,2020-01-18
    6,Chris Wilson,Sales,70000,2015-06-30
    7,Sarah Davis,Engineering,98000,2021-10-10
    8,Matthew Moore,Sales,72000,2017-02-22"""

    # Function to write CSV data to a file
    file_name="employees.csv"
    write_csv(file_name, csvData)

    departments = {}

    # Implement a function to read and parse the CSV file, 
    # creating Employee instances and organizing them into their respective Department instances.
    with open("employees.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader) # Always skip header row

        for row in csv_reader:
            emp = Employee(id=row[0], name=row[1], department=row[2], start_date=row[4], salary=row[3])
            if emp.department not in departments:
                departments[emp.department] = Department(emp.department)
            departments[emp.department].add_employee(emp)
            
    # Calculate and display average salary per department
    for dept in departments.values():
        print(f"Average salary in {dept.department_name}: ${dept.calc_avg_salary():,.2f}")
    
    # Summary of the engineering department
    engineering_dept = departments.get('Engineering')
    if engineering_dept:
        print(f"Employees in {engineering_dept.department_name} Department:")
        for emp in engineering_dept.get_employees():
            print(emp)

    # Sum of all salaries            
    print("\nSum of all Salaries")
    for dept in departments.values():
        print(f"{dept.department_name}: ${dept.sum_of_salaries():,.2f}")
    
    # How many employees were hired in the last 5 years? 
    print("\nEmployees hired in the last 5 years")
    cutoff_date = datetime.now() - timedelta(days=5*365)

    for dept in departments.values():
        for emp in dept.get_employees():
            if emp.start_date >= cutoff_date:
                print(emp)
    
    
if __name__ == "__main__":
    main()
    
    
