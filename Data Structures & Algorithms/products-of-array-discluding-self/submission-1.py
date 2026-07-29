class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # pre and post fix
        pre = []
        post = []
        final = []
        for i in range(len(nums)):
            pre_num = 1
            post_num = 1
            for j in range(i):
                pre_num *= nums[j]
            for k in range(i+1, len(nums)):
                post_num *= nums[k]
            pre.append(pre_num)
            post.append(post_num)
            print(pre)
            print(post)
            final.append(pre[i]*post[i])
        return final
