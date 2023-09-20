# in class coding for Wednesday, September 20

# we'll need this
states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado", "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
print(len(states))

#append a new state
states.append("DC")
print(len(states))

states.pop(50)
#print(states)

#list slicing - take a certain number of elements from the list
# "slice" the list
first_states = states[0:10] #the 10 is the first element in the list I don't want
print(first_states)
print (states[9])

#to take a slice from the list: list variable name [index of first element: index of first element NOT included]
mid_states = states[20:30]
print(mid_states)
print (states[30])
next_states = states[10:20]
more_states = states[30:40]
last_states = states[40:] # what did I do here?
print(first_states)
print(next_states)
print(mid_states)
print(more_states)
print(last_states)

# if you do not give a number after the colon, Python says go to the end
# start at that first number and include all the rest of the list items
#useful if you don't know how many elements you have

# if you don't put a number before the colon, Python starts at the beginning
# that's the same as having 0

# now let's work with strings

truth = "Purdue's football team will always break your heart by losing to teams they should beat"
#we can find the length

#string slicing
print(truth[0:6]) # results in 'Purdue'

#here is where lists and strings differ
# you can change an element of a list; you can't change an element of a string
states[19]= "Crescentia"
print(states[10:20])

#in my string 'truth' I want to change 'always' to 'never'
truth[28] = 'n'
truth[29] ='e'
# this always fails
