# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
# goal = [0, 4]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['v', '>', '^', '>']
  
def main():
    path_grid = [row[:] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            path_grid[i-1][j-1] = ' '
    path_grid[goal[0]][goal[1]] = '*'
    print("########## START #########");
    for i in range(len(grid)):
        print(grid[i]);
    # Define seeing, seen
    seeing = []
    seen = []
    seeing.append([goal[0],goal[1]])
    cost_grid = [row[:] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            cost_grid[i-1][j-1] = 100000
    cost_grid[goal[0]][goal[1]] = 0
    while len(seeing) > 0:
        #index is index of location in seeing with lowest cost
        minim = 1000000
        for x in seeing:
            if cost_grid[x[0]][x[1]] < minim:
                min_x = x
                minim = cost_grid[x[0]][x[1]]
        index = seeing.index(min_x)
        start_pos = seeing[index]
        for deltapos in delta:
            neighbor = [start_pos[0] + deltapos[0], start_pos[1] + deltapos[1]];
            # valid position 
            if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] <= (len(grid)-1) and neighbor[1] <= (len(grid[0])-1):
                # valid position and it open 
                if grid[neighbor[0]][neighbor[1]] != 1:
                    #position not in seen
                    if neighbor not in seen:
                        if neighbor not in seeing:
                            seeing.append(neighbor)
                            cost_grid[neighbor[0]][neighbor[1]] = min(cost_grid[neighbor[0]][neighbor[1]], 
                                                                        cost_grid[start_pos[0]][start_pos[1]] + 1)
                            if cost_grid[neighbor[0]][neighbor[1]] == cost_grid[start_pos[0]][start_pos[1]] + 1:
                                delta_index = delta.index(deltapos)
                                path_grid[neighbor[0]][neighbor[1]] = delta_name[delta_index]
        seen.append(seeing[index])
        seeing.remove(seeing[index])
    print("Optimum policy");
    # printing policy
    for i in range(len(path_grid)):
        print(path_grid[i]);
    return

if __name__== "__main__":
  main()
