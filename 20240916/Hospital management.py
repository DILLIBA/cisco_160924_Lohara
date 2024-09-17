class HospitalManagementSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, name):
        if name not in self.patients:
            self.patients.append(name)
            print(f"Patient '{name}' added successfully.")
        else:
            print(f"Patient '{name}' already exists.")

    def remove_patient(self, name):
        if name in self.patients:
            self.patients.remove(name)
            print(f"Patient '{name}' removed successfully.")
        else:
            print(f"Patient '{name}' not found.")

    def list_patients(self):
        if self.patients:
            print("List of patients:")
            for patient in self.patients:
                print(f"- {patient}")
        else:
            print("No patients currently in the system.")

def main():
    system = HospitalManagementSystem()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Remove Patient")
        print("3. List Patients")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter the patient's name: ")
            system.add_patient(name)
        elif choice == '2':
            name = input("Enter the patient's name: ")
            system.remove_patient(name)
        elif choice == '3':
            system.list_patients()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


