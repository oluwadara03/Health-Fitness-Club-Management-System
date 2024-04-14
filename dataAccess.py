import psycopg2
import logging

# Database connection details
dbHost = 'localhost'
dbName = 'Health and Fitness Club'
dbUser = 'postgres'
dbPassword = 'postgres'

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to establish a connection to the PostgreSQL database
def connectToDb():
    try:
        conn = psycopg2.connect(
            host=dbHost,
            database=dbName,
            user=dbUser,
            password=dbPassword
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        logging.error("Error connecting to the database: %s", error)
        return None

# Class to handle database interactions for the application
class DataInteractions:

    def __init__(self):
        # Establish a connection to the database
        self.conn = connectToDb()

    # Method to register a new member
    def registerMember(self, firstName, lastName, email, phoneNumber, fitnessGoal, healthMetric):
        try:
            with self.conn.cursor() as cur:
                # Format the phone number
                formatted_phone = self.formatPhoneNumber(phoneNumber)
                query = "INSERT INTO Member (FirstName, LastName, Email, PhoneNumber, FitnessGoal, HealthMetric) VALUES (%s, %s, %s, %s, %s, %s)"
                cur.execute(query, (firstName, lastName, email, formatted_phone, fitnessGoal, healthMetric))
                self.conn.commit()
                logging.info("Member registered successfully.")
        except (Exception, psycopg2.Error) as error:
            logging.error("Error registering member: %s", error)
            self.conn.rollback()

    # Method to update a member's profile
    def updateMemberProfile(self, memberId, firstName, lastName, email, phoneNumber, fitnessGoal, healthMetric):
        try:
            with self.conn.cursor() as cur:
                # Format the phone number
                formatted_phone = self.formatPhoneNumber(phoneNumber)
                query = "UPDATE Member SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s, FitnessGoal = %s, HealthMetric = %s WHERE MemberID = %s"
                cur.execute(query, (firstName, lastName, email, formatted_phone, fitnessGoal, healthMetric, memberId))
                self.conn.commit()
                logging.info("Member profile updated successfully.")
        except (Exception, psycopg2.Error) as error:
            logging.error("Error updating member profile: %s", error)
            self.conn.rollback()

    # Method to format the phone number provided
    def formatPhoneNumber(self, phoneNumber):
        # Remove any non-digit characters from the phone number
        cleaned_phone = ''.join(char for char in phoneNumber if char.isdigit())
        # Format the phone number
        formatted_phone = f"{cleaned_phone[:3]}-{cleaned_phone[3:6]}-{cleaned_phone[6:]}"
        return formatted_phone

    # Method to book a session for a member
    def bookSession(self, memberId, trainerId, bookingDate, bookingStartTime, bookingEndTime):
        try:
            with self.conn.cursor() as cur:
                query = "INSERT INTO Booking (BookingDate, BookingStartTime, BookingEndTime, MemberID, TrainerID, BookingStatus) VALUES (%s, %s, %s, %s, %s, 'Scheduled')"
                cur.execute(query, (bookingDate, bookingStartTime.strftime('%H:%M'), bookingEndTime.strftime('%H:%M'), memberId, trainerId))
                self.conn.commit()
                logging.info("Booking created successfully.")
        except (Exception, psycopg2.Error) as error:
            logging.error("Error creating booking: %s", error)
            self.conn.rollback()

    # Method to view all registered members
    def viewMembers(self):
        try:
            with self.conn.cursor() as cur:
                # Prepare and execute the SQL query to retrieve all members
                query = "SELECT MemberID, FirstName, LastName, Email, PhoneNumber, FitnessGoal, HealthMetric FROM Member"
                cur.execute(query)
                members = cur.fetchall()
                return members
        except (Exception, psycopg2.Error) as error:
            logging.error("Error retrieving members: %s", error)
            return None

    # Method to view all trainers
    def viewTrainers(self):
        try:
            with self.conn.cursor() as cur:
                query = "SELECT TrainerID, FirstName, LastName, Speciality, TO_CHAR(AvailableStartTime, 'HH24:MI') AS AvailableStartTime, TO_CHAR(AvailableEndTime, 'HH24:MI') AS AvailableEndTime FROM Trainer"
                cur.execute(query)
                trainers = cur.fetchall()
                return trainers
        except (Exception, psycopg2.Error) as error:
            logging.error("Error retrieving trainers: %s", error)
            return None

    # Method to update a trainer's available time slots
    def updateTrainerAvailability(self, trainerId, availableStartTime, availableEndTime):
        try:
            with self.conn.cursor() as cur:
                query = "UPDATE Trainer SET AvailableStartTime = %s, AvailableEndTime = %s WHERE TrainerID = %s"
                cur.execute(query, (availableStartTime, availableEndTime, trainerId))
                self.conn.commit()
                logging.info("Trainer availability updated successfully.")
        except (Exception, psycopg2.Error) as error:
            logging.error("Error updating trainer availability: %s", error)
            self.conn.rollback()

    # Method to view all bookings
    def viewBookings(self):
        try:
            with self.conn.cursor() as cur:
                query = "SELECT BookingID, MemberID, TrainerID, BookingDate, TO_CHAR(BookingStartTime, 'HH24:MI') AS BookingStartTime, TO_CHAR(BookingEndTime, 'HH24:MI') AS BookingEndTime, BookingStatus FROM Booking"
                cur.execute(query)
                bookings = cur.fetchall()
                return bookings
        except (Exception, psycopg2.Error) as error:
            logging.error("Error retrieving bookings: %s", error)
            return None

    # Method to view all rooms
    def viewRooms(self):
        try:
            with self.conn.cursor() as cur:
                # Prepare and execute the SQL query to retrieve all rooms
                query = "SELECT RoomID, RoomName, Capacity FROM Room"
                cur.execute(query)
                rooms = cur.fetchall()
                return rooms
        except (Exception, psycopg2.Error) as error:
            logging.error("Error retrieving rooms: %s", error)
            return None

    # Method to view the class schedule
    def viewClassSchedule(self):
        try:
            with self.conn.cursor() as cur:
                # Prepare and execute the SQL query to retrieve the class schedule
                query = "SELECT ClassID, ClassName, TO_CHAR(ClassStartTime, 'HH24:MI') AS ClassStartTime, TO_CHAR(ClassEndTime, 'HH24:MI') AS ClassEndTime, ClassDate, RoomID, ClassStatus FROM ClassSchedule"
                cur.execute(query)
                classSchedule = cur.fetchall()
                return classSchedule
        except (Exception, psycopg2.Error) as error:
            logging.error("Error retrieving class schedule: %s", error)
            return None

    # Method to view all equipment
    def viewEquipment(self):
        try:
            with self.conn.cursor() as cur:
                # Prepare and execute the SQL query to retrieve all equipment
                query = "SELECT EquipmentID, EquipmentName, Quantity, Condition FROM Equipment"
                cur.execute(query)
                equipment = cur.fetchall()
                return equipment
        except (Exception, psycopg2.Error) as error:
            logging.error("Error retrieving equipment: %s", error)
            return None

    # Method to view all equipment maintenance records
    def viewMaintenance(self):
        try:
            with self.conn.cursor() as cur:
                # Prepare and execute the SQL query to retrieve all equipment maintenance records
                query = "SELECT MaintenanceID, MaintenanceDate, MaintenanceDescr, EquipmentID FROM Maintenance"
                cur.execute(query)
                maintenanceRecords = cur.fetchall()
                return maintenanceRecords
        except (Exception, psycopg2.Error) as error:
            logging.error("Error retrieving equipment maintenance records: %s", error)
            return None

    # Method to update a member's dashboard
    def updateMemberDashboard(self, memberId, exerciseRoutine, fitnessAchievements, healthStatistics):
        try:
            with self.conn.cursor() as cur:
                # Prepare and execute the SQL query to update a member's dashboard
                query = "INSERT INTO MemberDashboard (MemberID, ExerciseRoutine, FitnessAchievements, HealthStatistics) VALUES (%s, %s, %s, %s)"
                cur.execute(query, (memberId, exerciseRoutine, fitnessAchievements, healthStatistics))
                self.conn.commit()
                logging.info("Member dashboard updated successfully.")
        except (Exception, psycopg2.Error) as error:
            logging.error("Error updating member dashboard: %s", error)
            self.conn.rollback()

    # Method to create a new billing record
    def createBilling(self, memberId, serviceType, amount, billingDate, paymentStatus):
        try:
            with self.conn.cursor() as cur:
                # Prepare and execute the SQL query to create a new billing record
                query = "INSERT INTO Billing (MemberID, ServiceType, Amount, BillingDate, PaymentStatus) VALUES (%s, %s, %s, %s, %s)"
                cur.execute(query, (memberId, serviceType, amount, billingDate, paymentStatus))
                self.conn.commit()
                logging.info("Billing record created successfully.")
        except (Exception, psycopg2.Error) as error:
            logging.error("Error creating billing record: %s", error)
            self.conn.rollback()

    # Method to update a class schedule
    def updateClassSchedule(self, classId, className, classStartTime, classEndTime, classDate, roomId, classStatus):
        try:
            with self.conn.cursor() as cur:
                # Prepare and execute the SQL query to update a class schedule
                query = "UPDATE ClassSchedule SET ClassName = %s, ClassStartTime = %s, ClassEndTime = %s, ClassDate = %s, RoomID = %s, ClassStatus = %s WHERE ClassID = %s"
                cur.execute(query, (className, classStartTime.strftime('%H:%M'), classEndTime.strftime('%H:%M'), classDate, roomId, classStatus, classId))
                self.conn.commit()
                logging.info("Class schedule updated successfully.")
        except (Exception, psycopg2.Error) as error:
            logging.error("Error updating class schedule: %s", error)
            self.conn.rollback()

    # Method to add a new equipment maintenance record
    def addEquipmentMaintenance(self, maintenanceDate, MaintenanceDescr, equipmentId):
        try:
            with self.conn.cursor() as cur:
                # Prepare and execute the SQL query to add a new equipment maintenance record
                query = "INSERT INTO Maintenance (MaintenanceDate, MaintenanceDescr, EquipmentID) VALUES (%s, %s, %s)"
                cur.execute(query, (maintenanceDate, MaintenanceDescr, equipmentId))
                self.conn.commit()
                logging.info("Equipment maintenance record added successfully.")
        except (Exception, psycopg2.Error) as error:
            logging.error("Error adding equipment maintenance record: %s", error)
            self.conn.rollback()

    # Method to retrieve a member's profile by first and last name
    def getMemberByName(self, firstName, lastName):
        try:
            with self.conn.cursor() as cur:
                query = "SELECT MemberID, FirstName, LastName, Email, PhoneNumber, FitnessGoal, HealthMetric FROM Member WHERE FirstName = %s AND LastName = %s"
                cur.execute(query, (firstName, lastName))
                member = cur.fetchone()
                return member
        except (Exception, psycopg2.Error) as error:
            logging.error("Error retrieving member: %s", error)
            return None