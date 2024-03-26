# # # # def miss(day):
# # # #     for dd in range(1,day+1):
# # # #         print(f"书桓走的第{dd}天,想他!")

# # # # miss(2)
# # # # miss(100)
# # # # color = "red"
# # # # if color == "red":
# # # #     print("it's a tomato")
# # # # elif color == "green":
# # # #     print("it's a green pepper")
# # # # elif color == "bee purple":
# # # #     print("i don't know what it is, but only bees can see it")
# # # # else:
# # # #     print("i've never heard of the color", )
# # # # letter='h'
# # # # a="this is your"
# # # # if letter == 'a' or letter == "e" or letter == "i"\
# # # #     or letter == "o" or letter == "u":
# # # #     print(f"{a}" ' a vowel')
# # # # else:
# # # #     print(f"{a}", " not a vowel")
# # # #############59
# # # # some_list=[]
# # # # if some_list:
# # # #     print("There's something in here")
# # # # else:
# # # #     print("key,it's empty!")
# # # ###########60
# # # # vowels= "aeiou"
# # # # letter="h"
# # # # vowels in letter 
# # # # if vowels in letter :
# # # #     print(vowels, "is a vowel")
# # # # else:
# # # #     print("funk")
# # # # letter="v"
# # # # vowel_set={'a','e','i','o','u'}
# # # # print(letter in vowel_set)
# # # # x=6
# # # # print(5<x and x>10)
# # # # print(5<x or x <10)
# # # # print(5<x and not x>10)
# # # #################61
# # # # tweet_limit=280
# # # # tweet_string= "blch"*50
# # # # diff=tweet_limit-len(tweet_string)
# # # # if diff>=90:
# # # #     print("A fitting tweet")
# # # # else:
# # # #     print("went over by",abs(diff))
# # # # tweet_limit=280
# # # # tweet_string= "blch"*50

# # # # if diff:=tweet_limit-len(tweet_string)>=0:
# # # #     print("A fitting tweet")
# # # # else:
# # # #     print("went over by",abs(diff))

# # # # secret=5
# # # # guess=5
# # # # if guess < secret:
# # # #     print("too low")
# # # # elif guess > secret:
# # # #     print("too high")
# # # # else:
# # # #     print("just right")
# # # # small = True
# # # # green = False
# # # # if small:
# # # #     if  green:
# # # #         print("pea")
# # # #     else:
# # # #         print("cherry")
# # # # else:
# # # #     if green:
# # # #         print("wetermelon")
# # # #     else:
# # # #         print("pumpkin")    
# # # # ################65
# # # # poem2="""I do not like thee, Doctor Fell.
# # # #     The reason why, I connot tell.
# # # #     but this I know, and know full well:
# # # #     I do not like thee, Doctor Fell"""
# # # # print(poem2)
# # # # print("give","us","""some""","""space""")
# # # #################66
# # # # num=input("你輸入數字")
# # # # print(type(int(num)))
# # # # print("a\tbv")
# # # # testimony="\"I did nothing!\" he said. \" or that oter thing.\""
# # # # print(testimony)
# # # # speech="The backslash\\bends over backwards to please you."
# # # # print(speech)
# # # # info=r"Type a \n to get a new line in a normal string"   
# # # # print(info)################取消換行
# # # # poem=r'''Boys and girls, come out to play.
# # # # the moon doth shine as bright as day.'''
# # # # print(poem)################原本已經換行+r 還是會換行
# # # ###############################68
# # # # a="release the kraken!"+ "no,wait!"
# # # # print(a)
# # # # a="duck"
# # # # b=a
# # # # c="grey duck"
# # # # print(a,b,c)
# # # #############################69
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[100])
# # # # name='Henny'
# # # # print(name.replace("H","A"))
# # # ############################70
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[:])
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[20:])
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[10:])
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[12:15])
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[::4])
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[4:20:3])字母第4個開始間隔3個到第20個
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[19::4]) 字母第19個開始間隔4個
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(letters[::-1]) 字母倒過來
# # # ######################73
# # # # letters="abcdefghijklmnopqrstuvwxyz"
# # # # print(len(letters))  計算長度  比如有26個字母
# # # # empty=""
# # # # print(len(empty))    符號不算 顯示文字長度
# # # # tasks="get gloves,get mask,give cat vitamins,call ambulance"
# # # # print(tasks.split())任務分割
# # # #######################74
# # # # crypto_list=["Yeti","Bigfoot","Loch Ness Monster"]
# # # # crypto_string=','.join(crypto_list)
# # # # print("Found and signing book deals:",crypto_string)兩段文字結合再一起
# # # # setup="a duck goes into a bar"
# # # # # print(setup.replace("duck","marmoset"))
# # # # print(setup.replace('a','a famous 100'))       替換
# # # #######################75
# # # # world="  earth "
# # # # print(world.strip("@"))
# # # # blurt="what the....!!?"
# # # # print(blurt.strip(".?!"))
# # # import string
# # # # blurt= "what the !!safdf%%"
# # # # # prospector="what in  tarnation.....??!!"
# # # # # print(prospector.strip(string.whitespace+string.punctuation))
# # # # print(blurt.strip(string.punctuation))
# # # ################################76 77 搜尋與選擇
# # # # poem='''all that doth flow we cannot liquid name
# # # #   or else would fire and water  be the same;
# # # #      but that is liquid which is moist and wet
# # # #       ire that property can never get.funny
# # # #      then 'tis not cold that doth the fire put out
# # # # but   tis the wet that makes it die, no doubt '''
# # # # # # word="the"
# # # # # print(poem.isalnum())
# # # # ################################78 79 字母大小變換
# # # # setup="a duck goes into a bar"
# # # # print(poem.rjust(50))
# # # ############################80
# # # # actor="Richard Gere"
# # # # cat="chester"
# # # # weight=29
# # # # print("my wife's favorite actor is %s" % actor)
# # # # a=42
# # # # print("%s" % a)
# # # #############################81 82 83

# # # # thing="woodchuck"
# # # # print("%.3s"% thing)
# # # # thing=98.6
# # # # print("%.1f"% thing)
# # # # thing=9876
# # # # print("%3d"% thing)
# # # # thing="woodchuck"
# # # # place="lake"
# # # # # print("The {} is in the {}".format(thing,place))
# # # # # print("the {0} is in the {0}".format(thing,place))
# # # # # print("the {thing} is in the {place}".format(thing="duck",place="baththb"))
# # # # d={"thing": "duck","place":"bathtub"}
# # # # print("the {0[thing]} is in the {0[place]}".format(d))
# # # # ###################################84 85
# # # # thing="wraith"
# # # # place="window"
# # # # # print("the{:!^8s}is at the{:^8s}".format(thing,place))
# # # # # thing="wereduck"
# # # # # place="werepond"
# # # # # # print(f"the {thing} is in the {place}")
# # # # # print(f"the {thing.capitalize()} is in the {place.rjust(40)}")
# # # # print(f"{thing[1:]=},{place[2:]=}")

# # # #############################85 86
# # # # song=""" when an eel grabs your arm,
# # # # and it cauases great harm,
# # # # that's - a moray!"""
# # # # song= song.replace("m", "M")
# # # # print(song)
# # # # questions=[
# # # #     "we don't serve strings around here. are you a string?",
# # # #     "what is said Father's day in the forest?",
# # # #     "what makes the sound 'sis! Boom! bah!'?"
# # # # ]
# # # # answers=[
# # # #     "an exploding sheep.",
# # # #     "no, i'm a frayed knot.",
# # # #     "'pop! goes the weasel."
# # # # ]
# # # # q_a=((0, 1), (1, 2), (2, 0))
# # # # for q,a in q_a:
# # # #     print("Q:",questions[q])
# # # #     print("A:", answers[a])
# # # #     print() #Q A 的空格

# # # letter="""Thank you for your letter. we are sorry that our {product}
# # # {verbed} in your {room}. please note that it should never
# # # be used in a {room}, especially near any {animals}.

# # # send us your receipt and {amount} for shipping and handing.
# # # we will send you another {product} that, in our tests,
# # # is {percent}% less likely to have {verbed}.

# # # thank you for your support.
# # # sincerely
# # # {spokesman}
# # # {job_title}"""

# # # print(letter.format(
# # #     salutation="ambassador",
# # #     name="Nibbler",
# # #     product="pudding",
# # #     verbed="evaporated",
# # #     room="gazebo",
# # #     animals="octothorpes",
# # #     amount="$1.99",
# # #     percent=88,
# # #     spokesman="shirley iugeste",
# # #     job_title="I Hate this job"))

# # #############################89

# # # count=0
# # # while count<= 5:
# # #     print(count)
# # #     count+=1#   # 不加count+=1 會無限11111  加了之後會123456....

# # # while True:
# # #     stuff = input("String to capitalize [type q to quit]:")
# # #     if stuff == "q":
# # #         break
# # #     print(stuff.capitalize())

# # # while True:
# # #     value = input("Integer, please [q to quit]")
# # #     if value == 'q':  #退出
# # #        break
# # #     number = int(value)
# # #     if number % 2 == 0:  #偶數
# # #         continue
# # #     print(number, "squared is", number*number)

# # # numbers = [7, 3, 5]
# # # position = 0 
# # # while position < len(numbers):
# # #     number = numbers[position]
# # #     if number % 2 == 0:
# # #         print("Found even number",number)
# # #         break
# # #     position +=1
# # # else:   ########break 沒有被呼叫
# # #     print("No even number found")

# # # word = "thud"
# # # offset = 0 
# # # while offset < len(word):  ########第一種
# # #     print(word[offset])
# # #     offset +=1

# # # # for letter in word:   #############第二種
# # # #     print(letter)

# # # for letter in word:    ##############第三種
# # #     if letter == "d":
# # #         break
# # #     print(letter)

# # #####################################94
# # # list( range(0, 11, 3))
# # # # list( range(2, -1, -1))
# # # for i in range(0, 11, 3):
# # #     print(i)

# # # list (range(5, -1, -1, ))
# # # for x in range(5, -1, -1, ):    #########從5開始 到-1  每間格遞數-1  會等於543210
# # #     print(x)


# # guess_me=7
# # number=1
# # while  True #######################################一定要加True 讓if更完整
# #     if  number < guess_me:  
# #         print("too low")
# #     elif  number == guess_me:
# #         print("found it!")
# #         break #######################################一定要加break 才會停止
# #     elif  number > guess_me:
# #         print("oops")
# #         break  
# #     number+= 1

# # guess_me=5

# # for number in range(10):
# #     if  number < guess_me:
# #         print("too low")
# #     elif  number == guess_me:
# #         print("found it!")
# #      #######################################一定要加break 才會停止
# #     else:
# #         print("oops")
        
# #     number+= 1

# ################################################96    97 tuple 
# enpty_tuple=()
# print(enpty_tuple)
# one_marx = ("Groucho", "hello","3.14") 
# print(type(one_marx))
# print(one_marx)
# # 创建一个元组
# my_tuple = (1, 2, 3, 'a', 'b', 'c')

# # 访问元组中的元素
# print("第一个元素:", my_tuple[0])  # 输出: 第一个元素: 1
# print("最后一个元素:", my_tuple[-1])  # 输出: 最后一个元素: c

# # 元组是不可变的，尝试修改元素会引发错误
# # my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# # 元组可以包含不同类型的元素
# another_tuple = ('apple', 3.14, True)

# # 可以通过索引访问不同类型的元素
# print("元组中的字符串:", another_tuple[0])  # 输出: 元组中的字符串: apple
# print("元组中的浮点数:", another_tuple[1])  # 输出: 元组中的浮点数: 3.14
# print("元组中的布尔值:", another_tuple[2])  # 输出: 元组中的布尔值: True

# marx_tuple = ("Groucho", 3.14, "Harpo")
# a, b, c =marx_tuple
# print(type(b))


# password = "swordfish"
# icecream = "tuttifrutti"
# password, icecream = icecream, password  #######################tuple  來對調值
# print(password)

