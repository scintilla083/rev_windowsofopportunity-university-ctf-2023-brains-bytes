# on adress 0x4060
hex_string = "9c96bdaf93c39460a2d1c2cf9ca3a66894c1d7ac969393d6a89fd294a7d68fa0a3a1a3569e"

hex_pairs = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

decimal_values = [int(pair, 16) for pair in hex_pairs]

print(decimal_values)
