import csv
import requests

from bs4 import BeautifulSoup as Soup

with open("lego_info.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(("id", "title", "price", "promo_price", "url"))


def lego_parse(url, geo_city_dm, geo_city_dm_iso, geo_city_dm_code):
    headers = {
        "authority": "www.detmir.ru",
        "method": "GET",
        "path": "/catalog/index/name/lego/",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "cookie": f"uid=X6NyEmL07Dqb+7nnDMBqAg==; ab2_90=ab2_90old90; ab2_33=ab2_33old34; ab2_50=33; ab3_75=ab3_75old75; ab3_33=ab3_33new33; ab3_20=ab3_20_20_3; cc=0; _gaexp=GAX1.2.8MwGXf_UQwWf1g2n0sBLCw.19243.x409; transactionId=9bbe65d2-0425-4193-ab61-edc8c58151fd.0; transactionSubId=e77318f0-4638-41af-9081-b5d8c4a8d326.0; _ga=GA1.2.67882972.1660218497; _gid=GA1.2.2141659420.1660218497; _gcl_au=1.1.1146876645.1660218497; _ym_uid=1660218497186530714; _ym_d=1660218497; flocktory-uuid=69c97b99-2cbd-4013-8dd6-ce506a9542f8-9; advcake_track_id=f4ce5756-b03e-bef5-8b4a-86beca0f09f4; advcake_session_id=11b24d62-0be8-6c72-08a5-c7c41f1b1bb8; auid=8d18935e-137f-43fb-a5b3-bdcbed977b3e; tmr_lvid=6f7c70c646b1f45814afd4dfee435376; tmr_lvidTS=1660218500672; adrcid=A0iQd0p5oCrjH6npHVo2_gg; dm.cookieMobileAppNotification=no; geoCityDM={geo_city_dm}; geoCityDMIso={geo_city_dm_iso}; geoCityDMCode={geo_city_dm_code}; _ym_isad=2; adrdel=1; JSESSIONID=0eb32850-ca21-43a8-93e9-8acafcf5f53c; detmir-cart=6909a242-5800-4ba1-b448-d8f53547cfa5; srv_id=cubic-front19-prod; _ym_visorc=w; _sp_ses.2b21=*; listingLink=https://www.detmir.ru/catalog/index/name/lego/; qrator_msid=1660317557.653.j0DC0RnbmWKWjuUB-7pehgj1nhqslijccs6thklaamcpiakbb; cto_bundle=z053pF8lMkZHNzB6eUgySE1MT3ZoMmJkUHVadUJVajR5VFEzTU81JTJGZG80bk1UYkRNbHF6eEd0JTJCMDh5NG5RZHA5S1UlMkJFNDh1TVFhNnVlMVBYdzZGc1BkN3pnTWY3VzR6VlFUT24lMkY4UlJPaWl2ZWlwUEZ4ZTJHTXlNSk9VUWFRQVJQd1VzcmoyaFZZODJyVSUyRkRHbWZEVjhQeHZyQnclM0QlM0Q; mindboxDeviceUUID=0b00a04d-68d5-4b98-846e-dd84f9ba4cfd; directCrm-session=%7B%22deviceGuid%22%3A%220b00a04d-68d5-4b98-846e-dd84f9ba4cfd%22%7D; tmr_detect=0%7C1660317602259; _sp_id.2b21=3e9de0af-0498-491a-bfc7-305dc959c334.1660218494.5.1660317603.1660311022.b6761ff1-ee68-4e25-a233-1b1c849dc26a; dm_s=L-0eb32850-ca21-43a8-93e9-8acafcf5f53c|kH6909a242-5800-4ba1-b448-d8f53547cfa5|Vj8d18935e-137f-43fb-a5b3-bdcbed977b3e|gqcubic-front19-prod|qa2c681b91-309a-4594-be31-8da441941529|RK1660317603385|-N1660317603384|110d10fef2-6f3f-4fec-96d3-eb3df8464f48#z7TMCz0iKZ3Sx4rg4KIttfCe1Ca8Q4vl3J_31KcYp7E; tmr_reqNum=161",
        "if-none-match": 'W/"21e4c5-LhEm4NfwwujcchhCchh+qHnjwY8"',
        "sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }
    page = requests.get(url=url, headers=headers)
    product_info = []
    i = 2
    flag = True
    while flag:
        soup = Soup(page.text, "html.parser")
        product = soup.find_all("a", class_="RS Sj")
        if product != []:
            for elem in product:
                product_info.append(elem.get("href")[39:-1])
                product_info.append((elem.find("p", class_="RW")).text)

                if elem.find("span", class_="R_8") is not None:
                    price = str((elem.find("span", class_="R_8")).text)
                    price = price.replace("\u2009", "")
                    price = price.replace("\xa0", "")
                    price = price.replace("₽", "")
                    product_info.append(price)
                    sale_price = str((elem.find("p", class_="R_6")).text)
                    sale_price = sale_price.replace("\u2009", "")
                    sale_price = sale_price.replace("\xa0", "")
                    sale_price = sale_price.replace("₽", "")
                    product_info.append(sale_price)
                else:
                    elem.find("p", class_="R_6")
                    price = str((elem.find("p", class_="R_6")).text)
                    price = price.replace("\u2009", "")
                    price = price.replace("\xa0", "")
                    price = price.replace("₽", "")
                    product_info.append(price)
                    product_info.append("None")

                product_info.append(elem.get("href"))
                with open("lego_info.csv", "a", encoding="UTF-8", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(product_info)
                    file.close()
                product_info.clear()
        else:
            product = soup.find_all("a", class_="RS Sj RT")
            for elem in product:
                product_info.append((elem.get("href")[39:-1]))
                product_info.append((elem.find("p", class_="RW")).text)
                product_info.append("Нет в наличии")
                product_info.append("Нет в наличии")
                product_info.append(elem.get("href"))
                with open("lego_info.csv", "a", encoding="UTF-8", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(product_info)
                    file.close()
                product_info.clear()
        next_page = soup.find("div", class_="dp").find_all("div")
        if not next_page:
            flag = False
        else:
            for page in next_page:
                if page.text == "Показать ещё":
                    url = f"https://www.detmir.ru/catalog/index/name/lego/page/{i}"
                    page = requests.get(url, headers=headers)
        i += 1


if __name__ == "__main__":
    url = "https://www.detmir.ru/catalog/index/name/lego"
    geoCityDM_MOW = "%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C"
    geoCityDMIso_MOW = "RU-MOW"
    geoCityDMCode_MOW = 7700000000000
    geoCityDM_SPE = "%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%20%D0%B8%20%D0%9B%D0%B5%D0%BD%D0%B8%D0%BD%D0%B3%D1%80%D0%B0%D0%B4%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C"
    geoCityDMIso_SPE = "RU-SPE"
    geoCityDMCode_SPE = 78000000000
    lego_parse(url, geoCityDM_MOW, geoCityDMIso_MOW, geoCityDMCode_MOW)
    lego_parse(url, geoCityDM_SPE, geoCityDMIso_SPE, geoCityDMCode_SPE)
