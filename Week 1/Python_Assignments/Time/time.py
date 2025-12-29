'''
Implement a class Time to represent and manipulate quantities of time stored in 
hours (non-negative integer-valued) and minutes (non-negative real-valued).
✅The number of minutes should always be less than 60.

✅The variables, inside the class, storing hours and minutes should be declared private.

✅Implement a constructor taking no argument, meant to initialize the times to 0 hours and 0 minutes.
When this is called, it should print out “Default Constructor called”.

✅Implement a constructor taking two arguments meant to initialize the hours and minutes values.
When this is called, it should print out “Constructor with two arguments called for (hours,minutes)”
where hours and minutes should actually show the values and not letters.

✅Implement the destructor, which should output a message, i.e, when this is called,
it should print out “Destructor called for (hours,minutes)” where hours and minutes should actually show the real values (not the letters).

✅Implement overloaded operators + and - to perform, respectively, addition and subtraction.
If a larger quantity of time is being subtracted from a smaller quantity of time, then the result should be 0 hours and 0 minutes.
The overloaded operators should work when:
both the operands are of the type of the time object;
the second operand is an integer (indicating minutes).

✅Implement overloaded operators * and / to perform multiplication and division with a positive scalar.

✅Implement an overloaded operator = to perform assignment when the right hand side is an object of type Time and also when the right hand side is an integer (indicating minutes).

✅Implement overloaded operators ==, <, > to perform comparisons and return a value of type bool. In this case, the second operand can either be an object of type Time or an integer (indicating minutes).

✅Implement a counter variable (count) within the class that keeps a track of the number of objects that are existing i.e. with memory allocated at any point in the program.

Instructions for usage:

Do not modify the main function, comment out some parts for debugging or testing purposes if needed.

Only modify the class Time in the TODO sections. Remove the pass statement before adding your code.

Run `python3 autograder.py` to check the output of your code.


'''

# Note about count: as i have called Time() many times inside the overloads and definitions of the class too, they can (if they are meant to) exist in memory when stored somewhere. But since the instructions clearly mention they want a count of all Time instances in memory, this seems perfectly fine.

