from django.http import HttpResponse
from django.shortcuts import render
import operator

#Following function will make first homepage in django python and content will be printed on website front page.
def homepage(request):
    return HttpResponse('<H1><Font color="red"><center>This is my homepage'
                        '<br><br> <ul type="circle"><b><Font color="green">Grocery Items List</b>'
                        '<li><Font color="violet">Sugar 10 kg </li>'
                        '<li><Font color="violet">GroundNuts 3 kg </li>'
                        '<li><Font color="violet">Sunflower Oil 4 kg </li>'
                        '<li><Font color="violet">Wheel Soaps 5 </li>'
                        '</center</Font></H1>')

def contact(request):
    return HttpResponse('<Font color="Red"><H1>This is the contact page</H1></Font>'
                        '<b><Font color="violet"><center>Contact No: 002-892718<br>'
                        'Address: 1 floor, shrirang apartment Pune<br>'
                        'Email: abcd@gmail.com'
                        '</Font></b>')

#The following function basically tells how we can code html seperatly in other file in python. as follows render function allows us
# to do so. in that render function just send the request object and your html file name as another parameter.
def template_homepage(request):
    return render(request,'home.html')


#the following function template_homepage() will run home2.html
#second function count will run when count button from form will be clicked and not here count function will run count.html file.

def template_homepage2(request):

    return render(request,'home2.html')

def count(request):
    data=request.GET['fulltextarea']  # This GET[] method will take contents submited from form and here we have saved it in string variable data
    print(data)                         #it will print the contents comming from form on to console not on web page.
    word_list=data.split()              #split method will split the string into words list and we have returned it to the list variable word_list
    print(word_list)                    # it will print the word list items in list format on console not on web page.
    list_length=len(word_list)          #Here our len() funcion will count all words from list and will return length and we have saved it in variable list_length.

    worddictionary = {}

    for word in word_list:
        print('*******************************************************8')
        if word in worddictionary:
            print("#######################################")
            worddictionary[word] +=1
        else:
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7")
            worddictionary[word]=1


    print(worddictionary.items())
    sorted_list=sorted(worddictionary.items(), key=operator.itemgetter(1))
    #above sorted function will sort over words count in ascending order    and it will make a list of it and we have passed that
    #list to count.html page via render function with key worddictionary_key.

    return render(request,'count.html',{'fulltext_key': data, 'wordcount_key': list_length, 'worddictionary_key':sorted_list})
    #Above render function we have given two key value pairs and this function will send that to the count.html page. so there in that html file we have called these values on its keys.


