def create_grap(words):
    related_word=dict()
    for src_word in range(0,len(words)):
        list_related=[]
        source_word= list(words[src_word])
        for des_word in range(0,len(words)):
            if words[src_word]==words[des_word]: continue
            length = len(words[src_word])  - len(words[des_word])
            #print "length", words[src_word], words[des_word], length
            dest_word= list(words[des_word])
            count = 0
            if length< 2:
                for char in source_word:
                    if char not in dest_word:
                        count = count+1
            else:
                continue
            if (length == 0 or length == 1) and count <2:
                list_related.append(words[des_word])
            else:
                if count==0:
                    list_related.append(words[des_word])
                #print "count",words[src_word], words[des_word], count
        related_word[words[src_word]]=list_related
    return related_word
