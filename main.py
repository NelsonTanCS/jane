# Employee Database Project
# Jane Flegel - Laney - ISIT333 - 11/29/22

import sqlite3
sqlite3.connect('employee.db')
conn = sqlite3.connect('test_database') 
c = conn.cursor()

employeeDetails=[]
def addEmployee():

  conn.commit()

firstName = ( input("First Name: "))  
lastName = ( input("Last Name : "))  
address = ( input("Address : "))  
city = ( input("City : "))  
state = ( input("State : "))  
zipcode = int( input("Zip Code : "))  
phoneNumber = int( input("Phone Number : "))  
hourlyRate = int( input("Hourly Rate : "))
departmentName = ( input("Department Name : "))
employeeId=len(employeeDetails)+1
email=firstName+lastName+".com"  

employeeDetails.append({
        'employeeId':employeeId,
        'firstName':firstName,
        'lastName':lastName,
        'address':address,
        'city':city,
        'state':state,
        'zipcode':zipcode,
        'email':email,
        'phoneNumber':phoneNumber,
        'hourlyRate':hourlyRate,
        'departmentName':departmentName })  

def ListEmployeeById():
    for data in employeeDetails:
        print('Employee Id :'+ str(data['employeeId']))
        print('Email Address :'+ data['email'])
        print('Name :'+ data['firstName']+" "+data['lastName'])
        print('Department Name :'+ data['departmentName'])
        print('\n')

def ListEmployeeByName():
    for data in employeeDetails:
        print('Name :'+ data['firstName']+" "+data['lastName'])
        print('Address :'+ data['address'])
        print('Phone Number :'+ str(data['phoneNumber']))
        print('\n')        

def searchByLastName(lastName):  
    for data in employeeDetails:
        if data['lastName']==lastName:
            print('Employee Id :'+ str(data['employeeId']))
            print('Name :'+ data['firstName']+" "+data['lastName'])
            print('Address :'+ data['address'])
            print('City :'+ data['city'])
            print('Zip Code :'+ str(data['zipcode']))
            print('Email Address :'+ data['email'])
            print('Phone Number :'+ str(data['phoneNumber']))
            print('Hourly Rate :'+ str(data['hourlyRate']))
            print('Department Name :'+ data['departmentName'])
            print('\n')

def updateHourlyRate(Id):  
    for data in employeeDetails:
        if data['employeeId']==Id:
            hourlyRate = int( input("Enter Hourly Rate : "))
            employeeDetails[employeeDetails.index(data)]['hourlyRate']=hourlyRate
            print("Update Successfully")
            break      

def updateContactInformation(Id):  
    for data in employeeDetails:
        if data['employeeId']==Id:
            city = ( input("Enter City Name : "))
            address = ( input("Enter address : "))
            zipcode = int( input("Enter zipcode : "))
            phoneNumber = int( input("Enter phone number : "))
            employeeDetails[employeeDetails.index(data)]['city']=city
            employeeDetails[employeeDetails.index(data)]['address']=address
            employeeDetails[employeeDetails.index(data)]['zipcode']=zipcode
            employeeDetails[employeeDetails.index(data)]['phoneNumber']=phoneNumber
            print("Update Successfully")
            return
          
def deleteEmployee(Id):  
    idx=None
    for data in employeeDetails:
        if data['employeeId']==Id:
            idx=employeeDetails.index(data)
            break
        
    if idx!=None:
        employeeDetails.pop(idx)
        print("Removed Successfully")
    else:
        print("Failed to Remove")
      
while True:  
    print("\nMENU")  
    print("1. Add Employee")  
    print("2. List Employee id numbers, names, email addresses, and their department name")  
    print("3. List Employee Name, Full Address & Phone Number")  
    print("4. Search By Last Name")  
    print("5. Update Hourly Rate")
    print("6. Update Contact Information")
    print("7. Delete Employee")
    print("8. Exit")
    
    choice = int(input("\nEnter the Choice: "))
    if choice == 1:  
        print( "\nAdd Employee\n")  
        addEmployee()  
    elif choice == 2:  
        print( "\nList Employee id numbers, names, email addresses, and their department name\n")  
        ListEmployeeById() 
    elif choice == 3:  
        print( "\nList Employee Name, Full Address & Phone Number\n")  
        ListEmployeeByName()  
        
    elif choice == 4:  
        print( "\nSearch By Last Name\n")  
        lastName = ( input("Last Name: "))  
        searchByLastName(lastName)  
  
    elif choice == 5:  
        print( "\nUpdate Hourly Rate\n")  
        Id = int( input("Enter the Employee Id: "))  
        updateHourlyRate(Id) 
    
    elif choice == 6:  
        print( "\nUpdate Contact Information\n")  
        Id = int( input("Enter the Employee Id: "))  
        updateContactInformation(Id)     
    
    elif choice == 7:  
        print( "\nDelete Employee \n")  
        Id = int( input("Enter the Employee Id: ")) 
      # Confirm username before deleting
      #input("\nAre you sure you want to delete [Id]?\n y for yes and n for no")
        
        deleteEmployee(Id)     
    
    elif choice == 8:  
        break  
      
    else:  
        print( "Please Provide a valid Input!")