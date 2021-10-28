def testsd():
	print("SD worked")

def getSalaryDeductions(gs, loan, insurance):
	tax = gs*.12
	d = tax + loan + insurance	
	#print("Total deduction: ", d)
	return d
