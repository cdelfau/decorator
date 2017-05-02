import time

def log(f):
  def inner(*arg):
		return f.f_name+": " + str(arg)
	return inner

def runtime(f):
	def inner(*arg):
		t1 = time.time()
		f(*arg)
		t2 = time.time()
		return "execution time: " + str(t2-t1)
	return inner

def print_new(word1, word2):
	time.sleep(5)
	return word1 + " " + word2

print print_new("hello","goodbye")