# marx_list = ("Groucho",) +  ("chico", "harpo")
# marx_list = ("how", "are", "you")*3
# print(tuple(marx_list))
# a=(4,2)
# b=(4,2,5)
# print(a==b)
##########################################################98  99   100
# words = ("fresh", "out", "of", "ideas")
# for words in words:   #############################有for就印出直行列表
#     print(words)
# t1 = ("fee", "fie", "foe")
# t2 = ("flop",)
# # print(id(t1))
# # t1 += t2
# # print(id(t1))
# # t1 = ("fee", "fie", "foe")
# # t2 = t1
# print(id(t1) == id(t2))  # 输出: True，t1 和 t2 引用了同一个元组对象

# empty_list = []
# weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# big_birds = ["emu", "ostrich", "casswary"]
# first_names = ["Graham", "John", "Terry", "Terry", "Michael"]
# leap_years = [2000, 2004, 2008]
# randomness = ["Punxsatawney", {"groundhog":"Phil"}, "Feb. 2"]
############################# list
# another_empty_list = list("cat") ####list("cat")印出["c","a","t"]   list=("cat")印出cat 
# print(another_empty_list)

# a_tuple = ("ready", "fire", "aim")
# print(list (a_tuple))

# talk_like_a_pirate_day = "9/19/2019"
# print(talk_like_a_pirate_day.split("/"))
# splitme = "a/b/ /c/d///e"
# print(splitme.split("/"))
# text = input("請輸入")

# #convert to uppercase
# #display on the screen
# print(text.lower())
# movies = ["Avatar", "Titanic", "Avengers", "mango"]
# movies.pop(0)
# print(movies)
# # colors = ["Red", "Blue", "Yellow"]
# # colors.insert(1, "pink")
# # print(colors)
#################################################101 102 103
####append , insert , offset , slice extend , pop , offset ,clear, index(要在print裡面)

# number = ["ab", "cd", "ef", "gh", "tt"]
# number [1:3] = [6, 7, 4, 5]  ###### 1以前不動  可以任意加多少
# number [1:3] = "wat?"
# del number [-1]
# number.remove(1)
# number.pop(1)
# print(number.index("ab"))
# print("aa" in number)

# my_string = ("Groucho", "Chico", "Garpo", "Shico")
# marxes = [1, 3, 5, 0]
# # marxes [0] = "apple" 
# # marxes.append("Zeppo")
# # marxes.insert(2, "Gummo")
# others =["Gummo", "Karl"]
# marxes.extend(others)
# print(marxes)
# separator = " ."
# joined = separator.join(marxes)
# print(joined)
# separated = marxes.split("/")
# print(separated)
# my_string = "apple,banana,orange,grape,mango"
# result = my_string.split(',', 1000000000)
# print(result)  # 输出：['apple', 'banana', 'orange,grape,mango']
# sorted_marxes = sorted(marxes)+
# my_string = "Hello World"
#############################################################109  110  111
# marxes = ["Groucho", "Chico", "Harpo", "Shico"]
# # 将列表中的英文单词首字母变为小写
# lowercase_marxes = [name.lower() for name in marxes]
# # 按照字母顺序排序
# sorted_lowercase_marxes = sorted(lowercase_marxes)
# # 输出排序后的列表
# print(sorted_lowercase_marxes)

# thing = ("mozzarella", "cinderella", "salmonella")
# things = tuple(s.capitalize() for s in thing)   #####capitalize 首字母大寫
# print(things)


# numbers = [2, 1, 4.0, 3]
# numbers.sort()   #########sort = 從小排到大
# print(numbers)
# numbers.sort(reverse= True)  ###sort = 從小排到大  再 ###reverse 從大排到小
# print(len(numbers))

# a = [1, 2, 3]
# print(a)
# b = a
# print(b)
# a [0] = "surprise"
# b [0] = "I hate surprises"
# print(a)

# a = [1, 2, 3]
# b = a.copy()     ######a.copy 改變任何變數都不會影響 b.c.d
# c = list(a)
# d = a [:]
# a [0] = "integer lists are boring"
# a [2] = [8, 9]
####################################################112  113 
# import copy
# a = [1, 2, [8, 9]]
# b = copy.deepcopy(a)
# c =list(a)
# d = a[:]
# a [2] [1] = 10
# print(b)

# cheeses = ["brie", "gjetost", "havarti"]
# for cheese in cheeses:
#     if cheese.startswith("g"):
#         print("I won't eat anything that starts with 'g'")
#         break
#     else:
#         print(cheese)

###############################################114
# cheeses = []
# for cheese in cheeses:
#     print("this shop has some lovely', cheese")
#     break
# else:
#     print("this is not much of a cheese shop =, is it?")
#################################################################用zip 讓變數裡一一對應其他變數
# days = ["moday", "Tuesday", "wednesday"]
# fruits = ["banana", "orange", "peach"]
# drinks = ["coffee", "tea", "beer"]
# desserts = ["tirmisu", "ice cream", "pie", "pudding"]
# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
#     print(day, ": drink", drink, "-eat", fruit, "-enjoy", dessert)

# english = "Monday", "Tuesday", "wednesday"
# french = "lundi", "mardi", "mercredi"
# print(dict(zip(english, french)))

# number_list = []
# number_list.append(1)
# number_list.append(2)
# number_list.append(3)
# number_list.append(4)
# number_list.append(5)
# print(number_list)

# for number in range(1, 60):
#     number_list.append(number)
# print(number_list)

# number_list = list(range(1, 6))
# print(number_list)

# number_list =[number-1 for number in range(1, 5)]
# print(number_list)

# a_list = [number for number in range(0 ,6) if number % 2 ==0]
# a_list = []
# for number in range(0, 8):
#     if number % 1 == 0:
#       a_list.append(number)
#     print(a_list)

# a_list = list(range(1, 8))
# for _ in range(len(a_list), 0, -1):
#     print(' '.join(map(str, a_list)))
#     a_list.pop()

# for i in range(1, 7):
#     for j in range(1, i + 1):
#         print(j, end= "")
#     print()

# rows = range(0, 2)
# cols = range(0, 10)
# for row in rows:
#     for col in cols:
#         print(row, col)

# w = input("請輸入數字")
# s  = input("請輸入數字")
# x = input("請輸入數字")
# z =  input("請輸入數字")   
# cols = range(1,  7)
# rows = range(1, 4)

# cells = [(col, row)for col in cols for row in rows]
# for row, col in cells:    ###########加了這一行顯示兩個數字中間沒有逗點  11  22  33
#       if  col<= 3:
#           print(col)

# for cell in range(1,   10000):
#        print(cell / 100.0)     #10.0   100.0   1000.0  數字越大,顯示小數點後位越多

# small_birds = ["hummingbird", "finch"]
# extingct_birds = ["dodo", "passenger pigeon", "Norwegian Blue" ]
# carol_birds = [3, "French hens", 2, "turtledoves"]
# all_birds = [small_birds, extingct_birds, carol_birds]
# print(all_birds[1][0])   ################取print(all_birds[1]extingct_birds [0]dodo)

# number_thing = (number for number in range(1, 6))
# print(type(number_thing))

######################################################119
# 7.1
# x= int(input("請輸入你出生年份"))
# years_list =[1980, 1981, 1982, 1983, 1984, 1985]  
# # print(years_list[5])
# if  x in years_list:
#     print(f"你是{x}出生的")
# else:
#     print("你猜錯了")

# thing = ["mozzarella", "cinderella", "salmonella"]
# # # things = [i for i in thing]
# # # print(things)
# print(thing[1].capitalize())
# print(thing)
# thing[1] = thing[1].capitalize()
# thing[0] = thing [0].upper()
# thing.remove("salmonella")
# del thing[0:2]
# print(thing)

# print(thing)
# name = "ada lovelace"
# print(name.title())    ##########使用title 變數不能有括號

# surprise = ["Groucho", "Chico", "Harpo"]
# surprise[2] = surprise[2].lower()
# surprise[2] = surprise[2][::-1]
# print(surprise[2].capitalize())

# even = [number for number in range(10) if number % 2 == 0]
# print(even)

# start1 = ["fee", "fie", "foe"]
# rhymes = [
#     ("flop", "get a mop"),
#     ("fope", "turn the rope"),
#     ("fa", "get your ma"),
#     ("fudge", "call the judge"),
#     ("fat", "pet the cat"),
#     ("fog", "walk the dog"),
#     ("fun", "say we're done"),
# ]
# start2 = "Someone better"
# start1_caps = " ".join([word.capitalize() + " ! "  for word in start1])
# for first, second in rhymes:
#     print(f"{start1_caps} {first.capitalize()}!")
#     print(f"{start2} {second},")

###################################################121 122 123
# empty_dict = {}
# print(empty_dict)

# bierce = {

#     "day": """A period of twenty-four hours, mostly misspent""",
#     "positive": """Mistaken at the top of one's voice""",
#     "misfortune": """the kind of fortune that never misses""" 
# }

# print(bierce)
# acme_customer = {"first": "white", "middle": "E", "last": "Coyote"}
# print(acme_customer)
# import json
# acme_customer = dict(first="white", middle="E", last= "Coyote")
# # print(json.dumps(acme_customer))
# x =dict(name = "Elmer", ef="hunter")
# print(x)

# lol = [ ["a", "b"], ["c", "d"], ["e", "f"]] ####有lol一定要用 [ [] ]
# print(dict(lol))

# lol = [ ("a", "b"), ("c", "d"), ("e", "f")]   ####用[ () ]印出來會顯示  a : b
# print(dict(lol))

# tol = [ ("a", "b"), ("c", "d"), ("e", "f")]   ####用[ () ]印出來會顯示  a : b
# print(dict(tol))  ##############雙字元字串的串列

# tos = ("ab", "cd", "ef")  ######雙字元字串的tuple
# print(dict(tos))

#################################################124  125  126

# pythons = {
#     "Chapman": "Graham",
#     "Cleese": "john",
#     "Idle": "Eric",
#     "Jones": "Terry",
#     "palin": "Michael",
# }
# pythons["Gilliam"] = "Terry"  ############加入成員
# print(pythons)

# some_pythons = {
#     "Graham": "Chapman",
#     "John": "cleese",
#     "Eric": "Idle",
#     "Terry": "Gilliam",
#     "MIchael": "palin",
# }
# # some_pythons["Gilliam"] = "Terry"  ############加入成員
# print(some_pythons.get("Jofsadf", "not a python"))

# y = 8
# z = lambda x:x * y
# print(z(6))

# signals = {"green": "go", "yellow": "go faster", "red": "smile for the camera"}
# # print(signals.keys())        ######keys   
# # print(list(signals.keys()))  ######list   字典的抬頭
# # print(list(signals.values()))  ######values 字典的內容
# # print(list(signals.items()))     ######items  字典全部
# print(len(signals))               #######len    字典長度  (3)

#####################################127  128  129  130 131
# first = {"a":"agony", "b":"bliss"}
# second = {"b":"bagels", "c":"candy"}
# third = {"d": "donuts"}
# print({**first,**second, **third})  ######print ({})加** 才能把字典結合

# pythons = {
#     "Chapman": "Graham",
#     "Cleese":  "John",
#     "Gilliam": "Terry",
#     "Idle":    "Eric",
#     "Jones":   "Terry",
#     "Palin":   "Michael",
# }
# others = {"Marx": "Groucho", "Howard": "Moe"}
# ithers = {"open": "my", "you": "school"}
# pythons.update(others)   #########用update()結合
# pythons.update(ithers) 
# print(pythons)

# first = {"a": 1 , "b": 2}
# second = {"b": "platypus"}
# first.update(second)
# print(first)

