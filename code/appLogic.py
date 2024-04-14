# Importing class from dataAccess.py file
from dataAccess import DataInteractions
# Python Module to handle date and time
from datetime import datetime
# Python module to parse command-line arguments
import argparse

# Try-except block to check if the required library is installed
try:
    # Importing the PrettyTable class from the prettytable library
    # This is a library displaying tabular data in a visually appealing ASCII table format
    from prettytable import PrettyTable
# If the import fails, the except block will be executed
except ImportError:
    # Print a message indicating that the prettytable library is being installed
    print("Installing the prettytable library:")
    import subprocess
    # Run the command to install the prettytable library using pip
    subprocess.check_call([
        "python", "-m", "pip", "install", "prettytable"
    ])
    # Import the PrettyTable class from the prettytable library after installing it
    from prettytable import PrettyTable

# Class to handle the core functionality of the application
class AppLogic:

    def __init__(self):
        # Initialize the DataInteractions instance
        self.dataAccessLayer = DataInteractions()

    # Method to register a new member
    def registerMember(self):
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        email = input("Enter email: ")
        phoneNumber = input("Enter phone number (format of: 123-456-7890): ")
        fitnessGoal = input("Enter fitness goal: ")
        healthMetric = input("Enter health metric: ")
        self.dataAccessLayer.registerMember(firstName, lastName, email, phoneNumber, fitnessGoal, healthMetric)

    # Method to update a member's profile
    def updateMemberProfile(self):
        memberId = int(input("Enter member ID: "))
        firstName = input("Enter new first name: ")
        lastName = input("Enter new last name: ")
        email = input("Enter new email: ")
        phoneNumber = input("Enter new phone number (format of: 123-456-7890): ")
        fitnessGoal = input("Enter new fitness goal: ")
        healthMetric = input("Enter new health metric: ")
        self.dataAccessLayer.updateMemberProfile(memberId, firstName, lastName, email, phoneNumber, fitnessGoal, healthMetric)

    # Method to book a session for a member
    def bookSession(self):
        memberId = int(input("Enter member ID: "))
        trainerId = int(input("Enter trainer ID: "))
        bookingDate = datetime.strptime(input("Enter booking date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        bookingStartTime = datetime.strptime(input("Enter booking start time (Use 24-hour time): "), "%H:%M").time()
        bookingEndTime = datetime.strptime(input("Enter booking end time (Use 24-hour time): "), "%H:%M").time()
        self.dataAccessLayer.bookSession(memberId, trainerId, bookingDate, bookingStartTime, bookingEndTime)

    # Method to view all registered members
    def viewMembers(self):
        members = self.dataAccessLayer.viewMembers()
        if members:
            table = PrettyTable()
            table.field_names = ["ID", "First Name", "Last Name", "Email", "Phone", "Fitness Goal", "Health Metric"]
            for member in members:
                table.add_row(member)
            print("Registered Members:")
            print(table)
        else:
            print("No members found.")

    # Method to view all trainers
    def viewTrainers(self):
        trainers = self.dataAccessLayer.viewTrainers()
        if trainers:
            table = PrettyTable()
            table.field_names = ["ID", "First Name", "Last Name", "Speciality", "Available Start Time", "Available End Time"]
            for trainer in trainers:
                table.add_row(trainer)
            print("Trainers:")
            print(table)
        else:
            print("No trainers found.")

    # Method to update a trainer's available time slots
    def updateTrainerAvailability(self):
        trainerId = int(input("Enter trainer ID: "))
        availableStartTime = datetime.strptime(input("Enter new available start time (Use 24-hour time): "), "%H:%M").time()
        availableEndTime = datetime.strptime(input("Enter new available end time (Use 24-hour time): "), "%H:%M").time()
        self.dataAccessLayer.updateTrainerAvailability(trainerId, availableStartTime, availableEndTime)

    # Method to view all bookings
    def viewBookings(self):
        bookings = self.dataAccessLayer.viewBookings()
        if bookings:
            table = PrettyTable()
            table.field_names = ["ID", "Member ID", "Trainer ID", "Booking Date", "Start Time", "End Time", "Status"]
            for booking in bookings:
                table.add_row(booking)
            print("Bookings:")
            print(table)
        else:
            print("No bookings found.")

    # Method to view all rooms
    def viewRooms(self):
        rooms = self.dataAccessLayer.viewRooms()
        if rooms:
            table = PrettyTable()
            table.field_names = ["ID", "Room Name", "Capacity"]
            for room in rooms:
                table.add_row(room)
            print("Rooms:")
            print(table)
        else:
            print("No rooms found.")

    # Method to view the class schedule
    def viewClassSchedule(self):
        classSchedule = self.dataAccessLayer.viewClassSchedule()
        if classSchedule:
            table = PrettyTable()
            table.field_names = ["ID", "Class", "Start Time", "End Time", "Date", "Room ID", "Status"]
            for row in classSchedule:
                table.add_row(row)
            print("Class Schedule:")
            print(table)
        else:
            print("No class schedule found.")

    # Method to view all equipment
    def viewEquipment(self):
        equipment = self.dataAccessLayer.viewEquipment()
        if equipment:
            table = PrettyTable()
            table.field_names = ["ID", "Name", "Quantity", "Condition"]
            for item in equipment:
                table.add_row(item)
            print("Equipment:")
            print(table)
        else:
            print("No equipment found.")

    # Method to view all equipment maintenance records
    def viewMaintenance(self):
        maintenanceRecords = self.dataAccessLayer.viewMaintenance()
        if maintenanceRecords:
            table = PrettyTable()
            table.field_names = ["ID", "Date", "Description", "Equipment ID"]
            for record in maintenanceRecords:
                table.add_row(record)
            print("Equipment Maintenance:")
            print(table)
        else:
            print("No maintenance records found.")

    # Method to update a member's dashboard
    def updateMemberDashboard(self):
        memberId = int(input("Enter member ID: "))
        exerciseRoutine = input("Enter exercise routine: ")
        fitnessAchievements = input("Enter fitness achievements: ")
        healthStatistics = input("Enter health statistics: ")
        self.dataAccessLayer.updateMemberDashboard(memberId, exerciseRoutine, fitnessAchievements, healthStatistics)

    # Method to create a new billing record
    def createBilling(self):
        memberId = int(input("Enter member ID: "))
        serviceType = input("Enter service type: ")
        amount = float(input("Enter amount (no need for $ before amount): "))
        billingDate = datetime.now().date()
        paymentStatus = input("Enter payment status with Paypal (enter 'Unpaid' or 'Paid'): ")
        self.dataAccessLayer.createBilling(memberId, serviceType, amount, billingDate, paymentStatus)

    # Method to update a class schedule
    def updateClassSchedule(self):
        classId = int(input("Enter class ID: "))
        className = input("Enter new class name: ")
        classStartTime = datetime.strptime(input("Enter new class start time (Use 24-hour time): "), "%H:%M").time()
        classEndTime = datetime.strptime(input("Enter new class end time (Use 24-hour time): "), "%H:%M").time()
        classDate = datetime.strptime(input("Enter new class date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        roomId = int(input("Enter new room ID: "))
        classStatus = input("Enter new class status (Scheduled/Cancelled): ")
        self.dataAccessLayer.updateClassSchedule(classId, className, classStartTime, classEndTime, classDate, roomId, classStatus)

    # Method to add a new equipment maintenance record
    def addEquipmentMaintenance(self):
        maintenanceDate = datetime.strptime(input("Enter maintenance date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        MaintenanceDescr = input("Enter maintenance description: ")
        equipmentId = int(input("Enter equipment ID: "))
        self.dataAccessLayer.addEquipmentMaintenance(maintenanceDate, MaintenanceDescr, equipmentId)

    # Method to view a member's profile by first and last name
    def viewMember(self):
        firstName = input("Please enter the member's FIRST name (case sensitive): ")
        lastName = input("Please enter the member's LAST name (case sensitive): ")
        member = self.dataAccessLayer.getMemberByName(firstName, lastName)
        if member:
            table = PrettyTable()
            table.field_names = ["ID", "First Name", "Last Name", "Email", "Phone", "Fitness Goal", "Health Metric"]
            table.add_row(member)
            print("Member Profile:")
            print(table)
        else:
            print("No member found with the given first and last name.")

def main():
    # Command-line arguments for different functionality
    parser = argparse.ArgumentParser(description="Health and Fitness Club Management System")
    parser.add_argument("--register-member", action="store_true", help="Register a new member")
    parser.add_argument("--update-member", action="store_true", help="Update a member's profile")
    parser.add_argument("--book-session", action="store_true", help="Book a session with a trainer")
    parser.add_argument("--view-members", action="store_true", help="View registered members")
    parser.add_argument("--view-trainers", action="store_true", help="View trainers")
    parser.add_argument("--view-bookings", action="store_true", help="View bookings")
    parser.add_argument("--view-rooms", action="store_true", help="View rooms")
    parser.add_argument("--view-class-schedule", action="store_true", help="View the class schedule")
    parser.add_argument("--view-equipment", action="store_true", help="View equipment")
    parser.add_argument("--view-maintenance", action="store_true", help="View equipment maintenance records")
    parser.add_argument("--update-member-dashboard", action="store_true", help="Update a member's dashboard")
    parser.add_argument("--create-billing", action="store_true", help="Create a billing record")
    parser.add_argument("--update-class-schedule", action="store_true", help="Update a class schedule")
    parser.add_argument("--add-equipment-maintenance", action="store_true", help="Add an equipment maintenance record")
    parser.add_argument("--view-member", action="store_true", help="View a member's profile")
    parser.add_argument("--update-trainer-availability", action="store_true", help="Update a trainer's available schedule")
    args = parser.parse_args()

    # Create an instance of the AppLogic class
    appLogic = AppLogic()

    # Execute the appropriate method based on the command-line arguments
    if args.register_member:
        appLogic.registerMember()
    elif args.update_member:
        appLogic.updateMemberProfile()
    elif args.book_session:
        appLogic.bookSession()
    elif args.view_members:
        appLogic.viewMembers()
    elif args.view_trainers:
        appLogic.viewTrainers()
    elif args.view_bookings:
        appLogic.viewBookings()
    elif args.view_rooms:
        appLogic.viewRooms()
    elif args.view_class_schedule:
        appLogic.viewClassSchedule()
    elif args.view_equipment:
        appLogic.viewEquipment()
    elif args.view_maintenance:
        appLogic.viewMaintenance()
    elif args.update_member_dashboard:
        appLogic.updateMemberDashboard()
    elif args.create_billing:
        appLogic.createBilling()
    elif args.update_class_schedule:
        appLogic.updateClassSchedule()
    elif args.add_equipment_maintenance:
        appLogic.addEquipmentMaintenance()
    elif args.view_member:
        appLogic.viewMember()
    elif args.update_trainer_availability:
        appLogic.updateTrainerAvailability()
    else:
        parser.print_help()

# Entry point of the application
if __name__ == "__main__":
    main()
