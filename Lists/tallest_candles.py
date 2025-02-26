"""
Write a function to find the number of tallest candles on a birthday cake
"""
def tallest_candles(candles):
    """

    :param candles:
    :return:
    """
    max_lst =candles[0]
    for i in range(1,len(candles)):
        if candles[i] > max_lst:
            max_lst =candles[i]
    return candles.count(max_lst)
candles =[4,4,1,3]
print(tallest_candles(candles))