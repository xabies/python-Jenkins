from calculator import Calculator

class PythonJenkins(object):

    def run(self):
        c = Calculator()
        print "5 + 3 = ", c.add(5,3)
        print "8 - 4 = ", c.subtract(8,4)
		



if __name__ == '__main__':
    PythonJenkins().run()