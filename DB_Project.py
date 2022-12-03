import mysql.connector
mydb = mysql.connector.connect(host="localhost", user='root', password='3377', auth_plugin='mysql_native_password',
                                   database="housing_admin_system")
def ListResidents():
    print("Printing community wise resident details.......................\n")
    print("\nres_id\t\tname\t\tDOB\t\tapt_num\t\tgender\t\tcommunity\n-----------------------------------------------------------------------------")
    try:

        mycursor = mydb.cursor()
        mycursor.execute("select r.*,c.name from resident r join apartment a on r.apt_num=a.apt_id join community c on c.com_id = a.com_id order by c.name")
        result = mycursor.fetchall()
        for i in result:
            for j in i:
                print(j, end="    :    ")
            print(end="\n")
        print("Total number of rows:", mycursor.rowcount)
    except:
        print("There is an error in accessing the relation!")

def Residentdetails(id):
    try:
        print("Printing resident details................")
        mycursor = mydb.cursor()
        q='select r.*,a.street_name,c.name from resident r join apartment a on r.apt_num=a.apt_id join community c on c.com_id = a.com_id where r.res_id=%s'
        data = (id,)
        mycursor.execute(q,data)
        result = mycursor.fetchall()
        if mycursor.rowcount == 0:
            print("Record Not Found!!")
        else:
            print("\nres_id\t\tname\t\tDOB\t\tapt_num\t\tgender\t\tstreet_address\t\tcommunity\n------------------------------------------------------------------------------------")
            for i in result:
                for j in i:
                    print(j, end="    :    ")
                print(end="\n")
        print("Total number of rows:", mycursor.rowcount)
    except:
        print("There is an error in accessing the relation!")

def DeleteResident(id1):
    try:
        mycursor = mydb.cursor()
        q = 'delete from resident where res_id = %s'
        data = (id1,)
        mycursor.execute(q, data)
        mydb.commit()
        if mycursor.rowcount == 1:
            print("Deleting the resident................")
            print("record deletion successful.")
            print("Rows affected:",mycursor.rowcount)
        else:
            print("No such record.")
    except:
        print("There is an error in accessing the relation!")

def InsertResident(id, name, dob,apt,g):
    try:
        mycursor = mydb.cursor()
        q = 'insert into resident values (%s, %s, %s, %s, %s)'
        data = (id,name,dob,apt,g,)
        mycursor.execute(q, data)
        mydb.commit()
        if mycursor.rowcount == 1:
            print("inserting into the resident................")
            print("record insertion successful.")
            print("Rows affected:",mycursor.rowcount)
        else:
            print("Please enter the valid details.")
    except:
        print("There is an error in accessing the relation! or Please enter valid details!")

def UpdateResident(id, name, dob,apt,g):
    try:
        mycursor = mydb.cursor()
        q = 'update resident set name=%s, DOB=%s,apt_num=%s, gender=%s where res_id=%s'
        data = (name,dob,apt,g,id,)
        mycursor.execute(q, data)
        mydb.commit()
        if mycursor.rowcount == 1:
            print("updating the resident................")
            print("record updation successful.")
            print("Rows affected:",mycursor.rowcount)
        else:
            print("Please enter the valid details.")
    except:
        print("There is an error in accessing the relation! or Please enter valid details!")

def EmployeeDepartment(inp):
    try:
        mycursor = mydb.cursor()
        q = 'select count(*) from employee where dept = %s'
        if inp==1:
            k="Leasing"
        elif inp==2:
            k ="Recreation"
        elif inp==3:
            k = "Cleaning"
        data = (k,)
        mycursor.execute(q, data)
        result = mycursor.fetchall()
        if mycursor.rowcount == 0:
            print("Record Not Found!!")
        else:
            print("The count of employees working in", k ,"is:")
            for i in result:
                for j in i:
                    print(j, end="")
                print(end="\n")
        print("Total number of rows:", mycursor.rowcount)

    except:
        print("There is an error in accessing the relation! or Please enter valid details!")

def PaymentMethod():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("select count(*),method from payment_account group by method")
        result = mycursor.fetchall()
        if mycursor.rowcount == 0:
            print("Record Not Found!!")
        else:
            print("\ncount\t\tmethod\n----------------------------------------------")
            for i in result:
                for j in i:
                    print(j, end="    :    ")
                print(end="\n")
        print("Total number of rows:", mycursor.rowcount)
    except:
        print("There is an error in accessing the relation! or Please enter valid details!")

