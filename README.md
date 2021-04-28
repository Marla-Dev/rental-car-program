# rental-car-program
A program that calculates the amount of cash due for a car rental given a few variations of renting options.

Features:
Roll-over-miles funcionality so it can accurately calulate an odometer going from 99995 to 00005 as 10 miles used.
Rounds to the nearest mile when calculating costs.

The three customer codes are "B", "D", and "W". For "Base Charge","Daily Charge", and "Weekly Charge".
Base Charge:
  $40 /DAY
  $0.25 /MI
Daily Charge:
  $60 /DAY
  $0.25 /MI for MI <= 100
Weekly Charge:
  $190 /WEEK
  $0.25 /MI for MI <= 900 OR
  $100 /WEEK for MI between 900 and 1500 (inclusive) OR
  $200/ WEEK + $0.25*(every mile over 900)
  
 
