class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        my_stack = digits
        c = 0
        while (my_stack and my_stack[-1] == 9):
            c += 1
            my_stack.pop()
        if (my_stack):
            return my_stack[:len(my_stack) - 1] + [my_stack[len(my_stack) - 1] + 1] + c * [0]
        else:
            return [1] + c * [0]