def getActivity(name):
    try:
        mycursor = mydb.cursor()
        q= "select a.type from activity a join opts_for o on a.activity_id=o.activity_id join resident r on r.res_id = o.res_id where name  = %s"
        data = (name,)
        mycursor.execute(q,data)
        result = mycursor.fetchall()
        if mycursor.rowcount == 0:
            print("Resident not involved in any activity!!")
        else:
            print("\nActivity_involved\n----------------------------------------------")
            for i in result:
                for j in i:
                    print(j, end="")
                print(end="\n")
        print("Total number of rows:", mycursor.rowcount)
    except:
        print("There is an error in accessing the relation! or Please enter valid details!")

def getComplaint(name):
    try:
        mycursor = mydb.cursor()
        q= "select c.c_type from complaints c join resident r on r.res_id=c.res_id where r.name= %s"
        data = (name,)
        mycursor.execute(q,data)
        result = mycursor.fetchall()
        if mycursor.rowcount == 0:
            print("Record Not Found!!")
        else:
            print("\nComplaint Type\n----------------------------------------------")
            for i in result:
                for j in i:
                    print(j, end="")
                print(end="\n")
        print("Total number of rows:", mycursor.rowcount)
    except:
        print("There is an error in accessing the relation! or Please enter valid details!")

def getApartments():
    try:
        mycursor = mydb.cursor()
        mycursor.execute("select c.name,a.a_type,count(*) from apartment a join community c on c.com_id=a.com_id group by c.com_id,a_type order by c.com_id")
        result = mycursor.fetchall()
        if mycursor.rowcount == 0:
            print("Record Not Found!!")
        else:
            print("\ncommunity name\t\ttype of apt\t\tnumber of apts available\n----------------------------------------------")
            for i in result:
                for j in i:
                    print(j, end="    :    ")
                print(end="\n")
        print("Total number of rows:", mycursor.rowcount)
    except:
        print("There is an error in accessing the relation! or Please enter valid details!")


if __name__ == '__main__':
    try:
        print("Hello! Welcome to Housing Administration System!!!!")
        while(True):
            a=input("\nWould you like to see the MENU(Y/N):")
            if a=='Y' or a=='y':
                print('MENU:\n1.List All Residents-community wise\n2.Print the details of the resident based on resident_id\n3.Delete a  record in Resident\n4.Insert into Resident\n5.Update Resident Details\n6.Number of employees working in a department\n7.payments made in each of the payment methods\n8.Type of activity a resident is involved in 3\n9.Type of complaint raised by a resident\n10.Apartments available in a community\n11.Exit\n')
            op = int(input("\nPlease Enter the operation that you would like to perform:"))
            if op==1:
                ListResidents()
            elif op==2:
                res_in = int(input("\nPlease enter the resident_id for which details are needed:"))
                Residentdetails(res_in)
            elif op==3:
                res_in1 = int(input("\nPlease enter the resident_id to be deleted from the records:"))
                DeleteResident(res_in1)
            elif op==4:
                res_id = int(input("Please enter the resident_id to be inserted:"))
                res_name = input("Enter the name of the resident:")
                res_DOB = input("Enter the DOB of  resident:(MM/DD/YYYY)")
                res_apt = int(input("Enter the apartment number of the resident:"))
                res_gender = input("Enter the gender of the resident:(male/female)")
                InsertResident(res_id,res_name,res_DOB,res_apt,res_gender)
            elif op==5:
                res_id1 = int(input("Please enter the resident_id to be updated"))
                res_name1 = input("Enter the name of the resident to be updated:")
                res_DOB1 = input("Enter the DOB of  resident to be updated:(MM/DD/YYYY)")
                res_apt1 = int(input("Enter the apartment number of the resident to be updated:"))
                res_gender1 = input("Enter the gender of the resident to be updated:(male/female)")
                UpdateResident(res_id1,res_name1,res_DOB1,res_apt1,res_gender1)
            elif op==6:
                inp1 = int(input("Please select from the following list of departments:\n1.Leasing\n2.Recreation\n3.Cleaning\nEnter a number:"))
                EmployeeDepartment(inp1)
            elif op==7:
                PaymentMethod()
            elif op==8:
                name = input('Enter the name of the resident:')
                getActivity(name)
            elif op==9:
                name1 = input('Enter the name of the resident:')
                getComplaint(name1)
            elif op==10:
                getApartments()
            elif op==11:
                print("\n=====================Bye! Thanks for using the Housing Administration System.===========================")
                break
            else:
                print("Please enter a valid option between 1 and 10.")
    except:
        print("Something went wrong!!Please try again.")

