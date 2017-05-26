
first_term=1
no_of_terms= input("Enter number of terms to be generated")

output_array=first_term

new_term= first_term
previous_term = first_term

for i in range(0,no_of_terms):
    output_array= [ output_array, new_term ]
    temp= new_term
    new_term= new_term + previous_term
    previous_term = temp

print(output_array)



