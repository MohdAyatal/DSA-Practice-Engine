def find_largest(numbers):
    largest = numbers[0]
    for x in numbers:
        if x > largest:
            largest = x
    return largest 

print(find_largest([3,7,1,9,4]))


def count_vowels(string):
    vowel = 'aeiouAEIOU'
    count = 0
    for x in string:
        if x.lower() in vowel:
            count += 1
    return count
print(count_vowels('HELLO WORLD'))



def reverse_list(numbers):
    left = 0
    right = len(numbers)-1
    while left < right : 
        numbers[left], numbers[right] = numbers[right],numbers[left]
        left +=1
        right -= 1
    return numbers

print(reverse_list([1,2,3,4,5,6]))


def has_duplicate(numbers):
    
    unique = set(numbers)
    if len(unique) < len(numbers):
        return True
    else:
        return False

numbers = [1,2,3,4,5]
print(has_duplicate(numbers))