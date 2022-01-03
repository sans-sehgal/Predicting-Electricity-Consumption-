import requests
import json

def send_ocr_and_translation_request(file_name, file_path):
	url = "http://34.93.201.102:5000/upload/sanskar@api/sans-sehgal/NEWPROJECT/eng/hi/false"
	payload={}
	files=[
	  ('files[]',(file_name,open(file_path,  'rb')))
	]
	headers = {}
	response = requests.request("POST", url, headers=headers, data=payload, files=files)
	print(response.text)


def send_translation_request():
	url = "http://34.93.201.102:5000/translate/en/hi"
	en_paragraph =''' 
	The pandemic has resulted in worldwide social and economic disruption. The world is facing the worstrecession since the global financial crisis. This led to the postponement or cancellation of sporting, religious, political and cultural events. Due to the fear, there was shortage of supply as more people purchased items like masks, sanitizers etc.
			'''
	response = requests.post(url , {"sentence" : en_paragraph})
	print(json.loads(response.text))

# def sned_pdf2img_request():
	
if __name__ == '__main__':
	send_ocr_and_translation_request('sop_v12.pdf' , '/home/sanskar/Desktop/sop_v12.pdf')
	# send_translation_request()
