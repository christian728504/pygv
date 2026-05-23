from __future__ import annotations

import pathlib

import anywidget
import msgspec
import traitlets

from ._config import Config


class Browser(anywidget.AnyWidget):
    _esm = pathlib.Path(__file__).parent / "static" / "widget.js"
    config = traitlets.Instance(Config).tag(
        sync=True, to_json=lambda x, _: msgspec.to_builtins(x)
    )

    def __init__(self, config: Config) -> None:
        super().__init__(config=config.servable())

    def search(self, locus: str | list[str]) -> None:
        """Navigate the live browser to a locus.

        Parameters
        ----------
        locus : str | list[str]
            A genomic locus (e.g. ``"chr2:1,000-2,000"``), a feature/gene name
            (e.g. ``"BRCA1"``), or a list of loci for a multi-locus view.

        Notes
        -----
        Takes effect only once the widget is displayed (the message is delivered
        to the rendered frontend). To set the locus a browser opens with, use
        :func:`pygv.locus` before :func:`pygv.browse`.
        """
        self.send({"type": "search", "locus": locus})
