# List of cities
cities = ["Ahmedabad", "Bangalore", "Chennai", "Delhi", "Mumbai", "Pune",
          "Hyderabad", "Cochin", "Lucknow", "Patna", "Srinagar", "Bhubaneswar"]

# Travel time matrix (each row represents travel times from one city to others)
travel_times = [
    [0, 28, 32, 16, 11, 14, 21, 38, 22, 28, 30, 34],  # Ahmedabad row
    [28, 0, 8, 38, 18, 16, 10, 11, 34, 36, 53, 25],  # Bangalore row
    [32, 8, 0, 40, 24, 22, 12, 13, 35, 38, 55, 22],  # Chennai row
    [16, 38, 40, 0, 26, 28, 30, 50, 8, 17, 17, 32],  # Delhi row
    [11, 18, 25, 26, 0, 3, 14, 28, 28, 29, 40, 28],  # Mumbai row
    [14, 16, 22, 28, 3, 0, 11, 26, 27, 29, 42, 28],  # Pune row
    [21, 10, 12, 30, 14, 11, 0, 20, 26, 28, 46, 18],  # Hyderabad row
    [38, 11, 13, 50, 28, 26, 20, 0, 44, 47, 61, 32],  # Cochin row
    [22, 34, 35, 8, 28, 27, 26, 44, 0, 8, 24, 24],  # Lucknow row
    [28, 36, 38, 17, 29, 29, 28, 47, 8, 0, 32, 17],  # Patna row
    [30, 53, 55, 17, 40, 42, 46, 61, 24, 32, 0, 45],  # Srinagar row
    [34, 25, 22, 32, 28, 28, 18, 32, 24, 17, 45, 0]  # Bhubaneswar row
]


def city_travel_time():
    # Take user input for source and destination cities
    source = input("Enter your city name: ").strip().capitalize()
    destination = input("Enter the city name you want to travel to: ").strip().capitalize()

    # Check if both cities exist in the list
    if source in cities and destination in cities:
        # Find the index of the cities
        src_index = cities.index(source)
        dest_index = cities.index(destination)

        # Get the travel time from the matrix
        travel_time = travel_times[src_index][dest_index]

        # Print the result
        print(f"The travel time from {source} to {destination} is {travel_time} hours by road.")
    else:
        print("One or both of the city names are not in the list. Please try again.")


# Example call to the function
city_travel_time()
