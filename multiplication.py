def print_table(n):
    for i in range (1,13):
        print(f"{n}*{i} = {n*i}")

def printTable(n, i=1):
   if (i==13):
      return
   print(f"{n}*{i} = {n*i}")
   i= i+1
   printTable(n, i)

   


if __name__ == "__main__":
  n = 5
  print_table(n)
  printTable(n)