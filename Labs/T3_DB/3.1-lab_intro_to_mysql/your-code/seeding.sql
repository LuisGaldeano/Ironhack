insert into cars (VIN, Manufacture, Model, Year, Color) values 
('3K096I98581DHSNUP', 'Volkswagen',  'Tiguan', 2019, 'Blue'),
('ZM8G7BEUQZ97IH46V', 'Peugeot',  'Rifter', 2019, 'Red'),
('RKXVNNIHLVVZOUB4M', 'Ford',  'Fusion', 2018, 'White'),
('HKNDGS7CU31E9Z7JW', 'Toyota',  'RAV4', 2018, 'Silver'),
('DAM41UDN3CHU2WVF6', 'Volvo',  'V60', 2019, 'Gray'),
('DAM41UDN3CHU2WVF7', 'Volvo',  'V60 Cross Country', 2019, 'Gray');


insert into customers (Name, Phone, Email, Adress, City, State, Country, Postal) values
('Pablo Picasso', +34636176382, '-', 'Paseo de la Chopera 14', 'Madrid', 'Madrid', 'Spain', 28045),
('Hedy Lamarr', +431514442250, '-', 'Weiglgasse 10', 'Viena', 'Vienna', 'Austria', 1150),
('Katherine Johnson', +12023580000, '-', '300 E St SW', 'Washington DC', 'Washington', 'United States', 20546);


INSERT INTO salesperson (Name, Store) values
('Petey Cruiser', 'Madrid'),
('Anna Sthesia', 'Barcelona'),
('Paul Molive', 'Berlin'),
('Gail Forcewind', 'Paris'),
('Paige Turner', 'Mimia'),
('Bob Frapples', 'Mexico City'),
('Walter Melon', 'Amsterdam'),
('Shonda Leer', 'São Paulo');


INSERT INTO invoices (Date, Cars_idCars, Salesperson_StaffID, Customers_CustomersID) values 
('2018-08-22', 1, 2, 1),
('2018-12-31', 3, 1, 3),
('2019-01-22', 5, 7, 1);
