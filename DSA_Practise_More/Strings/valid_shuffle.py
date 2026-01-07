class Solutions:
    def check_length(self, first:str, second:str, result:str) -> bool:
        return len(first) + len(second) == len(result)

    def valid_shuffle(self, first:str, second:str, result:str) -> bool:
        if not self.check_length(first, second, result):
            return False
        
        i, j, k = 0, 0, 0

        while k < len(result):
            if i < len(first) and result[k] == first[i]:
                i+=1
            elif j < len(second) and result[k] == second[j]:
                j+=1
            else:
                return False
            k+=1
        
        return i == len(first) and j == len(second)



if __name__ == "__main__":
    first = "XY"
    second = "12"
    results = ["1XY2", "Y1X2", "Y21XX"]

    s = Solutions()

    for string in results:
        if s.check_length(first, second, string) and s.valid_shuffle(first, second, string):
            print(f"{string} is a valid shuffle of {first} and {second}")
        else:
            print(f"{string} is not a valid shuffle of {first} and {second}")