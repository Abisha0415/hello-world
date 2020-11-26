#IF STATEMENTS QUESTIONS 
print("Question 34: Even or Odd?")
#Write a program that reads an integer from the user. Then your program should #display a message indicting is even or odd.
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))



print("Print 35:Dog Years ")
#It  is  commonly  said  that  one  human  year  is  equivalent  to  7  dog  years.  However  this simple  conversion  fails  to  recognize  that  dogs  reach  adulthood  in  approximately  two years.  As  a  result, some  people  believe  that  it  is  better  to  count  each  of  the  ﬁrst  two human  years  as  10.5  dog  years, and  then  count  each  additional  human  year  as  4  dog years. 
h_age = int(input("Input a dog's age in human years: "))

if h_age < 0:
	print("Age must be positive number.")
	exit()
elif h_age <= 2:
	d_age = h_age * 10.5
else:
	d_age = 21 + (h_age - 2)*4

print("The dog's age in dog's years is", d_age)



print("Exercise  36:Vowel  or  Consonant")
#In  this  exercise  you  will  create  a  program  that  reads  a  letter  of  the  alphabet  from  the user.  If  the  user  enters a, e, i, o or u then  your  program  should  display  a  message indicating  that  the  entered  letter  is  a  vowel.  If  the  user  enters y then  your  program should  display  a  message  indicating  that  sometimes  y  is  a  vowel, and  sometimes  y  is a  consonant.  Otherwise  your  program  should  display  a  message  indicating  that  the letter  is  a  consonant. 
l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
	print("%s is a consonant." % l) 



print("Exercise  37:Name  that  Shape ")
#Write  a  program  that  determines  the  name  of  a  shape  from  its  number  of  sides.  Read the  number  of  sides  from  the  user  and  then  report  the  appropriate  name  as  part  of a  meaningful  message.  Your  program  should  support  shapes  with  anywhere  from  3 up  to  (and  including)  10  sides.  If  a  number  of  sides  outside  of  this  range  is  entered then  your  program  should  display  an  appropriate  error  message. 
numSides=int(input("How many sides in the shape: "))
geometry = {
    3: "The shape is a triangle.",
    4: "The shape is a quadrilateral.",
    5: "The shape is a pentagon.",
    6: "The shape is a hexagon.",
    7: "The shape is a heptagon.",
    8: "The shape is a octagon.",
    9: "The shape is a nonagon.",
    10: "The shape is a decagon.",
    11: "The shape is a hendecagon.",
    12: "The shape is a dodecagon.",
    13: "The shape is a triskaidecagon",
    14: "The shape is a tetradecagon",
    15: "The shape is a pentadecagon",
}
if numSides == 3:
  print(geometry[3])
elif numSides == 4:
  print(geometry[4])
elif numSides == 5:
  print(geometry[5])
elif numSides == 6:
  print(geometry[6])
elif numSides == 7:
  print(geometry[7])
elif numSides == 8:
  print(geometry[8])
elif numSides == 9:
  print(geometry[9])
elif numSides == 10:
  print(geometry[10])
elif numSides == 11:
  print(geometry[11])
elif numSides == 12:
  print(geometry[12])
elif numSides == 13:
  print(geometry[13])
elif numSides == 14:
  print(geometry[14])
elif numSides == 15:
  print(geometry[15])
else:
  print("Error, sides must be in between 3 and 15. Please try again.")



print("Exercise  38:Month  Name  to  Number  of  Days")
#The  length  of  a  month  varies  from  28  to  31  days.  In  this  exercise  you  will  create a  program  that  reads  the  name  of  a  month  from  the  user  as  a  string.  Then  your program  should  display  the  number  of  days  in  that  month.  Display  “28  or  29  days” for  February  so  that  leap  years  are  addressed. 
month = input("Enter a month").lower()
if month == "january" or month == "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":print("31 days")
elif month in ["april", "june", "september", "november"]:print("30 days")
elif month == "february":print("28 or 29 days")
else:print("Not a month!")



print("Exercise  39:Sound  Levels")
#The  following  table  lists  the  sound  level  in  decibels  for  several  common  noises. Write  a  program  that  reads  a  sound  level  in  decibels  from  the  user.  If  the  user enters  a  decibel  level  that  matches  one  of  the  noises  in  the  table  then  your  program should  display  a  message  containing  only  that  noise.  If  the  user  enters  a  number of  decibels  between  the  noises  listed  then  your  program  should  display  a  message indicating  which  noises  the  level  is  between.  Ensure  that  your  program  also  generates reasonable  output  for  a  value  smaller  than  the  quietest  noise  in  the  table, and  for  a value  larger  than  the  loudest  noise  in  the  table. 
decibels = float(input("Enter the number of decibels: "))
	
