import csv
def write_to_csv(data):   
    with open('data.csv','w') as file:
        columns = ['title','description']
        writer = csv.DictWriter(file, columns)
        writer.writeheader()
        for prod in data:
            writer.writerow()