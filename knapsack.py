weight_limit = 11
n = 3
item_weight = [5, 4, 6,]
item_value = [50, 40, 30]
items_no  = [0, 1, 2, 3, 4]
current_items = [0, 0, 0]
best_value = 0
current_weight = 0
current_value = 0

#Exhaustive search

# def exhaustive_search(items):
#     global best_value
#     global current_weight
#     global current_value
#     if current_weight>=weight_limit:
#         print('base case')
#     elif len(items)==0:
#         print('base case')
#     else:
#         for i in range(len(items)):
#             if current_weight+item_weight[i]<=weight_limit:
#                 current_weight = current_weight+item_weight[i]
#                 current_value = current_value + item_value[i]
#                 if current_value>best_value:
#                     best_value = current_value
#             if len(items)>0:
#                 items_remaining = items
#                 del items_remaining[i]
#                 exhaustive_search(items_remaining)

# exhaustive_search(items_no)
# print(best_value)
# print(current_items)

# test and generate
count = 0
current_items = [0, 0, 0]
best_items = []
def generate_state(iterations):
    global n
    global weight_limit
    global count
    global current_value
    global current_weight
    global best_value
    global current_items
    global item_value
    global item_weight
    global best_items

    for i in range(2):
            current_value=0
            current_weight = 0
            current_items[iterations]=i
            for j in range(n):
                if current_items[j]==1:
                     current_value=current_value+item_value[j]
                     current_weight=current_weight+item_weight[j]
            print('current items', current_items)
            print('current weight' ,  current_weight)
            print('current value' ,current_value)
            if current_weight<=weight_limit:
                if current_value>best_value:
                     best_value=current_value

            print('best value' , best_value)
            if iterations<n-1:            
                 generate_state(iterations+1)
generate_state(0)

print(best_value)
print(best_items)