############################################
#### IMPORTS:                           ####
############################################
from sys import exit
from datetime import datetime



############################################
#### FUNCTIONS:                         ####
############################################

###############
### FUNCTION 1: Investment Portfolio Options ###
###############

def investing_service():

    # User questions
    user_age = str("\nHow old are you?:\t") ### user prompt (up)!
    user_health = str("\nWould you rate your health as bad, normal, good or very good?") ###up
    user_nworth = str("\nWhat's your net worth? Enter the number without commas (e.g. 280000):\t") ###up
    user_income = str("\nWhat are your current income levels? Enter the number without commas (e.g. 280000):\t") ###up
    user_invexp = str("\nDo you have investment experience? Answer 'yes', 'no' or 'just savings':")###
    user_scenario = str("""\nIf you invested 1 million, you would want...\t
                                        \na) to earn the minimum so as to not lose anything.
                                        \nb) to earn 100k, being able to lose 20k.
                                        \nc) to earn 300k, being able to lose 150k.
                                        \nd) to earn 400k, being able to lose 250k.
                                        \n\n Please enter 'a', 'b', 'c' or 'd':\t
                                        """)###
    user_lifesave = str("\nHow much have you managed to save in your life? Enter the number without commas (e.g. 280000):\t")###
    user_flip = str("\nHeads, you win $200k. Tails, you lose $100k. Would you play once? Answer 'yes' or 'no':\t")###
    user_flip2 = str("\nIf the odds remained the same (win $200k or lose $100k), would you play 100 times? Answer 'yes' or 'no':\t")###
    user_scenario2 = str("""\nIf you lost 5% of your investment in a month due to a crisis, what would you do?\t
                                        \na) hold.
                                        \nb) sell a part of my investments.
                                        \nc) sell all my investments.
                                        \nd) invest more.
                                        \n\n Please enter 'a', 'b', 'c' or 'd':\t
                                        """)###
    user_monthsave = str("\nHow much can you save per month? Enter the number without commas (e.g. 280000):\t")###
    user_monthly = str("\nDo you want to invest every month? Answer 'yes' or 'no':")###
    user_timehold = str("""\nHow long would you hold an investment for?\t
                                        \na) less than 6 months.
                                        \nb) 1 or 2 years.
                                        \nc) more than 3 years.
                                        \nd) more than 10 years.
                                        \n\n Please enter 'a', 'b', 'c' or 'd':\t
                                        """)###
    user_esg = str("\nAre you interested in the idea of investing in green funds (responsible future)? Answer 'yes' or 'no':")###


    # Calculating user risk aversion
    user_sum = 0
    ## user_age
    if int(user_age) < 70:
        user_sum += 4
    elif user_age > 69 and user_age < 80:
        user_sum += 3
    elif user_age > 79 and user_age < 90:
        user_sum += 2
    elif user_age > 89:
        user_sum =+ 1
    else:
        print("Something went wrong at the user_age points computation stage.")

    ## user_health
    if user_health.lower() == "very good":
        user_sum += 4
    elif user_health.lower() == "good":
        user_sum += 3
    elif user_health.lower() == "normal":
        user_sum += 2
    elif user_health.lower() == "bad":
        user_sum =+ 1
    else:
        print("Something went wrong at the user_health points computation stage.")

    ## user_nworth
    if user_nworth >= 1000000:
        user_sum += 4
    elif user_nworth < 1000000:
        user_sum += 3
    elif user_nworth < 500000:
        user_sum += 2
    elif user_nworth < 100000:
        user_sum =+ 1
    else:
        print("Something went wrong at the user_nworth points computation stage.")

    ## user_income
    if user_income >= 100000:
        user_sum += 4
    elif user_income < 100000 and user_income > 50000:
        user_sum += 2.5
    elif user_income < 50000:
        user_sum =+ 1
    else:
        print("Something went wrong at the user_income points computation stage.")

    ## user_invexp
    if user_invexp.lower() == "yes":
        user_sum += 4
    elif user_invexp.lower() == "no":
        user_sum += 2
    elif user_invexp.lower() == "just savings" or user_invexp == "savings":
        user_sum =+ 1
    else:
        print("Something went wrong at the user_invexp points computation stage.")
    
    ## user_scenario
    if user_scenario.lower() == "a":
        user_sum += 1
    elif user_scenario.lower() == "b":
        user_sum += 2
    elif user_scenario.lower() == "c":
        user_sum += 3
    elif user_scenario.lower() == "d":
        user_sum =+ 4
    else:
        print("Something went wrong at the user_scenario points computation stage.")
    
    ## user_lifesave
    if user_lifesave <= 1000:
        user_sum += 1
    elif user_lifesave > 1000 and user_lifesave <= 10000:
        user_sum += 1.5
    elif user_lifesave > 10000 and user_lifesave <= 100000:
        user_sum += 2.5
    elif user_lifesave > 100000 and user_lifesave < 500000:
        user_sum =+ 3.5
    elif user_lifesave >= 500000:
        user_sum =+ 4
    else:
        print("Something went wrong at the user_lifesave points computation stage.")
    
    ## user_flip
    if user_flip.lower() == "yes":
        user_sum += 4
    elif user_flip.lower() == "no":
        user_sum += 1
    else:
        print("Something went wrong at the user_flip points computation stage.")
    
    ## user_flip2
    if user_flip2.lower() == "yes":
        user_sum += 4
    elif user_flip2.lower() == "no":
        user_sum += 1
    else:
        print("Something went wrong at the user_flip2 points computation stage.")
    
    ## user_scenario2
    if user_scenario2.lower() == "a":
        user_sum += 3
    elif user_scenario2.lower() == "b":
        user_sum += 2
    elif user_scenario2.lower() == "c":
        user_sum += 1
    elif user_scenario2.lower() == "d":
        user_sum =+ 4
    else:
        print("Something went wrong at the user_scenario2 points computation stage.")
    
    ## user_monthsave
    if user_monthsave == 0:
        user_sum += 1
    elif user_monthsave < 1000:
        user_sum += 2
    elif user_monthsave <= 2500:
        user_sum += 3
    elif user_monthsave > 2500:
        user_sum =+ 4
    else:
        print("Something went wrong at the user_monthsave points computation stage.")
    
    ## computing total risk aversion score as user_score
    user_score = user_sum/11


    # Redirecting user to selected portfolio (user_score, ESG)
    def show_portfolio(user_score, user_esg):

        # high risk aversion (1-1.6)
        if user_score <= 1.6 and user_esg.lower() == "yes":
            portfolio_1 = [] ## NOTE: Need to modify this to SHOW selected portfolio (Philipp's part)
        elif user_score <= 1.6 and user_esg.lower() == "no":
            portfolio_2 = []
        
        # moderate risk aversion (1.6-2.2)
        elif user_score > 1.6 and user_score <= 2.2 and user_esg.lower() == "yes":
            portfolio_3 = []
        elif user_score > 1.6 and user_score <= 2.2 and user_esg.lower() == "no":
            portfolio_4 = []
        
        # low risk aversion (2.2-2.8)
        elif user_score > 2.2 and user_score <= 2.8 and user_esg.lower() == "yes":
            portfolio_5 = []
        elif user_score > 2.2 and user_score <= 2.8 and user_esg.lower() == "no":
            portfolio_6 = []
        
        # risk neutral (2.8-3.4)
        elif user_score > 2.8 and user_score <= 3.4 and user_esg.lower() == "yes":
            portfolio_7 = []
        elif user_score > 2.8 and user_score <= 3.4 and user_esg.lower() == "no":
            portfolio_8 = []
        
        # risk lover (3.4-4)
        elif user_score > 3.4 and user_score <= 4 and user_esg.lower() == "yes":
            portfolio_9 = []
        elif user_score > 3.4 and user_score <= 4 and user_esg.lower() == "no":
            portfolio_10 = []
    
    # Calling function to show selected portfolio
    show_portfolio(user_score, user_esg)



