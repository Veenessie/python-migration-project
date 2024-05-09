from rich import print
import csv 
    
with open('migration.csv', 'r') as file:
    migration_file = csv.DictReader(file)       
    for line in migration_file:
        continent = line['continent']
        year = line['year']
        migration_change = line['Five-year change immigrants']
        print(continent)
        print(year)
        print(migration_change)





