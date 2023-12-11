import os
os.chdir("/Users/alfredarsenault/Downloads")

FILES = ["Fall_2025.csv","Fall_2026.csv","Spring_2026.csv"]
KEYS = ["last name","first_name", "student ID","P1","P2","P3","T1","T2","T3"]
def read_file(filename):
    with open(filename, "r") as infile:
#throw away the two header lines
        infile.readline()
        infile.readline()
#now read the rest of the file
        data = infile.readlines()
        for i in range(len(data)):
            data[i] = data[i].split(',')
        return data

def create_dictionary(student_rec):
        new_student = {}
        new_student["last name"] = student_rec[0].strip("\"")
        new_student["first name"] = student_rec[1].strip("\"")
        new_student["student ID"] = student_rec[2]
        new_student["P1"] = int(student_rec[3])
        new_student["P2"] = int(student_rec[4])
        new_student["P3"] = int(student_rec[5])
        new_student["T1"] = int(student_rec[6])
        new_student["T2"] = int(student_rec[7])
        new_student["T3"] = int(student_rec[8])
        return new_student

def insert_fields(student_rec):
    student_rec["Project_Total"] = student_rec["P1"] + student_rec["P2"] + student_rec["P3"]
    student_rec["Total_Score"] = student_rec["Project_Total"] + student_rec["T1"] + student_rec["T2"] + student_rec["T3"]
    if student_rec["Total_Score"] >= 576:
        student_rec["Letter_Grade"] = "A"
    elif student_rec["Total_Score"] >= 512:
        student_rec["Letter_Grade"] = "B"
    elif student_rec["Total_Score"] >= 448:
        student_rec["Letter_Grade"] = "C"
    elif student_rec["Total_Score"] >= 384:
        student_rec["Letter_Grade"] = "D"
    else:
        student_rec["Letter_Grade"] = "F"
    return student_rec



def read_the_files():
    big_list = []
    for filename in FILES:
        student_list = read_file(filename)
        for i in range(len(student_list)):
            student_list[i] = create_dictionary(student_list[i])
            student_list[i] = insert_fields(student_list[i])
        big_list.append(student_list)
    return big_list

def main_menu():
    print ("Welcome to the Student Grade Information Service")
    print("\n What would you like to do?")
    print("\n To search by student last name, enter 'L'")
    print("\n To search by student ID, enter 'S'")
    print("\n To exit the system, enter 'Q'")
    choice = input("")
    return choice

def get_sem():

    print ("In which semester was the student enrolled \n")
    print ("Enter 'F' for Fall 2025\n")
    print ("Enter 'S' for Spring 2026\n")
    print ("Enter 'T' for Fall 2026\n")
    print ("Enter 'U' if you do not know")
    ans = input("").upper()
    while ans not in ["S","T","F","U"]:
        print ("That is not a valid input")
        print("In which semester was the student enrolled \n")
        print("Enter 'F' for Fall 2025\n")
        print("Enter 'S' for Spring 2026\n")
        print("Enter 'T' for Fall 2026\n")
        print("Enter 'U' if you do not know")
        ans = input("").upper()

    return ans

def find_ID(sID, c):
    i = 0
    while i < len(c):
        if c[i]["student ID"] == sID:
            return (c[i])
        else:
            i+= 1
    return {}


def find_name(name, c):
    num_matches = 0
    matches = []
    for i in range(len(c)):
        if name == c[i]["last name"]:
            num_matches += 1
            matches.append(i)
    if num_matches > 1:
        rec = disambiguate(matches,c)
    elif num_matches == 1:
        rec = c[i]
    else:
        rec = {}
    return rec

def disambiguate(matches,c):
    print("Which student did you mean?")
    for i in matches:
        print(i, c[i])
    ans = int(input(""))
    return c[ans]

def last_name_request(db):
    sem = get_sem()
    lname = input("Please enter the student's last name")
    if sem == "F":
        c = db[0]
        response = find_name(lname, c)
        if response == {}:
            print("We're sorry, that student was not enrolled during that semester")
            return
        else:
            print_response(response)
    elif sem == "S":
        c = db[2]
        response = find_name(lname, c)
        if response == {}:
            print("We're sorry, that student was not enrolled during that semester")
            return
        else:
            print_response(response)
    elif sem == "T":
        c = db[1]
        response = find_name(lname, c)
        if response == {}:
            print("We're sorry, that student was not enrolled during that semester")
            return
        else:
            print_response(response)
    else:
        found = False
        k = 0
        while k < 3 and not found:
            response = find_name(lname,db[k])
            if response == {}:
                k += 1
            else:
                print_response(response)
                found = True
        if not found:
            print ("We're sorry; that student was never enrolled")
    return

def print_response(student):
    for key in student.keys():
        print(key, student[key])
    return

def student_ID_request(db):
    sem = get_sem()
    sID = input("Please enter the student's ID")
    if sem == "F":
        c = db[0]
        response = find_ID(sID, c)
        if response == {}:
            print("We're sorry, that student was not enrolled during that semester")
            return
        else:
            print_response(response)
    elif sem == "S":
        c = db[2]
        response = find_ID(sID, c)
        if response == {}:
            print("We're sorry, that student was not enrolled during that semester")
            return
        else:
            print_response(response)
    elif sem == "T":
        c = db[1]
        response = find_ID(sID, c)
        if response == {}:
            print("We're sorry, that student was not enrolled during that semester")
            return
        else:
            print_response(response)
    else:
        found = False
        k = 0
        while k < 3 and not found:
            response = find_ID(sID, db[k])
            if response == {}:
                k += 1
            else:
                print_response(response)
                found = True
        if not found:
            print("We're sorry; that student was never enrolled")
    return


def transact(db):
    choice = main_menu().upper()
    while choice != "Q":
        if choice == "L":
            last_name_request(db)
        elif choice == "S":
            student_ID_request(db)
        else:
            print("Error; that is not a valid choice")
        choice = main_menu().upper()
    print("Thank you for using the system")
    return



if __name__ == "__main__":
    d = read_the_files()
    j = transact(d)
