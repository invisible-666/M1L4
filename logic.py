from random import randint
import requests
token = "7058753529:AAHEKGkWEwclTCOM6W8VG-AunOU-fu1QzpI"

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_common = randint(1, 200)
        self.pokemon_uncommon = randint(201,300)
        self.pokemon_rare = randint(301,500)
        self.pokemon_superare = randint(501,800)
        self.pokemon_epik = randint(801,900)
        self.pokemon_mifik = randint(901,980)
        self.pokemon_legend = randint(981,1000)

        self.img = self.get_img()
        self.name = self.get_name()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_defoult'])
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        if self.img >= 1 and self.img <= 200:
            return(self.pokemon_common)
        if self.img >= 201 and self.img <=300:
            return(self.pokemon_uncommon)
        if self.img >= 301 and self.img <= 500:
            return(self.pokemon_rare)
        if self.img >= 501 and self.img <= 800:
            return(self.pokemon_superare)
        if self.img >= 801 and self.img <= 900:
            return(self.pokemon_epik)
        if self.img >= 901 and self.img <=980:
            return(self.pokemon_mifik)
        if self.img >= 981 and self.img <=1000:
            return(self.pokemon_legend)



