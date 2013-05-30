import os
import sys

# 3rd party
import gi.repository as gir
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as\
    FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import pylab as pl

import quantpy as qp

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


class App:
    def __init__(self):
        self.builder = gir.Gtk.Builder()
        self.builder.add_from_file(os.path.join(DATA_DIR, "quantpy.glade"))
        self.builder.connect_signals(Handler(self))

        self.window = self.builder.get_object("window1")
        self.symbol = self.builder.get_object('entry1')

        self.window.show_all()


class Handler:
    def __init__(self, app):
        self.app = app

    def onDeleteWindow(self, *args):
        gir.Gtk.main_quit(*args)

    def onGoPressed(self, button):
        # Get symbols.
        symbol = self.app.symbol.get_text()
        asset = pd.io.data.DataReader(symbol, "yahoo")

        f = Figure(figsize=(5,4), dpi=100)
        a = f.add_subplot(111, label=symbol)
        a.plot(asset.index, asset['Adj Close'])

        canvas = FigureCanvas(f)
        canvas.set_size_request(800, 600)

        sw = self.app.builder.get_object('scrolledwindow1')
        # remove old children
        for child in sw.get_children():
            sw.remove(child)
        sw.add(canvas)
        sw.show_all()


def main():
    app = App()
    gir.Gtk.main()


if __name__ == "__main__":
    sys.exit(main())
