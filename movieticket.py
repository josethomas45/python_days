import datetime
while True:
 print('Welcome to movie ticket booking system')
 movie=int(input('Enter the movie name:\n1)Intestellar\n2)Inception\n3)The Dark Knight\n4)The Prestige\n5)Dunkirk\n'))
 ticket=int(input("Enter the number of tickets you want to book\n"))
 type=int(input('Enter the type of ticket you want to book\n1)Platinum\n2)normal\n'))
 if type==1:
     price=200
 else:
     price=100
 time=int(input('Enter the show time:\n 1)10:00am\n2)2:00pm\n3)6:00pm\n4)10:00pm\n'))
 date_str = input('Enter the date of the show (YYYY-MM-DD):\n')
 try:
     show_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
 except ValueError:
     print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
     continue
 if ticket > 5:
      price =ticket*price*0.9
 else:
        price =ticket*price

 if movie == 1:
        movie = 'Interstellar'
 elif movie == 2:
        movie = 'Inception'
 elif movie == 3:
        movie = 'The Dark Knight'
 elif movie == 4:
        movie = 'The Prestige'
 elif movie == 5:
        movie = 'Dunkirk'
 else:
        print('Invalid movie selection')
        continue
    
   
 if time == 1:
        time = '10:00am'
 elif time == 2:
        time = '2:00pm'
 elif time == 3:
        time = '6:00pm'
 elif time == 4:
        time = '10:00pm'
 else:
        print('Invalid time selection')
        continue
 
 print(f'The total price of the tickets is {price}\nyour show is {movie}\ntime is {time}\ndate is {show_date.strftime("%Y-%m-%d")}')
 break





