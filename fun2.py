# ...existing code...

def add_driver(drivers, name, team):
    """Add a new driver dict with empty laps list."""
    drivers.append({"name": name, "team": team, "laps": []})
    return drivers

def record_lap(drivers, name, lap_time):
    """Append lap_time to the driver's laps. Returns True if recorded, False if driver not found."""
    for d in drivers:
        if d["name"] == name:
            d.setdefault("laps", []).append(float(lap_time))
            return True
    return False 

def average_lap(drivers, name):
    """Return average lap time for driver or None if driver not found or no laps."""
    for d in drivers:
        if d["name"] == name:
            laps = d.get("laps", [])
            return (sum(laps) / len(laps)) if laps else None
    return None

def fastest_driver(drivers):
    """Return the driver dict with the lowest average lap (only drivers with laps considered)."""
    best = None
    best_avg = None
    for d in drivers:
        laps = d.get("laps", [])
        if not laps:
            continue
        avg = sum(laps) / len(laps)
        if best is None or avg < best_avg:
            best, best_avg = d, avg
    return best  # None if no driver with laps

def team_fastest_avg(drivers, team):
    """Return the lowest average lap time among drivers in the given team, or None if none."""
    best_avg = None
    for d in drivers:
        if d.get("team") != team:
            continue
        laps = d.get("laps", [])
        if not laps:
            continue
        avg = sum(laps) / len(laps)
        if best_avg is None or avg < best_avg:
            best_avg = avg
    return best_avg


# --- schedule helpers and functions ---

def _time_to_minutes(t):
    """Convert 'HH:MM' string to minutes since midnight."""
    h, m = map(int, t.split(":"))
    return h * 60 + m

def add_schedule(schedule, flight_no, time, type_):
    """Add a flight record to schedule (type_ should be 'Arrival' or 'Departure')."""
    schedule.append({"flight_no": flight_no, "time": time, "type": type_})
    return schedule

def cancel_flight(schedule, flight_no):
    """Remove flight by flight_no. Return True if removed, False if not found."""
    for i, f in enumerate(schedule):
        if f.get("flight_no") == flight_no:
            schedule.pop(i)
            return True
    return False

def flights_between(schedule, start_time, end_time):
    """Return list of flight dicts with times between start_time and end_time inclusive."""
    start = _time_to_minutes(start_time)
    end = _time_to_minutes(end_time)
    return [f for f in schedule if start <= _time_to_minutes(f["time"]) <= end]

def count_types(schedule):
    """Return a dict with counts of 'Arrival' and 'Departure'."""
    counts = {"Arrival": 0, "Departure": 0}
    for f in schedule:
        t = f.get("type")
        if t in counts:
            counts[t] += 1
    return counts

def next_flight(schedule, current_time):
    """Return the next flight dict after current_time, or None if none."""
    now = _time_to_minutes(current_time)
    candidates = [f for f in schedule if _time_to_minutes(f["time"]) > now]
    if not candidates:
        return None
    return min(candidates, key=lambda x: _time_to_minutes(x["time"]))

# Example usage (comment out or remove in production):
if __name__ == "__main__":
    drivers = []
    add_driver(drivers, "Lando Norris", "McLaren")
    record_lap(drivers, "Lando Norris", 91.3)
    record_lap(drivers, "Lando Norris", 89.7)
    print("Lando avg:", average_lap(drivers, "Lando Norris"))

    schedule = []
    add_schedule(schedule, "BA117", "14:30", "Departure")
    add_schedule(schedule, "AA101", "13:15", "Arrival")
    print("Flights 13:00-15:00:", flights_between(schedule, "13:00", "15:00"))
    print("Next after 14:00:", next_flight(schedule, "14:00"))
