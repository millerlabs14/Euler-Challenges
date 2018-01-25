#Project Euler Challenge: #002

def main():
   #0. Declare variables
   fib_list_all = [1,2]
   num = 0
   i = 0
   total = 0
   
   #1. Generate Fibonacci sequence below 4 million
   while True:
      num = fib_list_all[i] + fib_list_all[i+1]
      i += 1
      if num < 4000000:
         fib_list_all.append(num)
      else:
         break
      
   #2. Filter out odd values
   fib_list_even = [x for x in fib_list_all if x%2 == 0]
   
   #3. Sum remaining numbers
   for num in fib_list_even:
      total += num

   print("Total: ", total)


main()
