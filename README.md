# CreateDataCSV
Create Random Data in CSV Format 

# README - Data Generation Script (createCsv.py)

## Overview
The `createCsv.py` script is responsible for **generating synthetic data** for a PostgreSQL **Docker-based database**. The script ensures that all necessary tables are populated with randomized but realistic data, making it useful for database testing, query optimization, and analytics development.

## Key Features
- Generates **1 million+ records** for the `transaction` (fact) table.
- Covers the data period from **2014 to 2024**.
- All **cinemas are located in Qatar**.
- Creates **CSV files** for easy import into a PostgreSQL database.
- Supports structured tables such as `customers`, `movies`, `cinemas`, `transactions`, `tickets`, etc.
- Ensures logical relationships between entities (e.g., movies have directors, tickets belong to transactions, etc.).

## Tables and Generated Data
The script generates data for the following tables:

| Table Name       | Description |
|-----------------|-------------|
| `cinema`        | 100 cinemas located in Qatar |
| `hall`          | 300 cinema halls linked to cinemas |
| `customer`      | 50,000 customer profiles with age, gender, and DOB |
| `movie`         | 1,000 movies with different genres and release years |
| `director`      | 200 directors linked to movies |
| `star`          | 1,000 actors associated with movies |
| `promotion`     | 50 promotional campaigns |
| `showing`       | 500,000 showtimes for movies across different halls |
| `transaction`   | **1,000,000+ transactions** (fact table) |
| `ticket`        | Multiple tickets per transaction |

## How It Works
The script uses **Pandas and NumPy** to generate **randomized synthetic data**. It saves each dataset as a **CSV file**, which can later be imported into PostgreSQL.

### **Data Generation Logic:**
1. **Cinemas & Halls:** All cinemas are **based in Qatar**.
2. **Customers:** Random names, birthdates, and genders.
3. **Movies & Directors:** Movies have assigned directors and genres.
4. **Transactions & Tickets:** Each transaction involves **1-5 tickets**, with different payment methods (Cash, Credit Card, Online Payment).
5. **Time Period:** Data spans from **2014 to 2024**.

## Generated CSV Files
After running the script, the following CSV files will be created:
- `cinemas.csv`
- `halls.csv`
- `customers.csv`
- `movies.csv`
- `directors.csv`
- `stars.csv`
- `promotions.csv`
- `showings.csv`
- `transactions.csv`
- `tickets.csv`

## Usage Instructions
### **Prerequisites**
Ensure that Python and the necessary dependencies are installed:
```sh
pip install pandas numpy
```

### **Run the Script**
Execute the script using:
```sh
python createCsv.py
```

### **Import Data into PostgreSQL**
Once the CSV files are generated, you can import them into PostgreSQL using:
```sh
docker cp cinemas.csv postgres_container:/var/lib/postgresql/data/
```
Inside PostgreSQL:
```sql
\copy public.cinema FROM '/var/lib/postgresql/data/cinemas.csv' DELIMITER ',' CSV HEADER;
```
Repeat for all generated CSV files.

## Conclusion
This script automates the generation of structured test data for a PostgreSQL-based **cinema transaction database**. By running it, users can quickly populate a test database for analytics, testing, and performance tuning.

