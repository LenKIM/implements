#def compare(x, y): 처음 시도한 방법
    # len_x = len(x)
    # len_y = len(y)
    # len = len_x if len_x<len_y else len_y
    #
    # for i in range(len):
    #     if x[i] < y[i]:
    #         return 1
    #     elif x[i] > y[i]:
    #         return -1
    # if len_x == len_y:
    #     return 0
    # elif len_x<len_y:
    #     if x[len-1] < y[len]:
    #         return 1
def compare(x, y):
    str_x = str(x)
    str_y = str(y)

    num_x = int(str_x + str_y)
    num_y = int(str_y + str_x)
    if num_x > num_y:
        return -1
    elif num_x < num_y:
        return 1
    else:
        return 0

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res_nums = sorted(nums, key=cmp_to_key(compare))
        res = "".join(map(str,res_nums))
        # 테스트 케이스에 리스트 요소가 0인 경우가 있어 추가... 예시 자체가 말이 좀 안되는것 같음
        # cnt = 0;
        # for num in nums:
        #     if num == 0:
        #         cnt += 1
        # if cnt == len(nums):
        #     return "0"
        return res