# pythons = {
#     "Chapman": "Graham",
#     "Cleese":  "John",
#     "Gilliam": "Terry",
#     "Idle":    "Eric",
#     "Jones":   "Terry",
#     "Palin":   "Michael",
# }
# others = {"Marx": "Groucho", "Howard": "Moe", "a": "a"}
# pythons.update(others)   #########用update()結合
# # del pythons["Marx"]     #########用del刪除字典裡一個單字
# # print(pythons.pop("Palin"))  ######pop放在print裡面 字典相對應的單字也會印出來
# # print(len(pythons))
# # pythons.clear()                ###########clear清除所有項目
# # pythons ={}                    ###########{}放在最下面就能清除所有項目
# print("Chapman" in pythons)      ###########在print裡面用in來確認是否單字存在

# signals = {"green": "go",
#            "yellow": "go faster",
#            "red": "smaile for the camera"}
# origina_signals = signals.copy()   ########copy在上面blue字典就不會印出來
# signals["blue"] = "confuse evertone"   #############[]=XXX 才能加入一個字典單字
# # save_signals = signals
# print(origina_signals)

# signals = {"green": "go",
#            "yellow": "go faster",
#            "red": ["stop", "smile"]}
# # signals_copy = signals.copy()  
# signals["red"][1] = "sweat"   #######signals [][]改變red串列的值
# print(signals)

# import copy
# signals = {"green": "go",
#            "yellow": "go faster",
#            "red": ["stop", "smile"]}
# signals_copy = copy.deepcopy(signals)  ######深度拷貝
# signals["red"][1] = "sweat" ##########擺在deepcopy上面印出sweat 擺在下面印出smile
# print(signals_copy)

#####################################132  133   134
# a = {1:1, 2:2, 3:3}
# b = {3:3, 1:1, 2:2}
# print(a == b)     ###############比較字典 ==
# a = {1: [1, 2], 2: [1], 3:[1]}
# b = {1: [1, 2], 2: [1], 3:[1]}
# print(a == b)

# accusation = {"room": "ballroom", "weapon": "lead pipe",
#               "person": "col. Mustard"}
# for card in accusation:     ########accustion 印出字典的鍵
#     print(card)
# for value in accusation.values():  ####accusation.values 印出字典的內容
#     print(value)
# for item in accusation.items():   ######accusation.items 印出所有字典
#     print(item)
# for card, contents in accusation.items():  ####讓字典變成一句話
#     print("Card", card, "has the contents", contents)

# {Rey_expression: value_expression for expression in iterable}
# word = "letters"   
# # letter_counts = {letter:word.count(letter) for letter in word}
# letter_counts = {letter:word.count(letter) for letter in set(word)}  ##印出順便不一樣
# print(letter_counts)  ############letters單字 印出 L.1個 E.2個 T.2個 r.1個

# vowels = "aeiou"
# word = "onomatopoeia"   
# vowel_counts = {letter: word.count(letter) for letter in set(word)
#                 if letter in vowels}  
# print(vowel_counts)  #兩個單字 印出有幾個字母重疊
    
####################################  135 136 137 138 139 140 141
# empty_set = set()
# print(empty_set)
# even_numbers = {0, 2, 4, 6, 8}
# print(even_numbers)
# odd_numbers = {1, 3, 5, 7, 9}
# print(odd_numbers)
# print(set("letters"))    ########用set印出是無順序的

# print(set(["Dasher", "Dancer", "Prancer", "Mason-Dixon"]))  ###串列  set是無序
# print(set(("Ummagumma", "Echoes", "Atom Heart Mother")))   ####tuple set是無序
# print(set({"apple": "red", "orange": "orange", "cherry": "red"}))###字典的抬頭
# reindeer = set(["Dasher", "Dancer", "Prancer", "Mason-Dixon"])
# print(len(reindeer)) ##用set就要用()  沒有set也能印出len   
# s = set ((1, 2, 3))
# # s.add(4) ##用add加入4
# s.remove(3) ##用remove刪除3
# print(s)
# funriture = set(("sofa", "ottoman", "table"))
# for piece in funriture:
#     print(piece) ####for加set印出也是無順序
# drinks = {
#     "martini": {"vodka", "vermouth"},
#     "black russian": {"vodka", "kahlua", "coffee"},
#     "white russian": {"cream", "kahlua", "vodka"},
#     "manhattan": {"rye", "vermouth", "bitters"},
#     "screwdriver": {"orange juice", "vodka"}
# }
# # for  name, contents in drinks.items():
# #     if "vodka" in contents:  #####找出有vodka
# #         print(name)

# # for name, contents in drinks.items():
# #     if "vodka" in contents and not ("vermouth" in contents or "cream" in contents):
# #         print(name)   ###找出vodka並挑出內容有 "vermouth" "cream"就不印出

# # for name, contents in drinks.items():
# #     if contents & {"vermouth", "orange juice"}:
# #         print(name)   ##找出有vermouuth和orange 

# # for name,contents in drinks.items():
# #     if "vodka" in contents and not contents & {"vermouth", "cream"}:
# #         print(name)

# bruss = drinks["black russian"]  ####black  title
# wruss = drinks["white russian"]  ####white  title
# a = {1100, 1100, 1, 1100}
# b = {10, 1100}
# print(a&b)  ####找出兩個的內容相同  並列印
# print(a.intersection(b))
# print(bruss&wruss)  ##找出兩個的內容相同 並列印
# print(bruss|wruss)  ##印出兩個的內容
# print(a|b)  ###a和b 印出內容不相同 
# print(a.union(b))
# print(a-b)   ###a-b 找出兩個的內容相 並列印 a 剩的內容  如果是b-a 就印出 b 剩的內容
# print(a.difference(b))  ##加difference就變成集合
# print(bruss^wruss)  ##找出兩個的內容不相同 並列印
# print(a<=b)
# print(a.issubset(b))
# print(bruss<=wruss)
# print(a<=a)
# print(a.issubset(a)) ###issubset變成不可集合
# print(a<b)
# print(a<a)
# print(bruss<wruss)
# print(a>=b)
# print(a.issuperset(b)) ###superset超集合是子集合的相反
# print(wruss>=bruss)
# print(a>=a)
# print(a.issuperset(a))###任何集合都是它自己的超集合
# print(a>b)
# print(wruss>bruss)
# print(a>a)  #############不可能自己是超集合
# a_set = {number for number in range(1,6) if number % 3 ==1}
# print(a_set)
# print(frozenset([3, 2, 9])) ########用frozenset = 冰凍凝固
# print(frozenset(set([1, 3, 2])))
# print(frozenset({3, 1, 2}))
# print(frozenset((2, 1, 3)))
# fs = frozenset([3, 1, 2])
# print(fs)
# print(fs.add(3))####用frozenset = 冰凍凝固 就無法用add加入

########################################142  143
# marx_list = ["Groucho", "Chico", "Harpo"]
# marx_tuple = ("Groucho", "Chico", "Harpo")
# marx_dict = {"Groucho": "banjo", "Chico": "piano", "Harpo": "harp"}
# marx_set = {"Groucho", "Chico", "Harpo"}  ###用{} 無法只編寫print印出一個單字
# print(marx_list[2])
# print(marx_tuple[2])
# print(marx_dict["Harpo"])
# print(marx_set)    #####如果要印出Chico 要編寫if "Chico" in marx_set:  print("Chico")
# # print("Harpo" in marx_list)
# # print("Harpo" in marx_tuple)
# # print("Harpo" in marx_dict)
# # print("Harpo" in marx_set)

# marxes = ["Groucho", "Chico", "Harpo"]
# pythons = ["Chapman", "Cleese", "Gilliam", "jones", "Palin"]
# stooges = ["Moe", "Curly", "Larry"]
# # tuple_of_lists = marxes, pythons, stooges  ###三個串列當作一個tuple  ()
# # print(tuple_of_lists)  
# # list_of_lists = [marxes, pythons, stooges]  ###三個串列當作list []
# # print(list_of_lists)
# dict_of_lists = {"Marxes": marxes, "pythons": pythons, "stooges": stooges} ##{}
# print(dict_of_lists)

# houses = {
#     (44.79, -93.14, 285): "My House",
#     (38.89, -77.03, 13): "the white house"
# }
# print(houses)
################################  8.1
# e2f = {
#     "dog": "chien", 
#     "cat": "chat", 
#     "walrus": "morse"
# }
# print(e2f)
################################  8.2
# for name, contents in e2f.items():
#     if "morse" in contents:
#         print(name)
################################  8.3

################################  8.4
# print(e2f.get("dog"))
################################  8.5
# print(e2f.keys())
################################  8.6
life = {
    "animals": {
    "cats": ["Henri", "Grumpy", "Lucy"],
    "octopi": {}, 
    "emus":   {}                                                    
    },
    "plants": {},
    "other": {} 
}
###############################   8.7
# for i in life:
#     print(i)
###############################   8.8
# print(life.get("animals"))
###############################   8.9
# print(life["animals"]["cats"])  ###非常重要 非常重要 取得包中包
###############################   8.10
# squares = {key: key*key for key in range(10)}  ###
# print(squares)##{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
###############################   8.11
# odd = {number for number in range(10) if number % 2 == 1}
# print(odd)  ##印出奇數1.3.5.7.9     
###############################   8.12
# for thing in ("got %s" % number  for number in range(10)): ##
#     print(thing)##直行印出0-9, 用()順序印出0-9 用{}隨機排序印出0-9
###############################   8.13
# keys = ("opimist", "pessimist", "troll")
# values =(
#     "The glass is half full",
#     "Thre glass is half empty",
#     "How did you get a glass?"
# )###用()順序印出來  用{}隨機排序印出來   (dict =  key-value pairs) 鍵值對
# moive=dict (zip(keys, values))
# print(moive)
###############################   8.14
# titles = ["Crenture of Habit", "Crewel Fate", "Sharks On a plane"]
# plots = ["A nun turns into a monster", "A haunten yarn shop", "Check your exits"]
# moive = dict(zip(titles, plots))
# print(moive)
##############################################################################################
##############################145 146 147 148 149 150 151 152 153 154 
# def do_nothing():
#     pass
# print(do_nothing())

# def make_a_sound():
#     print("quack")
# print(make_a_sound())

# def agree():
#     return False
# if agree():
#     print("splendid")
# else:
#     print("That was unexpected")

# def echo(anything):
#     return anything + " "  + anything
# print(echo("Rumplestiltskin"))

# def commentary(color):
#     if color == "red":
#         return "It's a tomato."
#     elif color == "green":
#         return "It's a green peper,"
#     elif color == "bee purple":
#         return "I don't know what it is, but only bees can see it."
#     else:
#         return "I've never heard of the color" + color + "."
# comment = commentary("blue")
# print(comment)

# thing = None  ######None是有用的,雖然當它被當成布林來估值,會被視為false
# if thing:
#     print("It's some thing")
# else:
#     print("It's no thing")

# thing = None 
# if thing is None:
#     print("It's nothing")
# else:
#     print("It's something")

# def whatis(thing):
#     if thing is None:
#         print(thing, "is None")
#     elif thing:
#         print(thing, "is True")
#     else:
#         print(thing, "is False")
# print(whatis(None))
# print(whatis(True))
# print(whatis(False))
# print(whatis(0))
# print(whatis(0.0))
# print(whatis(""))
# print(whatis(''))
# print(whatis(''''''))
# print(whatis(()))
# print(whatis([]))
# print(whatis({}))
# print(whatis(set()))                    

# def menu(wine, entree, dessert):
#     return{"wine": wine, "entree": entree, "dessert": dessert}
# print(menu("chardonnay", "chicken", "cake"))
# print(menu("beef", "bagel", "bordeaux", ))
# print(menu(entree="beef", dessert = "bagel", wine = "bordeaux"))##避免忘記位子在哪,可以這樣編寫
# print(menu("frontenac", dessert = "flan", entree = "fish",))

# def buggy(arg, result=[]):
#     result.append(arg) #印出一次a後,會留下a,繼續印第二次b,所以是[a] [a, b]
#     print(result)
# buggy("a")
# buggy("b")

# def works(arg):
#     result = []
#     result.append(arg) #會開印出來,所以是["a"] ["b"]
#     return result
# print(works("a"))
# print(works("b"))

