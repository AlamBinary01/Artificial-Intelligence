import numpy as np
import random

def grassfire(grid, start, destination):
    rows, cols = np.shape(grid)
    dist = np.zeros((rows, cols), dtype=np.int32)
    dist[start[0], start[1]] = 1
    queue = [start]
    while queue:
        currentRow, currentColumn = queue.pop(0)
        for row, col in [(currentRow-1, currentColumn), (currentRow+1, currentColumn), (currentRow, currentColumn-1), (currentRow, currentColumn+1)]:
            if 0 <= row < rows and 0 <= col < cols and dist[row, col] == 0 and grid[row, col] == 0:
                dist[row, col] = dist[currentRow, currentColumn] + 1
                queue.append((row, col))
    return dist

def generate_search_map(rows, cols, obstaclePercentage):
    grid = np.zeros((rows, cols), dtype=np.int32)
    numberOfObstacles = int(round(rows * cols * obstaclePercentage / 100))
    obstacleIndices = random.sample(range(rows * cols), numberOfObstacles)
    for obstacleIndex in obstacleIndices:
        row = obstacleIndex // cols
        col = obstacleIndex % cols
        grid[row, col] = 1
    start = (0, random.randint(0, cols-1))
    destination = (random.randint(rows//2, rows-1), random.randint(cols*2//3, cols-1))
    return grid, start, destination

def main(): 
    rows = int(input("Enter the number of rows (minimum 8): "))
    cols = int(input("Enter the number of columns (minimum 8): "))
    obstaclePercentage = int(input("Enter the percentage of obstacle cells (10-20%): "))
    grid, start, destination = generate_search_map(rows, cols, obstaclePercentage)
    dist = grassfire(grid, start, destination)
    print("Search Map:")
    print(dist)
    print("Shortest Path Length:", dist[destination[0], destination[1]] - 1)

if __name__ == "__main__":# , when the file is executed as the main program, the main() function will be executed. 
    #If this file is imported as a module in another program, the code under the
    #  if __name__ == "__main__": statement will not be executed
    main()
