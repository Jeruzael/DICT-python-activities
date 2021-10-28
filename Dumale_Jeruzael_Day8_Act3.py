from stud import *

stu1 = Student("Jo", 90, 90, 90)

avg = float(stu1.getAvg(stu1.getMath(), stu1.getScience(), stu1.getEnglish()))
stu1.result(stu1.getName(), avg)

