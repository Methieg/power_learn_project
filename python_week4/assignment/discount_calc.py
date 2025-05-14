def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage to apply.

  Returns:
    The final price after the discount, or the original price if the discount is less than 20%.
  """
  if discount_percent >= 20:
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Get user input
while True:
    try:
        original_price = float(input("Enter the original price of the item: "))
        if original_price >= 0:
            break
        else:
            print("Price cannot be negative. Please enter a valid price.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the price.")

while True:
    try:
        discount = float(input("Enter the discount percentage: "))
        if 0 <= discount <= 100:
            break
        else:
            print("Discount percentage must be between 0 and 100. Please enter a valid percentage.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the discount percentage.")

# Calculate the final price
final_price = calculate_discount(original_price, discount)

# Print the result
if final_price == original_price:
    print(f"No discount applied. The final price is: ${original_price:.2f}")
else:
    print(f"The final price after the discount is: ${final_price:.2f}")
