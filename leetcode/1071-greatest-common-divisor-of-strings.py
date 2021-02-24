class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if strings are equal, then return a string
        if str1 == str2:
            return str1
        else:
            # Determine which is shorter string, if they're equal length, doesn't matter
            if len(str1) >= len(str2):
                longer_string = str1
                short_string = str2
            else:
                longer_string = str2
                short_string = str1
        
            # Check if whole shortstring divides longerstring, then decrease a split and check again
            for i in range(len(short_string)):
                split_point = len(short_string) - i
                splitter = short_string[:split_point]
                # If the splitter splits shortstring, then use this on the longer string
                short_split_test = short_string.split(splitter)
                if all(split_items == '' for split_items in short_split_test):
                    split_test = longer_string.split(splitter)
                    # If it splits, then all items will be empty
                    if all(split_item == '' for split_item in split_test):
                        return splitter
        # If no split found, then return empty string
        result = ""
        return result
