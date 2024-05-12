immutable_var = tuple(['Vladimir', 67, 5.9, False])
print(immutable_var)
#immutable_var[2] = 'sun'     Элементы кортежа изменять нельзя если в кортеж не добавлен изменяемый список
#print(immutable_var)
mutable_list = ['Vladimir', 58, 5.9, False]
mutable_list[1] = 'Симпозиум'
print(mutable_list)
