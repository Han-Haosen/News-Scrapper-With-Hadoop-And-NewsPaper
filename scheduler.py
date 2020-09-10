import custom_b
import custom_c
import custom_d
import newspaper
import pyhdfs
hdfsclient = pyhdfs.HdfsClient('192.168.137.2:50070',user_name="root")
for j in range(0,5):
    for i in range(0,20):
        response = hdfsclient.open("/newsData/test/"+ str(i) +"news" + str(j) + ".html")
        temp_html = response.read()
        article = newspaper.Article(url='')
        article.set_html(temp_html)
        article.parse()
        result = custom_b.run(article)
        result = custom_c.run(result,article)
        custom_d.run(result)
print("Finished")