import json

language = input('Type "en" to get output in English. Type whatever else to get output in Russian.')

if language == 'en':
    topicsNames = {
        "1": "Cooking",
        "2": "Drama",
        "3": "Occult",
        "4": "Art",
        "5": "Music",
        "6": "Martial Arts",
        "7": "Photography",
        "8": "Science",
        "9": "Sports",
        "10": "Gardening",
        "11": "Video Games",
        "12": "Anime",
        "13": "Cosplay",
        "14": "Jokes",
        "15": "Cats",
        "16": "Justice",
        "17": "Violence",
        "18": "Reading",
        "19": "Gossip",
        "20": "Socializing",
        "21": "Solitude",
        "22": "School",
        "23": "Family",
        "24": "Nature",
        "25": "Money"
    }
else: 
    topicsNames = {
        "1": "Кулинария",
        "2": "Драма",
        "3": "Оккультизм",
        "4": "Искусство",
        "5": "Музыка",
        "6": "Боевые искусства",
        "7": "Фотография",
        "8": "Наука",
        "9": "Спорт",
        "10": "Садоводство",
        "11": "Видеоигры",
        "12": "Аниме",
        "13": "Косплей",
        "14": "Мемы",
        "15": "Кошки",
        "16": "Справедливость",
        "17": "Насилие",
        "18": "Чтение",
        "19": "Сплетни",
        "20": "Общение",
        "21": "Одиночество",
        "22": "Школа",
        "23": "Семья",
        "24": "Природа",
        "25": "Деньги"
    }

with open('Topics.json') as file:
    data = json.load(file)

studentsList = list()

for dictionary in data: 
    studentDict = { }
    studentDict['Name'] = dictionary['Name']
    likes = list()
    dislikes = list()

    studentDict['Likes'] = likes
    studentDict['Dislikes'] = dislikes
    
    for key, value in dictionary.items():
        if value == '1' and key != 'ID':
            studentDict['Dislikes'].append(key)
        elif value == '2' and key != 'ID':
            studentDict['Likes'].append(key)
        else:
            pass
    
    studentsList.append(studentDict)


for dictionary in studentsList:
    listLikes = list(dictionary['Likes'])
    listDislikes = list(dictionary['Dislikes'])

    for i in range(len(listLikes)):
        listLikes[i] = topicsNames[str(listLikes[i])]
    
    for i in range(len(listDislikes)):
        listDislikes[i] = topicsNames[str(listDislikes[i])]

    dictionary['Likes'] = listLikes
    dictionary['Dislikes'] = listDislikes


for dictionary in studentsList:
    with open('output.txt', 'a') as output:
        output.write('\n\n' + dictionary['Name'] + '\n\n')

        for like in dictionary['Likes']:
            output.write('* ' + like + '\n')
        
        output.write('|\n')
        
        for dislike in dictionary['Dislikes']:
            output.write('* ' + dislike + '\n')
