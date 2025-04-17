def calculate_salary(hourly_rate, hours_worked, tax_rate=0.15):

        gross_salary = hourly_rate * hours_worked


        tax_deducted = gross_salary * tax_rate
        net_salary = gross_salary - tax_deducted

        return net_salary


def main(): 


        try:
            hourly_rate = float(input("Enter hourly rate: "))
            hours_worked = float(input("Enter hours worked: "))


            if hourly_rate < 0 or hours_worked < 0:
                print('no money earned')

                return


            net_salary = calculate_salary(hourly_rate, hours_worked)


            print(f"Net Salary: {net_salary:,.2f}")

        except ValueError:
            print("Error: Please enter valid numerical values for hourly rate and hours worked.")


if __name__ == "_main_":
    main()
    
