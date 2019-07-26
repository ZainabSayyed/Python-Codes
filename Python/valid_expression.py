#validate expression
expression=list("][{{()}})[{()}]")
print expression
valid_pair={']':'[','}':'{',')':'('}
stack =[]
valid_expression=[]
i,current_expression=0,''

while i < len(expression):
    if expression[i] not in valid_pair.keys():
        stack.append(expression[i])
    else:
        if len(stack)>0 and valid_pair[expression[i]] == stack.pop():
            current_expression = valid_pair[expression[i]]+ current_expression+expression[i]
            print current_expression
        else:
            if len(current_expression)>0: valid_expression.append(current_expression)
            current_expression =''
            print "Invalid Expression"
    i=i+1
valid_expression.append(current_expression)
print valid_expression
longest_string=max(map(len,valid_expression))
print longest_string