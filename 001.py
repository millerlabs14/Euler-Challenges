#Project Euler Challenge: #001

def main():
   max_num = 1000
   total = 0

   for i in range(max_num):
      if i%3 ==0 or i%5 == 0:
         total += i

   print("Total: ", total)



main()