# def nonbuggy(arg, result=None):
#     if result is None:
#         result = []
#     result.append(arg)####修正的做法,傳入別的東西來代表第一次呼叫
#     print(result)
# nonbuggy("a")

# def print_args(*args):#args是一种用于函数定义中的特殊语法，它允许函数接受任意数量的位置参数，并将它们作为一个元组传递给函数体内部的代码。在你的例子中，使用args使得函数print_args可以接受任意数量的位置参数，而不限制其数量
#     print("Positional tuple:", args)#
# # print_args() ##( )不傳入引數時,args不會提供任何東西
# print_args(3, 2, 1, "wait!", "uh....")

# def print_more(required1, required2, *args):###第三個後都是*args的
    # print("Need this one:", required1)
    # print("Need this one too:", required2)
    # print("All the rest:", args)
# print_more("cap", "gloves", "scarf", "monocle", "mustache wax")

# def print_args(*args):
#     print("Positional tuple:", args)
# print_args(2, 5, 7, "x")
# args = (2, 5, 7, "x")
# print_args(args) ##印出來會多一個()和,
# print_args(*args)
# *args #SyntaxError: can't use starred expression here

# def print_kwargs(**kwargs):
#     print("keyword arguments:", kwargs)
# print_kwargs()
# print_kwargs(wine = "merlot", entree = "mutton", dessert = "macaroon")


# def example_func(*args):
#     print("Positional arguments:", args)#Positional arguments=位置參數要加 *
# example_func(1, 2, 3, 4, 5)
# 输出：Positional arguments: (1, 2, 3, 4, 5)
# def example_func(**kwargs):  #kwargs 適合用於字典
#     print("Keyword arguments:", kwargs)#Keyword arguments=關鍵字參數要加 ** 適合用於字典
# example_func(a=1)   ##要用()
# 输出：Keyword arguments: {'a': 1, 'b': 2, 'c': 3}

#################################155  156  157  158 159 160 161
# def print_data(data, *, start=0, end = 1000):
#     for value in (data[start:end]):
#         print(value)
# data = ["a", "b", "c", "d", "e", "f"]
# print_data(data)
# print_data(data, start=4)
# print_data(data, end=2)

# outside = ["one", "fine", "day"]
# def mangle(arg):
#     arg[1] = "terrible!"
# # print(outside) #打outside  只會印出one fine day
# mangle(outside)  #要加入這一行 才會印出one terrible day
# print(outside)

# def echo(anything):
#     "echo returns its input argument"
#     return anything
# def print_if_ture(thing, check):
#     """prints the first argument if a second argument is true.
#     The operation is:
#      1. check whether the *second* argument is true.
#      2. If it is, print the *first* argument.
#     """
#     if check:
#         print(thing, check)
# help(echo)
# print(echo.__doc__)

# def answer():  #########函式是一級公民
#     print(42)  
# answer() #必須要打answer()才會印出42
# def run_something(func):
#     func()
# run_something(answer)
# print(type(run_something))

# def add_args(arg1, arg2):
#     print(arg1, arg2)
#     print(f"add_args({arg1}, {arg2})") #一定要加{} 才會印出add_args(5, 9)
# add_args(33,22) ##我自己想的
# print(type(add_args))
# def run_something_with_args(fun, arg1, arg2):
#     fun(arg1, arg2)
# run_something_with_args(add_args, 5,9)

# def sum_args(*args):
#     return sum(args) #把數字加總, 丟回print
# def run_with_positional_args(func, *args): #在把數字丟到sum
#     return func(*args)
# print(run_with_positional_args(sum_args, 1, 2, 3, 4)) #把數字丟到func
# print(sum_args(1, 2, 3, 4)) #把func和def run_with刪除 直接打這一行也能印出 10

# def outer(a, b):
#     def inner(c, d):
#         return c + d
#     return inner(a, b)
# print(outer(4, 7))

# def knights(saying):
#     def inner(quote):
#         return "we are the knights who say: '%s' " %quote
#     return inner(saying)
# print(knights("Ni!"))

# def knights2(saying):
#     def inner2():
#         return "we are the knights who say: '%s'" % saying
#     return inner2   ###它是一個closure 一種動態建立 並且記得它來自哪裡

# a = knights2("Duck")
# b = knights2("Hasenpfeffer")
# print(type(a))
# print(type(b))
# print(a) #它們是函式, 但它們也是closure
# print(b)
# print(a()) #它們會記得自己被knights2建立時使用saying
# print(b())

####################################161 162 163 164 165 166
# def edit_story(words, func):
#     for word in words:
#         print(func(word))
# stairs = ["thud", "meow", "thud", "hiss"]
# def enliven(word):
#     return word.capitalize() + '!'
# edit_story(stairs, enliven)
# edit_story(stairs, lambda word: word.capitalize() + "!")#只要用這一行 就不用加def enliven
# edit_story(stairs, lambda word: word) #不加title大寫就這樣寫

# print(sum(range(1, 101)))


# ranger = my_range(1, 10)#first 開始1  last 最後9  step 間隔1
# print(ranger)
# for x in ranger:
    # print(x) #迭代 1 2 3 4
# for try_again in ranger:
#     print(try_again)

# def my_generator():##################chat GPT
#     yield 1
#     yield 2
#     yield 3
# gen = my_generator()
# print(next(gen))  # 输出：1
# print(next(gen))  # 输出：2
# print(next(gen))  # 输出：3
# def my_generator():  ################我修改chat GPT
#     yield int(input("請輸入"))
#     yield int(input("請輸入"))
#     yield int(input("請輸入"))
# gen = my_generator()
# user = next(gen)  # 获取生成器中的值
# user1 = next(gen) #三個yield 要用next
# user2 = next(gen) 
# print(f"你輸入的數字是 {user}")
# print(f"你輸入的數字是 {user1}")
# print(f"你輸入的數字是 {user2}")

# genobj = (pair for pair in zip (["a", "b"], ["1", "2"]))
# print(genobj)
# for thing in genobj:
#     print(thing)

# def document_it(func):
#     def new_function(*args, **kwargs):
#         print("Running function:", func.__name__)
#         print("Positional arguments:", args)
#         print("Keyword arguments:", kwargs)
#         result = func(*args, **kwargs)
#         print("Result:", result)
#         return result 
#     return new_function
# def add_ints(a, b):
#     return a + b
# print(add_ints(3, 5))

# cooler_add_ints = document_it(add_ints)
# print(cooler_add_ints(3, 5))

# @document_it
# def add_ints(a, b):
#     return a + b
# print(add_ints(3, 5))

# def square_it(func):
#     def new_function(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * result
#     return new_function
# @document_it
# @square_it
# def add_ints(a, b):
#     return a + b
# print(add_ints(3, 5))

# @square_it
# @document_it
# def add_ints(a, b):
#     return a + b
# print(add_ints(3, 5))

#########################################167 168 169 170
# animal = "fruitbat"
# def print_global():
#     print("insde print_global:", animal)
# print("at the top level:", animal)
# print_global()

# def change_and_print_global():
#     print("inside change_and_print_global:", animal)
#     animal = "wombat"
#     print("after the change:", animal)
# change_and_print_global()

# def change_local():
#     animal = "wombat"
#     print("inside change_local:", animal, id(animal))
# change_local()
# print(animal)
# print(id(animal))

# animal = "fruitbat"
# def change_and_print_global():
#     global animal
#     animal = "wombat"
#     print("inside change_and_print_global:", animal)
# print(animal)
# change_and_print_global()

# animal = "fruitbat"
# def change_local():
#     animal = "wombat"  #區域變數
#     print("locals", locals())
# print(animal)
# change_local()
# print("globals:", globals()) #稍微重新排列, 以便顯示

# def amazing():
#     """This is the amazing function.
#     want to see it again?"""
#     print("This function is named:", amazing.__name__)
#     print("And its docstring is:", amazing.__doc__)
# amazing()
# def dive():
#     return dive()
# dive()

# def flatten(lol):
#     for item in lol:
#         if isinstance(item, list):
#             for subitem in flatten(item):
#                 yield subitem
#         else:
#             yield item  #以上程式能讓123456789整齊排列
# lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
# print(flatten(lol))
# print(list(flatten(lol)))
# def flatten(lol):
#     for item in lol:
#         if isinstance(item, list):
#             yield from flatten(item)
#         else:
#             yield item  #更簡化寫
# lol = [1, 2, [3, 4, 5], [6, [7, 8, 9], []]]
# print(list(flatten(lol)))

#####################################171
# short_list = [1, 2, 3]
# position = 5
# print(short_list[position])  #以上錯誤範例
# short_list = [1, 2, 3]
# position = 5
# try:
#     short_list[position] # try內有錯誤會丟到except, try內沒有錯誤直接跳過except
# except:
#     print("Need a position between 0 and", len(short_list)-1, "but got", position)
          
# short_list = [1, 2, 3]
# while True:
#     value = input("Position[q to quit]?")
#     if value == "q":
#         break
#     try:
#         position = int(value)
#         print(short_list[position])
#     except IndexError as err:
#         print("Bad index:", position)
#     except Exception as other:
#         print("Something else broke:", other)

# class UppercaseException(Exception):
#     pass
# words = ["eenie", "meenie", "miny", "MO"]
# for word in words:
#     if word.isupper():
#         raise UppercaseException(word)
# class OopsException(Exception):  ###一定定義OopsException然後pass
#     pass
# try:
#     raise OopsException("panic")
# except OopsException as exc:
#     print(exc)

##############################9.1
# def good():
#     return ["Harry", "Ron", "Hermione"]

# print(good())
##############################9.2
# def get_odds():
#     for number in range(1, 10, 2):
#         yield number
# count = 1
# for number in get_odds():
  
#     if count == 3:
#         print("The third odd number is ", number)
#         break
#     count += 1 #count寫在上面比較慢一步到達
###############################9.3
# def test(func):
#     def new_func(*args, **kwargs):
#         print("start")
#         result = func(*args, **kwargs)  
#         print("end")
#         return result
#     return new_func
# @test  ##用裝飾品才能呼叫 def test
# def greeting():
#     print("Greetings, Earthling")
# greeting()

# def test(func):
#     def new_func(*args, **kwargs):
#         print("start")
#         result = func(*args, **kwargs)  
#         print("end")
#         return result
#     return new_func
# @test  ##用裝飾品才能呼叫 def test
# def greeting():
#     print("Greetings, Earthling")
# greeting()

# ###############################9.4
# class OopsException(Exception):  ###一定定義OopsException然後pass
#     pass
# try:
#     raise OopsException()
# except OopsException:
#     print("Caught an oops")


#################################176 177 178 179 180 181 182 183 184 185 186 187 189 190
# class Cat():
#     pass
# class Cat:
#     pass
# a_cat =Cat()
# another_cat = Cat() ##以上示範錯誤

# class Cat():
#     pass
# a_cat = Cat()
# print(a_cat)
# another_cat = Cat()
# print(another_cat)

# a_cat.age = 3
# a_cat.name = "Mr. Fuzzybuttons"
# a_cat.nemesis = another_cat
# a_cat.nemesis.name = "Mr. Bigglesworth"
# print(a_cat.age)
# print(a_cat.name)
# print(a_cat.nemesis)
# print(a_cat.nemesis.name)

# class Cat:
#     def __init__(self):
#         pass

# class Cat():
#     def __init__(self, name):
#         self.name = name
# furball = Cat("Grumpy")
# print("Our latest addition:" , furball.name)

# class Car():
#     pass
# class Yugo(Car):
#     pass
# print(issubclass(Yugo, Car))
# give_me_a_car = Car()
# give_me_a_yugo = Yugo()
# print(give_me_a_car)
# print(give_me_a_yugo)

# class Car():
#     def exclaim(self):
#         print("I'm a Car!")
# class Yugo(Car):
#     pass
# give_me_a_car = Car()
# give_me_a_yugo = Yugo()
# give_me_a_car.exclaim()
# give_me_a_yugo.exclaim()

