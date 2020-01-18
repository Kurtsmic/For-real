def num_of_fours(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count

numbers = [int(n) for n in input('gime ur list :').split(',')]

print(num_of_fours(numbers))
