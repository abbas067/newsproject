from django.shortcuts import render
from testapp.models import *
 # Create your views here.
def Home_Page_view(request):
    return render(request,'testapp/results.html')
def movie_news_view(request):
  news1='Natkhat Review: Vidya Balan fights patriarchy from behind a ghunghat'
  news2='Throwback Thursday: Neena Gupta, cool since before cool was even a word'
  news3="Taimur has dad Saif Ali Khan's back. Kareena Kapoor shares proof"
  news4="Esha Gupta makes her relationship with Spanish boyfriend Manuel Campos Guallar Insta official: Te Amo"
  news5="Baaghi 3 Movie Review: Can we fight coronavirus like Tiger Shroff fights bad guys?"
  my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
  return render(request,'testapp/mnews.html',my_dict)
def Sports_news_view(request):
 news1='West Indies announce squad for England Test series, three players opt out'
 news2='Hyderabad Open badminton cancelled due to COVID-19 pandemic'
 news3='Australian Cricketers Association to challenge CA’s negative revenue forecast for next 2 summers'
 news4='Lockdown Drills: Father helping me with catching practice, says Wriddhiman Saha'
 news5='Lionel Messi concern after missed practice ahead of La Liga return'
 my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
 return render(request,'testapp/snews.html',my_dict)
def Political_news_view(request):
  news1='India-China border dispute: Importance of Pangong Tso and why its fingers are much sought after'
  news2='GDP: 3.1% for March quarter, 4.1% for year. But it is not due to coronavirus'
  news3='Lockdown, Day 72: The sinking bottom line'
  news4='Coronavirus | Setback for Arvind Kejriwal government’s ‘Delhi Corona’ app'
  news5='Karnataka bans entry of people from 5 States'

  my_dict={'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
  return render(request,'testapp/pnews.html',my_dict)
