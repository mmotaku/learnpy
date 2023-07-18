import json
import requests


def load_sample_file():
    f = open('sample.json')
    sample = f.read()
    f.close()

    super_heroes = json.loads(sample)
    print(super_heroes['secretBase'])
    print(super_heroes['members'][2]['powers'][3])
    sum = super_heroes['members'][0]['age'] + super_heroes['members'][1][
        'age'] + super_heroes['members'][2]['age']
    print(sum)


def load_sample_array():
    f = open('sample_array.json')
    sample_array = f.read()
    f.close()
    persons = json.loads(sample_array)
    print(persons[0]['powers'][0])


def generate_powers(powers):
    all_str = '<ul>'
    for power in powers:
        str = f''' 
        <li>{power}</li>
      '''
        all_str += str
    all_str += '</ul>'
    return all_str


def generate_articles(members):
    all_str = ''
    for member in members:
        ul = generate_powers(member['powers'])
        str = f'''
            <article>
              <h2>{member['name']}</h2>
              <p>Secret identity: {member['secretIdentity']}</p>
              <p>Age: {member['age']}</p>
              <p>Superpowers:</p>
              {ul}
            </article>
            '''
        all_str += str
    return all_str


def write_html():
    r = requests.get(
        'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json'
    )

    if r.status_code != 200:
        return

    super_heroes = r.json()

    squad_name = super_heroes['squadName']
    home_town = f"Hometown: {super_heroes['homeTown']} // Formed: {super_heroes['formed']}"

    members = super_heroes['members']

    articles = generate_articles(members)

    html = f'''<!DOCTYPE html>
  <html lang="en-us">
    <head>
      <meta charset="utf-8">

      <title>Our superheroes</title>

      <link href="https://fonts.googleapis.com/css?family=Faster+One" rel="stylesheet">
      <link rel="stylesheet" href="style.css">
    </head>

    <body>

        <header>
          <h1>{squad_name}</h1>
          <p>{home_town}</p>
        </header>

        <section>
          {articles}
        </section>

        <script>

        </script>
    </body>
  </html>'''

    f = open('index.html', 'w')
    f.write(html)
    f.close()


load_sample_file()
load_sample_array()

write_html()
