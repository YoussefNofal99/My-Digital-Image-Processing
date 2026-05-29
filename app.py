import os
import sys
import base64
import json
import io
import numpy as np
import cv2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['image.cmap'] = 'gray'
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from modules.Color_image_operation import color_operation
from modules.Edge_Detection import edge
from modules.Image_histogram import histogram
from modules.Image_Restoration import Salt_and_pepper_noise, Gaussian_noise
from modules.Image_segmentation import thresholding
from modules.Mathematical_Morphology import morphology
from modules.Neighborhood_processing import Non_linear_filters, Linear_filter
from modules.point_operation import point_operation

app = Flask(__name__, template_folder='frontend', static_folder='frontend')
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

def decoding(file):
    byte = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(byte, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("can't read this file")
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def encoding(img):
    if img is None:
        raise ValueError("Invalid image")
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    _, byte = cv2.imencode('.png', img)
    return base64.b64encode(byte).decode('utf-8')

def histplot(img1, img2, gray=True):
    plt.figure(figsize=(12, 6))
    if gray:
        if len(img1.shape) == 3:
            img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
        if len(img2.shape) == 3:
            img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
        plt.subplot(1, 2, 1)
        plt.hist(img1.ravel(), bins=256, range=[0, 256], color='gray')
        plt.title("Before Gray Histogram")
        plt.xlabel("Intensity")
        plt.ylabel("Frequency")
        plt.subplot(1, 2, 2)
        plt.hist(img2.ravel(), bins=256, range=[0, 256], color='gray')
        plt.title("After Gray Histogram")
        plt.xlabel("Intensity")
        plt.ylabel("Frequency")
    else:
        c = ['Red', 'Green', 'Blue']
        i = 0
        for j in c:
            plt.subplot(2, 3, i + 1)
            plt.hist(img1[:, :, i].ravel(), bins=256, range=[0, 256], color=j)
            plt.title("Before "+ j + " Histogram")
            plt.xlabel("Intensity")
            plt.ylabel("Frequency")
            plt.subplot(2, 3, i + 4)
            plt.hist(img2[:, :, i].ravel(), bins=256, range=[0, 256], color=j)
            plt.title("After "+ j + " Histogram")
            plt.xlabel("Intensity")
            plt.ylabel("Frequency")
            i += 1
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.clf()
    plt.close('all')
    return img_base64

def comparison(img1, img2):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(img1)
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.title('Result Image')
    plt.imshow(img2)
    plt.axis('off')
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.clf()
    plt.close('all')
    return img_base64

def processing(img, opt, para, img2):
    if opt == 'add':
        return point_operation(img).add(num=para.get('num', 50))
    elif opt == 'subtract':
        return point_operation(img).subtract(num=para.get('num', 50))
    elif opt == 'divide':
        return point_operation(img).divide(num=para.get('num', 1.5))
    elif opt == 'multiply':
        return point_operation(img).multiply(num=para.get('num', 1.5))
    elif opt == 'complement':
        return point_operation(img).complement()
    elif opt == 'addimg':
        if img2 is None:
            raise ValueError("image2 is required")
        return point_operation(img).addimg(img2)
    elif opt == 'subtractimg':
        if img2 is None:
            raise ValueError("image2 is required")
        return point_operation(img).subtractimg(img2)
    elif opt == 'divideimg':
        if img2 is None:
            raise ValueError("image2 is required")
        return point_operation(img).divideimg(img2)
    elif opt == 'multiplyimg':
        if img2 is None:
            raise ValueError("image2 is required")
        return point_operation(img).multiplyimg(img2)
    elif opt == 'change':
        return color_operation(img).change(num=para.get('num', 50), i=para.get('i', 0))
    elif opt == 'swap':
        return color_operation(img).swap(i=para.get('i', 0), j=para.get('j', 1))
    elif opt == 'eliminate':
        return color_operation(img).eliminate(i=para.get('i', 0))
    elif opt == 'histstretch':
        image2 = histogram(img).histstretch(gray=para.get('gray', True))
        plot = histplot(img, image2, para.get('gray'))
        return image2, plot
    elif opt == 'histequalization':
        image2 = histogram(img).histequalization(gray=para.get('gray', True))
        plot = histplot(img, image2, para.get('gray'))
        return image2, plot
    elif opt == 'sobel':
        return edge(img).sobel()
    elif opt == 'prewitt':
        return edge(img).prewitt()
    elif opt == 'roberts':
        return edge(img).roberts()
    elif opt == 'spadd':
        return Salt_and_pepper_noise(img).add(sprop=para.get('sprop', 0.01), pprop=para.get('pprop', 0.01))
    elif opt == 'spmean':
        return Salt_and_pepper_noise(img).averagefilter(x=para.get('x', 3), y=para.get('y', 3), add=para.get('add', False), sprop=para.get('sprop', 0.01), pprop=para.get('pprop', 0.01))
    elif opt == 'spmadian':
        return Salt_and_pepper_noise(img).medianfilter(x=para.get('x', 3), add=para.get('add', False), sprop=para.get('sprop', 0.01), pprop=para.get('pprop', 0.01))
    elif opt == 'outlier':
        return Salt_and_pepper_noise(img).outlierfilter(th=para.get('th', 30), x=para.get('x', 3), y=para.get('y', 3), add=para.get('add', False), sprop=para.get('sprop', 0.01), pprop=para.get('pprop', 0.01))
    elif opt == 'gadd':
        return Gaussian_noise(img).add(std=para.get('std', 15), mean=para.get('mean', 0))
    elif opt == 'gmean':
        return Gaussian_noise(img).averagefilter(x=para.get('x', 3), y=para.get('y', 3), std=para.get('std', 15), mean=para.get('mean', 0), add=para.get('add', False))
    elif opt == 'imageaverging':
        return Gaussian_noise(img).imageaverging(num=para.get('num', 10), std=para.get('std', 15), mean=para.get('mean', 0))
    elif opt == 'gthr':
        return thresholding(img).globalthresholding(thr=para.get('thr', 127))
    elif opt == 'adathr':
        return thresholding(img).adathresholding(bsize=para.get('bsize', 3), c=para.get('c', 5))
    elif opt == 'autothr':
        return thresholding(img).autothresholding(delta=para.get('delta', 0.1), maxi=para.get('maxi', 100))
    elif opt == 'dilation':
        return morphology(img).dilation(x=para.get('x', 3), y=para.get('y', 3))
    elif opt == 'erosion':
        return morphology(img).erosion(x=para.get('x', 3), y=para.get('y', 3))
    elif opt == 'closing':
        return morphology(img).closing(x=para.get('x', 3), y=para.get('y', 3))
    elif opt == 'opening':
        return morphology(img).opening(x=para.get('x', 3), y=para.get('y', 3))
    elif opt == 'internal':
        return morphology(img).internal(x=para.get('x', 3), y=para.get('y', 3))
    elif opt == 'external':
        return morphology(img).external(x=para.get('x', 3), y=para.get('y', 3))
    elif opt == 'gradient':
        return morphology(img).gradient(x=para.get('x', 3), y=para.get('y', 3))
    elif opt == 'mean':
        return Linear_filter(img).averagefilter(x=para.get('x', 3), y=para.get('y', 3))
    elif opt == 'laplacian':
        return Linear_filter(img).laplacianfilter(k=para.get('k', True))
    elif opt == 'median':
        return Non_linear_filters(img).medianfilter(x=para.get('x', 3))
    elif opt == 'max':
        return Non_linear_filters(img).maxfilter(x=para.get('x', 3), y=para.get('y', 3))
    elif opt == 'min':
        return Non_linear_filters(img).minfilter(x=para.get('x', 3), y=para.get('y', 3))
    elif opt == 'mode':
        return Non_linear_filters(img).modefilter(x=para.get('x', 3), y=para.get('y', 3))
    else:
        raise ValueError("Invalid operation")
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'NO image'}), 400
        img = decoding(request.files['image'])
        plot = None
        opt = request.form.get('opt', '')    
        para = json.loads(request.form.get('para', '{}'))
        img2 = None
        if 'image2' in request.files and request.files['image2'].filename:
            img2 = decoding(request.files['image2'])
        if opt == 'histequalization' or opt == 'histstretch':
            temp, plot = processing(img, opt, para, img2)
        else:
            temp = processing(img, opt, para, img2)
        comp = comparison(img, temp)
        result = encoding(temp)
        if plot is None:
            return jsonify({'image': result, 'comparison' : comp, 'format': 'png'})
        else:
            return jsonify({'image': result, 'comparison' : comp, 'plot': plot, 'format': 'png'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)