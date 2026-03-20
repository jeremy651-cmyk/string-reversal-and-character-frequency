# NAME: ORENDE JEREMY
# DATE: 20/03/2026
# DESCRIPTION: STRING REVERSAL AND CHERECTER FREQUENCY


# USER INPUT A STRING
text = input("Enter a string: ")

if not text:
    print("Error: Input cannot be empty!")
else:
    print("=== STRING REVERSAL TECHNIQUES ===")

    # Method 1: Slicing 
    slicing1 = text[::-1]
    print("slicing method:", slicing1)

    # Method 2: Using loop
    loop2 = ""
    for ch in text:
        loop2 = ch + loop2
    print("Loop method:", loop2)

    # CHARACTER FREQUENCY
    print("=== CHARACTER FREQUENCY ===")

    # Method 1: Dictionary 
    freq_dict = {}
    for ch in text:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1

    print("Character | Count")   #displays in a sorted table
    for ch in sorted(freq_dict):
        print(f"   {ch}     :   {freq_dict[ch]}")

    # totals
    print("Total characters:", len(text))
    print("Unique characters:", len(freq_dict))