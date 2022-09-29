tp = (1, 1, 2, 3, 6, 5)
tp1 = (1, 5, 79, 2, 6)
tp2 = tp[0: 3]+tp1[-3:]
print(tp2)
# we can concate 2 tuple normally without converting it into list
print(tp+(123,))
# coma is nessary when there is only one element in tuple or it will be regarded as integer
# eg(10,)
print(tp*3)
