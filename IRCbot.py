# Import some necessary libraries.
import socket, random 

# Some basic variables used to configure the bot        
server = "rizon.mibbit.org" # Server
channel = "#bots" # Channel
botnick = "IRCbot678787859" # Your bots nick

def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def hello(): # This function says hello
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")

def rr(): # Russian Roulette minigame 
  chamber = random.randrange(0,4)
  in_chamber = random.randrange(0,4)
  
  ircsock.send("PRIVMSG " + channel + " :*whirrrr*\n")

  if chamber == in_chamber:
      ircsock.send("PRIVMSG " + channel + " :*BANG*\n")
      ircsock.send("PRIVMSG " + channel + " :Hey, who put a blank in here??\n")

  else:
      ircsock.send("PRIVMSG " + channel + " :*click*\n")

def tough():
  ircsock.send("PRIVMSG " + channel + " :Fite me irl\n")

def help():
  ircsock.send("PRIVMSG " + channel + " :You think this crappy bot has documentation?\n")

#		Spam function I'll be working out later
#def spam():
#  ircsock.send("PRIVMSG " + channel + " :Leave my poor bot alone please\n")

def salute(): #Salutes
  ircsock.send("PRIVMSG " + channel + " :;_;7\n")

def pig_latin(original): #Pig latin translator
  pyg = 'ay'

  if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first == ('a' or 'e' or 'i' or 'o' or 'u'):
      new_word = word + pyg
      ircsock.send("PRIVMSG " + channel + " " + new_word + "\n")
    else:
      new_word = word[1:] + word[0] + pyg
      ircsock.send("PRIVMSG " + channel + " " + new_word + "\n")
  else:
    ircsock.send("PRIVMSG " + channel + " :Invalid Input\n")
                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :lolno\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

joinchan(channel) # Join the channel using the functions we previously defined

while 1: # Be careful with these! it might send you to an infinite loop
  ircmsg = ircsock.recv(2048) # receive data from the server
  ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
  print(ircmsg) # Here we print what's coming from the server

  if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
    ping()

  if ircmsg.find("PRIVMSG " + channel + " :hello " + botnick) != -1: #Looking for "hello IRCbot"
    hello() 

  if ircmsg.find("PRIVMSG " + channel + " :!tough") != -1: #Looking for !tough command
    tough()
  
  if ircmsg.find("PRIVMSG " + channel + " :!help") != -1: #Looking for the !help command
    help()

  if ircmsg.find("PRIVMSG " + channel + " :!salute") != -1: #Looking for salute command
    salute()

  if ircmsg.find("PRIVMSG " + channel + " :!rr") != -1: #Looking for the !rr command
    rr()

  if ircmsg.find("PRIVMSG " + channel + " :!def ") != -1: #looking for !def command
    def_word_start_pos = ircmsg.find("!def") #setting def_word_start_pos to the !'s location
    def_word = ircmsg[def_word_start_pos + 5:] #Grabbing everthing (besides the space) after the !def
    ircsock.send("PRIVMSG " + channel + " :https://duckduckgo.com/?q=define+" + def_word + "\n") #Makes the bot 'say' the DDG define goodie's URL
  
  if ircmsg.find("PRIVMSG " + channel + " :!pl ") != -1: #Looking for the !pl command
    pig_word_start_pos = ircmsg.find("!pl ") #Finding the word to be 'translated' and making it usable by the pig_lattin function
    pig_word = ircmsg[pig_word_start_pos + 4:]
    original = pig_word 
    pig_latin(pig_word)
