# What it is?

It is the car which finds it's oponents on it's own and pushes them out of the battle field. It also has black line sensors not to fall off the battle field. It's made using ESP8266. The code is on micropython. It has distance sensors on both sides to find the oponent fast.

# Components

### ESP8266
### L298n x2
### Motors 12V 370RPM x4
### SH-04 x2
### Chineese sensors of black line with adjustable with comparator.  x4
### Plastic wheels x4
### DC-DC down converter 1A


# Logic

The car rotates until it will find an oponent on a limited distance, then it moves toward it to push him out of the battle field. The car moves on this principle until the black line sencor doesn't see the black line. If that happens the car moves in oposite dirrection from the black line. 
