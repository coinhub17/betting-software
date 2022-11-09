import numpy as np
from time import sleep


deposit=int(input("Deposit:"))
class game:
	Stake=()
	
	def __init__(self):
		self.start=-5.0
		self.stop= 10.0
		self.step=.1
		self.Stake=int(input("Stake!!:"))
		odd="10"
		self.odds=float(odd)
		Cash_out=int(input("Cash_out??:"))
		self.Cash_out=float(Cash_out)
	def __str__(self):
		return (self.start,self.stop, self.odds,self.Cash_out)
	
run=game()
start=run.start
Stake=run.Stake
odds=run.odds
step=run.step
stop=run.stop
Cash_out=run.Cash_out
win=Cash_out*Stake

while 15<deposit>Stake:
	Account_balance =deposit-Stake
	Account_balance+=win
	Account_balance-=Stake
	run
while 15>deposit or deposit> 15 or Stake>Account_balance:
			if deposit<15:
				print("insufficient deposit: ksh_15min")
				deposit=int(input("Deposit:"))
			elif Stake>=(deposit or Account_balance):
				print ("Insufficient Stake!!")
			else:
				run
			
		
while Cash_out<odds and Stake<=deposit:
			for win_range in np.arange(start,Cash_out,step):
				print("{:.1f}".format(win_range))
				sleep(.2)
			print("\n")
			Account_balance. append(win)
			print("Won!",win)
			for i in np.arange(Cash_out,odds,step):
				print("{:.1f}".format (i))
				sleep(.25)
			break
				
while Cash_out>odds and Stake<=deposit:
		for loss_range in np.arange(start,odds,step):
			print("{:.1f}".format(loss_range))
			sleep(.1)
		print("\n")
		print("Busted!")
		break
		