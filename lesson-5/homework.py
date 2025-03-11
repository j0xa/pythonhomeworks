def convert_cel_to_far(celcius: float) -> float:
    return round(celcius*9/5+32,2)
def convert_far_to_cel(fahrenheit:float) ->float:
    return round((fahrenheit-32)*5/9, 2)
def main():
    fahrenheit = float(input("Enter a temperature in degrees Fahrenheit: "))
    celcius = convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit} F = {celcius} degrees C")

    celcius = float(input("\nEnter a temperature in degrees Celcius: "))
    fahrenheit = convert_cel_to_far(celcius)
    print(f"{celcius} C = {fahrenheit} degrees F")
if __name__ == "__main__":
    main()



    def main():
    num = int(input("Enter a positive integer: "))
    if num<=0:
        print("please enter a positive integer: ")
        return
    for i in range(1, num+1):
        if num%i==0:
            print(f"{i} is a factor of {num}")
if __name__=="__main__":
    main()


    def invest(amount, rate, years):
    for year in range(1, years+1):
        amount+=amount*rate
        print(f"year {year}: ${amount:.2f}")
principal = float(input("Enter the initial investment amount: "))
annual_rate = float(input("Enter the annual rate of return as a percentage: ")) /100
num_years = int(input("Enter the number of years: "))
invest(principal, annual_rate, num_years)

def enrollment_stats(universities):
    enrollments = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return enrollments, tuitions
def mean(lst):
    return sum(lst)/len(lst) if lst else 0
def median(lst):
    sorted_lst=sorted(lst)
    n = len(sorted_lst)
    mid = n//2
    if n%2 == 0:
        return (sorted_lst[mid-1] + sorted_lst[mid])/2
    else:
        return sorted_lst[mid]
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
enrollments, tuitions = enrollment_stats(universities)
total_students = sum(enrollments)
total_tuition = sum(tuitions)
student_mean = mean(enrollments)
student_median = median(enrollments)
tuition_mean = mean(tuitions)
tuition_median = median(tuitions)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: {total_tuition:,}\n")
print(f"Student mean: {student_mean:,.2}")
print(f"Student median: {student_median:,}\n")
print(f"Tuition mean: {tuition_mean:,.2}")
print(f"Tuition median: {tuition_median:,}")
print("******************************")


def is_prime(n):
    if n<2:
        return False
    for i in range (2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n = int(input("Enter an integer: "))
print(is_prime(n))