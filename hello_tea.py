import requests

def hello_tea_func():
    response = requests.get('https://app.tea.xyz/')
    print("Hello teaxyzzz5!")
    print("Status teaxyzzz5:", response.url, response.ok)
