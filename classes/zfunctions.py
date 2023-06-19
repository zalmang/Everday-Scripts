from datetime import datetime

def zinput(inputstm, str="", opt="y/n"):
    if str == "":
        str = input(f"{inputstm} {opt}")
    if str.lower() == "y":
        return 1
    elif str.lower() == "n":
        return 0
    else:
        return zinput("Invalid entry. Please try again (y/n): ")
    
def dateInput():
        #move this to zfunctions
        udate = input("What date did you download your files? (dd-mm-yyyy)")
        if (udate.length != 10 and udate.split("-").length == 3):
            print("Invalid date entry")
            return dateInput()
        uday = udate[0:1]
        umonth = udate[3:4]
        uyear = uyear[6:9]
        if (0 < uday < 32 and 0 < umonth < 12):
            return datetime.strptime(udate, "%m-%d-%Y").date()
        else:
            print("Invalid input. Try again")