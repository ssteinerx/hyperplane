# postmaster_general.py
#
# Copyright 2023 kramo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""A singleton class for sending signals throughtout the app."""
from gi.repository import Gio, GObject, Gtk


class HypPostmasterGeneral(GObject.Object):
    """A singleton class for sending signals throughtout the app."""

    __gtype_name__ = "HypPostmasterGeneral"

    @GObject.Signal(name="zoom")
    def zoom(self, zoom_level: int) -> None:
        """
        Emitted whenever the zoom level changes.

        All widgets that are affected by zooming should connect to it.
        """

    @GObject.Signal(name="toggle-hidden")
    def toggle_hidden(self) -> None:
        """Emitted when the visibility of hidden files changes."""

    @GObject.Signal(name="tags-added")
    def tags_added(self) -> None:
        """
        Emitted whenever items have been removed from the list of tags.

        You can connect to this instead of `tags-changed` for performance
        reasons in an object like a filter or if you don't care about removed items.
        """
        self.emit("tags-changed")

    @GObject.Signal(name="tags-removed")
    def tags_removed(self) -> None:
        """
        Emitted whenever items have been removed from the list of tags.

        You can connect to this instead of `tags-changed` for performance
        reasons in an object like a filter or if you don't care about added items.
        """
        self.emit("tags-changed")

    @GObject.Signal(name="tags-changed")
    def tags_changed(self) -> None:
        """
        Emitted whenever the list of tags changes.

        All objects that keep an internal list of tags should connect to it
        and update their list accordingly.

        You can connect to `tags-removed` and `tags-added` if you need more specificity
        like when updating a filter.
        """

    @GObject.Signal(name="tag-location-created")
    def tag_location_created(
        self, tags: Gtk.StringList, new_location: Gio.File
    ) -> None:
        """
        Emitted whenever a new directory is created for tags.

        All widgets that display items from tags should connect to it
        and set it up so they append `new_location` to their list of locations
        if all `tags` are in their tags.
        """

    @GObject.Signal(name="trash-emptied")
    def trash_emptied(self) -> None:
        """Emitted when the trash is emptied by the app."""
