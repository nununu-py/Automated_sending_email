import random
import pandas
import datetime as dt
import smtplib

my_email = ""  # your email
my_password = ""  # your email app password


list_of_text = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
chosen_text = random.choice(list_of_text)

current_time = dt.datetime.now()

df = pandas.read_csv("birthdays.csv")
birthday_data = df.to_dict(orient="records")
friend_name = ""

for data in birthday_data:
    if current_time.day == data["day"] and current_time.month == data["month"]:
        friend_name = data["name"]
        email_target = data["email"]

        with open(chosen_text) as file:
            send_text = file.read()
            send_text = "".join([i for i in send_text]).replace("[NAME]", f"{friend_name}")

        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=email_target, msg=f"Subject:HAPPY BIRTHDAY\n\n{send_text}")
        print("success sending msg")
        connection.close()
