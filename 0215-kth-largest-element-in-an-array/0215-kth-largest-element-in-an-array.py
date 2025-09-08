class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        target_index = n - k #the index of kth largest element in sorted order

        def quickselect(left, right):
            """
            helper function to perform the QuickSelect algorithm
            """

            # randomly choose a pivot index and swap with the leftmost element
            pivot_index = random.randint(left, right)
            nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
            pivot = nums[left]

            # partitioning
            # i moves from left + 1 to right, j moves from right to left

            i ,j = left+1, right
            while i <= j:
                # find element from left that is smaller than pivot
                # find element from right to left which is greater than pivot

                if nums[i] > pivot and nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                
                if nums[i] <= pivot:
                    i += 1
                if nums[j] >= pivot:
                    j -= 1
            # place the pivot in its correct positon
            nums[left], nums[j] = nums[j], nums[left]

            # check if we found the target
            if j == target_index:
                return nums[j]
            
            elif j < target_index:
                return quickselect(j+1, right) # search in the right partition
            
            else:
                return quickselect(left, j-1) # search in the left partiton


        return quickselect(0, n-1)