import csv

def write_to_file(name, dictionary):
    with open(str(name)+".csv", 'w', encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for key, value in dictionary.items():
            writer.writerow([key, value])