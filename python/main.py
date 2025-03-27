from visitor_management_system import VisitorManagementSystem
import datetime

if __name__ == "__main__":
    vms = VisitorManagementSystem()
    vms.add_visitor("John Doe", "P123456789", datetime.date(2025, 3, 25), 7)
    vms.add_visitor("Jane Smith", "P987654321", datetime.date(2025, 3, 26), 10)

    visitors = vms.list_all_visitors()
    for visitor in visitors:
        print(vars(visitor))

    report = vms.generate_report()
    print("Visitor Report by Year:", report)