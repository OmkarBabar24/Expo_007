# q1)Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
from os import remove


# def twoSum(nums, target):
#     num_map = {}  # Dictionary to store number and its index
#
#     for i, num in enumerate(nums):
#         diff = target - num  # Calculate the required pair value
#         if diff in num_map:
#             return [num_map[diff], i]  # Return indices of the pair
#         num_map[num] = i  # Store current number with its index
#
# # Example usage:
# nums = [2, 7, 11, 15]
# target = 9
#
# result = twoSum(nums, target)
# print("Indices of numbers that add up to target:", result)

# Q2) Remove Nth Node From End of List.

# class ListNode:
#     def __init__(self,val=0, next=None):
#         self.val=val
#         self.next=next
#
# def removeNthFromEnd(head: ListNode, n:int) -> ListNode:
#     dummy=ListNode(0,head)
#     fast = slow =dummy
#     #  move fast pointer N+1 steps ahead to maintain a gap
#     for _ in range(n+1):
#         fast = fast.next
#
#     #  move both fast and slow one step at a time
#     while fast:
#         fast = fast,next
#         slow = slow.next
#
#     # skip the target node
#     slow.next = slow.next.next
# result dummy.next

def create_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# helper to print linked list

def print_list (head):
    while head:
        print(head.vel,end=" -> ")
        head = head,next
    print("None")
 # test

head=create_list([1,2,3,4,5])
n = 2
new_head = removeNthFromEnd(head,n)
print_list(new_head)