"""
Учитывая массив целых чисел nums длины n, в котором все
целые числа nums находятся в диапазоне [1, n]
 и каждое целое число появляется один или дважды, верните массив
  всех целых чисел, которые появляются дважды.

Вы должны написать алгоритм, который выполняется за O(n) время
и использует только постоянное дополнительное пространство.
Автор: ЕВгений Петров
e-mail: epoy74@gmail.com

Сайт задачи: https://leetcode.com/problems/find-all-duplicates-in-an-array/
?envType=daily-question&envId=2024-07-07
"""

from typing import List


class Solution:

    """
    Клас для решения задач с leetcode
    """
    def find_duplicates(self, nums: List[int]) -> int:
        """
        Это решение написал тоже я, но leetcod-у оно не
        понравилось.
        Метод ищет дубликаты int во входящем массиве
        :param nums:  Массив int, в котором ищутся дубликат
        :return: Массив дубликатов
        """
        out_list: List[int] = []
        for k in range(len(nums)):
            count_nums: int = nums.count(nums[k])
            if count_nums > 1 and nums[k] not in out_list:
                out_list.append(int(nums[k]))
        return out_list[0]

    def find_duplicate_new(self, nums: List[int]) -> int:
        """
        LeetCode этот ответ принял.... И почему-то помеянлись условия задачи...
        :param nums:
        :return:
        """
        out_list: List[int] = []
        repeated_int: int = 0
        for l in range(len(nums)):
            count_nums: int = nums.count(nums[i])
            if count_nums > 1 and nums[l] not in out_list:
                # out_list.append(int(nums[l]))
                repeated_int = int(nums[l])
        return repeated_int

    def find_duplicate_new_2(self, nums: List[int]) -> int:
        """
        LeetCode этот ответ принял.... И почему-то помеянлись условия задачи...
        :param nums:
        :return:
        """
        nums.sort()
        for j in range(len(nums)):
            if j+1!= len(nums):
                if nums[j] == nums[j+1] :
                    return nums[j]

    def find_duplicate_new_3(self, nums: List[int]) -> int:
        """
        LeetCode этот ответ принял.... И почему-то помеянлись условия задачи...
        :param nums:
        :return:
        """

        # num = enumerate(nums)
        for j in range(len(nums)):
            if nums.count(nums[j]) > 1:
                return nums[j]


    def find_duplicate_new_4(self, nums: List[int]) -> int:
        """
        Корректно по условиям задачи использовать алгоритм Флойдовой черепахи
        :param nums:
        :return:
        """

        tortoise = hare = nums[0]
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if hare == tortoise:
                break
        print(hare)

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        print(hare)
        return hare



if __name__ == "__main__":
    # input_list: List[int] = [0]
    with open("20240723_num_list.txt","r") as f_list_int:
        # for line in f_list_int:
            #input_list.append([int(x) for x in line.split(",")])
        # Читаем содержимое файла и разделяем строки по запятым
        lines = f_list_int.read().split(",")
        # Преобразуем строки в числа
        input_list: List[int] = [int(line) for line in lines]

    # for i in range(len(input_list)):
    #     print(input_list[i])

    input_list.sort()
    for i in range(5):
        print("__________________________________________________________________________________")
    # print(len(input_list))
    # for i in range(len(input_list)):
    #     print(input_list[i])

    my_nums = Solution()
    print(my_nums.find_duplicate_new_4(input_list))