# class Car():
#     def exclaim(self):
#         print("I'm a Car!")
# class Yugo(Car):
#     def exclaim(self):
#         print("I'm a Yugo!Much like a Car, but more Yugo-ish.")
# give_me_a_car = Car()
# give_me_a_yugo = Yugo()
# give_me_a_car.exclaim()
# give_me_a_yugo.exclaim()

# class Person():
#     def __init__(self, name):
#         self.name = name
# class MDPerson(Person):
#     def __init__(self, name):
#         self.name = "Doctor " + name
# class JDPerson(Person):
#     def __init__(self, name):
#         self.name = name + ", Esquire"
# person = Person("Fudd")
# doctor = MDPerson("Fudd")
# lawyer = JDPerson("Fudd")
# print(person.name)
# print(doctor.name)
# print(lawyer.name)

# class Car():
#     def exclaim(self):
#         print("I'm a Car!")
# class Yugo(Car):
#     def exclaim(self):
#         print("I'm a Yugo! Much like a Car, but more Yugo-ish")
#     def need_a_push(self):
#         print("A little help here?")
# give_me_a_car = Car()
# give_me_a_yugo = Yugo()
# give_me_a_yugo.need_a_push() #
# give_me_a_car.need_a_push()  #通用的Car物件 無法呼叫 

# class Person():  ######   用super() 來取得父類別的幫助
#     def __init__(self, name):
#         self.name = name

# class EmailPerson(Person):
#     def __init__(self, name, email): #使用__init__()呼叫有額外的額外email的參數
#         super().__init__(name) #super可以繼承Person屬性與方法
#         self.email = email
        
# class EmailPerson(Person):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
# bob = EmailPerson("Bob Frapples", "bob@frapples.com")
# print(bob.name)
# print(bob.email)

# class Animal:
#     def says(self):
#         return "I speak!"
# class Horse(Animal):
#     def says(self):   #如果Horse沒有用says()方法 會使用Animal的says回傳"I speak"
#         return "Neigh!"

# class Donkey(Animal):
#     def says(self): #如果Donkey沒有用says()方法 會使用Animal的says回傳"I speak"
#         return "Hee-haw!"

# class Mule(Donkey, Horse):
#     pass
# class Hinny(Horse, Donkey):
#     pass
# print(Mule.mro()) #印出來 可以祖宗十八代
# print(Hinny.mro()) #印出來 可以祖宗十八代
# mule = Mule()
# hinny = Hinny()
# print(mule.says())   #印出Donkey的Hee-haw
# print(hinny.says())  #印出Horse的Neigh

# class PrettyMixin():
#     def dump(self):
#         import pprint
#         pprint.pprint(vars(self))
# class Thing(PrettyMixin):
#     pass

# t = Thing() #一定要擺第一個以下是打印內容
# t.name = "Nyarlathontep"
# t.feature = "ichor"
# t.age = "eldritch"
# t.tt  = "幹你娘"
# t.dump() #一定要擺最後一個以上是打印內容

# a_car = Car() ##1449行
# a_car.exclaim() ##1449行
# Car.exclaim(a_car) #也可以顛倒過來編寫
        
# class Duck():
#     def __init__(self, input_name):
#         self.name = input_name
# fowl = Duck('Daffy')
# print(fowl.name)
# fowl.name = "Daphne"
# print(fowl.name)

# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     def get_name(self):
#         print("inside the getter")
#         return self.hidden_name
#     def set_name(self, input_name):
#         print("inside the setter")
#         self.hidden_name = input_name
# don = Duck("Donald")
# print(don.get_name())
# don.set_name("Donna")
# print(don.get_name())
        
# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     def get_name(self):
#         print("inside the getter")
#         return self.hidden_name
#     def set_name(self, input_name):
#         print("inside the setter")
#         self.hidden_name = input_name
#     name = property(get_name, set_name)

# don = Duck("s3")  #印出幹你娘
# print(don.get_name()) #印出getter   一定要加don才打印 
# don.set_name("Donna") #印出setter
# print(don.get_name()) #印出Donna
######################以下不同的寫法   
# don = Duck("Donald")
# print(don.name)
# don.name = "Donna"
# print(don.name)
########################
# #####################################190 191 192 193 194 195
# class Duck():
#     def __init__(self, input_name):
#         self.hidden_name = input_name
#     @property
#     def name(self):
#         print("inside the getter")
#         return self.hidden_name
#     @name.setter
#     def name(self, input_name):
#         print("inside the setter")
#         self.hidden_name = input_name
# fowl = Duck("幹你娘")
# print(fowl.name)
# fowl.name = "Donald"
# print(fowl.name)

# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
#     @property
#     def diameter(self):
#         return 2 * self.radius
# c = Circle(10)
# print(c.radius)
# print(c.diameter)
# c.radius = 7
# print(c.diameter)
# c.diameter = 20  ###只打印 無法修改

# class Duck():
#     def __init__(self, input_name):
#         self.__name = input_name
#     @property
#     def name(self):
#         print("inside the getter")
#         return self.__name
#     @name.setter
#     def name (self, input_name):
#         print("insid the setter")
#         self.__name = input_name
# fowl = Duck("Howard")
# print(fowl.name)
# fowl.name ="Donald"
# print(fowl.name)
# print(fowl__name)  ##無法存取__name屬性
# print(fowl._Duck__name) ##這樣編寫才能存取

# class Fruit:
#     color = "red"
# blueberry = Fruit()
# print(Fruit.color)
# print(blueberry.color)

# blueberry.color = "blue"
# print(blueberry.color)
# print(Fruit.color)

# Fruit.color = "orange"
# print(Fruit.color)
# print(blueberry.color)

# new_fruit = Fruit()
# print(new_fruit.color)

# class A():
#     count = 0
#     def __init__(self):
#         A.count += 1
#     def exclaim(self):
#         print("I'm an A!")
#     @classmethod
#     def kids(cls):
#         print("A has", cls.count, "little objects.")
# easy_a = A()
# breezy_a = A()
# wheezy_a = A()
# four_a   = A()
# A.kids()

# class CoyoteWeapon():
#     @staticmethod  #裝飾器
#     def commercial():
#         print("This CoyoteWeapon has been brought to you by Acme")
# CoyoteWeapon.commercial()

# ###################################195 196 197 198 199 200 
# class Quote():
#     def __init__(self, person, words):
#         self.person = person
#         self.words = words
#     def who(self):
#         return self.person
#     def says(self):
#         return self.words + "."
# class QuestionQuote(Quote):
#     def says(self):
#         return self.words + "?"
# class ExclamationQuote(Quote):
#     def says(self):
#         return self.words + "!"
# hunter = Quote("Elmer Fudd", "I'm hunting wabbits")
# print(hunter.who(), "says:", hunter.says())

# hunted1 = QuestionQuote("Bugs Bunny","what's up, doc")
# print(hunted1.who(), "says:", hunted1.says())

# hunted2 = ExclamationQuote("Daffy Duck", "It's rabbit season")
# print(hunted2.who(), "says:", hunted2.says())

# class BabblingBrook():
#     def who(self):
#         return "Book"
#     def says(self):
#         return "Babble"
# brook = BabblingBrook()
# def who_says(obj):
#     print(obj.who(), "says", obj.says())
# who_says(hunter)
# who_says(hunted1)
# who_says(hunted2)

# class Word():
#     def __init__(self, text):
#         self.text = text
#     def equals(self, word2):
#         return self.text.lower() == word2.text.lower()
# first = Word("ha")
# second = Word("HA")
# third = Word("eh")
# print(first.equals(second)) #ha 與 HA的小寫時 是相等的
# print(first.equals(third)) #eh 與 ha 不相等
##################################以下不同寫法
# class Word():
#     def __init__(self, text):
#         self.text = text
#     def __eq__(self, word2):
#         return self.text.lower() == word2.text.lower()
# first = Word("ha")
# second = Word("Ha")
# third = Word("eh")
# print(first == second)
# print(first == third)
# first = Word("ha")
# print(first)
# #######################################
# class Word():
#     def __init__(self, text):
#         self.text = text
#     def __eq__(self, word2):
#         return self.text.lower() == word2.text.lower()
#     def __str__(self):
#         return self.text
#     def __repr__(self):
#         return "Word("     + self.text   + ")"
# first = Word("ha")
# print(repr(first))  # 使用 __repr__
# print(str(first))   # 使用 __str__
#############################################201 202 203 
# class Bill():
#     def __init__(self, description):
#         self.description = description

# class Tail():
#     def __init__(self, length):
#         self.length = length

# class Duck():
#     def __init__(self, bill, tail):
#         self.bill = bill
#         self.tail = tail
#     def about(self):
#         print("This duck has a", self.bill.description,
#               "bill and a", self.tail.length, "tail")
# a_tail = Tail("long")
# a_bill = Bill("wide orange")
# duck = Duck(a_bill, a_tail)
# duck.about() ######  類別可以繼承 ##### #### 模組不行#######

# from collections import namedtuple
# Duck = namedtuple("Duck", "bill tail")
# duck = Duck("wide orange", "long")
# print(duck)
# print(duck.bill)
# print(duck.tail)
####################################以下第二種寫法
# parts = {"bill": "wide orange", "tail": "long"}
# duck2 = Duck(**parts)
# print(duck2)
# ################################### 以下第三種寫法
# duck2 = Duck(bill = "wide orange", tail = "long")
# print(duck2)
# ###################################以下第四種寫法
# duck3 = duck2._replace(tail ="magnificent")
# print(duck3)
# ###################################以下第五種寫法
# duck_dict = {"bill": "wide orange", "tail": "long"}
# print(duck_dict)
# ##########加入字典
# duck_dict["color"] = "green"
# print(duck_dict)
# ##########不能加入不具名tuple
# duck.color = "green"
#########################################204 205 206
# class TeenyClass():
#     def __init__(self, name):
#         self.name = name
# teeny = TeenyClass("itsy")
# print(teeny.name)
# #########################以下第二種寫法
# from dataclasses import dataclass
# @dataclass
# class TeenyDataClass:
#     name: str
#     name: type
# teeny = TeenyDataClass("bitsy")
# print(teeny.name)

# from dataclasses import dataclass
# @dataclass
# class AnimalClass:
#     name: str
#     habitat: str
#     teeth: int = 0
# snowman = AnimalClass("yeti", "Himalayas", 46)
# duck = AnimalClass(habitat = "lake", name = "duck")
# print(snowman)
# print(duck)
# print(duck.habitat)
# print(snowman.teeth)

