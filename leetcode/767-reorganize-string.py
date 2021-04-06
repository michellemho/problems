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
            # Alternate adding letter to beginning and end:
            alternating_list = []
            for i, (k,v) in enumerate(sort_list):
                if i%2 == 0:
                    for j in range(v):
                        alternating_list = [k] + alternating_list
                else:
                    for j in range(v):
                        alternating_list.extend(k)
            print(alternating_list)
            # alternate pulling from end and start of ordered_string
            if len(sort_list)%2==0:
                alternating_list = alternating_list[::-1]
            while alternating_list:
                new_string += alternating_list.pop(0)
                if alternating_list:
                    new_string += alternating_list.pop()
            return new_string