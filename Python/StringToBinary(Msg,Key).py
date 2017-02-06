str2convert = "Hello world!"
[ bin(ord(ch))[2:].zfill(8) for ch in str2convert ]
import random
data=['a','B','C','B','R','Y','I','0','9','8','4','5','6']
key=random.sample(data,6)
print key
[ bin(ord(ch))[2:].zfill(8) for ch in key ]
