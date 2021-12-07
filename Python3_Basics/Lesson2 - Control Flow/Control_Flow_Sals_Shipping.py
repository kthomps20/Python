
#Ground Shipping

weight = 25

if weight <= 2:
  ground_shipping = weight * 1.5 + 20
elif weight <= 6:
  ground_shipping = weight * 3.00 + 20
elif weight <= 10:
  ground_shipping = weight * 4.00 + 20
else:
  ground_shipping= weight * 4.75 + 20

print("The cost of Ground Shipping is: $" + str(ground_shipping))

#Drone Shipping

weight_d = 6

if weight_d <= 2:
    drone_shipping = weight_d * 4.5
elif weight_d <=6:
    drone_shipping = weight_d * 9
elif weight_d <= 10:
    drone_shipping = weight_d * 13.5 + 30

print("The cost of Drone Shipping is: $" + str(drone_shipping))
