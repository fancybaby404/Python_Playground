import requests
from datetime import datetime
import smtplib
import time

# Need to change to work: my_email, password, to_email, MY_LAT and MY_LNG

MY_LAT = 0 # Your latitude
MY_LNG = 0 # Your longitude
my_email = '' # Your Email
password = '' # Your Password
to_email = '' # The email you want to send the message to if ISS is overboard

#Your position is within +5 or -5 degrees of the ISS position.
def is_close_to_ISS():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        print(f'MY_LAT: {MY_LAT}, MY_LNG: {MY_LNG}\nISS_LAT: {iss_latitude}, ISS_LNG: {iss_longitude}')
        print('ISS pos is close: True')
        return True
    else:
        print(f'MY_LAT: {MY_LAT}, MY_LNG: {MY_LNG}\nISS_LAT: {iss_latitude}, ISS_LNG: {iss_longitude}')
        print('ISS pos is close: False')
        return False

while True:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    # Grab ISS API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Grab sunset&sunrise API
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    
    def is_night():
        # if sunset is > time_now and time_now is < sunrise 
        #   SUNSET         SUNRISE (api doesnt work as well)
        if 18 >= time_now <= 5:
            return True
        
    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.
    
    if is_close_to_ISS() and is_night():
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=f'Subject:LOOK UP BRO DA ISS THERE BRO\n\ncheck it outttt\nTIME: {datetime.now().hour}:{datetime.now().minute}'
                )
            print('Email sent!')
    time.sleep(60)
    print('\n')