from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
from fastbook import *
from fastai.vision.all import *
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


urls = search_images_ddg('driver on phone', max_images=1)
len(urls), urls[0]

dest = Path('driveronphone.png')
if not dest.exists(): download_url(urls[0], dest, show_progress=False)

im = Image.open(dest)

searches = 'driver on phone', 'people driving'
path = Path('phone or not')

if not path.exists():
    for o in searches:
        dest = path/o
        dest.mkdir(exist_ok=True, parents=True)
        results = search_images_ddg(f'{o}')
        download_images(dest, urls=results[:50])
        resize_images(dest, max_size=400, dest=dest)

failed = verify_images(get_image_files(path))
failed.map(Path.unlink);

dls = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=[Resize(192, method='squish')]
).dataloaders(path)

dls.show_batch(max_n=6)

learn = cnn_learner(dls, resnet18, metrics=error_rate)
learn.fine_tune(3)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        is_onphone, _, probs = learn.predict(PILImage.create('static/uploads/' + filename))
        flash("This is a " + is_onphone + ".")
        print(f"Probability driver is on phone: {probs[0]:.4f}")
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)