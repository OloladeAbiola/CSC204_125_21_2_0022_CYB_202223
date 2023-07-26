SingleLinkedList

if__name__=="main"
data_list=[1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28]

# create a single limked list and insert the data
singlell=SingleLinkedList()
for data in data_list:
    singlell.insert(data)

# display the single linked list
singlell.display()