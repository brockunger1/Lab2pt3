print("Enter number of seconds at the beginning of the year:")
number_of_sec=int(input())
# 1 day=86400
#b=population
Days=(number_of_sec)//86400
Hours=(number_of_sec%86400)//3600
Minutes=(number_of_sec%3600)//60
Seconds=(number_of_sec%3600)%60
total_sec=(6*24*3600)+(12*60*60)+(31*60)+30
Birth=total_sec//7
Death=total_sec//13
Immigrant=total_sec//35
b= Birth+Immigrant + 334205119 - Death
flapjack=(((334205119+350)**2-12)//50)**(1/5)
print("Days :", Days, "Hours: ", "Minutes: ", Minutes, "Seconds: ", Seconds, "After the start of 2022, total population was: ", b)
