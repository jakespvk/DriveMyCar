# declare constants
MONTHS = 12

# print main menu
print("1. Cost of Fuel")
print("2. Used Value")
print("3. Stopping Distance")
print("4. Quit")

# validate user input
flag = False
while (flag != True):
     # get user's menu choice
     function = int(input("Choose a function: "))
     
     # decipher user input
     if (function == 1):
          # calculating cost of fuel
          # set flag to true, input is valid
          flag = True

          # get necessary values from user
          car1_kwh = float(input("Enter car 1's miles per kW-h: "))
          # validate car1_kwh
          while car1_kwh <= 0:
               print("ERROR! Please enter a positive value!")
               car1_kwh = float(input("Enter car 1's miles per kW-h: "))
                           
          car1_kwh_cost = float(input("Enter car 1's cost per kW-h: "))
          # validate car1_kwh_cost
          while car1_kwh_cost <= 0:
               print("ERROR! Please enter a positive value!")
               car1_kwh_cost = float(input("Enter car 1's cost per kW-h: "))
          
          car2_mpg = float(input("Enter car 2's miles-per-gallon: "))
          # validate car2_mpg
          while car2_mpg <= 0:
               print("ERROR! Please enter a positive value!")
               car2_mpg = float(input("Enter car 2's miles-per-gallon: "))
               
          car2_gallon_cost = float(input("Enter car 2's cost per gallon of gasoline: "))
          # validate car2_gallon_cost
          while car2_gallon_cost <= 0:
               print("ERROR! Please enter a positive value!")
               car2_gallon_cost = float(input("Enter car 2's cost per gallon of gasoline: "))
          
          avg_miles_driven = float(input("Enter the average number of miles driven per month: "))
          # validate avg_miles_driven
          while avg_miles_driven <= 0:
               print("ERROR! Please enter a positive value!")
               avg_miles_driven = float(input("Enter the average number of miles driven per month: "))

          # calculate total costs to drive each car
          car1_total_cost = avg_miles_driven * MONTHS * car1_kwh * car1_kwh_cost          
          car2_total_cost = avg_miles_driven * MONTHS / car2_mpg * car2_gallon_cost

          # find which car is cheaper and output results
          if car1_total_cost < car2_total_cost:
               print("Car 1 will save", "${:,.2f}".format(car2_total_cost - car1_total_cost), "in a year.")
          elif car2_total_cost < car1_total_cost:
               print("Car 2 will save", "${:,.2f}".format(car1_total_cost - car2_total_cost), "in a year.")
          else:
               print("The two cars cost the same.")
          
     elif (function == 2):
          # calculate used value
          # set flag to true, input is valid
          flag = True

          # get inputs from user
          original_price = float(input("Enter original car price (no symbols necessary): "))
          # validate input
          while original_price <= 0:
               print("ERROR! Please enter a positive value.")
               original_price = float(input("Enter original car price (no symbols necessary): "))
          num_years = int(input("Enter number of years (whole number): "))
          # validate input
          while num_years <= 0:
               print("ERROR! Please enter a positive value.")
               num_years = int(input("Enter number of years (whole number): "))

          # define current_value for use in calculations
          current_value = original_price

          # calculate current values for each year (1 iteration = 1 year)
          i = 0
          for i in range(1, num_years + 1):
               current_value *= .82
               print("Year", str(i), "value:", "${:,.2f}".format(current_value))
               i += 1

     elif (function == 3):
          # calculate stopping distance
          # set flag to true, input is valid
          flag = True

          MU_NEW = 0.8
          MU_GOOD = 0.6
          MU_POOR = 0.5
          GRAVITY = 32.174
          FEET_PER_MILE = 5280
          SECONDS_PER_HOUR = 3600

          # get inputs from user
          initial_speed = float(input("Enter initial speed: "))
          # validate input
          while initial_speed <= 0:
               print("ERROR! Please enter a positive value.")
               initial_speed = float(input("Enter initial speed: "))

          # convert speed to ft/s
          initial_speed_ft_s = initial_speed * FEET_PER_MILE / SECONDS_PER_HOUR

          # get tire condition from user
          tire_condition = int(input("Enter tire condition (1 = new, 2 = good, 3 = poor): "))
          # validate input
          while not (tire_condition == 1 or tire_condition == 2 or tire_condition == 3):
               print("ERROR! Please enter a '1', '2', or '3'")
               tire_condition = int(input("Enter tire condition (1 = new, 2 = good, 3 = poor): "))
          
          # perform calculations
          # find mu
          if tire_condition == 1:
               # calculate distance
               distance = ((initial_speed_ft_s * initial_speed_ft_s) / ((2 * MU_NEW) * GRAVITY))
               # print to screen
               print("At", str(initial_speed), "miles per hour, with new tires, the car will stop in", "{:,.2f}".format(distance), "feet.")
          # find mu
          if tire_condition == 2:
               # calculate distance
               distance = ((initial_speed_ft_s * initial_speed_ft_s) / ((2 * MU_GOOD) * GRAVITY))
               # print to screen
               print("At", str(initial_speed), "miles per hour, with good tires, the car will stop in", "{:,.2f}".format(distance), "feet.")
          # find mu
          if tire_condition == 3:
               # calculate distance
               distance = ((initial_speed_ft_s * initial_speed_ft_s) / ((2 * MU_POOR) * GRAVITY))
               # print to screen
               print("At", str(initial_speed), "miles per hour, with poor tires, the car will stop in", "{:,.2f}".format(distance), "feet.")

     elif (function == 4):
          # set flag to true, input is valid
          flag = True
          # quit
          exit()

     else:
          # display error message, ask user to enter valid input
          print("That path does not exist, please choose a menu option 1 to 4.")
