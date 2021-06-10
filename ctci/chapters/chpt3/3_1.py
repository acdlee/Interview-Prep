# To implement three stacks with one array, we could have indexing
#such that we separate the array into three parts. We maintain 
#a starting and ending index for each stack. The 'ending index' would
#be the location where we add and remove items from each stack.
#whenever the stacks are about to overlap, we would reallocate the array
#to a new array size 3(size of previous array) and equally divide and
#space each section. When we pop items off any of the stacks, we would
#just need to decrement the ending index of that stack. 