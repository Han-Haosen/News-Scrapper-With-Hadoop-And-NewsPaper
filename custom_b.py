import newspaper
class Result:
    def __init__(self):
        self.temp_url = ""
        self.temp_time = ""
        self.temp_text = ""
        self.html = ""
        self.temp_image_links = []
def run(newspaperobj):
    if(newspaperobj == None):
        print("No News Object being passed")
    print(newspaperobj.html)
    result = Result()
    result.temp_url = newspaperobj.url
    result.temp_time = newspaperobj.publish_date
    result.html = newspaperobj.html
    result.text = newspaperobj.text
    if(result.text == None):
        print("Not Successful")
    return result