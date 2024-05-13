# list indexing -> getting singular values out of a list

game_prices = [150, 12.5, 7, 18.9, 10]
# game_prices1 = game_prices[4]
# print(game_prices1)

# for loop (with element)

# for game_price in game_prices:
#     print(game_price)

def double_numbers(nums_list):
    output_list = []
    for number in nums_list:
        output_list.append(number)
    return output_list


doubled_numbers = double_numbers([1, 2, 3, 4, 5])
print(doubled_numbers)

def sum_list(nums_list):
    result_number = 0
    for number in nums_list:
        result_number = result_number + number

    return result_number

    
# summed_numbers = sum_list([1, 2, 3, 4, 5])
# print(summed_numbers)
