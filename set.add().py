#Input Format
#The first line contains an integer , the total number of country stamps.
#The next  lines contains the name of the country where the stamp is from.
#Output Format
#Output the total number of distinct country stamps on a single line.

numberOfCountryStamps = int(input())
countrynames=set()
for i in range(numberOfCountryStamps):
    country = input()
    countrynames.add(country)
print(len(countrynames))