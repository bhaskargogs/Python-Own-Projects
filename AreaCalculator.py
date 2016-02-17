"""
 ******************Area Calculator Project**********************************
    This project is a description of areas with sizes. User can select the shape sizes ranging from 0 to 10. 
    It would print out the shape along with the area.
    """
    
    print "************Area Calculator project**********"
    import math
    from math import pi
    from datetime import datetime
    
    now =datetime.now()
    print "%s of %s, %s %s:%s" %(now.day,now.month,now.year,now.hour,now.minute)
    print "To find the name and area of your shape, we start by entering the number of sides "
    print "Note: The area that is printed is of 2 decimal points." 
    option = raw_input("Enter the number of sides: ")
    if option == 0:
      print "You have selected a Circle"
      radius = float(raw_input("Enter a radius: "))
      area = pi * radius**2
      print "The area of the circle is: %0.2f" %(area)
    elif option == 3:
      print "You have selected a Triangle"
      base = float(raw_input("Enter the base: "))
      height = float(raw_input("Enter the height: "))
      area = base*height/2;
      print "The area of the circle is: %0.2f" %area
    elif option == 4
    elif option == 5:
      print "You have selected a pentagon"
      side = float(raw_input("Enter the side: "))
      area = ((5*(5+2*(5**0.5)))**0.5) * (side**2)/4;
      print "The area of the pentagon is: %0.2f" %area
    elif option == 6:
      print "You have selected a hexagon"
      side = float(raw_input("Enter the side: "))
      area = (3*(3**2))* (side**2)/2
      print "The area of the hexagon  is: %0.2f" %area
    elif option == 7:
      print "You have selected a heptagon"
      side = float(raw_input("Enter a side: ")
      area = ((option * side**2) / ((4 * tan)*(pi/option)))
    elif option == 8:
      print "You have selected an octagon"
      side = float(raw_input("Enter a side: ")
      area = ((option * side**2) / ((4 * tan)*(pi/option)))
    elif option == 9:
      print "You have selected a nonagon"
      side = float(raw_input("Enter a side: ")
      area = ((option * side**2) / ((4 * tan)*(pi/option)))
    elif option == 10
      print "You have selected a decagon"
      side = float(raw_input("Enter a side: ")
      area = ((option * side**2) / ((4 * tan)*(pi/option)))
    
      
