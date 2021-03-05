def bowel():

   f = open("quotes.txt")
   quotes = f.readlines()
   #f.write("\n crazy stuff")
   f.close()

   print(quotes[4])
   print('\n')
   print(quotes[14])

if __name__== "__main__":
  bowel()
