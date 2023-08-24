class FlightTable:
    def __init__(self):
        self.data = [
            ("Mumbai", "India", "Sri Lanka", "DAY"),
            ("Delhi", "England", "Australia", "DAY-NIGHT"),
            ("Chennai", "India", "South Africa", "DAY"),
            ("Indore", "England", "Sri Lanka", "DAY-NIGHT"),
            ("Mohali", "Australia", "South Africa", "DAY-NIGHT"),
            ("Delhi", "India", "Australia", "DAY")
        ]

    def search_by_team(self, team_name):
        team_matches = [
            (location, team1, team2, timing)
            for location, team1, team2, timing in self.data
            if team_name in (team1, team2)
        ]
        return team_matches

    def search_by_location(self, location_name):
        location_matches = [
            (location, team1, team2, timing)
            for location, team1, team2, timing in self.data
            if location == location_name
        ]
        return location_matches

    def search_by_timing(self, timing_name):
        timing_matches = [
            (location, team1, team2, timing)
            for location, team1, team2, timing in self.data
            if timing == timing_name
        ]
        return timing_matches

def main():
    flight_table = FlightTable()


    print("NAME: ARYAN")
    print("Enroll_Number: E22CSEU0382")
    print("Select search parameter:")
    print("1. List of all the matches of a Team")
    print("2. List of Matches on a Location")
    print("3. List of Matches based on timing")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        team_name = input("Enter the team name: ")
        team_matches = flight_table.search_by_team(team_name)
        print_matches(team_matches)

    elif choice == 2:
        location_name = input("Enter the location name: ")
        location_matches = flight_table.search_by_location(location_name)
        print_matches(location_matches)

    elif choice == 3:
        timing_name = input("Enter the timing: ")
        timing_matches = flight_table.search_by_timing(timing_name)
        print_matches(timing_matches)

    else:
        print("Invalid choice")

def print_matches(matches):
    if not matches:
        print("No matches found.")
    else:
        print("Match Location  |  Team 01  |  Team 02  |  Timing")
        print("-" * 49)
        for location, team1, team2, timing in matches:
            print(f"{location}  |  {team1}  |  {team2}  |  {timing}")

if __name__ == "__main__":
    main()