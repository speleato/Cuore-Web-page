__author__ = 'Kirby'

from .Model import Department
import Title.py
import Person.py
import Newsfeed.py

sandy = Person("Sandy", "Siththanandan", "sandymeep@gmail.com", "Applications Developer", 3)
store.save_unique("People", "email", sandy.email, sandy)
leo = Person("Leo", "Schultz", "leo@cuore.io", "President", 3)
leo.submit_settings()

#if store.load_unique("People", "first_name", "george", Person) = None:
#    print me

Kirby = Person("Kirby", "Linvill", "kirby@cuore.io", "Applications Developer", 3)
Kevin = Person("Kevin", "Ryan", "kevincryan23@gmail.com", "Vice President", 3)
#List of people in each position, first entry is the name of the position
President = ["President", leo]
Vice_President = ["Vice President", Kevin]
Lead_Applications_Developer = ["Lead Applications Developer"]
Applications_Developer = ["Applications Developer", Kirby, sandy]
Web_Applications_Developer = ["Web Applications Developer"]
Lead_Systems_Engineer = ["Lead Systems Engineer"]
Lead_Hardware_Engineer = ["Lead Hardware Engineer"]

#Lists of titles in each department
business = [President, Vice_President]
applications = [Lead_Applications_Developer, Applications_Developer, Web_Applications_Developer]
systems = [Lead_Systems_Engineer]
hardware = [Lead_Hardware_Engineer]

#List of departments containing the lists of titles in that department
departments = [business, applications, systems, hardware]
departmentNames = ["Business", "Applications", "Systems", "Hardware"]

#Company node tying departments together
cuore = Company("Cuore")
'''
#List of employees
Kirby = Person("Kirby", "Linvill", "kirby@cuore.io", "Applications Developer")
Kevin = Person("Kevin", "Ryan", "kevincryan23@gmail.com", "Vice President")
employees = [Kirby, Kevin]

for i in range(0, len(employees)):
    title=Title(employees[i].title)
    store.relate(title, "IS A", employees[i])
    store.save_unique("People", "email", employees[i].email, employees[i])
'''
for i in range(0, len(departments)):
    dep = Department(departmentNames[i])
    newsfeed = Newsfeed(departmentNames[i], 0)
    store.relate(cuore, "UNDER", dep)
    store.relate(dep, "NEWSFEED", newsfeed)
    for j in range(0, len(departments[i])):
        title = Title(departments[i][j][0])
        store.relate(dep, "IN", title)
        for k in range(1, len(departments[i][j])):
            employee = departments[i][j][k]
            print departments[i][j][k]
            print type(employee)
            store.save_unique("People", "email", employee.email, employee)
            store.relate(title, "IS A", employee)
        store.save_unique("Title", "name", title.name, title)
    store.save_unique("Newsfeed", "name", departmentNames[i], newsfeed)
    store.save_unique("Department", "name", departmentNames[i], dep)
store.save_unique("Company", "name", "Cuore", cuore)

