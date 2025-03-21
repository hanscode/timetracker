import csv
import utils


def start_tracking(client, description):
    print(f"Start tracking {description} for {client}")

    # TODO: Grab the current time and store it as a string in start_time
    # in the format: HH:MM(AM/PM) YYYY-MM-DD
    # for example: 09:40AM 2023-08-11

    start_time = ""

    # Code to append a new job to the CSV
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', lineterminator='')
        writer.writerow([client, description, start_time, ''])


def stop_tracking():
    print("Stopping tracking")

    # TODO: Grab the current time and store it as a string in end_time
    # in the format: HH:MM(AM/PM) YYYY-MM-DD
    # for example: 09:40AM 2023-08-11

    end_time = ""

    # Code to append a new job to the CSV
    with open('data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([end_time])


def display_all_totals(client):
    print(f"Calculating time spent on all jobs for {client}...")
    client_jobs = utils.get_by_client(client)

    # TODO: List out all the different jobs, and then a total time spent
    # For example, if the user chooses Emmerton:
    # Monthly Meeting - 1 hours 0 minutes
    # Onboarding replacement - 2 hours 0 minutes
    # Follow-up questions - 0 hours 28 minutes
    # TOTAL FOR EMMERTON: 3 hours 28 minutes

    # references
    print(client)
    print(client_jobs)


def display_range_totals(client, dates_str_list):
    print(f"Calculating time spent on jobs for {client} in the specified range...")
    client_jobs = utils.get_by_client(client)

    # dates_str_list contains 2 date strings in the format YYYY-MM-DD
    # TODO: turn the two date strings in dates_str_list to datetime objects and store in range_start_dt and range_end_dt

    range_start_dt = None
    range_end_dt = None

    # TODO: filter client_jobs to only include those within the start and end datetimes

    # TODO: List out all the different jobs, and then a total time spent - just like display_all_totals


def display_x_days_totals(client, days):
    print(f"Calculating time spent on jobs for {client} in the last {days} days...")
    client_jobs = utils.get_by_client(client)

    # TODO: determine the start and end datetimes for this range
    range_start_dt = None
    range_end_dt = None

    # TODO: filter and display client_jobs to only include those with the start and end datetimes