######################################10.1
# class Thing():
#     pass
# print(Thing)
# example = Thing()
# print(example)
######################################10.2
# class Thing2():
#     letters = "abc"
# print(Thing2.letters) ###Thing2.letters要結合才能打印
# ######################################10.3
# class Thing3():
#     def __init__(self):
#         self.letters = "xyz"
# print(Thing3.letters)  ###錯誤示範
# something = Thing3()
# print(something.letters)
########################################10.4
# class Element():
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
# hydrogen = Element("Hydrogen", "H",  1)#10.4
# # ########################################10.5   延續10.4
# el_dict = {"name": "Hydrogen", "symbol": "H", "number": 1}
# hydrogen = Element(el_dict["name"], el_dict["symbol"], el_dict["number"])
# print(hydrogen.name)
# hydrogen = Element(**el_dict)
# print(hydrogen.name)
##########################################10.6  延續10.5
# class Element():   第一種打印
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#     def dump(self):
#         print("name = %s, symbol = %s, number = %s" %
#              (self.name, self.symbol, self.number))
# hydrogen = Element(**el_dict) 
# hydrogen.dump()
#######################################10.7  延續10.6 
# class Element():   #########第二種打印
#     def __init__(self, name, symbol, number):
#         self.name = name
#         self.symbol = symbol
#         self.number = number
#     def __str__(self):
#         return("name = %s, symbol = %s, number = %s" %   ###改成return
#              (self.name, self.symbol, self.number))
# hydrogen = Element(**el_dict) 
# print(hydrogen)
#####################################10.8
# class Element():   #########第三種打印  單獨印出
#     def __init__(self, name, symbol, number):
#         self.__name = name
#         self.__symbol = symbol
#         self.__number = number
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def symbol(self):
#         return self.__symbol
#     @property
#     def number(self):
#         return self.__number
# hydrogen = Element("Hydrogen", "H", 1)
# print(hydrogen.name)
# print(hydrogen.symbol)
# print(hydrogen.number)
#####################################10.9
# class Beer():
#     def eats(self):
#         return "berries"
# class Rabbit():
#     def eats(self):
#         return "clover"
# class Octothorpe():
#     def eats(self):
#         return "campers"
# b = Beer()
# R = Rabbit()
# O = Octothorpe()
# print(b.eats())
# print(R.eats())
# print(O.eats())
#####################################10.10
# class Laser():
#     def does(self):
#         return "disintergrata"
# class Claw():
#     def does(self):
#         return "crush"
# class SmartPhone(): 
#     def does(self):
#         return "ring"
# class Robot():
#     def __init__(self):
#         self.laser = Laser()
#         self.claw = Claw()
#         self.smartphone = SmartPhone()
#     def does(self):
#         return """I have many attachments:
# My laser, to %s.
# My claw, to %s.
# My smartphone, to %s. """ %(
#     self.laser.does(),
#     self.claw.does(),
#     self.smartphone.does()
# )
# robbie = Robot()
# print(robbie.does())
#########################################207
#模組建立練習
########################################216 217 218 219
# periodic_table = {"Hydrogen" : 1, "Helium": 2}
# # print(periodic_table)

# carbon = periodic_table.setdefault("Carbon", 12) #setdefault和get很像
# print(carbon)         
# print(periodic_table) #可以同時打印periodic和carbon

# helium = periodic_table.setdefault("Helium", 947)
# print(helium)         #會印出2
# print(periodic_table) #不會印出Helium

# from collections import defaultdict
# periodic_table = defaultdict(int)  #預設字典
# periodic_table["Hydrogen"] = 1
# print(periodic_table["Lead"]) #不會打印出 Lead
# # print(f"Lead: {periodic_table['Lead']}") #這樣才能打印出Lead
# print(periodic_table)  #印出Hydrogen = 1 Lead = 0

# from collections import defaultdict

# def no_idea():   #defaultdict 回傳指派缺漏的值
#     return "Huh?" #當沒有bestiary["C"] 就印出Huh?

# bestiary = defaultdict(no_idea)
# bestiary["A"] = "Abominable Snowman"
# bestiary["B"] = "Basilisk"
# print(bestiary["A"])
# print(bestiary["B"])
# print(bestiary["C"])  #印出Huh

# bestiary = defaultdict(lambda: "Huh1?") #可以在呼叫裡用lambda定義自己預設值
# print(bestiary["E"])
# ###in可以用來製作自己的計數器  第一種編寫
# from collections import defaultdict

# food_counter = defaultdict(int)
# for food in ["spam", "spam", "eggs", "spam"]:
#     food_counter[food] += 1

# for food, count in food_counter.items(): #items()用在於字典
#     print(food, count)
# # 第二種編寫
# dict_counter = {}
# for food in ["spam", "spam", "eggs", "spam"]:
#     if not food in dict_counter:
#         dict_counter[food] = 0
#     dict_counter[food] += 1
# for food, count in dict_counter.items():
#     print(food, count)
# 第三種編寫
# from collections import Counter
# breakfast = ["spam", "spam", "eggs", "spam"]
# breakfast_counter = Counter(breakfast)
# print(breakfast_counter)
# # 第四種編寫
# print(breakfast_counter.most_common())
# print(breakfast_counter.most_common(1))
# print(breakfast_counter)
# #####製作一個新的串列  lunch
# lunch = ["eggs", "eggs", "bacon"]
# lunch_counter = Counter(lunch)
# print(lunch_counter)
# ###   結合兩個計數器的第一種做法
# print(breakfast_counter + lunch_counter)
# ###  可以用 - 減去計數器
# print(breakfast_counter - lunch_counter)
# print(lunch_counter - breakfast_counter )
# ### 用交集運算子&來取得公同的項目
# print(breakfast_counter & lunch_counter)
# ### 聯集運算子 | 來取得所有項目
# print(breakfast_counter | lunch_counter)
#################################################219 220 221
# quotes = {
#     "Moe": "A wise guy, huh?",
#     "Larry": "ow!",
#     "Curly": "Nyuk nyuk!",
# }
# for stooge in quotes:
#     print(stooge)
# ####建立有序字典 orderedDict
# from collections import OrderedDict
# quotes = OrderedDict([
#     ("Moe", "A wise guy, huh?"),
#     ("Larry", "Ow!"),
#     ("Curly", "Nyuk nyuk!"),
# ])
# for stooge in quotes:
#     print(stooge)
# ###堆疊 + 佇=(住)列 == deque
# def palindrome(word):
#     from collections import deque
#     dq = deque(word)
#     while len(dq) > 1:
#         if dq.popleft() != dq.pop():  ##第一個字母和最後一個字母比較 
#             return False              ##相同就刪除 並回到while
#     return True
# print(palindrome("a"))
# print(palindrome("racecar"))
# print(palindrome(""))
# print(palindrome("radar"))
# print(palindrome("halibut"))
# ####字串反過來, 快速第寫出回文檢查程式
# def another_palindrome(word):
#     return word == word[::-1]
# print(another_palindrome("radar"))
# print(another_palindrome("halibut"))
############################################221
# import itertools
# for item in itertools.chain([1, 2], ["a", "b"]):
#     print(item)
#####cycle() 是一種無限迭代器,可循環遍歷它的引數
# import itertools
# for item in itertools.cycle([1, 2]):
#     print(item) ##無限印出
###accumulate()可計算累計值,在預設情況下,它會計算總和
# import itertools
# for item in itertools.accumulate([1, 2, 3, 4]): # 1 + 2 + 3 +4
#     print(item)
###accumulate()第二個引數提供一個函式來取代加法,函式接收兩個引數,回傳一個結果
###itertools模組有許多函式,組合與排列置換(permutation)可以幫你節省時間
# import itertools
# def multiply(a, b):
#     return a * b
# for item in itertools.accumulate([2, 2, 32], multiply): 2 * 2 * 32
#     print(item)

