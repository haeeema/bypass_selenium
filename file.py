def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    # open() : Built-in function, open or create file
    # CSV : comma-separated-value, a format of a file
    # "w" : only write mode
    file.write("Position, Company, Location, URL\n")
    # Write a column seperated by comma

    for job in jobs:
        file.write(
            f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

    file.close()
