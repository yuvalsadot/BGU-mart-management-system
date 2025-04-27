from persistence import *

def main():
    #1
    print("Activities")
    for activity in repo.activities.find_all(order_by='date'):
        print(activity.__str__())
    print("Branches")
    for branche in repo.branches.find_all(order_by='id'):
        print(branche.__str__())
    print ("Employees")
    for employee in repo.employees.find_all(order_by='id'):
        print(employee.__str__())
    print ("Products")
    for product in repo.products.find_all(order_by='id'):
        print(product.__str__())
    print ("Suppliers")
    for supplier in repo.suppliers.find_all(order_by='id'):
        print(supplier.__str__())
    #2
    print("Employees report")
    for employee in repo.employees.find_all(order_by='name'):
        name = employee.name
        salary = employee.salary
        branche = repo.branches.find(id=employee.branche)[0].location
        totalSales = 0
        if len(repo.activities.find_all()) > 0:
            for activity in repo.activities.find_all():
                if activity.activator_id == employee.id & activity.quantity < 0:
                    totalSales += (-1) * activity.quantity * repo.products.find(id = activity.product_id).price
        print("{} {} {} {}".format(name, salary, branche, totalSales))
    #3
    print("Activities report")
    if len(repo.activities.find_all()) > 0:
        query = """
            SELECT activities.date, products.description, activities.quantity,
                CASE WHEN activities.quantity < 0 THEN employees.name ELSE 'None' END as seller_name,
                CASE WHEN activities.quantity > 0 THEN suppliers.name ELSE 'None' END as supplier_name
            FROM activities
            LEFT JOIN products ON activities.product_id = products.id
            LEFT JOIN employees ON activities.activator_id = employees.id AND activities.quantity < 0
            LEFT JOIN suppliers ON activities.activator_id = suppliers.id AND activities.quantity > 0
            ORDER BY activities.date
        """
        newActivities = repo.execute_command(query)
        for activity in newActivities:
            date, description, quantity, seller_name, supplier_name = activity
            if (seller_name == 'None'):
                print("('{}', '{}', {}, {}, '{}')".format(date, description, quantity, seller_name, supplier_name))
            else:
                print("('{}', '{}', {}, '{}', {})".format(date, description, quantity, seller_name, supplier_name))

if __name__ == '__main__':
    main()