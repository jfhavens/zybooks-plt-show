import base64
from io import BytesIO
import textwrap

import matplotlib.pyplot as plt

BASE_URL = 'https://jfhavens.github.io/zybooks-plt-show/'


def plt_show():
    buffer = BytesIO()
    plt.savefig(buffer, format='svg')
    svg_data = base64.b64encode(buffer.getbuffer()).decode('ascii')
    wrapped = textwrap.fill(svg_data, width=80, break_on_hyphens=False)
    print(f'{BASE_URL}/#')
    print(wrapped)


plt.show = plt_show
