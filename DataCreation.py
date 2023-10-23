import sqlite3

db = sqlite3.connect("Main.db")
cur = db.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS profiles (
    phone INT PRIMARY KEY NOT NULL,
    name CHAR(20) NOT NULL,
    age INT NOT NULL,
    gender CHAR(1) NOT NULL,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    interests TEXT NOT NULL                           
);""")

cur.execute("""
    INSERT INTO profiles (
        phone,
        name,
        age,
        gender,
        latitude,
        longitude,
        interests
    ) VALUES
    (1234567890, 'Sushila S.', 55, 'W', 12.9716, 77.5946, 'Exercise'),
    (0987654321, 'Richard M.', 46, 'M', 12.9352, 77.6245, 'Reading'),
    (5678901234, 'Arindam G.', 62, 'M', 12.9791, 77.5913, 'Exercise'),
    (4321098765, 'Diya R.', 32, 'W', 13.0329, 77.6183, 'Visual Arts'),
    (9012345678, 'Padma R.', 35, 'W', 12.9279, 77.6271, 'Cooking'),
    (5928476932, 'Yamini K.', 42, 'W', 13.018030, 77.529583, 'Exercise')        
""")

cur.execute("""CREATE TABLE IF NOT EXISTS activities (
    name TEXT NOT NULL,
    capacity INT NOT NULL,
    category TEXT NOT NULL,
    address TEXT NOT NULL,
    description CHAR(200) NOT NULL,
    orgname CHAR(50) NOT NULL,
    phone BLOB NOT NULL,
    dateandtime BLOB NOT NULL,
    agepref BLOB NOT NULL,
    genderpref CHAR(1) NOT NULL                                     
);""")


cur.execute("""
    INSERT INTO activities (
        name,
        capacity,
        category,
        address,
        description,
        orgname,
        phone,
        dateandtime,
        agepref,
        genderpref
    ) VALUES
    ('Yoga Group', 20, 'Exercise', '2155 Jha Islands', 'Morning yoga group for seniors', 'Sushila S.', '1234567890', '2022-12-01 08:00:00', '60+', 'M'),
    ('Bollywood karaoke', 15, 'Singing', '915 Nayar Station', 'Weekly karaoke, Every thursday', 'Richard M.', '0987654321', '2022-12-15 14:00:00', 'All', 'A'),
    ('Walking Group', 10, 'Exercise', '536 Achintya Cove', 'Daily walking group', 'Arindam G.', '5678901234', '2022-12-07 09:00:00', '50+', 'W'),
    ('Art Community', 25, 'Visual Arts', '237 Dutta Run', 'Weekly art community', 'Diya R.', '4321098765', '2022-12-08 13:00:00', 'All', 'A'),
    ('Cooking Group', 30, 'Cooking', '19928 Ekaaksh Summit', 'Monthly cooking group', 'Padma R.', '9012345678', '2022-12-20 11:00:00', 'All', 'A'),
    ('Yoga Group', 20, 'Exercise', '343F Brigade Gateway', "Join my Yoga Class", "Yamini K.", "5928476932", "2022-12-07 09:00:00", "25+", 'W')        
""")


db.commit()
db.close()

print('it is done')