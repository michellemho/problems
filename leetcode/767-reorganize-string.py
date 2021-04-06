class Solution:
    def reorganizeString(self, S: str) -> str:
        freq = {}
        for i in S:
            freq[i] = S.count(i)
        halflength = (len(S)+1)//2
        print(halflength)
        if any([val > halflength for val in freq.values()]):
            return ""
        else:
            new_string = ""
            # Sort by second item in tuple of freq dictionary key-value pairs
            sort_list = sorted(freq.items(), key=lambda kv: kv[1])
            
            # Expand into a list...
            sort_string = []
            for (k, v) in sort_list:
                sort_string.extend([k*v])
                
            # Reverse so most common is first, and make a string actually
            sort_string = "".join(sort_string[::-1])
            
            # Split in half
            first_half = list(sort_string[:halflength])
            second_half = list(sort_string[halflength:])
            print(first_half, second_half)
            
            # Placing alternating letters until string is full
            while first_half:
                new_string = new_string + first_half.pop(0)
                if second_half:
                    new_string = new_string + second_half.pop(0)
                    
            return new_string