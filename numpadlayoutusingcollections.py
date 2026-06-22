calculator_numpad = (("1", "2", "3"),
                    ("4", "5", "6"),
                    ("7", "8", "9"),
                    ("#", "/", "*"))

for nums in calculator_numpad:
    for digits in nums:
        print(digits, end=" ")
    print()