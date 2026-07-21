##################### Normal Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
data = pd.read_csv("birthdays.csv")
birthday_dict={(data["month"],data["day"]): (data["name"],data["email"],data["year"],data["month"],data["day"]) for (index, data) in data.iterrows()}

print(birthday_dict)

current_date = dt.datetime.today()
today_month = current_date.month
today_day = current_date.day
today=(today_month,today_day)
birthday_person=[]
if today in birthday_dict:
    with open("C:/Users/krish/PycharmProjects/PythonProject/birthday-wisher-normal-start/letter_templates/letter_1.txt","r") as letter_1:
        format_1=letter_1.read()
    with open("C:/Users/krish/PycharmProjects/PythonProject/birthday-wisher-normal-start/letter_templates/letter_2.txt","r") as letter_2:
        format_2=letter_2.read()
    with open("C:/Users/krish/PycharmProjects/PythonProject/birthday-wisher-normal-start/letter_templates/letter_3.txt","r") as letter_3:
        format_3=letter_3.read()

    birthday_person=birthday_dict[today]
    name=birthday_person[0]
    email=birthday_person[1]

    letters=[format_1,format_2,format_3]
    random_letter = random.choice(letters)
    final_letter=random_letter.replace("[NAME]",name)
    print(final_letter)


# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.
my_email = "***@gmail.com"
password="***"

with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
    connection.starttls()
    connection.login(my_email,password)
    connection.sendmail(from_addr=my_email,to_addrs=email,msg=f"Subject: Happy Birthday! \n\n {final_letter}".encode("utf-8"))


