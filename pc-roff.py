inp = '''Hello my name is rohan omg why u like this fam pls stop fuck fjklj knhkjjbnn 
f djsnssjn jnjn jn jff fjfsnsf  ffffsfsfsi hhddd h'''

n= 40

lists = inp.split()
count = 0
sum=0

for i in lists:
    sum = sum + len(lists[count])
    count= count+1
    
    if sum >= 10:
        lists.insert((count), '\n')
        sum=0

print(sum) 
print(lists)