# from collections import OrderedDict
# from pprint import pprint
# quotes = OrderedDict ([
#     ("Moe", "A wise guy, huh?"),
#     ("Larry", "Ow!"),
#     ("Curly", "Nyuk nyuk!"),
# ])
# print(quotes)   ####跟書上有差別 再觀察
# for name, quote in quotes.items():
#     pprint(f"({name}, {quote}),")
# #########################取得隨機值
# from random import choice
# print(choice ([23, 9, 46, "bacon", 0x123abc]))
# print(choice (("a", "one", "and-a", "two")))
# print(choice (range(100)))
# print(choice ("alphabet"))
#########################取得隨機值 使用sample()函式可以一次取得多個值
# from random import sample
# print(sample([23, 9, 46, "bacon", 0x123abc], 2))  #最後一個數字是你取想多個數值
# print(sample(("a", "one", "and-a", "two"), 2))  #最後一個數字是你取想多個數值
# print(sample(range(100),4))  #最後一個數字是你取想多個數值
# print(sample(("alphabet"),7))  #最後一個數字是你取想多個數值
##############要在取得任何範圍之內隨機整數,可以使用randint()
# from random import randint
# print(randint(38, 74))  #38-74 隨機印出一個整數
##########randrange()很像range(),它也有開始(包含)與結束(不包含)整數,以及一個選用的整數步幅
# from random import randrange 
# print(randrange(38, 74))
# print(randrange(38, 74, 10))  #只會隨機印出38 48 58 68 
# print(randrange(38, 74, 20))  #只會隨機印出38 58 
##########若要取得介於0.0和1.0之間的隨機實數(浮點數)
# from random import random
# print(random())  ###隨機印出浮點數
# print(random())  ###隨機印出浮點數
# print(random())  ###隨機印出浮點數
############################################11.1
# import zoo
# zoo.hours()
############################################11.2
# import zoo as menagerie
# menagerie.hours()
###########################################11.3
# from zoo import hours
# hours()
##########################################11.4
# from zoo import hours as info
# info()
##########################################11.5
# plain = {"a": 1, "b": 2, "c": 3}
# print(plain)
##########################################11.6
# from collections import OrderedDict  ##OederedDict 一定要搭配collections
# fancy = OrderedDict ([("a", 1), ("b", 2), ("c", 3)])
# print(fancy)
##########################################11.7
# from collections import defaultdict #defaultdict=預設字典
# dict_of_lists = defaultdict(list)
# dict_of_lists["c"].append("something for a")
# print(dict_of_lists["c"])
# ##############################################231 232 233 234 235 236 237
# def unicode_test(value):
#     import unicodedata
#     name = unicodedata.name(value)
#     value2 =unicodedata.lookup(name)
#     print('value="%s", name="%s", value2="%s"' % (value, name, value2))
# ###########################"LATIN SMALL LETTER E WITH ACUTE"
#     print(unicodedata.name("\u00e9"))
#     print(unicodedata.lookup("LATIN SMALL LETTER E WITH ACUTE"))
# ############################從一般的ASCII字母開始:   
# # print(unicode_test("A"))
# # LETTER E WITH ACUTE"
# # print(place)###########################ASCII 標點符號:
# print(unicode_test("$"))
# # # ############################Unicode 貨幣字元:
# # print(unicode_test("\u00a2"))
# # # ############################另一個Unicode 貨幣字元:
# # print(unicode_test("\u20ac"))
# # # ############################特殊符號
# # print(unicode_test("\u2603"))
# # ############################cafe
# place = "cafe"
# print(place)
# ###########################現在我們可以用代碼或名稱來指定字串 cafe
# place = "caf\u00e9"
# print(place)
# place = "caf\N{LATIN SMALL LETTER E WITH ACUTE}"
# ###########################我們直接在字串插入e 但我們也可以用附加的方式建立字串
# u_umlaut = "\N{LATIN SMALL LETTER U WITH DIAERESIS}"
# print(u_umlaut)
# drink = "Gew" + u_umlaut + "rztraminer" 
# print("Now I can finally have my", drink, "in a", place)
# ###########################len()函式會計算Unicode字元的數目, 不是byte
# print(len("$"))
# print(len("\U0001f47b"))
# ##########################如果知道Unicode數字ID,可以使用標準的ord()與chr()函式在整數ID與單字元Unicode字串之間快速轉換
# print(chr(233))
# print(chr(0xe9))
# print(chr(0x1fc6))
##############編碼
#編碼名稱        說明
#"ascii"        古老的七位元ASCII
#"utf-8"        八位元可變長度編碼,這是你幾乎一定會使用的格式
#"latin-1"      也稱為ISO 8859-1
#cp-1252"       一般的Windons編碼
#unicode-escape" Python Unicode常值格式, \u' XXXX或 \U'XXXXXXX
############################可以將任何東西編碼成UTF-8 我們將Unicode字串"\2603"指派給名稱snowman
# snowman = "\u2603"
# print(snowman)
# print(len(snowman))
# ds = snowman.encode("utf-8")
# print(len(ds))
# print(ds)
# # ds = snowman.encode("ascii")
# print(snowman.encode("ascii", "replace"))
# print(snowman.encode("ascii", "backslashreplace"))
# print(snowman.encode("ascii", "xmlcharrefreplace"))
###########################################解碼
# place = "caf\u00e9"
# print(place)
# print(type(place))
# place_bytes = place.encode("utf-8")
# print(place_bytes)
# print(type(place_bytes))
# place2 = place_bytes.decode("utf-8")
# print(place2)
# # place3 = place_bytes.decode("ascii")
# # print(place3)
# place4 = place_bytes.decode("latin-1")
# print(place4)
# place5 = place_bytes.decode("windows-1252")
# print(place5)
# #########################################238 239 2400
# import html
# print(html.unescape("&egrave"))
# ############################十進制
# print(html.unescape("&#233;"))
# ############################十六進制
# print(html.unescape("&#xe9;"))
# ############################實體轉換字典
# from html.entities import html5
# print(html5["egrave"])
# print(html5["egrave;"])
#############################要進行反向的轉換,要先用ord()
# import html
# char = "\u00e9"
# dec_value = ord(char)
# print(html.entities.codepoint2name[dec_value])
############################要處裡有多個字元的Unicode字串時,請用兩個步驟來轉換
# place = "caf\u00e9"
# byte_value = place.encode("ascii", "xmlcharrefreplace")
# print(byte_value)
# print(byte_value.decode())
###########################標準化
# eacute1 = "é"                                        # UTF-8 貼上
# eacute2 = "\u00e9"                                   #Unicode 碼位
# eacute3 = \
#         "\N{LATIN SMALL LETTER E WITH ACUTE}"        #Unicode 名稱
# eacute4 = chr(233)                                   # 十進制 byte值
# eacute5 = chr(0xe9)                                  # 十六進制 byte值
# print(eacute1, eacute2, eacute3, eacute4, eacute5)
# print(eacute1 == eacute2 == eacute3 == eacute4 == eacute5)
# # ###########################################試著做一些健全性測試
# # import unicodedata 
# # print(unicodedata.name(eacute1))
# # print(ord(eacute1))                                  # 十進制整數
# # print(0xe9)                                          #Unicode 十六進制整數
# ############################################接著藉著結合一般的e和重音符號
# eacute_combined1 = "e\u0301"
# eacute_combined2 = "e\N{COMBINING ACUTE ACCENT}"
# eacute_combined3 = "e" + "\u0301"
# print(eacute_combined1, eacute_combined2, eacute_combined3)
# print(eacute_combined1 == eacute_combined2 == eacute_combined3)
# print(len(eacute_combined3))
# print(eacute1 == eacute_combined1 )
# #################可以用unicodedata 模組的 normalize("NFC", eacute_combined1)
# import unicodedata
# eacute_normalized = unicodedata.normalize("NFC", eacute_combined1)
# print(len(eacute_normalized))
# print(eacute_normalized == eacute1)
# print(unicodedata.name(eacute_normalized))
######################################################241 242 243 244
# import re
# result = re.match("You", "Young Frankenstein")
# print(result)
# ########################進行較複雜的比對時,可以先編譯模式來提升之後的比對速度
# import re
# youpattern = re.compile("You")
# print(youpattern)
# ########################接著用編譯過的模式來執行比對
# import re
# result = youpattern.match("Young Frankenstein")
# print(result)
################match()之外還有其他比對模式與來源的方式
################search() 會回傳第一個符合的,如果有的話
################findall()會回傳一個串列,裡面有所有不重疊的,符合的實例,如果有的話
################split()會在符合模式的地方拆開來源,並回傳一個存有每一段字串的串列
################sub()會接收一個替換引數,將來源中符合模式的部分都換成替換物
###############################match()來確定開頭是否符合
# import re
# source = "Young Frankenstein"
# m = re.match("You", source)   #match 在source的開頭開始處理
# if m:               #match 回傳一個物件: 看看符合的是什麼
#     print(m.group())
# ###########################加 ^ 也能回傳 You
# m = re.match("^You", source)   #match 在source的開頭開始處理
# if m:               #match 回傳一個物件: 看看符合的是什麼
#     print(m.group())
###########################Frank是否會回傳
# import re
# source = "Young Frankenstein"
# m = re.match("Frank", source) ###########不會回傳也不回應
# if m:
#     print(m.group())  
#########################縮短這個範例
# import re
# source = "Young Frankenstein"
# if m := re.search("Frank", source):
#     print(m.group()) #########印出Frank
########################用search()來看看Frank有沒有在來源字串的任何地方
# import re
# source = "Young Frankenstein"
# m = re.search("Frank", source)
# if m:
#     print(m.group()) ###########印出Frank
########################改變模式,並且再次使用match()來比對開頭
# import re
# source = "Young Frankenstein"
# m = re.match(".*Frank", source)#" . * Frank" .代表任何單一字元  *代表零或多個它前面的東西,
# if m:                   ###match 回傳物件                . *一起用使用代表任何數量的字元(包括零)
#     print(m.group())  #########match()回傳符合,.*Frank的字串:Young Frank
# #########################用search()找到第一個符合的對象
# import re
# source = "Young Frankenstein"
# m = re.search("Frank", source)
# if m:              #####search 回傳一個物件
#     print(m.group())
# #########################用findall()尋找所有符合的對象
# import re
# source = "Young Frankenstein"  #這字串有四個 n
# m = re.findall("n", source)
# print(m) ####findall 回傳一個串列
# print("Found", len(m), "matches")  ##Found 4 matches = 找到四個n
# #########################在 "n" 之後有任何字元的模式
# import re
# source = "Young Frankenstein"
# m = re.findall("n.", source)  ##"n." 找出n加後面的字母 如果後面沒字母就不打印
# print(m)
# #########################必須用?來表示在"n"後面的字元是可有可無
# import re
# source = "Young Frankenstein"
# m = re.findall("n.?", source) ### "n.?"顯示後面的字母和後面沒字母
# print(m)
# #########################用split()在符合的地方拆開
# import re
# source = "Young Frankenstein"
# m = re.split("n", source)  ######字串有n,會分割變成一個串列
# print(m)  ####split 會回傳一個串列
# #########################用sub()來替換符合的對象
# import re
# source = "Young Frankenstein"
# m = re.sub("n", "?", source)  ##把n變成?
# print(m)  #sub 會回傳一個字串
##################################################245 246 247 248 249 
#######\d 一個數字, \D 一個非數字, \w 一個英數字元, \W 一個非英數字元, \s 一個空白字元
#######\S 一個非空白字元, \b 一個單字範圍(介於\w與\W,無論順序為何), \B 一個非單字範圍
#python string 模組定義了許多可用來進行測試的字串常數,我們將使用printable,它有100個可列
#印ASCII字元,包括大小寫的字母.數字.空白字元與標點符號
# import string 
# import re
# printable = string.printable
# print(len(printable)) 
# print(printable[0:50])  ##印出數字與英文字母
# print(printable[50:])  ##印出英文與%^*&()
#####################printable裡面的字元有哪些是數字?
# print(re.findall("\d", printable)) #123456789
# print(re.findall("\w", printable))  #數字與英文字母
# print(re.findall("\s", printable)) #在 Python 中，這些空白字元包括空格 (' ')、水平制表符 ('\t')、
# #換行符 ('\n')、回車符 ('\r')、垂直制表符 ('\x0b') 和換頁符 ('\x0c')。
# x = "abc" + "-/*" + "\u00ea" + "\u0115"
# print(re.findall("\w", x)) #一如預期,這個模式只找到三個字母
# ############################看這些範例可能會讓你眼花撩亂,我們先定義source字串
# source = """I wish I may, I wish I might
# .... Have a dish of fish tonight."""
# print(re.findall("wish", source))  ##找出wish,並印出來
# #########################接著找出任何地方的wish或fish
# print(re.findall("wish|fish", source)) ##找出wish和fish,並印出來
# #########################在開頭尋找wish
# print(re.findall("^wish", source))  ##印出[]
# #########################在開頭尋找 I wish
# print(re.findall("^I wish", source)) ##印出 I wish
# #########################在結尾尋找fish
# print(re.findall("fish$", source)) ##[]
# #########################最後,在結尾尋找fish tonight.
# print(re.findall("fish tonight.$", source)) ###fish tonight
# #######^與$字元稱為錨點,^會定錨搜尋字串的開頭,$會定錨搜尋結尾, .$會比對行尾的任何字元,包括句點
# #######所以它找到東西,為了更精華,我們應該轉義句點.用字面值來比對
# print(re.findall("fish tonight\.$", source))
# #######搜尋W或F接著是ish的模式
# print(re.findall("[wf]ish", source))
# #######尋找一或多個w,s或h
# print(re.findall("[wsh]+", source))
# #######尋找開頭是ght接下來是非英數字元的模式
# print(re.findall("ght\W", source))
# #######尋找wish之前的I
# print(re.findall("I (?=wish)", source))
# #######最後, I之後的wish
# print(re.findall("(?<=I) wish", source))
# #######尋找fish
# print(re.findall("\bfish", source))
# #######用r字元來停用python的轉義字元
# print(re.findall(r"\bfish", source))
# #######模式:指定match()輸出
# m = re.search(r"(. dish\b).*(\bfish)", source)
# print(m.group())
# print(m.groups())
# #######(?P< name > expr) 它會比對expr,將匹配的實例放在name群組
# m = re.search(r"(?P<DISH>. dish\b).*(?P<FISH>\bfish)", source)#寫法和上面不一樣,但印出一樣
# print(m.group())
# print(m.groups())
# print(m.group("DISH"))
# print(m.group("FISH"))
#################################################250 251 252 253 254 255
#################################################二進制資料
########用blist的串列建立一個bytes變數,稱為the_bytes.與一個bytearray變數稱為the_byte_array:
# blist = [1, 2, 3, 255]      #########十六進制  = X    255 = xff
# the_bytes = bytes(blist)
# print(the_bytes)
# the_bytes_array = bytearray(blist)
# print(the_bytes_array)
# ########bytes值的表示法是以一個b與一個引號字元開頭的,接下來是十六進制序列
# print(b"\x61")
# print(b"\x01abc\xff")
########這個範例為了告訴你,你無法改變bytes變數
# blist = [1, 2, 3, 255]
# the_bytes = bytes(blist)
# the_bytes[1] = 127  ###無法改變
# print(the_bytes)
########但是bytesarray變數比較聽話,可以更改
# blist = [1, 2, 3, 255]
# the_byte_array = bytearray(blist)
# print(the_byte_array)
# the_byte_array[1] = 127  
# print(the_byte_array)
# the_bytes = bytes(range(0, 256))
# the_bytes_array = bytearray(range(0, 256))
# print(the_bytes)
# print(the_bytes_array)
###################################用struct來轉換二進制資料
# import struct
# valid_png_header = b"\x89PNG\r\n\x1a\n"
# data = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" +\
# b"\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc9"
# if data[:8] == valid_png_header:
#     width, height = struct.unpack(">LL", data[16:24])
#     print("Valid PNG, width", width, "height", height)
# else:
#     print("Not a valid PNG")
# print(data[16:20])
# print(data[20:24])
# print(0x9a)
# print(0x8d)
# print(struct.pack(">L", 154))
# print(struct.pack(">L", 141))
# print(struct.unpack(">2L", data[16:24]))
# print(struct.unpack(">16x2L6x", data))
##############################下面是使用construct從data bytestringt擷取PNG長寬的方式
# from construct import struct, magic, UBInt32, Const, String
# # https://github.com/construct
# fmt = struct("png",
#       magic(b"\x89PNG\r\n\x1a\n"),
#       UBInt32("length"),
#       Const(String("type", 4), b"IHDR"),
#       UBInt32("width"),
#       UBInt32("height")
# )
# data = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" +\
#     b"\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0"
# result = fmt.parse(data)
# print(result)
###############################################256
############用binascii()來轉換byte/字串
# import binascii
# valid_png_header = b"\x89PNG\r\n\x1a\n"
# print(binascii.hexlify(valid_png_header))
# ###############這個東西也可以轉回去
# print(binascii.unhexlify(b"89504e470d0a1a0a"))
###############位元運算子  256頁
######################################12.1
# import unicodedata
# mystery = "\U0001f4a9"  #大便=\U0001f4a9
# print(mystery)
# print(unicodedata.name(mystery)) # 一大堆便便
# ######################################12.2
# pop_bytes = mystery.encode("utf-8")
# print(pop_bytes)
# ######################################12.3
# pop_string = pop_bytes.decode("utf-8") ##也能印出大便
# print(pop_string)
# ######################################12.4
# mammoth = """
# We have seen thee, queen of cheese,
# Lying quietly at your ease,
# Gently fanned by evening breeze,
# Thy fair form no flies dare seize.

