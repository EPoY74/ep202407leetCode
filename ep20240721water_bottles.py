"""
Цель: Поднять скилы по программированию.  Решить задачу с leetcode.
Описание задачи: There are numBottles water bottles that are initially full of water.
 You can exchange numExchange empty water bottles from the market with one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Given the two integers numBottles and numExchange, return the maximum number of water
 bottles you can drink.
Сайт:
https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2024-07-07
Автор: Евгений Петров
email: p174@mail.ru
"""


class Solutions:

    """
    Данный класс решают проблему, сколько бутылок воды можно выпить,
     если сдавать старые бутылки и менять на новые
    """
    def __init__(self):
        pass

    def num_water_bottles(self, num_bottles: int, num_exchange: int) -> int:
        """
        :type num_bottles: int Количество бутылок воды
        :type num_exchange: int Количество бутылок, которые нужно сдать,
        что бы получит одну полную бутылку.
        :rtype: int
        """
        print(f"Бутылок на входе: {num_bottles}")
        if num_bottles < num_exchange:
            return num_bottles
        new_exchanged_bottles: int = int(num_bottles / num_exchange)
        exchanged_bottles:int = num_bottles - new_exchanged_bottles
        exchanged_bottles_tail: int = int(num_bottles % num_exchange)
        print(f"Бутылок c обмена: {new_exchanged_bottles}")
        print(f"Хвост от бутылок {exchanged_bottles_tail}")
        # bottles_drinked = int(num_bottles/num_exchange)

        if (exchanged_bottles_tail == 0):
            total_bottles: int = (num_bottles +
                             self.num_water_bottles(new_exchanged_bottles, num_exchange))
            print(f"Всего бутылок {total_bottles}")
        else:
           remains_bottles = exchanged_bottles_tail
           total_bottles: int = (num_bottles +
                                 self.num_water_bottles(new_exchanged_bottles
                                                        , num_exchange))


        return total_bottles

    def set_water_bottles(self, num_of_bottles: int):
        """
        Устанавливает начальное количество бутылок  водой
        :param num_of_bottles:  - количество бутылок
        :return:
        """

    def get_water_bottles(self):
        """
        Возвращает первоначальное количество бутылок с водой
        :return:
        """

if __name__ == "__main__":
   bottles = Solutions()
   print(bottles.num_water_bottles(
       15,4
   ))