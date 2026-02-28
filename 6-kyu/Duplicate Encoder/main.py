def duplicate_encode(word):
    lowercased = word.lower()    
    return ''.join(')' if lowercased.count(x) > 1 else '(' for x in lowercased)
    
    
        # if you want not two lines solution:
    #     lowercased = word.lower()
    #     encoded = ''
        
    #     for x in lowercased:
    #         if lowercased.count(x) > 1:
    #             encoded += ')'
    #         else:
    #             encoded += '('
    #     return encoded
    