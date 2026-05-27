import igv from "https://esm.sh/igv@3.7.3";

/**
 * @typedef Config
 * @property {string} genome
 * @property {(string | Array<string>)=} locus
 * @property {Array<Record<string, unknown>>} tracks
 */

/**
 * @typedef Model
 * @property {Config} config
 */

/**
 * Custom messages sent from Python.
 * @typedef {{ type: "search", locus: string | Array<string> }} SearchMessage
 */

/** @type {import("npm:@anywidget/types").Render<Model>} */
async function render({ model, el }) {
  const browser = await igv.createBrowser(el, model.get("config"));

  /** @param {SearchMessage} msg */
  const onMsg = (msg) => {
    if (msg?.type === "search" && msg.locus) {
      const locus = Array.isArray(msg.locus) ? msg.locus.join(" ") : msg.locus;
      Promise.resolve(browser.search(locus)).catch((e) => console.error(e));
    }
  };
  model.on("msg:custom", onMsg);

  return () => {
    model.off("msg:custom", onMsg);
    igv.removeBrowser(browser);
  };
}

export default { render };
