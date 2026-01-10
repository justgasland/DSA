def closest_number(n, m):
    closest=0
    min_differ= float('inf')

    # checking for the closest n
    for i in range(n- abs(m) + n+ abs(m)+1):
       if i % m==0:
           diff= abs(n-i)

           if diff < min_differ or \
            (diff == min_differ and abs(i) > abs(closest)):
            closest = i
            min_differ = diff
    return closest  

def closestNumber(n,m):
    q= int(n/m)

    n1= m * q
    if (n*m>0):
       n2=m * (q + 1)
    else:
       n2= m * (q - 1)
    
    if abs(n - n1) < abs(n - n2):
        return n1

if __name__ == "__main__":
  n = 13
  m = 4
  print(closest_number(n, m))

  n = 16
  m = 4
  print(closestNumber(n, m))