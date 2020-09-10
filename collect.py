import newspaper 
site1 = "http://xinmin.cn/"
site2 = "http://news.cn/"
site3 = "http://www.people.com.cn/"
site4 = "http://www.sina.com.cn/"
site5 = "http://xinhuanet.com/"
news1 = newspaper.build(site1,memoize_articles=False)
print("Building News 1")
news2 = newspaper.build(site2,memoize_articles=False)
print("Building News 2")
news3 = newspaper.build(site3,memoize_articles=False)
print("Building News 3")
news4 = newspaper.build(site4,memoize_articles=False)
print("Building News 4")
news5 = newspaper.build(site5,memoize_articles=False)
print("Building News 5")
htmlname = "news1.html"
htmlname2 = "news2.html"
htmlname3 = "news3.html"
htmlname4 = "news4.html"
htmlname5 = "news5.html"
print(len(news1.articles))
print(len(news2.articles))
print(len(news3.articles))
print(len(news4.articles))
print(len(news5.articles))
for i in range(0,min(20,len(news1.articles))):
    temp_article = news1.articles[i]
    temp_article.download()
    with open(str(i) + htmlname,"w") as fp:
        fp.write(temp_article.html)
        fp.close()
for i in range(0,min(20,len(news2.articles))):
    temp_article = news2.articles[i]
    temp_article.download()
    with open(str(i) + htmlname2,"w") as fp:
        fp.write(temp_article.html)
        fp.close()
for i in range(0,min(20,len(news3.articles))):
    temp_article = news3.articles[i]
    temp_article.download()
    with open(str(i)+ htmlname3,"w") as fp:
        fp.write(temp_article.html)
        fp.close()
for i in range(0,min(20,len(news4.articles))):
    temp_article = news4.articles[i]
    temp_article.download()
    with open(str(i) + htmlname4,"w") as fp:
        fp.write(temp_article.html)
        fp.close()
for i in range(0,min(20,len(news5.articles))):
    temp_article = news5.articles[i]
    temp_article.download()
    with open(str(i) + htmlname5,"w") as fp:
        fp.write(temp_article.html)
        fp.close()