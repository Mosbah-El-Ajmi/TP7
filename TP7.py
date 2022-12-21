import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : Mosbah El-Ajmi
    Date : December 2022
    This class allows fraction manipulations through several operations.
    """

    def __init__(self,num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num and den are integers
        POST : a fraction object is created, it has a numerator and a denominator, and it's reduced
        Raise : Exception if den = 0 or TypeError if num and den are not real number
        """
        if den == 0:
            raise ValueError("the denominator must not be zero!")
        try:
            self.num = int(num)
            self.den = int(den)
            self.reduce()
        except ValueError:
            print("The numerator and denominator values must be integers!")

    @property
    def numerator(self):
        return self.num

    @property
    def denominator(self):
        return self.den

    def reduce(self):
        """Return a reduced version of the fraction

        PRE : a Fraction object
        POST : return a string representing of the reduced fraction
        """
        if self.numerator < 0 and self.denominator < 0:
            self.num = -self.numerator
            self.den = -self.denominator
        elif self.numerator < 0:
            self.num = -self.numerator

        gcd = math.gcd(self.numerator, self.denominator)
        self.num = self.numerator // gcd
        self.den = self.denominator // gcd

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : a Fraction object
        POST : returns a string representing the fraction
        """
        if self.numerator == self.denominator:
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : a Fraction object
        POST : returns a string representing the reduced fraction as a mixed number (integer + proper fraction), 
        or as a proper fraction if the integer is 0
        """
        integer_part = self.numerator // self.denominator
        fractional_part = Fraction(self.numerator % self.denominator, self.denominator)
        if integer_part == 0:
            return str(fractional_part)
        elif fractional_part.is_zero():
            return str(integer_part)
        else:
            return f"{integer_part} {str(fractional_part)}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

        PRE : other is a Fraction object
        POST : returns an object of the Fraction class representing the result of the addition between self and other
        """
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : other is a Fraction object
        POST : returns an object of the Fraction class representing the result of the substraction between self and other
        """
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : other is a Fraction object
        POST : returns an object of the Fraction class representing the result of the multiplication between self and other
        """
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other is a Fraction object
        POST : returns an object of the Fraction class representing the result of the division between self and other
        """
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other is a Fraction object
        POST : returns an object of the Fraction class representing the result of the power between self and other
        """
        num = (self.numerator ** (other.numerator / other.denominator)).real
        den = (self.denominator **
               (other.numerator / other.denominator)).real
        if num < 0 and den < 0:
            num = -1 * num
            den = -1 * den

        return Fraction(num, den)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other is a Fraction object
        POST : return True if self and the other are equals, False otherwise
        """
        self_reduced = Fraction(self.numerator, self.denominator)
        other_reduced = Fraction(other.numerator, other.denominator)
        return (self_reduced.numerator == other_reduced.numerator) and (
                    self_reduced.denominator == other_reduced.denominator)

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : a Fraction object
        POST : Return decimal value of an object Fraction
        """
        return round(self.numerator / self.denominator, 2)

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : a Fraction object
        POST : return True if the value of the zero is equal 0
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : a Fraction object
        POST : return true if the Fraction is integer (its numerator is divisible by the denominator)
        False otherwise
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : a Fraction object
        POST : return True if the absolute value of the fraction is <1 
        """
        return abs(self.numerator / self.denominator) < 1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : a Fraction object
        POST : return True if the numerator of the reduced fraction is equal 1
        """
        reduced_fraction = Fraction(self.numerator, self.denominator)
        return reduced_fraction.numerator == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : other is a Fraction object
        POST : return True if self and other are adjacent fractions 
        (i.e. if the absolute value of the difference between self and other is equal to a unit fraction)
        """
        difference = self - other
        reduced_difference = Fraction(difference.numerator, difference.denominator)
        return reduced_difference.is_unit()

if __name__ == "__main__":
    try:
        f = Fraction(-2, -3)
        fraction7 = Fraction(524, 124.58)
        fraction8 = Fraction(18, 57.5)
        fraction9 = Fraction(47.2, -9)
        fraction10 = Fraction(-1.2, 3.6)
        fraction0 = Fraction(1, 2)
        fraction01 = Fraction(10, 23)
        fraction1 = Fraction(45.35654, 12.4214)
        fraction2 = Fraction(15.3, 102.8)
        fraction3 = Fraction(-87, -87)
        fraction6 = Fraction(17.4, 17.4)
        print(fraction6==fraction3)
        print(fraction6)
        print(fraction3)
    except ValueError as error:
        print(error)
