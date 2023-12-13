# Dictionary
# Mapping between two items

# 
users = {
    "name": "Viktor",
    "password": "whatever"
}

# The way to get data out of a dictionary
print(users["password"])

def count_words(sentence):
    word_count = {}

    for word in sentence:
        word = word.strip(".,!?").lower()

        if word:
            word_count[word] = word_count.get(word, 0) + 1
        
    return word_count

result = count_words("mnogo dulgo izrechenie s pone 15 razlichni dumi za da ima smisul ccqlata tazi rabota")
print(result)

student = {
    "name": "Viktor",
    "grades": {
        "math": 5,
        "physics": 3
    }
}

students = [
    {"name": "John", "age": 22},
    {"name": "Emily", "age": 20},
    {"name": "Mike", "age": 21},
]
