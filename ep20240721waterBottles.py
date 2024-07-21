"""
Цель: Поднять скилы по программированию.  Решить задачу с leetcode.
Описание задачи: There are numBottles water bottles that are initially full of water.
 You can exchange numExchange empty water bottles from the market with one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Given the two integers numBottles and numExchange, return the maximum number of water
 bottles you can drink.
Сайт: https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2024-07-07
Автор: Евгений Петров
email: p174@mail.ru
"""

class Solution(object):
    """
    Данный класс решают проблему, сколько бутылок воды можно выпить,
     если сдавать старые бутылки и менять на новыые
    """
    def num_water_bottles(self, num_bottles, num_exchange):
        """
        :type num_bottles: int Количество бутылок воды
        :type num_exchange: int Количество бутылок, которые нужно сдать,
        что бы получит одну полную бутылку.
        :rtype: int
        """
