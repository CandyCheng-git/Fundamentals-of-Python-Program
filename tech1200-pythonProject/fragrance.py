# Constants
chanel_no5_description = ("""No5, the very essence of femininity. 
                          A powdery floral bouquet housed in an iconic bottle with a minimalist design.""")
chanel_no5_price = 399.99
tom_ford_costa_azzura_description = ("""COSTA AZZURRA PARFUM breathes an air of freshness through crisp Italian lemon, 
                                     while the dense coastal forest is felt with magnified oakwood extract and cypress.""")
tom_ford_costa_azzura_price = 250
dior_miss_dior_description ="""Miss Dior Eau de Parfum reinvents itself 
                 with a new scent."""
dior_miss_dior_price = 319.95
tax = 0.1 #10% tax
customer_one_cost = 0
customer_one_items = ""
customer_total_cost = 0

#customer_one_cost = customer_one_cost + chanel_no5_price
customer_one_cost += chanel_no5_price

#customer_one_items = customer_one_items + dior_miss_dior_description
customer_one_items += dior_miss_dior_description

customer_one_gst = customer_one_cost * tax

#customer_total_cost = customer_total_cost + customer_one_gst
customer_total_cost += customer_one_gst

#FUNCTION
print("Items purchased by Customer One: ")
#print(customer_one_items)
print(str(type(customer_one_items)) + "\t " + customer_one_items)
print("Customer total cost:　")
#print(customer_total_cost)
print(str(type(customer_total_cost)) + "\t " + str(customer_total_cost))


