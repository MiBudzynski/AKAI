import json, datetime, urllib.request
import requests

class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        data = datetime.date.today()
        with open('ratios.json', 'r') as ratios:
            ratios = json.load(ratios)
            for ratio in ratios:
                if ratio["base_currency"] == self.base and ratio["target_currency"] == self.target and ratio["date_fetched"] == data:
                    return True
        return False

    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it
        url = f'https://api.exchangerate.host/convert?from={self.base}&to={self.target}'
        response = requests.get(url)
        data = response.json()
        result = data['result']
        self.save_ratio(result)
        return result

    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)
        nowy = True
        with open('ratios.json', 'r') as ratios:
            ratios = json.load(ratios)
            for zapis in ratios:
                if zapis["base_currency"] == self.base and zapis["target_currency"] == self.target:
                    zapis["date_fetched"] = datetime.date.today()
                    zapis["ratio"] == ratio
                    nowy = False
                    break
            if nowy:
                with open('ratios.json', 'w') as kursy:
                    ratios.append({"base_currency":self.base,"target_currency":self.target,"date_fetched":str(datetime.date.today()),"ratio":ratio})
                    json.dump(ratios, kursy)

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file
        if self.was_ratio_saved_today():
            with open('ratios.json', 'r') as ratios:
                ratios = json.load(ratios)
                for ratio in ratios:
                    if ratio["base_currency"] == self.base and ratio["target_currency"] == self.target:
                        return ratio["ratio"]
        else:
            return self.fetch_ratio()

dane = input("wpisz sume, bierzaca walute, docelowa walute\n").split()
zmiana = RatioObtainer(base=dane[1], target=dane[2])
przewalutowane = zmiana.get_matched_ratio_value()*float(dane[0])
print(f'{dane[0]} {dane[1]} = {przewalutowane} {dane[2]}\n')