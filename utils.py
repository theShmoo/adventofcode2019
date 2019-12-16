from urllib.request import Request, urlopen
import os.path

def get_input(year, day):
    input_file_name = f'advent input {year}-{day}.txt'
    if os.path.exists(input_file_name):
        with open(input_file_name, 'r') as input_file:
            return input_file.read()

    try:
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        request = Request(url, headers={'cookie': 'session=get_your_value_from_your_browser_by_looking_at_the_request_header'})
        input_bytes = urlopen(request).read()
        input_text = input_bytes.decode('utf-8')
        with open(input_file_name, 'w') as input_file:
            input_file.write(input_text)
        return input_text
    except Exception as e:
        print(e)
        return None
