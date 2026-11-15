# Reflection 1:
# Python makes it easier to automate tasks, calculate totals, and process large amounts of data.
# Excel is better for visually organizing information, creating charts, and manually editing data.

# Reflection 2:
# A business could use an append-mode log to record daily sales and transactions.
# Append mode is useful because it adds new records without deleting information from previous days.

import csv
from datetime import datetime

# EXERCISE 1: Setup
# Open the sales CSV file

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    print("Exercise 1: CSV file opened successfully.")

    # EXERCISE 2: Read and print raw rows
    print("\nExercise 2: Raw CSV rows")

    for row in reader:
        print(row)


# EXERCISE 3: Skip the header

print("\nExercise 3: Skip the header")

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    print("Header:", header)

    for row in reader:
        print(row)


# EXERCISE 4: Compute totals

print("\nExercise 4: Compute totals")

total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units × ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")


# EXERCISE 5: Filter and write

print("\nExercise 5: Filter and write")

original_count = 0
written_count = 0

with open("data/sales.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    with open("data/cleaned.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)

        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1

            product = row[0]
            price = float(row[1])
            quantity = int(row[2])

            total = price * quantity

            if total > 100:
                writer.writerow([product, price, quantity, total])
                written_count += 1

print(f"Wrote {written_count} rows out of {original_count} original rows.")


# EXERCISE 6: csv.DictReader

print("\nExercise 6: DictReader")

dict_total_revenue = 0

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        dict_total_revenue += total

        print(f"{product}: ${total:.2f}")

print(f"DictReader total revenue: ${dict_total_revenue:.2f}")

# csv.reader uses column positions to access information.
# DictReader uses column names, making it easier to understand and organize data.


# EXERCISE 7: Sales summary by product

print("\nExercise 7: Sales summary")

sales_summary = {}

with open("data/sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity

        if product in sales_summary:
            sales_summary[product] += total
        else:
            sales_summary[product] = total

for product in sorted(sales_summary):
    print(f"{product}: ${sales_summary[product]:.2f}")


# EXERCISE 8: Append mode log

print("\nExercise 8: Append mode log")

current_time = datetime.now()

with open("data/run_log.txt", "a") as log_file:
    log_file.write(
        f"{current_time} - Total Revenue: ${total_revenue:.2f}\n"
    )

print("Run log updated successfully.")