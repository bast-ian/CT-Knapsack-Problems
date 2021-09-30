# inputs: 
#   n: the number of members in your team
#   W: weight limit of each vehicle used for deliveries.
#   packages: 2D list [[packageID, reward, weight], [packageID, reward, weight], ...]
# returns:
#   2D list of package IDs to represent n sets of packages. 
#   e.g. if n = 2, this is a possible solution: [["P001", "P003"], ["P010"]]

def select_packageSets(n, W, packages):

  res = [[] for _ in range(n)]

  packages.sort(key = lambda x: x[1]/x[2])

  max_weight = [W for i in range(n)]

  if len(packages) > 40:

    while len(packages) > 0:
          breaker = [0 for i in range(n)]
          for i in range(n):
              if len(packages) > 0:
                  if max_weight[i] - packages[-1][2] >= 0:
                      res[i].append(packages[-1][0])
                      max_weight[i] -= packages[-1][2]
                      del(packages[-1])
                  else:
                      breaker[i] = 1

          if sum(breaker) == n and len(packages) >= 1:
              del(packages[-1])

  else:
    while len(packages) > 0:
      breaker = [0 for i in range(n)]
      for j in range(n):
        if len(packages) > 0:
          if packages[0][2] + packages[-1][2] <= max_weight[j]:
            max_weight[j] -= packages[0][2] + packages[-1][2]
            res[j].extend([packages[0][0], packages[-1][0]])
            del packages[0], packages[-1]
          
          elif packages[-1][2] <= max_weight[j]:
            max_weight[j] -= packages[-1][2]
            res[j].append(packages[-1][0])
            del packages[-1]
          
          elif packages[0][2] <= max_weight[j]:
            max_weight[j] -= packages[0][2]
            res[j].append(packages[0][0])
            del packages[0]

          else:
            breaker[j] = 1
      
      if sum(breaker) == n:
        if len(packages) >= 2:
          del packages[0]
          del packages[-1]
        if len(packages) == 1:
          del packages[0]
  return res

#output res: 2-d list containing the different knapsacks, each with their packages