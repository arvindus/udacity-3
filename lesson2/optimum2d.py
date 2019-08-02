# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    # x of pred, y of pred, direction of pred

    predecessor_grid = [[[-1 for k in range(3)] for j in range(len(grid[0]))] for i in range(len(grid))]
    print(len(predecessor_grid), " ", len(predecessor_grid[0]), " ", len(predecessor_grid[0][0]))
    print("########## START #########");
    for i in range(len(grid)):
        print(grid[i]);
    # Define seeing, seen
    seeing = []
    seen = []
    seeing.append([init[0],init[1],init[2]])
    cost_grid = [row[:] for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            cost_grid[i-1][j-1] = 100000
    cost_grid[init[0]][init[1]] = 0
    while len(seeing) > 0:
        #index is index of location in seeing with lowest cost
        minim = 1000000
        for x in seeing:
            if cost_grid[x[0]][x[1]] < minim:
                min_x = x
                minim = cost_grid[x[0]][x[1]]
        index = seeing.index(min_x)
        start_pos = seeing[index]
        print("start_pos = ", start_pos)
        if start_pos[0] == goal[0] and start_pos[1] == goal[1]:
            return predecessor_grid
        for deltapos in forward:
            delta_index = forward.index(deltapos)
            print("delta_index = ", delta_index)
            neighbor = [start_pos[0] + deltapos[0], start_pos[1] + deltapos[1], delta_index];
            # valid position 
            if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] <= (len(grid)-1) and neighbor[1] <= (len(grid[0])-1):
                # valid position and it open 
                if grid[neighbor[0]][neighbor[1]] != 1:
                    #position not in seen
                    if neighbor not in seen:
                        if neighbor not in seeing:
                            seeing.append(neighbor)
                            print("neighbor = ", neighbor)
                            # find action involved
                            if start_pos[2] == delta_index:
                               cost_index = 1
                            if start_pos[2] == 0 and delta_index == 2 or start_pos[2] == 2 and delta_index == 0 or start_pos[2] == 1 and delta_index == 3 or start_pos[2] == 3 and delta_index == 1:
                               cost_index = 1
                            if start_pos[2] == 0 and delta_index == 1 or start_pos[2] == 1 and delta_index == 0 or start_pos[2] == 2 and delta_index == 3 or start_pos[2] == 3 and delta_index == 2:
                               cost_index = 2
                            if start_pos[2] == 0 and delta_index == 3 or start_pos[2] == 3 and delta_index == 0 or start_pos[2] == 1 and delta_index == 2 or start_pos[2] == 2 and delta_index == 1:
                               cost_index = 0

                            print("cost_index = ", cost_index)
                            print("cost_grid[neighbor[0]][neighbor[1]] = ", cost_grid[neighbor[0]][neighbor[1]])
                            print("cost_grid[start_pos[0]][start_pos[1]] = ", cost_grid[start_pos[0]][start_pos[1]])
                            print("cost[cost_index] = ", cost[cost_index])
                            cost_grid[neighbor[0]][neighbor[1]] = min(cost_grid[neighbor[0]][neighbor[1]], 
                                                                        cost_grid[start_pos[0]][start_pos[1]] + cost[cost_index])
                            print("AFTER: cost_grid[neighbor[0]][neighbor[1]] = ", cost_grid[neighbor[0]][neighbor[1]])
                            if cost_grid[neighbor[0]][neighbor[1]] == cost_grid[start_pos[0]][start_pos[1]] + cost[cost_index]:
                                predecessor_grid[neighbor[0]][neighbor[1]][0] = start_pos[0]
                                predecessor_grid[neighbor[0]][neighbor[1]][1] = start_pos[1]
                                predecessor_grid[neighbor[0]][neighbor[1]][2] = cost_index
        seen.append(seeing[index])
        seeing.remove(seeing[index])
    print("NOT FOUND")

policy2D = optimum_policy2D(grid,init,goal,cost)
answer = [[' ' for j in range(len(grid[0]))] for i in range(len(grid))]
for i in range(len(grid)):
        for j in range(len(grid[0])):
            answer[i-1][j-1] = action_name[policy2D[i-1][j-1][2]]
print("Optimum policy");
# printing policy
for i in range(len(answer)):
    print(answer[i]);

# path_grid = [row[:] for row in grid]
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             path_grid[i-1][j-1] = ' '
#     path_grid[goal[0]][goal[1]] = '*'
#     print("########## START #########");
#     for i in range(len(grid)):
#         print(grid[i]);
#     # Define seeing, seen
#     seeing = []
#     seen = []
#     seeing.append([goal[0],goal[1]])
#     cost_grid = [row[:] for row in grid]
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             cost_grid[i-1][j-1] = 100000
#     cost_grid[goal[0]][goal[1]] = 0
#     while len(seeing) > 0:
#         #index is index of location in seeing with lowest cost
#         minim = 1000000
#         for x in seeing:
#             if cost_grid[x[0]][x[1]] < minim:
#                 min_x = x
#                 minim = cost_grid[x[0]][x[1]]
#         index = seeing.index(min_x)
#         start_pos = seeing[index]
#         for deltapos in delta:
#             neighbor = [start_pos[0] + deltapos[0], start_pos[1] + deltapos[1]];
#             # valid position 
#             if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] <= (len(grid)-1) and neighbor[1] <= (len(grid[0])-1):
#                 # valid position and it open 
#                 if grid[neighbor[0]][neighbor[1]] != 1:
#                     #position not in seen
#                     if neighbor not in seen:
#                         if neighbor not in seeing:
#                             seeing.append(neighbor)
#                             cost_grid[neighbor[0]][neighbor[1]] = min(cost_grid[neighbor[0]][neighbor[1]], 
#                                                                         cost_grid[start_pos[0]][start_pos[1]] + 1)
#                             if cost_grid[neighbor[0]][neighbor[1]] == cost_grid[start_pos[0]][start_pos[1]] + 1:
#                                 delta_index = delta.index(deltapos)
#                                 path_grid[neighbor[0]][neighbor[1]] = delta_name[delta_index]
#         seen.append(seeing[index])
#         seeing.remove(seeing[index])
#     print("Optimum policy");
#     # printing policy
#     for i in range(len(path_grid)):
#         print(path_grid[i]);
#     return
