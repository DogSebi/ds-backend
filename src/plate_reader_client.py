import requests
import io
import sys


class PlateReaderServerClient:
    def __init__(self, host: str, server: str):
        self.host = host
        self.server = server

    def get_image(self, image_id):
        
        try:
            image_path = self.server + '/' + image_id
            response = requests.get(image_path, timeout=3)
            response.raise_for_status()
            image = io.BytesIO(response.content)
            return image
        except requests.exceptions.HTTPError:
            raise RuntimeError(f'client error, status code {response.status_code}')
        except requests.exceptions.RequestException:
            raise RuntimeError(f'server error, status code {response.status_code}')
    
    def get_car_number(self, image_ids):

        if len(image_ids) == 1:
            url = f'{self.host}/readPlateNumber'
            arguments = {
                'id': image_ids[0]
            }
        else:
            url = f'{self.host}/readManyNumbers'
            arguments = {
                f'id_{i}': image_ids[i] for i in range(len(image_ids))
            }

        res = requests.post(
            url,
            json=arguments,
        )

        return res.json()

if __name__ == '__main__':
    image_ids = sys.argv[1:]
    client = PlateReaderServerClient(host='http://84.252.130.126:8080', server='http://89.169.157.72:8080/images')
    res = client.get_car_number(image_ids)
    print(res)
