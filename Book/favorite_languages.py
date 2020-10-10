from _collections import OrderedDict

"""
#Без импорта, стандартный словарь
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

print("Srah's favorite language is " +
      favorite_languages["sarah"].title() +
      ".")

print("-------------")

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")

print("-------------")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

print("-------------")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

print("-------------")
"""

favorite_languages = OrderedDict()

favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"
for name, languages in favorite_languages.items():
    print(name.title() + "любимый язык это " +
          languages.title() + ".")