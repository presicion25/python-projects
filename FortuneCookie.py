import random 

lucky_number = random.randint(1,500) 

fortune_number = random.randint(1,20)

fortune_text = ''

if fortune_number == 1:
  fortune_text = 'You will win a car today!'
if fortune_number == 2:
  fortune_text = 'You will have a good day!'
if fortune_number == 3:
  fortune_text = 'You will get lucky today!'
if fortune_number == 4:
  fortune_text = 'You will win a trip today!'
if fortune_number == 5:
  fortune_text = 'You will find a job today!'
if fortune_number == 6:
  fortune_text = 'You will gain some new friends today!'
if fortune_number == 7:
  fortune_text = 'You can do anything!'
if fortune_number == 8:
  fortune_text = 'Your life is great!'
if fortune_number == 9:
  fortune_text = 'The FBI will find you!'
if fortune_number == 10:
  fortune_text = 'You will live forever!'
if fortune_number == 11:
  fortune_text = 'The CIA is watching!'
if fortune_number == 12:
  fortune_text = 'Welcome to your life!'
if fortune_number == 13:
  fortune_text = 'The NSA knows your moves!'
if fortune_number == 14:
  fortune_text = 'The key to life is adapting!' 
if fortune_number == 15:
  fortune_text = 'Count your blessings!'
if fortune_number == 16:
  fortune_text = 'You will go far in life!'
if fortune_number == 17:
  fortune_text = 'Your days will be filled with love!'
if fortune_number == 18:
  fortune_text = 'Never give up!'
if fortune_number == 19:
  fortune_text = 'Your perseverance will pay off!'
if fortune_number == 20:
  fortune_text = 'Never forget where you came from!'

print(f'{fortune_text} Your Lucky Number is: {lucky_number}')