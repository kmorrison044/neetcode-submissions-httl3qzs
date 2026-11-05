class Solution:
    def reverse(self, x: int) -> int:
        # Max signed 32 bit int
        max_int = 0x7FFFFFFF
        # Min signed 32 bit int
        min_int = -0x7FFFFFFF - 1
        # Our output
        res = 0

        # Loop until x == 0, since we are continuously taking digits from x to 
        # evaluate
        while x != 0:
            # grab the last digit in the number via modding by 10 (123 % 10 == 3)
            # We use this function since python handles negative number mods wierdly.
            digit = int(math.fmod(x, 10))
            # To get the remaining number after grabbing the last digit, we simply
            # integer divide by 12 (123 // 10 == 12). We use the int(a / b) method 
            # because again python handles integer division with negative numbers
            # wierdly.
            x = int(x / 10)
            # To find out if the number will be within the appropriate range, check if
            # res is currently valid up to the last digit. If it is, or exactly valid up
            # to the last digit (i.e. // 10), then check if the digit is greater than
            # the last digit in the max value to determine if it is inbound (less than
            # the min value for the other direction)
            if res > max_int // 10 or (res == max_int // 10 and digit > max_int % 10):
                return 0
            if res < min_int // 10 or (res == min_int // 10 and digit < min_int % 10):
                return 0
            
            # If the result will be valid at this turn, add the new digit to the result
            # via the below function (lets say you wanted to add 3 to 12, then 12 * 10
            # is 120 + 3 is 123)
            res = (res * 10) + digit
        
        # Return res once we break out of the loop.
        return res
