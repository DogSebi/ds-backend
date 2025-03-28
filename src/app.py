import logging
from flask import Flask, request
from models.plate_reader import PlateReader, InvalidImage
import io
from plate_reader_client import PlateReaderServerClient

client = PlateReaderServerClient(host='http://84.252.130.126:8080', server='http://89.169.157.72:8080/images/')

app = Flask(__name__)
plate_reader = PlateReader.load_from_file('./model_weights/plate_reader_model.pth')


def read_one_image(image_id):

    try:
        image = client.get_image(image_id=image_id)
        res = plate_reader.read_text(image)
    except RuntimeError as exception:
        logging.error(str(exception))
        return str(exception)
    
    return res

# Этап 1

@app.route('/readPlateNumber', methods=['POST'])
def read_plate_number():

    image_id = request.get_json()['id']
    res = read_one_image(image_id=image_id)

    return {
        f'plate_number_{image_id}': res
    }      

#Этап 2

@app.route('/readManyNumbers', methods=['POST'])
def read_many_numbers():

    image_ids = request.get_json()
    final_json = {}

    for image_id in image_ids.values():
        res = read_one_image(image_id=image_id)
        final_json[f'plate_number_{image_id}'] = res

    return final_json

if __name__ == '__main__':
    logging.basicConfig(
        format='[%(levelname)s] [%(asctime)s] %(message)s',
        level=logging.INFO,
    )

    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=8080, debug=True)
