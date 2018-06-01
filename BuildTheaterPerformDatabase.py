import sqlite3
from sqlite3 import Error

def build_database():
    '''connect to the database'''

    try:
        conn = sqlite3.connect('theater_perform.db')
        cur = conn.cursor()  

        '''create tables'''

        cur.execute("CREATE TABLE Genre( G_ID int NOT NULL UNIQUE, G_Name varchar(20) NOT NULL, PRIMARY KEY(G_ID) );")
        cur.execute("CREATE TABLE Customer( C_ID int NOT NULL UNIQUE, C_Name varchar(20) NOT NULL, PRIMARY KEY(C_ID) ); ")
        cur.execute("CREATE TABLE Performer( Per_ID int NOT NULL UNIQUE, Per_Name varchar(20) NOT NULL, PRIMARY KEY(Per_ID) ); ")
        cur.execute("CREATE TABLE Producer( Pro_ID int NOT NULL UNIQUE, Pro_Name varchar(30), Pro_Description varchar(30), PRIMARY KEY (Pro_ID) ); ")
        cur.execute("CREATE TABLE Venue( V_ID int NOT NULL UNIQUE, V_Name varchar(30), V_Description varchar(30), PRIMARY KEY(V_ID) ); ")
        cur.executescript("CREATE TABLE Event_Schedule( S_ID int NOT NULL UNIQUE, S_Time datetime NOT NULL, PRIMARY KEY(S_ID) ); ")
        cur.executescript("CREATE TABLE Tickets( T_ID VARCHAR(10) NOT NULL UNIQUE, C_ID int, S_ID int);  ")
        cur.executescript("DROP TABLE IF EXISTS Events; CREATE TABLE Events ( E_ID int NOT NULL UNIQUE,  E_Name      varchar(100), Pro_ID int, G_ID int, S_ID int, V_ID int,         primary key (E_ID),         foreign key (Pro_ID) references Producer(Pro_ID),         foreign key (G_ID) references Genre(G_ID),         foreign key (S_ID) references Event_Schedule(S_ID),         foreign key (V_ID) references Venue(V_ID) );  ")
        cur.executescript("DROP TABLE IF EXISTS Schedule_Performer; CREATE TABLE Schedule_Performer( Per_ID int,  S_ID int,  primary key (Per_ID, S_ID),  foreign key (Per_ID) references Performer(Per_ID),  foreign key (S_ID) references Event_Schedule(S_ID) ); ")

        print "tsble creation completed"

        '''data injection'''

        cur.execute("INSERT INTO Genre VALUES (1003,'Music');")
        cur.execute("INSERT INTO Genre VALUES (1004,'Music-Jazz');")
        cur.execute("INSERT INTO Genre VALUES (1005,'Music-University Bands');")
        cur.execute("INSERT INTO Genre VALUES (1006,'Theatre-Social Issues');")
        cur.execute("INSERT INTO Genre VALUES (1007,'Tours');")
        cur.execute("INSERT INTO Customer VALUES ('Robin van Persie', 78976);")
        cur.execute("INSERT INTO Customer VALUES ('Christian Eriksen', 78987);")
        cur.execute("INSERT INTO Customer VALUES ('Philipp Lahm', 78977);")
        cur.execute("INSERT INTO Customer VALUES ('Thiago Silva', 78981);")
        cur.execute("INSERT INTO Performer VALUES ('Jeanine Genkazi', 500);")
        cur.execute("INSERT INTO Performer VALUES ('George Smith', 400);")
        cur.execute("INSERT INTO Performer VALUES ('Chuck Smith', 300);")
        cur.execute("INSERT INTO Performer VALUES ('Nina Simone', 900);")
        cur.execute("INSERT INTO Producer VALUES ('Marquee', 3458, 'Marquee is a production team who dedicates in creating innovative school performance such as plays and musicals.');")
        cur.execute("INSERT INTO Producer VALUES ('School of Music', 3459, 'The School of Music embraces cutting-edge innovation and discovery while providing an array of musical and engagement opportunities within the artistic and educational communities of Urbana and Champaign.');")
        cur.execute("INSERT INTO Venue VALUES ('Colwell Playhouse', 0001, 'This venue features seating for up to 641 patrons in the continental style.');")
        cur.execute("INSERT INTO Venue VALUES ('Foellinger Great Hall', 0002, 'This venue is primarily used for vocal and instrumental music concerts dance and theatre events.');")
        cur.execute("INSERT INTO Venue VALUES ('Lobby/Stage 5/Stage 6', 0003, 'Stage 5 is at once a bandstand a grandstand and a club stage.');")
        cur.execute("INSERT INTO Venue VALUES ('Studio Theatre', 0004, 'This venue offers completely flexible black box theatre allows for several seating configurations and up to 200 people can enjoy performances in this 2700-square-foot space.');")
        cur.execute("INSERT INTO Event_Schedule VALUES (3783, '2018-04-17 19:30:00');")
        cur.execute("INSERT INTO Event_Schedule VALUES (3790, '2018-4-17 18:00:00');")
        cur.execute("INSERT INTO Event_Schedule VALUES (3795, '2018-4-20 19:30:00');")
        cur.execute("INSERT INTO Event_Schedule VALUES (3796, '2018-4-2 19:30:00');")
        cur.execute("INSERT INTO Event_Schedule VALUES (3800, '2018-4-29 15:00:00');")
        cur.execute("INSERT INTO Tickets VALUES ('a', 78976, 3783);")
        cur.execute("INSERT INTO Tickets VALUES ('b', 78987, 3792);")
        cur.execute("INSERT INTO Tickets VALUES ('c', 78977, 3783);")
        cur.execute("INSERT INTO Tickets VALUES ('d', 78987, 3783);")
        cur.execute("INSERT INTO Tickets VALUES ('e', 78977, 3783);")
        cur.execute("INSERT INTO Tickets VALUES ('f', 78981, 3796);")
        cur.execute("INSERT INTO Tickets VALUES ('g', 78987, 3783);")
        cur.execute("INSERT INTO Tickets VALUES ('h', 78977, 3792);")
        cur.execute("INSERT INTO Tickets VALUES ('i', 78987, 3790);")
        cur.execute("INSERT INTO Tickets VALUES ('j', 78977, 3795);")
        cur.execute("INSERT INTO Schedule_Performer VALUES (900, 3783);")
        cur.execute("INSERT INTO Schedule_Performer VALUES (500, 3783);")
        cur.execute("INSERT INTO Schedule_Performer VALUES (300, 3796);")
        cur.execute("INSERT INTO Schedule_Performer VALUES (400, 3800);")
        cur.execute("INSERT INTO Schedule_Performer VALUES (400, 3783);")
        cur.execute("INSERT INTO Schedule_Performer VALUES (300, 3790);")
        cur.execute("INSERT INTO Events VALUES (2010, 'Songs of Freedom', 3458, 1004, 3783, 0001);")
        cur.execute("INSERT INTO Events VALUES (2017, 'UI Symphony Orchestra', 3459, 1005, 3783, 0002);")
        cur.execute("INSERT INTO Events VALUES (2012, 'UI Campus and University Bands', 3459, 1005, 3783, 0002);")
        cur.execute("INSERT INTO Events VALUES (2000, 'Barbecue', 3459, 1006, 3796, 0004);")
        cur.execute("INSERT INTO Events VALUES (2015, 'UI Latin Jazz Ensemble', 3459, 1005, 3790, 0004);")
        cur.execute("INSERT INTO Events VALUES (2014, 'UI Jazz Vocal Ensembles', 3459, 1004, 3795, 0004);")

        print "data injection completed"

        '''data query'''

        cur.execute("SELECT * FROM Customer ORDER BY C_NAME, C_ID;")
        rows = cur.fetchall()
        print "List all customers, ordered by customer name, and then by customer ID:"
        for row in rows: 
            print "\t%s"%str(row)
        print "\n\n"

        cur.execute("SELECT COUNT(E_ID) FROM Events;")
        data = cur.fetchone()
        print "Count the number of events."
        print data
        print "\n\n"


        cur.execute("SELECT * FROM Customer WHERE C_Name LIKE '%s%';")
        rows = cur.fetchall()
        print "List all customers whose last name contains the letter s."
        for row in rows: 
            print "\t%s"%str(row)
        print "\n\n"


        cur.execute("SELECT * FROM Event_Schedule NATURAL JOIN Schedule_Performer NATURAL JOIN Performer")
        rows = cur.fetchall()
        print "List performers’ perform history."
        for row in rows: 
            print "\t%s"%str(row)
        print "\n\n"

        '''
        cur.execute("SELECT * FROM Customer Right JOIN Tickets on Customer.C_ID=Tickets.C_ID;")
        rows = cur.fetchall()
        print " Right JOIN Customer table with Tickets table."
        for row in rows: 
            print "\t%s"%row
        print "\n\n"


        cur.execute("SELECT * FROM Customer Left JOIN Tickets on Customer.C_ID=Tickets.C_ID;")
        rows = cur.fetchall()
        print " Left JOIN Customer table with Tickets table."
        for row in rows: 
            print "\t%s"%str(row)
        print "\n\n"


        cur.execute("SELECT * FROM Customer Right JOIN Tickets on Customer.C_ID=Tickets.C_ID UNION SELECT * FROM Customer Left JOIN Tickets on Customer.C_ID=Tickets.C_ID;")
        rows = cur.fetchall()
        print " Full JOIN Customer table with Tickets table."
        for row in rows: 
            print "\t%s"%row
        print "\n\n"
        '''

    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    build_database()
 