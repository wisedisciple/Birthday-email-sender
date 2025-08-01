import smtplib
from datetime import datetime as dt
import pandas as pd
import random

MY_EMAIL = "FROM_EMAIL"
PASSWORD = "APP_PASSWORD"

today = dt.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"] )

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIl, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIl, to_addrs=birthdays_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{contents}")
