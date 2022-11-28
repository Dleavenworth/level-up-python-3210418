import csv


def merge_csv(files, result):
    fields = []
    data = []
    for file in files:
        with open(file, "r") as f:
            reading = csv.DictReader(f)
            all_fields = reading.fieldnames
            print(all_fields)
            for field in all_fields:
                if field not in fields:
                    fields.append(field)
            for row in reading:
                data.append([row])
    print(data)
    print(fields)
    with open(result, "w") as f:
        writing = csv.DictWriter(f, fields)
        writing.writeheader()
        for rows in data:
            writing.writerows(rows)


merge_csv(["src/12 Merge CSV Files/class1.csv",
          "src/12 Merge CSV Files/class2.csv"], "res.csv")