if decibels > 0 and decibels < 40:
    print('quieter than a quiet room.')
		
elif decibels == 40:
    print('about the same as a quiet room.')
	
elif decibels > 40 and decibels < 70:
    print('quieter than an alarm clock.')
elif decibels == 70:
    print('about the same as an alarm clock.')
		
elif decibels > 70 and decibels < 106:
    print('quieter than a lawn mower.')
	
elif decibels == 106:
    ('about the same as a lawn mower.')
	
elif decibels > 106 and decibels < 130:
    print(" quieter than a jackhammer.")
		
elif decibels == 130:
    print('about the same as a jackhammer.')
		
elif decibels > 130:
    print('way too loud.')
		
else:
    print('Please enter a correct data value.')
		
    print('Your sound level is')



print("Exercise  40:Name that Triangle")
#A  triangle  can  be  classiﬁed  based  on  the  lengths  of  its  sides  as  equilateral, isosceles or  scalene.  All  3  sides  of  an  equilateral  triangle  have  the  same  length.  An  isosceles triangle  has  two  sides  that  are  the  same  length, and  a  third  side  that  is  a  different length.  If  all  of  the  sides  have  different  lengths  then  the  triangle  is  scalene. Write  a  program  that  reads  the  lengths  of  3  sides  of  a  triangle  from  the  user. Display  a  message  indicating  the  type  of  the  triangle. 
print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
	print("Equilateral triangle")
elif x==y or y==z or z==x:
	print("isosceles triangle")
else:
	print("Scalene triangle")



print("Exercise 43: Faces  on  Money")
#Write  a  program  that  begins  by  reading  the  denomination  of  a  banknote  from  the user.  Then  your  program  should  display  the  name  of  the  individual  that  appears  on  the banknote  of  the  entered  amount.  An  appropriate  error  message  should  be  displayed if  no  such  note  exists. 
def main():
    notes = {"1"  : "George Washinton",
             "2"  : "Thomas Jefferson",
             "5"  : "Abraham Lincoln",
             "10" : "Alexander Hamilton",
             "20" : "Andrew Jackson",
             "50" : "Ulysses S. Grant",
             "100": "Benjamin Franklin"}
     
    value = input("Please enter the value of an US dollar note: ")
    if value not in notes:
        print("Sorry that is not a valid US dollar note")
    else:
        print("On that note you will find", notes[value])
 
            
if __name__ == '__main__':
    main()



print("Question 44: Date to Holiday Name")
#Write  a  program  that  reads  a  month  and  day  from  the  user.  If  the  month  and  day match  one  of  the  holidays  listed  previously  then  your  program  should  display  the holiday’s  name.  Otherwise  your  program  should  indicate  that  the  entered  month  and day  do  not  correspond  to  a  ﬁxed-date  holiday. 
month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

if month in ('January', 'February', 'March'):
	season = 'winter'
elif month in ('April', 'May', 'June'):
	season = 'spring'
elif month in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

if (month == 'March') and (day > 19):
	season = 'spring'
elif (month == 'June') and (day > 20):
	season = 'summer'
elif (month == 'September') and (day > 21):
	season = 'autumn'
elif (month == 'December') and (day > 20):
	season = 'winter'

print("Season is",season)



print("Exercise 47: Birth Date to Astrological Sign")
#Write  a  program  that  asks  the  user  to  enter  his  or  her  month  and  day  of  birth.  Then your  program  should  report  the  user’s  zodiac  sign  as  part  of  an  appropriate  output message. 
day = int(input("Input birthday: "))
month = input("Input month of birth (e.g. march, july etc): ")
if month == 'december':
	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'march':
	astro_sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'april':
	astro_sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
	astro_sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'june':
	astro_sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'july':
	astro_sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'august':
	astro_sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'september':
	astro_sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'october':
	astro_sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'november':
	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
print("Your Astrological sign is :",astro_sign)




#CODINGBAT PYTHON STRING-1 QUESTIONS 
def hello_name(name):
  return "Hello " + name + "!"

def make_abba(a, b):
  return a+2*b+a

def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"

def make_out_word(out, word):
  return out[:2] + word + out[2:]

def extra_end(str):
  return str[-2:]*3

def first_two(str):
  return str if len(str)<=2 else str[:2]

def first_half(str):
  return str[:len(str)/2]

def without_end(str):
  return str[1:-1]

def combo_string(a, b):
  return a+b+a if len(a)<len(b) else b+a+b

def non_start(a, b):
  return a[1:]+b[1:]

def left2(str):
  return str[2:]+str[:2]
