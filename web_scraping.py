import requests
from bs4 import BeautifulSoup

req = requests.get("https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/")
soup = BeautifulSoup(req.content, "html.parser")

# print(soup.prettify())
# print(soup.get_text())
res = soup.title
# print(res.prettify())
print(res.get_text())

# def get_menu_details(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         menu_items = soup.find_all('div', class_='sc-fznWqX')
#
#         menu_details = []
#         for item in menu_items:
#             food_name = item.find('div', class_='sc-iIHSe').text.strip()
#             price = item.find('div', class_='sc-hBEYos').text.strip()
#             menu_details.append({'Food Name': food_name, 'Price': price})
#
#         return menu_details
#     else:
#         print("Failed to fetch the page.")
#         return None
#
#
# sample_link = "https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/"
# menu = get_menu_details(sample_link)
#
# if menu:
#     for item in menu:
#         print(item)
# else:
#     print("No menu details found.")
