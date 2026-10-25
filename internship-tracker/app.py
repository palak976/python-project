import json
import sqlite3




'''connection = sqlite3.connect("internship.db")

connection.execute("""
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    role TEXT,
    status TEXT
)
""")

connection.commit()
connection.close()


connection = sqlite3.connect("internship.db")

connection.execute("""
INSERT INTO applications (company_name, role, status)
VALUES ('Wipro', 'Software Engineer Intern', 'Applied')
""")

connection.commit()
connection.close()
'''


def saveApplications():
    import os
    print(os.path.abspath("applications.json"))
    with open("applications.json", "w") as file:
        json.dump(Application, file, indent=4)


def loadApplications():
    global Application
    try:
        with open("applications.json", "r") as file:
            Application = json.load(file)
            if not isinstance(Application, list):
                Application = []
    except FileNotFoundError:
        Application = []
    except json.JSONDecodeError:
        Application = []



Application= [
    {'Company_Name':'Google','Role':'Software Engineer Intern','Status':'Applied'},
    {'Company_Name':'Amazon','Role':'Software Engineer Intern','Status':'Interested'},
    {'Company_Name':'Microsoft','Role':'Software Engineer Intern','Status':'Interested'}
    ]
loadApplications()

def validStatus():
    valid_status = ['Interested', 'Applied', 'Interview', 'Rejected', 'Selected']

    status = input("Enter Status:").strip().title()

    while status not in valid_status:
        print("Invalid Status. Please Enter a Valid Status.")
        status = input("Enter Status:").strip().title()

    return status


def addApplication() :
    user_input = input("Do you want to add an application? (yes/no):")
    if user_input == 'yes' :
        company_name = input("Enter Company Name:")
        role_name = input("Enter Role:")
        status = validStatus()
        
        new_application = {
            'Company_Name': company_name,
            'Role': role_name,
            'Status': status
        }

        Application.append(new_application)
        print("Application added successfully")
        print(displayApplication())
        saveApplications()
    else:
        print("No application added")
    




def countInterestedApplications() :
    interested_internship = 0
    for i in Application :
        if i['Status'] == 'Interested':
            interested_internship += 1
    return interested_internship


def changeStatus() :
    for app in Application :
        if (app['Status'] == 'Interested') :
            app['Status'] = 'Applied'
            print(app['Company_Name'], "status updated")

    print('Total Application:',len(Application))

def updateStatus():
    company_name = input("Enter Company Name:")
    new_status= validStatus()
    for app in Application:
        if app['Company_Name'] == company_name:
            app['Status'] = new_status
            saveApplications()
            print("Status updated successfully")
            break
    else :
        print("Company Not Found")
    saveApplications()



def displayApplication() :
    return Application


while (True) :
    print("\n===== INTERNSHIP TRACKER =====")
    print("1. Add application")
    print("2. View applications")
    print("3. Count interested applications")
    print("4. Update application status")
    print("5. Exit")
    choice = input("Enter you choice:")
    if choice == "1":
        addApplication()
    elif choice == "2":
        print(displayApplication())
    elif choice == "3":
        print("Interested applications:",countInterestedApplications())
    elif choice == "4":
        updateStatus()
    elif choice == "5":
        break
    else:
        print("Invalid Input")