class Time:
	
	count = 0 # static variable to keep track of the number of objects

	def __init__(self, hours=None, minutes=None): # modified the default values so as Time() and Time(0,0) call the 2 different cases, which i think is what is in the spirit of the instructions
		Time.count += 1
		if (hours is None and minutes is None):
			self.__hours, self.__mins = int(0), 0.0
			print("Default Constructor called")
		elif (hours is not None and minutes is not None):
			self.__hours, self.__mins = int(hours), float(minutes)
			print(f"Constructor with two arguments called for ({self.__hours},{self.__mins})")
		else:
			raise ValueError("Arguments provided incorrectly")

		self.__hours, self.__mins = self.__normalize(self.__hours, self.__mins)
		
	def __del__(self):
		Time.count -= 1
		if hasattr(self, "_Time__hours") and hasattr(self, "_Time__mins"): # ik this is kind of cheating first considering them private then using at public, but its here only for safety
			print(f"Destructor called for ({self.__hours},{self.__mins})")
		else:
			print("Destructor called, but initialization wasn't done successfully") # this is the case when the constructor raised the ValueError and values were not initialized, but destructor called while garbage collection

	def __str__(self): # creating a print output based on the expected_output.txt file given
		return f"{self.__hours} hours, {self.__mins} minutes"

	def __add__(self, other):
		if isinstance(other, Time):
			newHours = self.__hours + other.getHours()
			newMins = self.__mins + other.getMinutes()
			return Time(*self.__normalize(newHours, newMins))
		elif isinstance(other, int): # could technically be floats too, but instructions say int
			newMins = self.__mins + other
			return Time(*self.__normalize(self.__hours, newMins))
		else:
			raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")

	def __sub__(self, other):
		if isinstance(other, Time):
			if self > other:
				newMins = self.totalInMins() - other.totalInMins()
				return Time(*self.__normalize(0, newMins))
			else:
				return Time()
		elif isinstance(other, int): # could technically be floats too, but instructions say int
			if self.totalInMins() > other:
				newMins = self.totalInMins() - other
				return Time(*self.__normalize(0, newMins))
			else:
				return Time()
		else:
			raise TypeError(f"unsupported operand type(s) for -: '{type(self)}' and '{type(other)}'")

	def __mul__(self, scalar):
		if isinstance(scalar, float) or isinstance(scalar, int):
			newMins = self.totalInMins() * scalar
			return Time(*self.__normalize(0, newMins))
		else:
			raise TypeError(f"unsupported operand type(s) for *: '{type(self)}' and '{type(scalar)}'")

	def __truediv__(self, scalar):
		if isinstance(scalar, float) or isinstance(scalar, int):
			newMins = self.totalInMins() / scalar
			return Time(*self.__normalize(0, newMins))
		else:
			raise TypeError(f"unsupported operand type(s) for /: '{type(self)}' and '{type(scalar)}'")

	def __eq__(self, other):
		if isinstance(other, Time):
			return self.totalInMins() == other.totalInMins()
		elif isinstance(other, int): # could technically be floats too, but instructions say int
			return self.totalInMins() == other
		else:
			return False # apparently that is what python returns for non similar types

	def __lt__(self, other):
		if isinstance(other, Time):
			return self.totalInMins() < other.totalInMins()
		elif isinstance(other, int): # could technically be floats too, but instructions say int
			return self.totalInMins() < other
		else:
			raise TypeError(f"'<' not supported between instances of '{type(self)}' and '{type(other)}'")

	def __gt__(self, other):
		if isinstance(other, Time):
			return self.totalInMins() > other.totalInMins()
		elif isinstance(other, int): # could technically be floats too, but instructions say int
			return self.totalInMins() > other
		else:
			raise TypeError(f"'>' not supported between instances of '{type(self)}' and '{type(other)}'")

	def __assign__(self, other):
		if isinstance(other, Time):
			self.__hours = other.getHours()
			self.__mins = other.getMinutes()
		elif isinstance(other, float) or isinstance(other, int):
			self.__hours, self.__mins = self.__normalize(0, other)
		else:
			raise TypeError(f"Cannot assign value of type '{type(other)}' to '{type(self)}'")

	def __normalize(self, hours, mins): # caps minutes to 60, and adds excess to hours
		if mins >= 60:
			hours += mins//60
			mins %= 60
		return (int(hours), float(mins))
	
	def getHours(self):
		return self.__hours
	def getMinutes(self):
		return self.__mins
	def totalInMins(self):
		return (self.__hours*60) + self.__mins

def main():
	print(f"current count: {Time.count}")
	

	t1 = Time(7, 4.5)
	t2 = Time(3, 30)
	scalar = 5

	print(f"t1 = {t1}")
	print(f"t2 = {t2}")
	print(f"current count: {Time.count}")

	sum_time = t1 + t2
	print(f"t1 + t2 = {sum_time}")

	difference = t1 - t2
	print(f"t1 - t2 = {difference}")

	product = t1 * scalar
	print(f"t1 * scalar = {product}")
	print(f"current count: {Time.count}")

	divided = t2 / scalar
	print(f"t2 / scalar = {divided}")

	t3 = Time()
	t3.__assign__(100.5)
	
	print(f"t3 = {t3}")

	t3 = t3 + 100
	print(f"t3 += 100: {t3}")
	print(f"current count: {Time.count}")

	t3 = t3 - 70
	print(f"t3 -= 70: {t3}")

	if t3 < 100:
		print("t3 is less than 100")
	else:
		print("t3 is not less than 100")

	if t3 > 100:
		print("t3 is greater than 100")
	else:
		print("t3 is not greater than 100")

	if t1 < t2:
		print("t1 is less than t2")
	else:
		print("t1 is not less than t2")

	if t3 > t2:
		print("t3 is greater than t2")
	else:
		print("t3 is not greater than t2")

	if t1 == t3:
		print("t1 is equal to t3")
	else:
		print("t1 is not equal to t3")

	print(f"current count: {Time.count}")

if __name__ == "__main__":
	main()