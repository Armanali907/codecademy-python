weight = 41.5
#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else :
  cost_ground = weight * 4.75 + 20
print("Ground Shipping $",cost_ground)
# Ground Shipping Premium
cost_ground_premium = 125.00
print("Ground Shipping Premium $",cost_ground_premium)

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 1.50*3
elif weight <= 6:
  cost_drone = weight * 3.00*3
elif weight <= 10:
  cost_drone = weight * 4.00*3
else :
  cost_drone = weight * 4.75*3

print("Drone Shipping $",cost_drone)
