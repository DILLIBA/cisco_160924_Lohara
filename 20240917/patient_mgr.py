#1. class Patient {id, name}
import json


class Patient:
    def __init__(self, id, name):
        self.id = id 
        self.name = name 
    def __str__(self):
        return f'[id={self.id}, name={self.name}]'
    def __repr__(self):
        return self.__str__()
#2. patients[]
patients = []

#3. patient_add(id, name)
def patient_add(id, name):
    global patients
    patient = Patient(id, name)
    patients.append(patient)
#4. patient_remove(id)
def patient_remove(id):
    global patients
    for patient in patients:
        if patient.id == id:
            print(patient)
            if input('Are you sure to delete(yes/no)?').lower() == 'yes':
                patients.remove(patient)
                print('Patient deleted successfully')
            return 
        #end if 
    #end for 
    print(f'No such id {id}')

# display by id
def patient_displayById(id):
    global patients
    for patient in patients:
     if patient.id == id:
      print(patients)
     else:
      print("pateint not found")
def patient_updateById(id , name):
     global patients
     for patient in patients:
         if patient.id == id:
             print(patient)
             if ('Are you sure to update the patient?(yes/no):').lower == 'yes':
                patient.name = name
                print('patient details updated succesfully!')
                return
            
#5. patient_display()
def patient_display():
    global patients
    for patient in patients:
        print(patient)
#6. menu 
def menu():
    choice = int(input('''1-add patient
2-delete patient by id
3-display all patients
4-display by Id
5-update by Id
7-end                       
your choice:'''))
    if choice == 1:
        id = int(input('Enter patient id:'))
        name = input('Enter patient name:')
        patient_add(id, name)
    elif choice == 2:
        id = int(input('Enter patient id to delete:'))
        patient_remove(id)
    elif choice == 3:
        patient_display()
    elif choice == 4:
        id =int(input('Enter patient id:'))
        patient_displayById(id)
    elif choice == 5:
        id =int(input('Enter patient id:'))
        name=input ('enter the name: ')
        patient_updateById(id , name)
    #elif choice==6:
    #  with open('patient_dict.json','w') as pt_db:
    #     json.dump(patient_add,pt_db)
    #     print('written file succefull') 
    
    elif choice == 7:
        pass 
    else:
        print('Invalid menu')
    return choice
#7. menus 
def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('Thank you for using the app')
#8. driver program
menus()
