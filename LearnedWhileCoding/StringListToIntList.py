# Convert string tuple to int list

T1 = (('13', '17', '18', '21', '32'),
      ('07', '11', '13', '14', '28'),
      ('01', '05', '06', '08', '15', '16'))

# map(function, iterable). map this function to each element of the iterable
# and return a list of the results
T2 = [map(int, x) for x in T1]
print T2