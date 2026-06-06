from datetime import datetime, time

#Reccomendation Engine 
#Rule based

def getMonth(month):
    if month in [3,4,5]:
        return "Spring"
    if month in [6,7,8]:
        return "Summer"
    if month in [9,10,11]:
        return "Fall"
    if month in [12,1,2]:
        return "Winter"
def getTimeOfDay(check_time = None):
    if check_time is None:
        check_time = datetime.now().time()
    
    if time(5,0) <= check_time < time(8,0):
        return "Dawn"
    elif time(8,0) <= check_time < time(12,0):
        return "Morning"
    elif time(12,0) <= check_time < time(15,0):
        return "Midday"
    elif time(15,0) <= check_time < time(18,0):
        return "Afternoon"
    elif time(18,0) <= check_time < time(21,0):
        return "Evening"
    else:
        return "Night"
    
def waterTemp():