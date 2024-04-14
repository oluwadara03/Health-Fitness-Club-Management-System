-- The sample data for the Member table
INSERT INTO Member (MemberID, FirstName, LastName, Email, PhoneNumber, FitnessGoal, HealthMetric)
VALUES
    (1, 'John', 'Doe', 'john.doe@example.com', '613-113-4827', 'Lose 20 lbs', 'BMI: 28, Body Fat: 25%'),
    (2, 'Jane', 'Smith', 'jane.smith@example.com', '613-087-6903', 'Improve Cardiovascular Fitness', 'Blood Pressure: 120/80, Resting Heart Rate: 72 bpm'),
    (3, 'Michael', 'Johnson', 'michael.johnson@example.com', '613-456-3890', 'Gain 10 lbs of Muscle', 'Body Weight: 160 lbs, Body Fat: 18%'),
    (4, 'Emily', 'Wilson', 'emily.wilson@example.com', '613-509-0123', 'Maintain Current Fitness Level', 'BMI: 22, Body Fat: 22%'),
    (5, 'David', 'Lee', 'david.lee@example.com', '613-821-9744', 'Improve Flexibility', 'Sit and Reach: 12 inches');

-- The sample data for the Trainer table
INSERT INTO Trainer (TrainerID, FirstName, LastName, Speciality, AvailableStartTime, AvailableEndTime)
VALUES
    (1, 'Emily', 'Harrison', 'Strength Training', '9:00 AM', '12:00 PM'),
    (2, 'Cameron', 'Walker', 'Agility Training', '10:00 AM', '2:00 PM'),
    (3, 'Sarah', 'Brown', 'Cardio', '8:00 AM', '11:00 AM'),
    (4, 'Michael', 'Thompson', 'Pilates', '11:00 AM', '3:00 PM'),
    (5, 'Jessica', 'Martinez', 'Nutrition', '9:30 AM', '1:30 PM');

-- The sample data for the Room table
INSERT INTO Room (RoomID, RoomName, Capacity)
VALUES
    (1, 'Indoor Track', 20),
    (2, 'Spin Class', 15),
    (3, 'Weight Room', 30),
    (4, 'Pilates Studio', 18),
    (5, 'Dance Studio', 25);

-- The sample data for the Equipment table
INSERT INTO Equipment (EquipmentID, EquipmentName, Quantity, Condition)
VALUES
    (1, 'Treadmill', 5, 'Good'),
    (2, 'Stationary Bike', 8, 'Fair'),
    (3, 'Dumbbell Set', 20, 'Good'),
    (4, 'Hurdles', 15, 'Good'),
    (5, 'Pilates Reformer', 4, 'Good');

-- The sample data for the Booking table
INSERT INTO Booking (BookingID, BookingDate, BookingStartTime, BookingEndTime, MemberID, TrainerID, BookingStatus)
VALUES
    (1, '2024-05-15', '10:00 AM', '11:00 AM', 1, 1, 'Scheduled'),
    (2, '2024-05-16', '11:30 AM', '12:30 PM', 2, 2, 'Scheduled'),
    (3, '2024-05-17', '2:00 PM', '3:00 PM', 3, 3, 'Scheduled'),
    (4, '2024-05-18', '3:30 PM', '4:30 PM', 4, 4, 'Scheduled'),
    (5, '2024-05-19', '1:00 PM', '2:00 PM', 5, 5, 'Scheduled');

-- The sample data for the ClassSchedule table
INSERT INTO ClassSchedule (ClassID, ClassName, ClassStartTime, ClassEndTime, ClassDate, RoomID, ClassStatus)
VALUES
    (1, 'Strength Training', '6:00 PM', '7:00 PM', '2024-05-18', 1, 'Scheduled'),
    (2, 'Spin Class', '9:00 AM', '10:00 AM', '2024-05-19', 2, 'Scheduled'),
    (3, 'Pilates Reformer', '11:00 AM', '12:00 PM', '2024-05-20', 3, 'Scheduled'),
    (4, 'Zumba', '7:00 PM', '8:00 PM', '2024-05-21', 4, 'Scheduled'),
    (5, 'Cardio Kickboxing', '8:30 AM', '9:30 AM', '2024-05-22', 5, 'Scheduled');

-- The sample data for the Maintenance table
INSERT INTO Maintenance (MaintenanceID, MaintenanceDate, MaintenanceDescr, EquipmentID)
VALUES
    (1, '2024-05-01', 'Replaced the belt on the treadmill', 1),
    (2, '2024-04-10', 'Cleaned and oiled the stationary bike', 2),
    (3, '2024-05-08', 'Tightened the screws on the dumbbell sets', 3),
    (4, '2024-04-22', 'Inspected and cleaned the hurdles', 4),
    (5, '2024-04-12', 'Checked the tension on the resistance bands', 5);

-- The sample data for the MemberDashboard table
INSERT INTO MemberDashboard (MemberID, ExerciseRoutine, FitnessAchievements, HealthStatistics)
VALUES
    (1, 'Cardio: 30 mins, 3 times a week\nStrength Training: 2 times a week', 'Lost 10 lbs in 2 months', 'BMI: 27.5, Body Fat: 23%'),
    (2, 'Yoga: 1 hour, 2 times a week\nCardio: 45 mins, 4 times a week', 'Improved resting heart rate from 78 to 72 bpm', 'Blood Pressure: 118/75, Resting Heart Rate: 72 bpm'),
    (3, 'Weight Lifting: 1 hour, 3 times a week\nCardio: 20 mins, 5 times a week', 'Gained 8 lbs of muscle', 'Body Weight: 168 lbs, Body Fat: 16%'),
    (4, 'Pilates: 1 hour, 2 times a week\nCardio: 30 mins, 3 times a week', 'Maintained current fitness level', 'BMI: 21.5, Body Fat: 20%'),
    (5, 'Stretching: 30 mins, daily\nFlexibility Training: 1 hour, 2 times a week', 'Improved sit and reach by 2 inches', 'Sit and Reach: 14 inches');

-- The sample data for the Billing table
INSERT INTO Billing (BillingID, MemberID, ServiceType, Amount, BillingDate, PaymentStatus)
VALUES
    (1, 1, 'Membership', 99.99, '2024-01-01', 'Paid'),
    (2, 1, 'Personal Training', 50.00, '2024-03-15', 'Paid'),
    (3, 2, 'Membership', 99.99, '2024-02-01', 'Paid'),
    (4, 2, 'Group Class', 20.00, '2024-04-01', 'Unpaid'),
    (5, 3, 'Membership', 99.99, '2024-03-01', 'Paid');