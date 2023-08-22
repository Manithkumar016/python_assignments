# 1) Write a python class to convert an integer into a roman numeral and viceversa

class RomanConverter:
    def __init__(self):
        self.val_to_symbol = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        self.symbol_to_val = {v: k for k, v in self.val_to_symbol.items()}

    def int_to_roman(self, num):
        roman_numeral = ''
        for val, symbol in self.val_to_symbol.items():
            while num >= val:
                roman_numeral += symbol
                num -= val
        return roman_numeral

    def roman_to_int(self, roman):
        num = 0
        i = 0
        while i<len(roman):
            if i==len(roman)-1:
                num+=self.symbol_to_val[roman[i]]
                break
            elif roman[i]+roman[i+1] in self.symbol_to_val:
                num+=self.symbol_to_val[roman[i]+roman[i+1]]
                i+=2
            else:
                num+=self.symbol_to_val[roman[i]]
                i+=1
        return num


# Example usage
converter = RomanConverter()

num = 7654

print(converter.int_to_roman(num))

roman = "MMMMMMMDCLIV"
print(converter.roman_to_int(roman))