###############
### FUNCTION 2: Inheritance Plan ### NILESH, SKIP THIS PART BECAUSE I'M STILL WORKING ON THIS PART
###############

def inheritance_plan():

    # user inputs
    user_age = str("\nHow old are you?\t") ###up
    user_inheritance = str("\nHow much would you like to pass on to younger generations (inheritance)?\t")###up
    # user_state = str("\nWhich American state do you reside in?\t")###up - DEMO (for real app would have to code tax_on_inh per state)
    user_relationship = str("\nWhat is the relationship of the person to inherit the money to you?\t") ###up

    # set state-set variables
    # max_tax_free_amount = 3000 # set by US government, example, max/year
    # avg_life_exp =  77.8 # in US currently
    tax_on_inh =  [] # in US currently

    # calculating tax_in_inh
    if user_relationship == "daughter" or user_relationship == "son":
        tax_on_inh.append(0.045)
    elif user_relationship == "spouse" or user_relationship == "wife" or user_relationship == "husband":
        tax_on_inh.append(0)
    elif user_relationship == "sibling" or user_relationship == "sister" or user_relationship == "brother":
        tax_on_inh.append(0.12)
    else:
        tax_on_inh.append(0.15) 
    
    # set arithmetic variables
    years_to_pay = (77.8 - int(user_age))
    payments_as_max = int(user_inheritance)/3000
    years_with_tax = payments_as_max - years_to_pay
    taxable_inh = years_with_tax*3000
    tax_on_inh = taxable_inh * tax_on_inh

    
    print(f"""
    To minimize the tax payable on your inheritace you should pay $3000 
    for {years_to_pay} years, when you will reach the age of 77.8.

    You'll have ${taxable_inh} left to pay then, with a tax payable of {tax_on_inh}.
    """)



###############
### FUNCTION 3: App Launch ###
###############

def app_start():
    global user_name

    # Getting user name
    print("Welcome to your personalized investment service.")
    user_name = str("\nPlease enter your name:\t")###

    # Finding service to be provided during this visit to the app
    print(f"Hello, {user_name}.")
    service_choice = str("\nWould you like to manage your investments or your inheritance?\t").lower()###

    if service_choice == "investments":
        investing_service()
    # elif service_choice == "inheritance":
    #     inheritance_plan()
    else:
        service_choice = str("\nChoose between 'investments' or 'inheritance':\t")###




