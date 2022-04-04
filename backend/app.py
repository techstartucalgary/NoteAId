
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from summarizer import summarize
# from cloudVision import detect_text
app = Flask(__name__)
UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return "<p>Hello, World!</p>"


@app.route('/upload', methods=['POST'])
def upload():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    files = request.getlist("file[]")
    texts = []
    # if user does not select files, browser also submit a empty part without filename
    if files.filename == '':
        flash('No selected file')
        return redirect(request.url)
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            text = summarize('''The cat(Felis catus) is a domestic species of small carnivorous mammal.[1][2] It is the only domesticated species in the family Felidae and is often referred to as the domestic cat to distinguish it from the wild members of the family.[4] A cat can either be a house cat, a farm cat or a feral cat the latter ranges freely and avoids human contact.[5] Domestic cats are valued by humans for companionship and their ability to kill rodents. About 60 cat breeds are recognized by various cat registries.[6]
                                The cat is similar in anatomy to the other felid species: it has a strong flexible body, quick reflexes, sharp teeth and retractable claws adapted to killing small prey. Its night vision and sense of smell are well developed. Cat communication includes vocalizations like meowing, purring, trilling, hissing, growling and grunting as well as cat-specific body language. A predator that is most active at dawn and dusk(crepuscular), the cat is a solitary hunter but a social species. It can hear sounds too faint or too high in frequency for human ears, such as those made by mice and other small mammals.[7] Cats also secrete and perceive pheromones.[8]
                                Female domestic cats can have kittens from spring to late autumn, with litter sizes often ranging from two to five kittens.[9] Domestic cats are bred and shown at events as registered pedigreed cats, a hobby known as cat fancy. Population control of cats may be affected by spaying and neutering, but their proliferation and the abandonment of pets has resulted in large numbers of feral cats worldwide, contributing to the extinction of entire bird, mammal, and reptile species.[10]
                                Cats were first domesticated in the Near East around 7500 BC.[11] It was long thought that cat domestication began in ancient Egypt, where cats were venerated from around 3100 BC.[12][13] As of 2021, there were an estimated 220 million owned and 480 million stray cats in the world.[14][15] As of 2017, the domestic cat was the second-most popular pet in the United States, with 95.6 million cats owned[16][17][18] and around 42 million households own at least one cat.[19] In the United Kingdom, 26 % of adults have a cat with an estimated population of 10.9 million pet cats as of 2020.[20]''')
            os.remove(filename)
            texts.append(text)
        else:
            redirect(url_for('upload_pdf'))

    return texts


#no conversion to images
# @app.route('/upload/pdf', methods=['POST'])
# def upload_pdf():
#     # check if the post request has the file part
#     if 'file' not in request.files:
#         flash('No file part')
#         return redirect(request.url)
#     file = request.files['file']
#     # if user does not select file, browser also submit a empty part without filename
#     if file.filename == '':
#         flash('No selected file')
#         return redirect(request.url)
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(UPLOAD_FOLDER, filename))
#         text = summarize('''The cat(Felis catus) is a domestic species of small carnivorous mammal.[1][2] It is the only domesticated species in the family Felidae and is often referred to as the domestic cat to distinguish it from the wild members of the family.[4] A cat can either be a house cat, a farm cat or a feral cat the latter ranges freely and avoids human contact.[5] Domestic cats are valued by humans for companionship and their ability to kill rodents. About 60 cat breeds are recognized by various cat registries.[6]
#                          The cat is similar in anatomy to the other felid species: it has a strong flexible body, quick reflexes, sharp teeth and retractable claws adapted to killing small prey. Its night vision and sense of smell are well developed. Cat communication includes vocalizations like meowing, purring, trilling, hissing, growling and grunting as well as cat-specific body language. A predator that is most active at dawn and dusk(crepuscular), the cat is a solitary hunter but a social species. It can hear sounds too faint or too high in frequency for human ears, such as those made by mice and other small mammals.[7] Cats also secrete and perceive pheromones.[8]
#                          Female domestic cats can have kittens from spring to late autumn, with litter sizes often ranging from two to five kittens.[9] Domestic cats are bred and shown at events as registered pedigreed cats, a hobby known as cat fancy. Population control of cats may be affected by spaying and neutering, but their proliferation and the abandonment of pets has resulted in large numbers of feral cats worldwide, contributing to the extinction of entire bird, mammal, and reptile species.[10]
#                          Cats were first domesticated in the Near East around 7500 BC.[11] It was long thought that cat domestication began in ancient Egypt, where cats were venerated from around 3100 BC.[12][13] As of 2021, there were an estimated 220 million owned and 480 million stray cats in the world.[14][15] As of 2017, the domestic cat was the second-most popular pet in the United States, with 95.6 million cats owned[16][17][18] and around 42 million households own at least one cat.[19] In the United Kingdom, 26 % of adults have a cat with an estimated population of 10.9 million pet cats as of 2020.[20]''')
#         os.remove(filename)
#         return text
if __name__ == "__main__":
    app.run(debug=True)
