import os
import sys
import threading

# 3rd party
from gi.repository import Gdk, Gio, GLib, GObject, Gtk
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as\
    FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import pylab as pl

import quantpy as qp
from quantpy.gui import settings, utils


class App(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id='apps.quantpy',
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # load UI files
        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.join(settings.DATA_DIR, 'app_menu.ui'))

        # get and set the App Menu
        app_menu = self.builder.get_object('app_menu')
        self.set_app_menu(app_menu)

        # Add App Menu About action
        about_action = Gio.SimpleAction.new('about', None)
        about_action.connect('activate', self.on_about_action_activate)
        self.add_action(about_action)

        # Add App Menu Quit action
        quit_action = Gio.SimpleAction.new('quit', None)
        quit_action.connect('activate', self.on_quit_action_activate)
        self.add_action(quit_action)

    def do_activate(self):
        self.builder.add_from_file(os.path.join(settings.DATA_DIR, 'quantpy.ui'))
        # connect signals
        self.builder.connect_signals(Handler(self))

        # main window
        self.main_window = self.builder.get_object('main_window')
        self.main_window.set_application(self)
        self.main_window.show_all()

    def on_about_action_activate(self, action, parameter):
        """Show the About dialog"""
        self.builder.get_object('about_dialog').present()

    def on_quit_action_activate(self, action, parameter):
        """Quit the Application"""
        self.quit()

    def _display_assets(self, data=None):
        """Display the dashboard assets
        'data' is not needed, but Gdk.threads_add_idle needs to pass that
        """
        # download the asset updates
        assets = utils.get_dashboard_asset_updates()

        assets_box = self.builder.get_object('assets_box')
        # remove the spinner and the loading text
        for child in assets_box.get_children():
            assets_box.remove(child)

        builder = Gtk.Builder()
        for asset in assets.iterrows():
            # get the asset UI
            builder.add_from_file(os.path.join(
                settings.DATA_DIR, 'dashboard_asset.ui'))
            # change the link button text and link
            name_link_button = builder.get_object('name_link_button')
            name_link_button.set_label(settings.DASHBOARD_ASSETS[asset[0]][0])
            name_link_button.set_uri('http://finance.yahoo.com/q?s=%s' %
                                     asset[0])
            # change the price label and tooltip
            price_label = builder.get_object('price_label')
            price_label.set_label(str(asset[1]['l1']))
            price_label.set_tooltip_text(settings.YAHOO_SYMBOL_TAGS['l1'])
            # change the change in price label and tooltip
            change_label = builder.get_object('change_label')
            change_label.set_label(str(asset[1]['c6']))
            change_label.set_tooltip_text(settings.YAHOO_SYMBOL_TAGS['c6'])
            # change the percentage change in price label and tooltip
            pct_change_label = builder.get_object('pct_change_label')
            pct_change_label.set_label(str(asset[1]['p2']))
            pct_change_label.set_tooltip_text(settings.YAHOO_SYMBOL_TAGS['p2'])

            # add the asset_box to assets_box
            asset_box = builder.get_object('asset_box')
            assets_box.pack_start(asset_box, False, False, 5)

        assets_box.show_all()
        # update every 5 minutes
        GLib.timeout_add_seconds(5 * 60, self._display_assets, None)

    def display_assets(self):
        """Call the _display_assets as a Gdk child thread"""
        Gdk.threads_add_idle(GLib.PRIORITY_DEFAULT_IDLE, self._display_assets,
                             None)


class Handler:
    def __init__(self, app):
        self.app = app
        self.symbol = self.app.builder.get_object('search_entry')

    def on_about_dialog_response(self, dialog, response_id):
        """About dialog response handler"""
        if response_id in (Gtk.ResponseType.CANCEL,
                           Gtk.ResponseType.DELETE_EVENT):
            dialog.hide_on_delete()

    def on_about_dialog_delete_event(self, *args):
        """About dialog quit handler"""
        # we don't want to destroy the about dialog, we just want to hide it
        return True

    def onGoPressed(self, button):
        symbol = self.symbol.get_text()
        asset = pd.io.data.DataReader(symbol, 'yahoo')  # @UndefinedVariable

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

    def on_main_window_show(self, *args):
        """When the main window is shown"""
        # display assets
        # Gdk.threads_add_idle(GLib.PRIORITY_DEFAULT, self.app.display_assets())
        threading.Thread(target=self.app.display_assets).start()


def main():
    GObject.threads_init()
    Gdk.threads_init()
    app = App()
    status = app.run(sys.argv)
    return status


if __name__ == '__main__':
    sys.exit(main())
