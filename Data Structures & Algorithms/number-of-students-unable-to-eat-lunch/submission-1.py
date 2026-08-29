class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while (len(students)):
            if students[0] == sandwiches[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
            elif sandwiches[0] not in students:
                return len(students)
            else:
                students = students[1:] + [students[0]]
        return 0


"""

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]


Step 1:
[1,1,1,0,0,1]
[1,0,0,0,1,1]

Step 2:
[1,1,0,0,1]
[0,0,0,1,1]


Step 3:
[0,0,1,1,1]
[0,0,0,1,1]

Step 4:
[1, 1, 1]
[0, 1, 1]


"""