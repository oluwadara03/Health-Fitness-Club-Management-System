-- Member's Table - used for administrative purposes
CREATE TABLE IF NOT EXISTS Member (
    -- Unique identifier for each member
    MemberID SERIAL PRIMARY KEY,
    -- Member's first and last name (must be unique)
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    UNIQUE (FirstName, LastName),
    -- Unique email address - no two emails can be the same
    Email VARCHAR(100) NOT NULL UNIQUE,
    -- Unique phone number in the format "123-456-7890" (numbers with dashes)
    PhoneNumber VARCHAR(20) NOT NULL UNIQUE,
    -- Health/fitness related
    FitnessGoal VARCHAR(200),
    HealthMetric VARCHAR(200),
    -- Constraint to ensure phone number is in the correct format
    CHECK (PhoneNumber SIMILAR TO '[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')
);

-- Trainer Table - used for information about the trainer
CREATE TABLE IF NOT EXISTS Trainer (
    -- Unique identifier for each trainer
    TrainerID SERIAL PRIMARY KEY,
    -- Trainer's first and last name (must be unique)
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    UNIQUE (FirstName, LastName),
    -- Area of speciality
    Speciality VARCHAR(100) NOT NULL,
    -- Available start time
    AvailableStartTime TIME NOT NULL,
    -- Available end time
    AvailableEndTime TIME NOT NULL,
    -- Constraint to ensure available start time is before available end time
    CHECK (AvailableStartTime < AvailableEndTime)
);

-- Room Table - used for information about available rooms in the health and fitness club
CREATE TABLE IF NOT EXISTS Room (
    -- Unique identifier for each room
    RoomID SERIAL PRIMARY KEY,
    -- The name of the room must be unique
    RoomName VARCHAR(50) NOT NULL UNIQUE,
    -- The maximum capacity of the room must be greater than 0
    Capacity INT NOT NULL CHECK (Capacity > 0)
);

-- Equipment Table - used for information about the available fitness equipment
CREATE TABLE IF NOT EXISTS Equipment (
    -- Unique identifier for each piece of equipment
    EquipmentID SERIAL PRIMARY KEY,
    -- The name of the equipment must be unique
    EquipmentName VARCHAR(100) NOT NULL UNIQUE,
    -- The number of units of the equipment must be greater than 0
    Quantity INT NOT NULL CHECK (Quantity > 0),
    -- Current condition of the equipment
    -- There are only three choices here - it must be one of the valid values below
    Condition VARCHAR(50) NOT NULL CHECK (Condition IN ('Good', 'Fair', 'Poor'))
);

-- Booking Table - used for bookings made by members with trainers
CREATE TABLE IF NOT EXISTS Booking (
    -- Unique identifier for each booking
    BookingID SERIAL PRIMARY KEY,
    -- Date of the booking
    BookingDate DATE NOT NULL,
    -- Booking start time
    BookingStartTime TIME NOT NULL,
    -- Booking end time
    BookingEndTime TIME NOT NULL,
    -- Constraint to ensure booking start time is before booking end time
    CHECK (BookingStartTime < BookingEndTime),
    -- Foreign Key (referencing Member table)
    MemberID INT NOT NULL,
    -- Foreign Key (referencing Trainer table)
    TrainerID INT NOT NULL,
    -- Foreign Key relationship with the Member table
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID),
    -- Foreign Key relationship with the Trainer table
    FOREIGN KEY (TrainerID) REFERENCES Trainer(TrainerID),
    -- Constraint to ensure the booking date is not in the past
    CHECK (BookingDate >= CURRENT_DATE),
    -- Booking status (Scheduled, Rescheduled, Cancelled)
    BookingStatus VARCHAR(20) NOT NULL DEFAULT 'Scheduled'
    CHECK (BookingStatus IN ('Scheduled', 'Rescheduled', 'Cancelled'))
);

-- ClassSchedule Table - used for information about the scheduled classes
CREATE TABLE IF NOT EXISTS ClassSchedule (
    -- Unique identifier for each class
    ClassID SERIAL PRIMARY KEY,
    -- Name of the class
    ClassName VARCHAR(100) NOT NULL,
    -- Starting class time
    ClassStartTime TIME NOT NULL,
    -- Ending class time
    ClassEndTime TIME NOT NULL,
    -- Constraint to ensure class start time is before class end time
    CHECK (ClassStartTime < ClassEndTime),
    -- Date of the class
    ClassDate DATE NOT NULL,
    -- Foreign Key (referencing Room table)
    RoomID INT NOT NULL,
    -- Foreign Key relationship with the Room table
    FOREIGN KEY (RoomID) REFERENCES Room(RoomID),
    -- Constraint to ensure the class date is not in the past
    CHECK (ClassDate >= CURRENT_DATE),
    -- Class status (Scheduled, Cancelled)
    ClassStatus VARCHAR(20) NOT NULL DEFAULT 'Scheduled'
	-- Constraint to ensure the answer is either one of these two
    CHECK (ClassStatus IN ('Scheduled', 'Cancelled'))
);

-- Maintenance Table - used for storing maintenance records for the fitness equipment
CREATE TABLE IF NOT EXISTS Maintenance (
    -- Unique identifier for each maintenance record
    MaintenanceID SERIAL PRIMARY KEY,
    -- Maintenance date
    MaintenanceDate DATE NOT NULL,
    -- Description of the maintenance performed
    MaintenanceDescr TEXT NOT NULL,
    -- Foreign Key (referencing Equipment table)
    EquipmentID INT NOT NULL,
    -- Establish a foreign key relationship with the Equipment table
    FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID)
);

-- Member Dashboard Table - used for storing member's exercise routines, fitness achievements, and health statistics
CREATE TABLE IF NOT EXISTS MemberDashboard (
    -- Foreign Key (referencing Member table)
    MemberID INT NOT NULL,
    -- Member's exercise routine
    ExerciseRoutine TEXT,
    -- Member's fitness achievements
    FitnessAchievements TEXT,
    -- Member's health statistics
    HealthStatistics TEXT,
    -- Foreign Key relationship with the Member table
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID)
);

-- Billing Table - used for storing billing information for members
CREATE TABLE IF NOT EXISTS Billing (
    -- Unique identifier for each billing record
    BillingID SERIAL PRIMARY KEY,
    -- Foreign Key (referencing Member table)
    MemberID INT NOT NULL,
    -- Type of service provided (e.g., membership, personal training, class)
    ServiceType VARCHAR(100) NOT NULL,
    -- Amount charged for the service - the amount must be more than $0.00
    Amount DECIMAL(10,2) NOT NULL CHECK (Amount > 0),
    -- Date the bill was generated
    BillingDate DATE NOT NULL,
    -- Payment status (Unpaid or Paid)
    PaymentStatus VARCHAR(20) NOT NULL DEFAULT 'Unpaid'
	-- Constraint to ensure that the answer is either one of these two
    CHECK (PaymentStatus IN ('Unpaid', 'Paid')),
    -- Foreign Key relationship with the Member table
    FOREIGN KEY (MemberID) REFERENCES Member(MemberID)
);