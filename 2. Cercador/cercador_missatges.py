import anvil.server

query = ""
enlace1 = ""
enlace2 = ""
enlace3 = ""
enlace4 = ""
enlace5 = ""
enlace6 = ""
enlace7 = ""
enlace8 = ""
enlace9 = ""
enlace10 = ""
anvil.server.connect("server_NQZFO4JSZO3N6EHFS3PCOJKO-LMR3FBYTVH6KLQW4")

@anvil.server.callable
def blended_search(query, proportion, count=10):

    import tensorflow as tf
    import numpy as np
    import os
    import time
    import requests
    import random

    def google_search_engine_a(query):
        url = f'https://www.googleapis.com/customsearch/v1?q={query}&cx=2177da69345fc455a&key=AIzaSyCKzlwjPEKdZNoZMLDcRbDbW3Llc4BoZjU'
        response = requests.get(url)
        data = response.json()
        return data.get('items', [])

    def google_search_engine_b(query):
        url = f'https://www.googleapis.com/customsearch/v1?q={query}%20porn&cx=34446e1ae7ed74b76&key=AIzaSyCKzlwjPEKdZNoZMLDcRbDbW3Llc4BoZjU'
        response = requests.get(url)
        data = response.json()
        return data.get('items', [])

    if proportion < 0 or proportion > 100:
        raise ValueError("Proportion must be between 0 and 100")

    results_a = google_search_engine_a(query)
    results_b = google_search_engine_b(query)

    num_results_a = int(len(results_a) * (proportion / 100))
    num_results_b = count - num_results_a

    blended_results = random.sample(results_a, num_results_a) + random.sample(results_b, num_results_b)
    return blended_results

# Substituir ruta per ubicació de carpeta ModelText

@anvil.server.callable
def prediction(query):

    import tensorflow as tf
    import numpy as np
    import os
    import time
    import requests
    import random

    one_step_reloaded = tf.saved_model.load('<UBICACIÓ_CARPETA_MODELTEXT>')
    states = None
    next_char = tf.constant([query])
    result = [next_char]

    for n in range(100):
      next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
      result.append(next_char)

    output1 = tf.strings.join(result)[0].numpy().decode("utf-8")

    return output1

@anvil.server.callable
def update_query(new_query):
    global query
    query = new_query

# Substituir ruta per ubicació arxiu publicSentenceList.txt

@anvil.server.callable
def write():
    with open("<UBICACIÓ_PUBLICSENTENCELIST.TXT>", "w") as myfile:
      myfile.write(prediction(query))

#Substituir rutes per carpeta d'URLs

@anvil.server.callable
def popups(enlace1, enlace2, enlace3, enlace4, enlace5, enlace6, enlace7, enlace8, enlace9, enlace10):

    with open("/<UBICACIÓ_URLS>/1.txt", "w") as myfile:
      myfile.write(enlace1)
    with open("/<UBICACIÓ_URLS>/2.txt", "w") as myfile:
      myfile.write(enlace2)
    with open("/<UBICACIÓ_URLS>/3.txt", "w") as myfile:
      myfile.write(enlace3)
    with open("/<UBICACIÓ_URLS>/4.txt", "w") as myfile:
      myfile.write(enlace4)
    with open("/<UBICACIÓ_URLS>/5.txt", "w") as myfile:
      myfile.write(enlace5)
    with open("/<UBICACIÓ_URLS>/6.txt", "w") as myfile:
      myfile.write(enlace6)
    with open("/<UBICACIÓ_URLS>/7.txt", "w") as myfile:
      myfile.write(enlace7)
    with open("/<UBICACIÓ_URLS>/8.txt", "w") as myfile:
      myfile.write(enlace8)
    with open("/<UBICACIÓ_URLS>/9.txt", "w") as myfile:
      myfile.write(enlace9)
    with open("/<UBICACIÓ_URLS>/10.txt", "w") as myfile:
      myfile.write(enlace10)

proportion = 40

results = blended_search(query, proportion)
