print("Hello user, this program function is to convert units more specifically "
      "kilometers into miles")

while True:

      number_to_convert = float(input("Enter the number of kilometers): "))

      converted_number = number_to_convert*0.621371

      print(str(number_to_convert)+" kilometers is "+str(converted_number)+" miles.")

      answer = str(input("Do you want to do another conversion(Yes/NO): "))

      if (answer.lower() != "yes"):
           print("Goodbye")
           break






