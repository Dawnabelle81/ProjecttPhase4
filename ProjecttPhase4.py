#
#
#
from datetime import datetime
#################################################################################
def CreateUsers():
    print('##### Create users, passwords, and roles #####')
    ########## Open the file user.txt in append mode and assign to UserFile

    while True:
        ########## Write the line of code that will call function GetUserName and assign the return value to username

        if (username.upper() == "END"):
            break
        ########## Write the line of code that will call function GetUserPassword and assign the return value to userpwd

        ########## Write the line of code that will call function GetUserRole and assign the return value to userrole

        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(userDetail)
    # close file to save data
    ########### Write the line of code that will close the file UserFile



def GetUserName():
    ##### Write the code to enter the username or End and return username


def GetUserPassword():
    ##### Write the code to enter the pwd and return pwd


def GetUserRole():
    userrole = input("Enter role (Admin or User): ")
    while True:
        ###### Write the if statement that validates that Admin or User has been entered. If true, return userrole. If false, re-input userrole.


def printuserinfo():
    UserFile = open("Users.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "") #remove carriage return from end of line
        UserList = UserDetail.split("|")
        username = UserList [0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("User Name: ", username, "Password: ", userpassword, "Role: ", userrole)

##################################################################################################

def Login():
        # read login information and store in a list
    ########## Write the line of code that will open the file Users.txt in read mode

    UserName = input("Enter User Name: ")
    UserRole = "None"
    while True:
        ########## Write the line of code that will read a line from UserFile and assign it to UserDetail

        if not UserDetail:
            return UserRole, UserName
        ########## Write the line of code that will replace the carriage return in UserDetail

        ########## Write the line of code that will split UserDetail on the pipe delimiter (|) and assign it to UserList

        if UserName == UserList[0]:
            UserRole = UserList[2] # user is valid, return role
            return UserRole, UserName
    return UserRole, UserName
####################################################################################################