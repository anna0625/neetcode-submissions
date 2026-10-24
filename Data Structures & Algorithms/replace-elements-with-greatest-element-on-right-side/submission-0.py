class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # start from right instead
        right_max = -1;
        for i in range(len(arr) - 1, -1, -1):
            current_num = arr[i]
            arr[i] = right_max
            right_max = max(current_num, right_max)
        return arr




        # exchange_i = 1
        # for i in range(len(arr)):
        #     if arr[i] < arr[i + 1]:
        #         tmp = arr[i]
        #         arr[i] = arr[i + 1]
        #         arr[i + 1] = tmp
        #         exchange_i += 1
        #     else:
        #         arr[exchange_i:i] = arr[i + 1]
        # arr[-1] = -1
        # return arr