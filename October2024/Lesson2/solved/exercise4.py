import datetime

if __name__  == "__main__":
    now = datetime.datetime.now() 
    timestamp = now.timestamp()
    with open("logfile.txt", mode="w",) as log_file:
        log_file.write( str (f"The current date and time is {now} and the timestamp: {timestamp}"))
        