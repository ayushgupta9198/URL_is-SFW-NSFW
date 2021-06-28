from image_scrapper import image_scrapper , get_detail
import os
from nsfw_detector import predict 
from nsfw_detector.predict import thresold_calculation

model = predict.load_model('/home/ayush-ai/Music/final_model/mobilenet_v2_140_224/')

if __name__ == '__main__':
    path="/home/ayush-ai/Music/final_model/scrapped_images"   
    url =  'https://exweb.jp/'
    # url = "https://news.dwango.jp/gravure/"

    try:
        # os.mkdir("explict_0")
        if os.path.exists(path):
            os.system(f"rm -r {path}/*")
        else:
            os.mkdir(path)
    except Exception as e:
        print (e)
    sr_no=0
    try:
        get_detail(sr_no,path, url)
        sr_no=sr_no+1
    except Exception as e:
        print (e)
    image_scrapper(path)

output = predict.classify(model, path)

thresold_calculation(output)
