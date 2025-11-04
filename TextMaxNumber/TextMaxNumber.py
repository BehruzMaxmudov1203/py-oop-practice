class TextMaxNumber:
    @staticmethod
    def get_max_number(text: str) -> int | None:
        """
        Finds the largest positive number in the text.
        Returns None if no number exists.
        """
        number = ""
        max_number = None

        for char in text:
            if char.isdigit():
                number += char
            else:
                if number:
                    num = int(number)
                    if max_number is None or num > max_number:
                        max_number = num
                    number = ""
        # Check if last number at end of text
        if number:
            num = int(number)
            if max_number is None or num > max_number:
                max_number = num

        return max_number


# ===== Test code =====
def check_test(result, expected):
    if result != expected:
        raise ArithmeticError(f"Test failed: result={result}, expected={expected}")
    else:
        print("✅ Test passed")


if __name__ == "__main__":
    check_test(TextMaxNumber.get_max_number("Hello today the weather is good"), None)
    check_test(TextMaxNumber.get_max_number("Today 15-Jan. Temperature 20 degrees."), 20)
    check_test(TextMaxNumber.get_max_number("Today is 15.01.2021."), 2021)
    check_test(TextMaxNumber.get_max_number("In 1991 we became independent."), 1991)
    check_test(TextMaxNumber.get_max_number("-20 and 5"), 20)
    check_test(TextMaxNumber.get_max_number("15"), 15)
    check_test(TextMaxNumber.get_max_number("00200"), 200)
