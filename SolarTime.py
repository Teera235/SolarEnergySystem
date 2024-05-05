TotalCost = float(input("Enter your Total Cost (Bath): "))
SystemSize = float(input("Enter your System Size (Kw): "))
FtCost = float(input("Enter your Current FT: "))

SunHours = 4
Efficiency = 0.9
RealDay = 360 

AllTime = SystemSize * SunHours * FtCost * Efficiency * RealDay
PayBackTime = TotalCost / AllTime 

print("Your PayBackTime: " + str(round(PayBackTime, 1)) + " years")
