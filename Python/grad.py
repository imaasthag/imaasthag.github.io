import matplotlib.pyplot as plt
import graduates

years = []
Males = []
Females = []

entries = graduates.get_majors()

for entry in entries:
    if entry["Demographics"]["Gender"]["Males"] == "Males":
        Males.append(entry["Demographics"]["Gender"]["Males"])
        years.append(entry["Year"])
    if entry["Demographics"]["Gender"]["Females"] == "Females":
        Females.append(entry["Demographics"]["Gender"]["Females"])

plt.plot(years, Males)
plt.plot(years, Females)
plt.legend(["Males","Females"], loc ="upper left")

plt.xlabel("Years")
plt.ylabel("Number of Graduates")
plt.title("Number of Graduates by Gender in 1993")

plt.show()
