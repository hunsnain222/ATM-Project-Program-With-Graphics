import csv
import os

def join():
    directory = "Data"
    name = "usersdata.csv"
    filename = os.path.join(directory, name)
    return filename

#when 1 is entered from main(login_user)
def data():
    filename = join()
    d = {}
    # with open(filename, "r") as ap:
    with open(filename, "r") as rd:
            reader = csv.reader(rd) # This is an object for reader
            for us in reader:
                    if us == []:
                        continue
                    else:
                        name = us[0]
                        pin = us[1]
                        amt = float(us[2])
                        d[name] = (pin,amt)
            # print(d)
            return d
        
    
