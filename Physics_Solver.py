print("Welcome to the Kinematic Physics Calculator!")
if __name__ == "__main__":
    def calculate_final_velocity(u, a, t):
        return u + a * t

    def calculate_displacement(u, t, a):
        return u * t + 0.5 * a * t**2

    def calculate_time(u, v, a):
        if a == 0:
            raise ValueError(
                "Acceleration cannot be zero when calculating time.")
        return (v - u) / a

    while True:
        print("\nChoose the quantity to calculate:")
        print("1. Final Velocity (v)")
        print("2. Displacement (s)")
        print("3. Time (t)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            u = float(input("Enter initial velocity (u) in m/s: "))
            a = float(input("Enter acceleration (a) in m/s²: "))
            t = float(input("Enter time (t) in seconds: "))
            v = calculate_final_velocity(u, a, t)
            print(f"The final velocity (v) is {v} m/s")

        elif choice == '2':
            u = float(input("Enter initial velocity (u) in m/s: "))
            t = float(input("Enter time (t) in seconds: "))
            a = float(input("Enter acceleration (a) in m/s²: "))
            s = calculate_displacement(u, t, a)
            print(f"The displacement (s) is {s} meters")

        elif choice == '3':
            u = float(input("Enter initial velocity (u) in m/s: "))
            v = float(input("Enter final velocity (v) in m/s: "))
            a = float(input("Enter acceleration (a) in m/s²: "))
            try:
                t = calculate_time(u, v, a)
                print(f"The time (t) is {t} seconds")
            except ValueError as e:
                print(e)

        elif choice == '4':
            print("Exiting the Kinematic Calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
