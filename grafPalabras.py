# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 09:08:10 2019

@author: Luna Kadysz
"""

# Libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image    # to import the image
 
# Create a list of word (https://en.wikipedia.org/wiki/Data_visualization)
text=("El arte es entendido generalmente como cualquier actividad o producto realizado con una finalidad estética y también comunicativa, mediante la cual se expresan ideas, emociones y, en general, una visión del mundo, a través de diversos recursos, como los plásticos, lingüísticos, sonoros, corporales y mixtos.2? El arte es un componente de la cultura, reflejando en su concepción las bases económicas y sociales, y la transmisión de ideas y valores, inherentes a cualquier cultura humana a lo largo del espacio y el tiempo. Se suele considerar que con la aparición del Homo sapiens el arte tuvo en principio una función ritual, mágica o religiosa (arte paleolítico), pero esa función cambió con la evolución del ser humano, adquiriendo un componente estético y una función social, pedagógica, mercantil o simplemente ornamental. La noción de arte continúa sujeta a profundas disputas, dado que su definición está abierta a múltiples interpretaciones, que varían según la cultura, la época, el movimiento, o la sociedad para la cual el término tiene un determinado sentido. El vocablo ‘arte’ tiene una extensa acepción, pudiendo designar cualquier actividad humana hecha con esmero y dedicación, o cualquier conjunto de reglas necesarias para desarrollar de forma óptima una actividad: se habla así de “arte culinario”, “arte médico”, “artes marciales”, “artes de arrastre” en la pesca, etc. En ese sentido, arte es sinónimo de capacidad, habilidad, talento, experiencia. Sin embargo, más comúnmente se suele considerar al arte como una actividad creadora del ser humano, por la cual produce una serie de objetos (obras de arte) que son singulares, y cuya finalidad es principalmente estética. En ese contexto, arte sería la generalización de un concepto expresado desde antaño como “bellas artes”, actualmente algo en desuso y reducido a ámbitos académicos y administrativos. De igual forma, el empleo de la palabra arte para designar la realización de otras actividades ha venido siendo sustituido por términos como ‘técnica’ u ‘oficio’. En este artículo se trata de arte entendido como un medio de expresión humano de carácter creativo.")
 
# Load the image (http://python-graph-gallery.com/wp-content/uploads/wave.jpg)
wave_mask = np.array(Image.open("wave.png"))
 
# Make the figure
wordcloud = WordCloud(mask=wave_mask).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