# All gaily dressed soon you'll go
# To the great Provincial show,
# To be admired by many a beau
# In the city of Toronto.

# Cows numerous as a swarm of bees,
# Or as the leaves upon the trees,
# It did reuire to make thee pleace,
# And stand unrivalled, queen of cheese.

# May you not receive a scar as 
# We have heard that Mr. Harris
# Intends to send you off as far as
# The great world's show at paris.

# Of the youth beware of these,
# For some of them might rudely squeeze
# And bite your cheek, then songs or glees
# We could not sing, oh! queen of cheese.

# We'rt thou suspended from balloon,
# You'd cast a shade even at noon,
# Folks would think it was the moon
# About to fall and crush them soon.
# """
# ####################################12.5
# import re
# pat = r"\bc\w*"                   #r"\b(e)搜尋
# print(re.findall(pat, mammoth))
# pat = r"\ba\w*"
# print(re.findall(pat, mammoth))
# ####################################12.6
# pat = r"\bc\w{3}\b"    #### {3} 找出所有C開頭的四字母單字
# print(re.findall(pat, mammoth))
# pat = r"\bc\w{3}"      #### {3} 取得C開頭所有單字的前四個字母  .chee.se
# print(re.findall(pat, mammoth))
# ####################################12.7
# pat = r"\b\w*r\b"    ##取得結尾是r的單字的正確結果
# print(re.findall(pat, mammoth))
# pat = r"\b\w*1\b"   ##取得結尾是l的單字不太理想
# print(re.findall(pat, mammoth))
# pat = r"\b[\w']*l\b" ###正確取得11
# print(re.findall(pat, mammoth))
# pat = r'\b[\w\']*l\b'###正確取得11
# print(re.findall(pat, mammoth))
# pat = r"\b[\w\']*l\b"###正確取得11(外面用雙引號,裡面用單引號)
# print(re.findall(pat, mammoth))
# ####################################12.8 取得三個母音
# pat = r'\b[^aeiou]*[aeiou]{3}[^aeiou]*\b' #取得單字有三個母音 (,在前面)
# print(re.findall(pat, mammoth))
# pat = r'\b\w*[aeiou]{3}[^aeiou\s]\w*\b'
# print(re.findall(pat, mammoth))   #######這次沒找到beau   (,在後面)
# pat = r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b'
# print(re.findall(pat, mammoth))   ###這次印出非常正確
# ###12.9 unhexlify來將這個十六進制字串,因為頁寬的關係切成兩個字串,轉換成bytes變數gif
# import binascii
# hex_str = '47494638396101000100800000000000ffffff21f9' + \
#     '0401000000002c000000000100010000020144003b'
# gif = binascii.unhexlify(hex_str)
# ###########################12.10
# print(len(gif))
# print(gif[:6] == b"GIF89a") #True
# print(gif[:6] == "GIF89a")  #False
# print(type(gif))
# print(type("GIF89a"))
# print(type(b"GIF89a"))
# ########################12.11
# import struct
# width, height = struct.unpack("<HH", gif[6:10])
# print(width, height)
#####################################259 --- 271
###############閏年
# import calendar
# print(calendar.isleap(1900))
# import calendar
# print(calendar.isleap(1906))
# import calendar
# print(calendar.isleap(1999))
# import calendar
# print(calendar.isleap(2000))
# import calendar
# print(calendar.isleap(2002))
# import calendar
# print(calendar.isleap(2004))
############datetime模組 dat
###用date 來處理年 , 月與日
###用time 來處理小時, 分鐘, 秒與分數(fraction)
###用datetime 來一併處理日期與時間
###用timedelte來處理日期與/或時間間隔
# from datetime import date
# halloween = date(2019, 10, 31)
# print(halloween)  #印出2019-10-31
# print(halloween.day) #印出31
# print(halloween.month) #印出10
# print(halloween.year)  #印出2019
# ########可以用date的isoformat()來將日期印出:
# print(halloween.isoformat()) #2019-10-31
# from datetime import date
# now = date.today()
# print(now)  #印出現在日期
# ###用timedelta物件為date日期加上一段時間間隔
# from datetime import timedelta
# one_day = timedelta(days = 1)
# tomorrow = now + one_day
# print(tomorrow) ###印出現在日期加上明天
# print(now + 17*one_day) ###印出現在日期加上17天
# yesterday = now - one_day
# print(yesterday)   ###印出現在日期減少一天
###datetime模組的time物件的用途是代表一天中的時間
# from datetime import time
# noon = time(12, 0, 1)
# print(noon)  ###印出上面編寫時間
# print(noon.hour) ##12點
# print(noon.minute) ##0分
# print(noon.second) ##1秒
# print(noon.microsecond) ##0微秒
###datetime物件同包含日期與一天的時間
# from datetime import datetime
# some_day = datetime(2019, 1, 2, 3, 4, 5, 6)
# print(some_day) ###印出2019-01-02 03:04:05.000006
# ###datetime物件也有isoformat()方法
# print(some_day.isoformat()) ###印出2019-01-02 03:04:05.000006 它用中間T來分隔日期
###datetime有個now()方法可回傳目前的日期與時間
# from datetime import datetime
# now = datetime.now()
# print(now)   ###印出現在時間  年.月.日.時.分.秒.微秒
# print(now.year) ###印出現在年份
# print(now.month) ###印出現在月份
# print(now.day)  ###印出現在 天
# print(now.hour) ###印出現在 小時
# print(now.minute) ###印出現在 分鐘
# print(now.second) ###印出現在 秒
# print(now.microsecond)  ###印出現在 微秒
# ######可以將一個date與一個time物件 combine() (結合) 成一個datetime
# from datetime import datetime, time, date
# noon = time(1)
# this_day = date.today()
# noon_today = datetime.combine(this_day, noon)
# print(noon_today)  ###印出現在日期,上面noon = time () 可以調整幾點
# ######可以用date()與time()方法從datetime中取出date與time:
# print(noon_today.date()) ###只印出現在日期 
# print(noon_today.time()) ###只印出上面的時間
# # #######使用time模組
# import time
# now = time.time() 
# print(now) #從1970年1月1日算起的秒數到現在
# ###可以用ctime()來將epoch值轉換成字串
# print(time.ctime(now)) ###印出現在時間 Sun Mar 24 23:51:01 2024
# print(time.localtime(now))##印出現在時間 tm_year=2024, tm_mon=3, tm
# print(time.gmtime(now))   ##印出現在時間  但時區
#tm_yea 年 0000-9999, #tm_mon 月 1-12,  #tm_mday 一月的日期 1-31
#tm_hour 小時 0-23,   #tm_min 分鐘 0-59, #tm_sec  秒 0-60
#tm_wday 一週的星期幾 (Monday)-(Sunday), #tm_yday 一年的第幾天 1-365
#tm_isdst 日光節約 0 = 不是,  1 = 是,   -1 = 不明
# import time 
# now = time.localtime()
# print(now)  #跟print(time.localtime(now)) 一樣
# print(now[0]) ###印出現在年份
# print(list(now[x] for x in range(9)))#印出現在時間[2024, 3, 25, 0, 2, 10, 0, 85, 0]
# now = time.time()  ########書上少這一行
# tm = time.localtime(now)
# print(time.mktime(tm)) ##1711296347.0
#######讀取與寫入日期與時間
# import time 
# now = time.time()
# print(time.ctime(now))###印出現在時間Mon Mar 25 00:09:19 2024
## %Y 年 1900...., #%m 月 01-12, #%B 月名稱 January,  #%b 月縮寫 Jan..,
## %d 月日期 1-31,  #%A 星期幾名稱 Sunday, %a 星期幾縮寫 sun, 
## %H 小時(24小時) 00-23, #%I 小時(12小時) 01-12, #%p AM/PM AM.PM,
## %M 分 00-59, #%S 秒 00-59,
# import time
# fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
# t = time.localtime()
# print(t) ###印出現在時間tm_year=2024, tm_mon=3, tm_mday=25, tm_hour=0
# print(time.strftime(fmt, t))#It's Monday, March 25, 2024, local time 12:18:13AM
# ########來處理 date 物件 就只有日期的部分有效,時間會被預設為午夜
# from datetime import date
# some_day = date(2024, 3, 25)
# fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
# print(some_day.strftime(fmt))#It's Monday, March 25, 2024, local time 12:00:00AM
# ######處理time物件時,它時會轉換時間的部分
# from datetime import time
# fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
# some_time = time(10, 35)#你不會使用time物件的日期部分,因為它們沒有任何意義
# print(some_time.strftime(fmt))#It's Monday, January 01, 1900, local time 10:35:00AM
# import time 
# fmt = "%Y-%m-%d"
# print(time.strptime("2024 03 25", fmt)) ##少 2024-03-25會是錯誤
# import time
# fmt = "%Y-%m-%d" ###這是正確的
# print(time.strptime("2024-03-25", fmt))#It's Monday, January 01, 1900, local time 10:35:00AM
# ###修改fmt字串來讓它符合日期字串
# import time 
# fmt = "%Y %m %d"  #少 -
# print(time.strptime("2024 03 25", fmt))#time.struct_time(tm_year=2024, tm_mon=3, tm_mday=25, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=85, tm_isdst=-1)
# print(time.strptime("2024-03-25", fmt))##格式不同 %Y少- print就不能用 -
# import locale
# from datetime import date 
# halloween = date(2019, 10, 31)
# for lang_country in ["en_us", "fr_fr", "de_de", "es_es", "is_is",]:
#     locale.setlocale(locale.LC_TIME, lang_country)
#     print(halloween.strftime("%A, %B %d"))#印出各國日期語言
# ###怎麼找到這些神奇的lang_country值? 有好幾百個
# import locale
# names = locale.locale_alias.keys()
# good_names = [name for name in names if \
# len(name) ==5 and name[2] == "_"]
# print(good_names[:5])
# ####想要取得所有的德語語言環境 可以試試
# de = [name for name in good_names if name. startswith("de")]
# print(de)
# ##     其他的模組 
# ##arrow 用簡單API許多日期與時間函式
# ##dateutil 可以解析幾乎所有日期格式
# ##iso8601 他可以填補ISO8601格式的標準式庫的不足
# ##fleming 有許多時區函式
# ##maya 處理日期, 時間, 時間間隔的值觀介面
# ##dateinfer 可以猜測日期/時間字串的格式字串
#############################13.1
# from datetime import datetime, date
# import datetime
# now = date.today()
# now_str = now.isoformat()
# with open("today.txt", "wt") as output:
#     print(now_str, file = output)  #會自動建立today.txt檔案 現在日期
# #############################13.2
# with open("today.txt", "rt") as input:
#     today_string = input.read()

# print(repr(today_string)) ##印出現在日期
# #############################13.3
# from datetime import datetime
# fmt = "%Y-%m-%d\n"  ##跟書上不一樣
# today_string = "2024-03-26\n"  # 注意空格和连字符
# print(repr(datetime.strptime(today_string, fmt)))
# #############################13.4
# my_day = date(1983, 11, 25)
# print(repr(my_day))  ###要加上repr才會印出datetime.date(1983.11.25)
# #############################13.5
# print(my_day.weekday()) #我出生是星期幾 星期一是0  星期天是6
# print(my_day.isoweekday())#我出生是星期幾 星期一是1  星期天是7
# #############################13.6
# from datetime import timedelta
# party_day = my_day + timedelta(days = 10000)  #我的生日+10000
# print(party_day)
###################################十四章 274
##########用open()建立或開啟
fout = open("oops.txt", "wt")
print(fout.close())
##########用print()來寫入文字檔
fout = open("oops.txt", "wt")
print("Oops, I created a file.", file=fout)
print(fout.close())
