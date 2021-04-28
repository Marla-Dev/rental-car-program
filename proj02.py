    ###########################################################

    #  Computer Project #2

    #

    #  Algorithm

    #    prompt for a continuation

    #       ask for customer code

    #       ask for rental period(in days)
    
    #       ask for staring odometer miles
    
    #       ask for ending odometer miles

    #       calculate the amount due with info above

    #    loop until customer does not continue


    ###########################################################
    
import math

BANNER = "\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
print(BANNER)
 
PROMPT = '''\nWould you like to continue (Y/N)? '''
#start the program while this is true
start = True 
while start:
    start_prompt = input(PROMPT)
    
    if start_prompt.lower() != 'y':
        print("Thank you for your loyalty.")
        break
        
    if start_prompt.lower() == 'y':
        cust_code = input("\nCustomer code (BDW): ")
        
        while not( cust_code.lower() == 'b' or cust_code.lower() == 'd' \
        or cust_code.lower() == 'w'):
            print("\n\t*** Invalid customer code. Try again. ***")
            cust_code = input("\nCustomer code (BDW): ")
            
        if cust_code.lower() == 'b':
            BASE_CHARGE = 40.00
            MILE_CHARGE = 0.25
            char_num_start = 0
            char_num_end = 0
            num_days = input("\nNumber of days: ")
            odom_start = input("Odometer reading at the start: ")
            odom_end = input("Odometer reading at the end:   ")
            odom_start_list = [str(odom_start)]
            odom_end_list = [str(odom_end)]
            new_odom_start_list = []
            new_odom_end_list = []
            new_odom_end = 0
            new_odom_start = 0
            # count the number of numbers in the starting odometer \
            # if the number is more than 5 insert a decimal
            for c in odom_start:
                char_num_start += 1
            if char_num_start > 5:
                new_odom_start = float(odom_start)
                new_odom_start /= 10
            else:
                new_odom_start = float(odom_start)
            for c in odom_end:
                char_num_end += 1
            if char_num_end > 5:
                new_odom_end = float(odom_end)
                new_odom_end /= 10
            else:
                new_odom_end = float(odom_end)
            # skip the leading zeroes for customer summary \
            # unless the start is 0
            for n in odom_end_list:
                while n[0] == "0":
                    n = n[1:] 
                new_odom_end_list.append(n)
            if int(odom_start_list[0][0:])/10 != 0:
                for n in odom_start_list:
                    while n[0] == "0":
                        n = n[1:] 
                    new_odom_start_list.append(n)                    
            else:
                new_odom_start_list.append("0")                    
            #  rolls over the miles
            if new_odom_end < new_odom_start:
                max_to_now = (100000.0 - new_odom_start)
                miles_driven = (max_to_now + new_odom_end)
            else:
                miles_driven = (new_odom_end - new_odom_start)
                
            
            # rounds the miles up if number has .5 or more
            next_mile = math.ceil(miles_driven)
            #calculates the charge
            charge = round((BASE_CHARGE*float(num_days)) + (MILE_CHARGE*float(next_mile)),1)
            
            
                
            
        if cust_code.lower() == 'd':
            BASE_CHARGE = 60.00
            MILE_CHARGE = 0.25
            char_num_start = 0
            char_num_end = 0
            num_days = input("\nNumber of days: ")
            odom_start = input("Odometer reading at the start: ")
            odom_end = input("Odometer reading at the end:   ")
            odom_start_list = [str(odom_start)]
            odom_end_list = [str(odom_end)]
            new_odom_start_list = []
            new_odom_end_list = []
            new_odom_end = 0
            new_odom_start = 0
            # count the number of numbers in the starting odometer \
            # if the number is more than 5 insert a decimal
            for c in odom_start:
                char_num_start += 1
            if char_num_start > 5:
                new_odom_start = float(odom_start)
                new_odom_start /= 10
            else:
                new_odom_start = float(odom_start)
            for c in odom_end:
                char_num_end += 1
            if char_num_end > 5:
                new_odom_end = float(odom_end)
                new_odom_end /= 10
            else:
                new_odom_end = float(odom_end)
            # skip the leading zeroes for customer summary \
            # unless the start is 0
            for n in odom_end_list:
                while n[0] == "0":
                    n = n[1:] 
                new_odom_end_list.append(n)
            if int(odom_start_list[0][0:])/10 != 0:
                for n in odom_start_list:
                    while n[0] == "0":
                        n = n[1:] 
                    new_odom_start_list.append(n)                    
            else:
                new_odom_start_list.append("0")                    
            #  rolls over the miles
            if new_odom_end < new_odom_start:
                max_to_now = (100000.0 - new_odom_start)
                miles_driven = (max_to_now + new_odom_end)
            else:
                miles_driven = (new_odom_end - new_odom_start)
                
            
            # rounds the miles up if number has .5 or more
            next_mile = math.ceil(miles_driven)                    
            #calculates the charge
            avg_mi_per_day = next_mile/float(num_days)
            if avg_mi_per_day <= 100:
                next_mile = 0 
                charge = (BASE_CHARGE*float(num_days)) + (MILE_CHARGE*float(next_mile))
            else:
                mi_over_100 = (miles_driven - 100*float(num_days))
                charge = round((BASE_CHARGE*float(num_days)) + \
                (MILE_CHARGE*float(mi_over_100)),2)
                
            
    
        if cust_code.lower() == 'w':
            BASE_CHARGE = 190.00
            MILE_CHARGE = 0.25
            char_num_start = 0
            char_num_end = 0
            num_days = input("\nNumber of days: ")
            odom_start = input("Odometer reading at the start: ")
            odom_end = input("Odometer reading at the end:   ")
            odom_start_list = [str(odom_start)]
            odom_end_list = [str(odom_end)]
            new_odom_start_list = []
            new_odom_end_list = []
            new_odom_end = 0
            new_odom_start = 0
            # count the number of numbers in the starting odometer \
            # if the number is more than 5 insert a decimal
            for c in odom_start:
                char_num_start += 1
            if char_num_start > 5:
                new_odom_start = float(odom_start)
                new_odom_start /= 10
            else:
                new_odom_start = float(odom_start)
            for c in odom_end:
                char_num_end += 1
            if char_num_end > 5:
                new_odom_end = float(odom_end)
                new_odom_end /= 10
            else:
                new_odom_end = float(odom_end)
            # skip the leading zeroes for customer summary \
            # unless the start is 0
            for n in odom_end_list:
                while n[0] == "0":
                    n = n[1:] 
                new_odom_end_list.append(n)
            if int(odom_start_list[0][0:])/10 != 0:
                for n in odom_start_list:
                    while n[0] == "0":
                        n = n[1:] 
                    new_odom_start_list.append(n)                    
            else:
                new_odom_start_list.append("0")                    
            #  rolls over the miles
            if new_odom_end < new_odom_start:
                max_to_now = (100000.0 - new_odom_start)
                miles_driven = (max_to_now + new_odom_end)
            else:
                miles_driven = (new_odom_end - new_odom_start)
                
            
            # rounds the miles up if number has .5 or more
            next_mile = math.ceil(miles_driven)                    
            #calculates the charge
            avg_mi_per_week = (next_mile/float(num_days))*7
            days_in_week = float(num_days)/7
            num_weeks = math.ceil(days_in_week)
            if avg_mi_per_week <= 900:
                next_mile = 0 
                charge = (BASE_CHARGE*num_weeks) + (MILE_CHARGE*float(next_mile))
            elif avg_mi_per_week > 900 and avg_mi_per_week <= 1500:
                charge = round((BASE_CHARGE*num_weeks) + \
                (100*num_weeks),2)
            else:
                max_mi_per_day = 900/7
                mi_over_900 = (miles_driven - 1500*num_weeks)
                charge = round((BASE_CHARGE*num_weeks) + \
                (MILE_CHARGE*float(mi_over_900) + 200*num_weeks),2)
                
    
        print("\nCustomer summary:")
        print("\tclassification code: " + cust_code)
        print("\trental period (days): " + num_days)
        print("\todometer reading at start: " + new_odom_start_list[0])
        print("\todometer reading at end:   " + new_odom_end_list[0])
        print("\tnumber of miles driven:  " + str(round(miles_driven,1)))
        print("\tamount due: $ " + str(charge))
        