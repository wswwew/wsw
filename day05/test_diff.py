with open('/etc/passwd','r') as src_data:
    aset = set(src_data)
with open('/root/wsw/passwd','r') as dst_data:
        bset = set(dst_data)
print(aset)
print('-'*30)
print(bset)

with open('/root/wsw/diff.txt','w') as diff_data:
    diff_data.writelines(bset-aset)