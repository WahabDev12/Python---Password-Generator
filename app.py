
from flask import Flask,url_for,render_template,request
import string,random
from random import randint

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST","GET"])
def generatePassword():
    if request.method == "POST":
        # The result variable will contain the generated password
        result = ""
        # Getting the number entered to input field
        #The input field contains the length of the password to be generate
        password_length = request.form["length"]
        # Looping through the password length
        for num in range(int(password_length)):
            # Searches for random characters within the given range
            random_char = randint(10,94)
            #Appends character to the result variable
            result += string.printable[random_char]
            # Rendering our template and instantiating our result variable to it
        return render_template("index.html", result = result)
    else:
        return render_template("index.html")


        

if __name__ == "__main__":
    app.run(debug = True)



# TESTING MY THEORY

#import random, string

#def generatePassword(num):
   # password = ""

  #  for n in range(num):
  #      x = random.randint(10,94)
  #      password += string.printable[x]

 #   return password
#print(generatePassword(16))