def mask_credit_card(card_number):
    # Extract the last 4 digits
    last_four = card_number[-4:]
    # Create a mask of 12 asterisks
    masked_part = '*' *( len(card_number)-4)
    # Concatenate the masked part with the last 4 digits
    masked_card_number = masked_part + last_four
    return masked_card_number

# Example usage
card_number = "1234567812345678"
print(mask_credit_card(card_number))  # Output: ************5678