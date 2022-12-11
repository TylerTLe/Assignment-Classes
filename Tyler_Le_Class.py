# Name: Tyler Le
# Course: CPRG-216-G
# Date: 12/10/2022
# Assignment: Classes | Parts did for assignment: Doctor Class and Display menu 

def DisplayMenu():
    print("Welcome to Alberta Hospital (AH) Managment system\nSelect from the following options, or select 0 to stop:\n1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients")
    while True:
        choice = input()
        if choice == "1":
            DoctorsMenu()
        elif choice == "2":
            FacilitiesMenu()
        elif choice == "3":
            LaboratoriesMenu()
        elif choice == "4":
            PatientsMenu()
        elif choice == "0":
            break

def DoctorsMenu():
    print("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu")
    while True:
        choice = input()
        doctor = Doctor()
        doctor_list = doctor.readDoctorsFile()
        if choice == "1":
            # Display Doctors list
            doctor.displayDoctorsList(doctor_list)
            print('\nBack to the prevoius Menu\n')
            DoctorsMenu()
        elif choice == "2":
            # Search for doctor by ID
            doctor.searchDoctorById(doctor_list)
            print('\nBack to the prevoius Menu\n')
            DoctorsMenu()
        elif choice == "3":
            # Search for doctor by name
            doctor.searchDoctorByName(doctor_list)
            print('\nBack to the prevoius Menu\n')
            DoctorsMenu()
        elif choice == "4":
            # Add doctor
            updated_doctor_list = doctor.addDrToFile(doctor_list)
            format_doctor_list = doctor.formatDrInfo(updated_doctor_list)
            doctor.writeListOfDoctorsToFile(format_doctor_list)
            print('\nBack to the prevoius Menu\n')
            DoctorsMenu()
        elif choice == "5":
            # Edit doctor info
            updated_doctor_list = doctor.editDoctorInfo(doctor_list)
            format_doctor_list = doctor.formatDrInfo(updated_doctor_list)
            doctor.writeListOfDoctorsToFile(format_doctor_list)
            print('\nBack to the prevoius Menu\n')
            DoctorsMenu()
        elif choice == "6":
            DisplayMenu()

def FacilitiesMenu():
    print("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu")
    while True:
        choice = input()
        if choice == "1":
            # Display Facilities list
            print('\nBack to the prevoius Menu\n')
            FacilitiesMenu()
        elif choice == "2":
            # Add Facility
            print('\nBack to the prevoius Menu\n')
            FacilitiesMenu()
        elif choice == "3":
            DisplayMenu()

def LaboratoriesMenu():
    print("Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu")
    while True:
        choice = input()
        if choice == "1":
            # Display laboratories list
            
            
            print('\nBack to the prevoius Menu\n')
            LaboratoriesMenu()
 
        elif choice == "2":
            # Add laboratory
            
            
            print('\nBack to the prevoius Menu\n')
            LaboratoriesMenu()
        elif choice == "3":
            DisplayMenu()

def PatientsMenu():
    print("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu")
    while True:
        choice = input()
        if choice == "1":
            # Display patients list
            
            
            print('\nBack to the prevoius Menu\n')
            PatientsMenu()
        elif choice == "2":
            # Search for patient by ID
            
            
            print('\nBack to the prevoius Menu\n')
            PatientsMenu()
        elif choice == "3":
            # Add patient
            
            
            print('\nBack to the prevoius Menu\n')
            PatientsMenu()
        elif choice == "4":
            # Edit patient info


            print('\nBack to the prevoius Menu\n')
            PatientsMenu()
        elif choice == "5":
            DisplayMenu()

class Doctor:
    def __init__(self):
        pass

    def __str__(self):
        return f"{self.id}, {self.name}, {self.specialization}, {self.workingtime}, {self.qualification}, {self.roomnumber}"
        
    def formatDrInfo(self,doctor_list):
        format_doctor_list=''
        for values in doctor_list:
            values = values[0]+'_'+values[1]+'_'+values[2]+'_'+values[3]+'_'+values[4]+'_'+values[5]+'\n'
            format_doctor_list += values
        return format_doctor_list
    
    def addDrToFile(self,doctor_list):
        self.id= input("Enter the doctor's ID:\n")
        self.name = input("Enter the doctor's name:\n")
        self.specialization = input("Enter the doctor's specialization:\n")
        self.workingtime = input("Enter the doctor's working time:\n")
        self.qualification = input("Enter the doctor's qualification:\n")
        self.roomnumber = input("Enter the doctor's room number:\n")
        add_doctor = [self.id,self.name,self.specialization,self.workingtime,self.qualification,self.roomnumber]
        doctor_list.append(add_doctor)
        return doctor_list
    
    def readDoctorsFile(self):
        # Create an empty list to store the doctors
        doctor_list = []
        with open("Class Assignment\doctors.txt", "r") as doctors_file:
            for line in doctors_file:
                values = line.strip().split("_")
                doctor_list.append(values)
        return doctor_list
    
    def displayDoctorsList(self,doctor_list):
        table = ""
        for doctor in doctor_list:
            table += f"{doctor[0]:<5} {doctor[1]:^15} {doctor[2]:^15} {doctor[3]:^15} {doctor[4]:^15} {doctor[5]:^15}\n"
        print(table)
        
    def searchDoctorById(self,doctor_list):
        id = input("Enter the doctor's ID:\n")
        for doctor in doctor_list:
            if id == doctor[0]:
                print('\nId','       Name','         Speciality','    Timing','    Qualification','    Room Number\n')
                print(f"{doctor[0]:<5} {doctor[1]:^15} {doctor[2]:^15} {doctor[3]:^15} {doctor[4]:^15} {doctor[5]:^15}\n")
                return doctor
        print("\nCan't find the doctor with the same name on the system\n")
        return None

    def searchDoctorByName(self,doctor_list):
        name = input("Enter the doctor's name:\n")
        for doctor in doctor_list:
            if name == doctor[1]:
                print('\nId','       Name','         Speciality','    Timing','    Qualification','    Room Number\n')
                print(f"{doctor[0]:<5} {doctor[1]:^15} {doctor[2]:^15} {doctor[3]:^15} {doctor[4]:^15} {doctor[5]:^15}\n")
                return doctor
        print("\nCan't find the doctor with the same name on the system\n")
        return None
    
    def displayDoctorinfo(self,doctor_list):
        str_list = [str(doctor) for doctor in doctor_list]
        print(str_list)
        return None
    
    def editDoctorInfo(self,doctor_list):
        id = input('Please enter the id of the doctor that you want to edit their information:\n')
        for doctor_info in doctor_list:
            if id == doctor_info[0]:
                doctor_info[1]=input('Enter new Name: \n')
                doctor_info[2]=input('Enter new Specilist in:\n')
                doctor_info[3]=input('Enter new Timing: (e.g., 7am-10pm):\n')
                doctor_info[4]=input('Enter new Qualification: \n')
                doctor_info[5]=input('Enter new Room number: \n')
                edit_doctor = doctor_list.index(doctor_info)
                doctor_list[edit_doctor]=doctor_info
                return doctor_list
        print("Can't find the doctor with the same ID on the system")
        pass
    
    def writeListOfDoctorsToFile(self,format_doctor_list):
        with open('Class Assignment\doctors.txt','w') as write_to_file:
            write_to_file.write(format_doctor_list)
        pass

if __name__ == '__main__':
    DisplayMenu()
    

