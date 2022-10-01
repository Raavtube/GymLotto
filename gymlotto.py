# This program will generate a workout routine for the user and save the routine to a file. It will have logic to make sure the user does not hit the same muscle group back to back days.

from datetime import datetime
from logging import PlaceHolder
import random
import os
import sys
import time
from tkinter import *

root = Tk()




def get_quote():
    # This will import the text file that contains possible workouts for each muscle group.
    with open("quotes.txt", "r") as f:
        quotes = f.readlines()
    quote = random.choice(quotes)
    quote = quote.replace("\n", "")
    return quote


# This will import the text file that contains possible workouts for each muscle group.
def import_workouts():
    # This will import the text file that contains possible workouts for each muscle group.
    with open("workouts.txt", "r") as f:
        workouts = f.readlines()
    
    # This will add all the workouts to a list. Lines starting with "B@@", are back workouts, "C@@" are chest workouts, "L@@" are leg workouts, "A@@" are abs workouts, "Ba@@" are back workouts and "S@@" are shoulder workouts.
    # It will add back workouts and bicep workouts together in the same list.
    # It will add chest workouts and abs workouts together in the same list.
    # It will add tricep workouts and shoulder workouts together in the same list.
    # It will add leg workouts and calf workouts together in the same list.
    backbicepr = []
    chestabsr = []
    trishoulderr = []
    legcalfr = []
    for workout in workouts:
        if workout.startswith("B@@"):
            backbicepr.append(workout)
        elif workout.startswith("C@@"):
            chestabsr.append(workout)
        elif workout.startswith("L@@"):
            legcalfr.append(workout)
        elif workout.startswith("A@@"):
            chestabsr.append(workout)
        elif workout.startswith("Ba@@"):
            backbicepr.append(workout)
        elif workout.startswith("S@@"):
            trishoulderr.append(workout)
    
    # This will remove the muscle group characters from each workout in the list and replace the items with the workout only.
    print(backbicepr)
    backbicep = []
    chestabs = []
    trishoulder = []
    legcalf = []


    # This will remove the muscle group characters from each workout in the list and replace the items with the workout only.
    for workout in backbicepr:
        if workout.startswith("B@@"):
            workout = workout.replace("B@@", "")
            workout = workout.replace("\n", "")
            backbicep.append(workout)
        elif workout.startswith("Ba@@"):
            workout = workout.replace("Ba@@", "")
            workout = workout.replace("\n", "")
            backbicep.append(workout)
    for workout in chestabsr:
        if workout.startswith("C@@"):
            workout = workout.replace("C@@", "")
            workout = workout.replace("\n", "")
            chestabs.append(workout)
        elif workout.startswith("A@@"):
            workout = workout.replace("A@@", "")
            workout = workout.replace("\n", "")
            chestabs.append(workout)
    for workout in trishoulderr:
        if workout.startswith("S@@"):
            workout = workout.replace("S@@", "")
            workout = workout.replace("\n", "")
            trishoulder.append(workout)
    for workout in legcalfr:
        if workout.startswith("L@@"):
            workout = workout.replace("L@@", "")
            workout = workout.replace("\n", "")
            legcalf.append(workout)

    
        
    
   
    
    # This will return a dictionary with the workouts for each muscle group.
    workout_dict = {"backbicep": backbicep, "chestabs": chestabs, "trishoulder": trishoulder, "legcalf": legcalf}
    return workout_dict

    

