def sort_balls(balls):
    low, mid, high = 0, 0, len(balls) - 1
    while mid <= high:
        if balls[mid] == 'R':
            balls[low], balls[mid] = balls[mid], balls[low]
            low += 1
            mid += 1
        elif balls[mid] == 'G':
            mid += 1
        else:
            balls[mid], balls[high] = balls[high], balls[mid]
            high -= 1
    return balls

# Example Usage
balls = ['R', 'G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
print(sort_balls(balls))

