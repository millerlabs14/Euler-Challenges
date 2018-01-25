#Project Euler Challenge: #002
#Don't quite understand math in this one...

def largest_prime_factor(target):
   #0. Declare variables
   potential_factor = 2
   prime_factors = []
   
   #1. Determine prime factors of num
   while target > 1:
      if target % potential_factor == 0:
         prime_factors.append(potential_factor)
         target = target/potential_factor
      else:
         potential_factor += 1
   print("Prime factors: ", prime_factors)
   
   #2. Find largest from remaining numbers
   return max(prime_factors)

print("Largest Prime: ", largest_prime_factor(600851475143))
