from collections import deque

def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    platforms_needed = 1
    max_platforms = 1
    i, j = 1, 0
    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        max_platforms = max(max_platforms, platforms_needed)
    return max_platforms

# Example Usage
arrivals = [9.0, 9.4, 9.5, 11.0, 15.0, 18.0]
departures = [9.1, 12.0, 11.2, 11.3, 19.0, 20.0]
print(min_platforms(arrivals, departures))
