# inputs: 
#   W: weight limit of the vehicle used for deliveries.
#   packages: 2D list [[packageID, reward, weight], [packageID, reward, weight], ...]
# returns:
#   1D list of package IDs to represent a package selection. e.g. ["P001", "P003, "P010]

#The following code is largely a derivation of Bhavya Jain on GeeksForGeeks - https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

def knapSack(W, packages):

  n = len(packages)

  K = [[0 for x in range(W + 1)] for x in range(n + 1)]

  for i in range(n + 1):
      for w in range(W + 1): 
          if i == 0 or w == 0:
              K[i][w] = 0
          elif packages[i-1][2] <= w: 
              K[i][w] = max(packages[i-1][1] + K[i-1][w-packages[i-1][2]], K[i-1][w]) 
          else:
              K[i][w] = K[i-1][w]
  
  return n, w, K

# End of derivation

def select_packageSet(W, packages):
  res = list()

  n = len(packages)

  n, w, K = knapSack(W, packages)

  for i in range(n,-1,-1):
    if K[i][w] == K[i-1][w]:
      continue
    else:
      res.append(packages[i-1][0])
      w -= packages[i-1][2]
  
  return res

# outputs res: List of chosen packages for the knapsack