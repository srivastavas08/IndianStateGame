import turtle
import pandas

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

screen = turtle.Screen()
screen.title("Indian States/UT Game")
image = "blank.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("States.csv")
all_states = data.States.to_list()
guessed_states = []
Name = screen.textinput(title="Welcome", prompt="Enter your Name:")
mail = screen.textinput(title="Ready to go", prompt="Enter your E-mail:")
while len(guessed_states) < 37:
    guess_state = screen.textinput(title=f"{len(guessed_states)}/37 correct",
                                   prompt="What's the another state/UT name?")
    answer_state = guess_state.title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(f"States {Name} needs to learn.csv")
        break
    elif answer_state.title() in all_states:
        t = turtle.Turtle()
        guessed_states.append(answer_state)
        t.hideturtle()
        t.pu()
        state_data = data[data.States == answer_state]
        t.goto(int(state_data.X_cor), int(state_data.Y_cor))
        t.write(answer_state)
        # t.write(state_data.States.item())

# Python code to illustrate Sending mail with attachments
# from your Gmail account


from_addr = "mongoengine@gmail.com"
password = "SHIvam7426"
to_addr = mail

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = from_addr

# storing the receivers email address
msg['To'] = to_addr

# storing the subject
msg['Subject'] = "STATES YOU NEED TO LEARN"

# string to store the body of the mail
body = "Hey There!\n \n I am attaching the file with the list of names you need to learn\n \n \n " \
       "Thanks and Regards\n Python"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# open the file to be sent
filename = f"States {Name} needs to learn.csv"
attachment = open(f"States {Name} needs to learn.csv", "rb")

# instance of MIMEBase and named as p
p = MIMEBase('application', 'octet-stream')

# To change the payload into encoded form
p.set_payload(attachment.read())

# encode into base64
encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# attach the instance 'p' to instance 'msg'
msg.attach(p)

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login(from_addr, password)

# Converts the Multipart msg into a string
text = msg.as_string()

# sending the mail
s.sendmail(from_addr, to_addr, text)

# terminating the session
s.quit()

'''To get coordinates of states'''
# def get_mouse_click_coor(x, y):
#     print([x, y])
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()#ALTERNATIVE WAY TO keep our code running

'''Scraped Name of all the states from government of India'''
# import requests
# from bs4 import BeautifulSoup
#
# URL = "https://knowindia.gov.in/states-uts/"
#
# response = requests.get(URL)
# website_html = response.text
#
# soup = BeautifulSoup(website_html, "html.parser")
# all_states = soup.find_all(name="h3")
# state_title = [state.getText() for state in all_states]
# with open("states.txt", mode = "w") as file:
#     for state in state_title:
#         x = state.split("(")
#         file.write(f"{x[0]}\n")
