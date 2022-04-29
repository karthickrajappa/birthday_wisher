import smtplib
import random
import pandas
import datetime as dt

USER_NAME = "MAIL ID"
PASSWORD = "PASSWORD"

today = dt.datetime.now()
today = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
data_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in data_dict:
    birth_person = data_dict[today]
    file_path = (f"letter_templates/letter_{random.randint(1,3)}.txt")
    with open(file_path) as letter:
        letter = letter.read()
        letter = letter.replace("[NAME]", birth_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER_NAME, password=PASSWORD)
        connection.sendmail(from_addr=USER_NAME,
                            to_addrs=birth_person["email"],
                            msg=f"subject: Happy Birthday \n\n{letter} "
                            )
