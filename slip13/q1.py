#sorting dict ascen and descen

data = {'apple':5,'banana':2,'orange':8,'grape':3}

a_order = dict(sorted(data.items(),key=lambda x:x[1]))
d_order = dict(sorted(data.items(),key=lambda x:x[1],reverse = True))

print("ascending order ",a_order)
print("descending order",d_order)