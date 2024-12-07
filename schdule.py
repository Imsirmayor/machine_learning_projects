import os
from datetime import datetime
from time import sleep

def create_schedule(task, time_str):
    try:
        schedule_time = datetime.strptime(time_str, "%H:%M").time()
        print(f"Task '{task}' scheduled at {time_str}.")
        return schedule_time
    except ValueError:
        print("Invalid time format. Please use HH:MM in 24-hour format.")
        return None

def notify(task):
    print(f"⏰ Reminder: It's time for your task: {task}")
  

def check_schedule(task, schedule_time):
    print("Waiting for the scheduled time...")
    while True:
        now = datetime.now().time()
        print(f"Current Time: {now}")  # Debugging
        if now.hour == schedule_time.hour and now.minute == schedule_time.minute:
            notify(task)
            break
        sleep(5)  # Check every 5 seconds

if __name__ == "_main_":
    print("Welcome to the AI Scheduler!")
    
    # Taking input from the user for task and time
    task_name = input("Enter the task you want to schedule: ")
    task_time = input("Enter the time for the task (HH:MM in 24-hour format): ")

    # Creating schedule
    schedule_time = create_schedule(task_name, task_time)
    if schedule_time:
        check_schedule(task_name, schedule_time)