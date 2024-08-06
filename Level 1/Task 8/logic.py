# Calculating the average cost for each term including the fee for extra subjects and the percentage that fees increase excluding extra subjects.

# Declaring cost of each term
term1 = "10000"
term2 = "10500"
term3 = "11000"
term4 = "11500"

# Declaring annual cost of extra subjectes 
extra_sub = 4800.00

# Calculating sum of annual school fees
total_cost = int(term1) + int(term2) + int(term3) + int(term4) + extra_sub
avg_fee = total_cost / 5 # Logical error: average fees should be divided by 4 as there are only four terms in one year
perc_inc = (int(term4) - int(term1)) / int(term1) * 100

# Printing the average fees per term and stating the percentage that fees increase per term excluding the cost of extra subjects
print("The average cost of school fees per term is: " + "R" + str(avg_fee) + ". " + "Your fees will increase by: " + str(perc_inc) + "% per term, excluding extra subjects. ")
print("Kids are expensive!")

