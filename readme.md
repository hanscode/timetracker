Time Tracker App
---

### Introduction
Welcome to the Time Tracker App. It works with a CSV file, and it stores data on the time we've spent working on projects for different clients. When the app is run, it loads data from the CSV and presents users with a menu.
We can:
- Start tracking time we're spending on project for a client (which is reflected in the CSV)
- Stop tracking time on a project we're currently working on (also reflected in the CSV)
- Calculate the total times we've spent on a client by entering their ID when prompted
  - And we can choose to see data from a specific date range
  - Or within the X number of days
  - Or simply retrieve all the data we have from that client

Much of the logic and navigation of the app has already been written by other developers of your team. Your job is to complete the `datetime` related functions of the app. It is recommended to explore the files to see what data you have to work with.

### Getting started:
1. Create a virtual environment for this project
2. Install `dateutil` (the PPI name is `python-dateutil`!)
3. Tackle the three `datetime` related functions below

### Your mission, should you choose to accept it:
1. `start_tracking()` and `stop_tracking()` in `functions.py` - Start and stop time tracking
2. `display_all_totals()` in `functions.py` - Calculate and display all tracked time for a client
3. `display_range_totals()` and `display_x_days_totals()` - Filter, calculate and display tracked time

### Extra challenges
- Create a helper function that returns "now" as a datetime string. Both `start_tracking()` and `stop_tracking()` can use this
- In `display_range_totals()`, it's possible that the user used an invalid date string. Catch any exceptions
- Create one function used to take a client and client job list to calculate and display data.
- Use list comprehension, `filter()`, and `lambda` to filter through client jobs and date ranges
---

Created for the [Team Treehouse](https://teamtreehouse.com/) Python Dates and Times (2023) course