def main():
    name = input("Enter Spacecraft Name : ")
    distance = input("Enter Spacecraft distance [AU] :")
    imperator = input("Spacecraft's Imperator :")
    orbit = input("Enter Spacecraft's present Orbit :")
    galaxy = input("Current Galaxy : ")
    spacecraft = {
        "name" : name,
        "distance" : distance,
        "imperator": imperator,
        "orbit" : orbit,
        "galaxy" : galaxy                                                                                 }
    print(create_report(spacecraft)) 



def create_report(spacecraft):
    return f"""
========= REPORT =========
Name : {spacecraft.get("name")}
Imperator = {spacecraft.get("imperator")}
Orbit = {spacecraft.get("orbit")}
Galaxy = {spacecraft.get("galaxy")}
Distance = {spacecraft.get("distance")} AU
===========================
"""

main()