# This will generate a workout routine for the user.
def generate_workout():
    # This will import the workouts from the text file.
    workout_dict = import_workouts()
    
    # This will generate a workout routine for the user. It will make sure the user hits all upper body muscle groups on the same day and all lower body muscle groups on the same day.
    # It will also make sure the user does not hit the same muscle group back to back days.
    # It will assign the amount of set and reps for each workout.
    # It will make sure a user hits all back and bi workouts on the same day and all chest and abs workouts on the same day, etc.
    # It will make sure the user does not hit the same muscle group back to back days.
    
    # This will allow the program to select a random workout from the list of workouts for each muscle group.
    workout_areas = ["Back & Bicep", "Chest & Abs", "Tricep & Shoulders", "Legs"]

    # This will generate a random number between 1 and 4. This will be used to determine the selected workout group for the day.
    workout_group = random.randint(1, 4)
    workout_group = workout_areas[workout_group - 1]

    # This will open the previous workout file and read the last workout group.
    try:
        with open("previous_workout.txt", "r") as f:
            previous_workout = f.read()
            previous_workout = previous_workout.replace("\n", "")
            # Logic
            # If Past Day was A Back and Bicep Day then today will be a Chest and Abs Day OR a Tricep and Shoulder Day
            # If Past Day was a Chest and Abs Day then today will be a Tri and Shoulder Day OR a Leg Day
            # If Past Day was a Tri and Shoulder Day then today will be a Leg Day OR a Back and Bicep Day
            # If Past Day was a Leg Day then today will be a Back and Bicep Day OR a Chest and Abs Day
            if previous_workout == "Back & Bicep":
                workout_areas.remove("Back & Bicep")
                workout_group = random.choice(workout_areas)
            elif previous_workout == "Chest & Abs":
                workout_areas.remove("Chest & Abs")
                workout_group = random.choice(workout_areas)
            elif previous_workout == "Tricep & Shoulders":
                workout_areas.remove("Tricep & Shoulders")
                workout_group = random.choice(workout_areas)
            elif previous_workout == "Legs":
                workout_areas.remove("Legs")
                workout_group = random.choice(workout_areas)
            
        # THis will write the current workout group to the previous workout file.
    except:
        with open("previous_workout.txt", "w") as f:
            f.write(workout_group)
        f.close()

    workout_list = []

    workout_list.append("Todays Date: " + time.strftime("%m/%d/%Y"))
    workout_list.append("-------------------------")
    selectedWarmup = ["50 Jumping Jacks", ".3 Mile Run Treadmill", "2 Lap Run on Track", "Stairmaster for 4 Minutes"]
    workout_list.append("Warmup: " + random.choice(selectedWarmup))
    workout_list.append("Today you will be hitting " + workout_group)
    workout_list.append("Todays Main Set:")
    # Each Day Will Have 4 Workouts
    if workout_group == "Back & Bicep":
        # This will select 4 random back and bicep workouts
        usedworkouts = []
        for i in range(7):
            workout = random.choice(workout_dict["backbicep"])
            while workout in usedworkouts:
                workout = random.choice(workout_dict["backbicep"])
            usedworkouts.append(workout)
            sets = random.randint(3, 5)
            reps = random.randint(8, 12)
            # This will now format a variable with the workout, sets and reps.
            workout = workout + " " + str(sets) + " sets of " + str(reps) + " reps" + "\n"
            workout_list.append(workout)
    elif workout_group == "Chest & Abs":
        # This will select 4 random chest and abs workouts
        usedworkouts = []
        for i in range(7):
            workout = random.choice(workout_dict["chestabs"])
            while workout in usedworkouts:
                workout = random.choice(workout_dict["chestabs"])
            usedworkouts.append(workout)
            sets = random.randint(3, 5)
            reps = random.randint(8, 12)
            # This will now format a variable with the workout, sets and reps.
            workout = workout + " " + str(sets) + " sets of " + str(reps) + " reps" + "\n"
            workout_list.append(workout)
    elif workout_group == "Tricep & Shoulders":
        # This will select 4 random tricep and shoulder workouts
        usedworkouts = []
        for i in range(7):
            workout = random.choice(workout_dict["trishoulder"])
            while workout in usedworkouts:
                workout = random.choice(workout_dict["trishoulder"])
            usedworkouts.append(workout)
            sets = random.randint(3, 5)
            reps = random.randint(8, 12)
            # This will now format a variable with the workout, sets and reps.
            workout = workout + " " + str(sets) + " sets of " + str(reps) + " reps" + "\n"
            workout_list.append(workout)
    elif workout_group == "Legs":
        # This will select 4 random leg and calf workouts but not select the same workout twice.
        usedworkouts = []
        for i in range(7):
            workout = random.choice(workout_dict["legcalf"])
            while workout in usedworkouts:
                workout = random.choice(workout_dict["legcalf"])
            usedworkouts.append(workout)

            sets = random.randint(3, 5)
            reps = random.randint(8, 12)
            # This will now format a variable with the workout, sets and reps.
            workout = workout + " " + str(sets) + " sets of " + str(reps) + " reps" + "\n"
            workout_list.append(workout)

    # This will select a random warmdown workout.
    warmdownSection = ["10 Minute Stairstepper", "10 Minute Elliptical","10 Minute Bike", "10 Minute Rowing Machine", "10 Minute Treadmill"]
    warmdown = random.choice(warmdownSection)
    workout_list.append("WARM DOWN: " + warmdown)
    workout_list.append("----------------------------------------")
    workout_list.append("Excellent Job! Keep up the good work!")
    # This will get a random inspirational quote and put it at the end of the workout.
    workout_list.append(get_quote())

    return workout_list


    
    

    


dailyworkout = generate_workout()
# This will print the workout to the console and create a new file with the workout.
# Then the AI will send the workout to the user via email and print the workout to the recipt printer.
for workout in dailyworkout:
    print(workout)
    # This will check if the last 2 characters in the workout are "\n" and if not it will add them.
    if workout[-2:] != "\n":
        workout = workout + "\n"
    workoutfilename = "workouts/workout" + datetime.now().strftime("%Y%m%d%H%M%S") + ".txt"
    # This will create a new file with the workout.
    with open(workoutfilename, "a") as workout_file:
        workout_file.write(workout)
    # This will send the workout to the user via email.
    #send_email()
    # This will print the workout to the recipt printer.
    #print_workout()


