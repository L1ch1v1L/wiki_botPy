import wikipedia as wiki

global lang
global title
global page
global choose 

russian_alphabet = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
english_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def main():
	print("Привет, вы включили функцию вики-бота.")
	print("Что вы хотите найти?")
	print("Выберите язык: ( название статьи тоже должно быть на соответсвующем языке ).")
	print("1. Русский; 2. Английский;")
	choosing_lang()
	choosing_page()
	print("Название желаемой статьи:",title)
	page = wiki.page(title)
	print("Что вы хотите сделать?")
	while(1):
		choose = int(input("1. Вывести весь контент; 2. URL; 3.Вывести html (Осторожно это может быть медленно) 4. Вывести категории > "))
		if choose == 1:
			print_content(page)
		elif choose == 2:
			print_URL(page)
		elif choose == 3:
			print_html(page)
		elif choose == 4:
			print_categor(page)
		else:
			print("Нет такого!")
def choosing_lang():
	while (1):
		choose_lang = int(input())
		if (choose_lang == 1):
			lang = "ru" 
			set_lang(lang)
			break
		elif (choose_lang == 2):
			lang = "en" 
			set_lang(lang)
			break

		else:
			print("Нет в списке такой цифры.")


def choosing_page():
	global title
	print("Введите название желаемой статьи:")
	title = input()
	try:
		debug_page = wiki.summary(title)
	except wiki.exceptions.DisambiguationError:
		print("Нет такой статьи! Выключаю функцию.")
		# в боте конечно другое можно использовать;
		# также можно сделать бесконечный цикл, но мне достаточно просто выход;
		exit()



def set_lang(lang):
	wiki.set_lang(lang)

def print_content(page):
	print(page.content)

def print_URL(page):
	print("URL:",page.url)

def print_html(page):
	# скорее всего не будем это юзать т.к это небезопасно, можно так ддос делать.
	print(page.html())

def print_categor(page):
	print(page.categories)

if __name__ == '__main__':
	main()