"""
Учитывая массив целых чисел nums длины n, в котором все
целые числа nums находятся в диапазоне [1, n]
 и каждое целое число появляется один или дважды, верните массив
  всех целых чисел, которые появляются дважды.

Вы должны написать алгоритм, который выполняется за O(n) время
и использует только постоянное дополнительное пространство.
Автор: ЕВгений Петров
e-mail: epoy74@gmail.com

Сайт задачи: https://leetcode.com/problems/find-all-duplicates-in-an-array/?envType=daily-question&envId=2024-07-07
"""

from typing import List


class Solution:

    """
    Клас для решения задач с leetcode
    """
    def find_duplicates(self, nums: List[int]) -> List[int]:
        """
        Метод ищет дубликаты int во входящем массиве
        :param nums:  Массив int, в котором ищутся дубликат
        :return: Массив дубликатов
        """
        out_list: List[int] = []
        for i in range(len(nums)):
            count_nums: int = nums.count(nums[i])
            if count_nums == 2 and nums[i] not in out_list :
                out_list.append(nums[i])
        return out_list


if __name__ == "__main__":
    my_nums = Solution()
    my_nums.find_duplicates( [4,3,2,7,8,2,3,1])