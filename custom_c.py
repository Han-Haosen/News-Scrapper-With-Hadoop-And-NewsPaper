import newspaper
def run(result,newspaperobj):
    result.temp_image_links = newspaperobj.images
    if(newspaperobj == None):
        print("No news object being passed")
    return result
    