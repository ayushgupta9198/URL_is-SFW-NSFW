
Command to run :

python3 main.py

for running :

we need to put the main folder directory in the model path and it will work :
like this : 
model = predict.load_model('/home/ayush-ai/Music/final_model/mobilenet_v2_140_224/')

we have to run only main.py file and have to put the url in code line rest it will everything.

for testing on single image we need to put the image path mannually.

like this : 

python3 /home/ayush-ai/Music/final_model/nsfw_detector/predict.py --saved_model_path ./mobilenet_v2_140_224 --image_source /home/ayush-ai/Music/final_model/scrapped_images/13.jpg

