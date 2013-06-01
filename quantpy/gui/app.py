import os
import sys

# 3rd party
from gi.repository import Gio, Gtk
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as\
    FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import pylab as pl

import quantpy as qp

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


class App(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id='apps.quantpy',
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.join(DATA_DIR, 'app_menu.ui'))
        self.builder.add_from_file(os.path.join(DATA_DIR, "quantpy.ui"))

        self.builder.connect_signals(Handler(self))

        app_menu = self.builder.get_object('app_menu')
        self.set_app_menu(app_menu)

        # todo: look for a way to attach actions automatically, like handlers
        about_action = Gio.SimpleAction.new('about', None)
        about_action.connect('activate', self.onAppMenuAbout)
        self.add_action(about_action)

        quit_action = Gio.SimpleAction.new('quit', None)
        quit_action.connect('activate', self.onAppMenuQuit)
        self.add_action(quit_action)

    def do_activate(self):
        window = self.builder.get_object("window1")
        window.set_application(self)

        window.show_all()

    def onAppMenuAbout(self, action, parameter):
        self.builder.get_object('aboutdialog1').present()

    def onAppMenuQuit(self, action, parameter):
        self.quit()


class Handler:
    def __init__(self, app):
        self.app = app
        self.symbol = self.app.builder.get_object('entry1')

    def onDeleteWindow(self, *args):
        self.app.quit()

    def onGoPressed(self, button):
        symbol = self.symbol.get_text()
        asset = pd.io.data.DataReader(symbol, 'yahoo')

        figure = Figure(figsize=(5, 4), dpi=100, frameon=False)
        subplot = figure.add_subplot(1, 1, 1)
        subplot.plot(asset.index, asset['Adj Close'])
        subplot.autoscale_view(True, True, True)

        canvas = FigureCanvas(figure)
        canvas.set_size_request(500, 250)

        sw = self.app.builder.get_object('scrolledwindow1')
        # remove old children
        for child in sw.get_children():
            sw.remove(child)
        sw.add(canvas)
        sw.show_all()

    def onAboutResponse(self, dialog, response_id):
        if response_id in (Gtk.ResponseType.CANCEL,
                           Gtk.ResponseType.DELETE_EVENT):
            dialog.hide_on_delete()

    def onAboutDestroy(self, *args):
        # we don't want to destroy the about dialog
        return True


def main():
    app = App()
    status = app.run(sys.argv)
    return status


if __name__ == "__main__":
    sys.exit(main())
