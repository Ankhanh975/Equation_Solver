document.addEventListener("keydown", (event) => {
  if (
    window.location.href.includes("edit?") &&
    document.activeElement === document.body
  ) {
    let element;
    switch (event.key) {
      case "0":
        element = document.querySelector(
          "#editor-grid-settings-snap > div > div.editor__inspector__select__advanced.js-inspector__select__container > div > ul > li:nth-child(1) > a"
        );
        break;
      case "1":
        element = document.querySelector(
          "#editor-grid-settings-snap > div > div.editor__inspector__select__advanced.js-inspector__select__container > div > ul > li:nth-child(2) > a"
        );
        break;
      case "2":
        element = document.querySelector(
          "#editor-grid-settings-snap > div > div.editor__inspector__select__advanced.js-inspector__select__container > div > ul > li:nth-child(3) > a"
        );
        break;
      case "3":
        element = document.querySelector(
          "#editor-grid-settings-snap > div > div.editor__inspector__select__advanced.js-inspector__select__container > div > ul > li:nth-child(4) > a"
        );
        break;
      case "4":
        element = document.querySelector(
          "#editor-grid-settings-snap > div > div.editor__inspector__select__advanced.js-inspector__select__container > div > ul > li:nth-child(5) > a"
        );
        break;
      case "5":
        element = document.querySelector(
          "#editor-grid-settings-snap > div > div.editor__inspector__select__advanced.js-inspector__select__container > div > ul > li:nth-child(6) > a"
        );
        break;
      case "6":
        element = document.querySelector(
          "#editor-grid-settings-snap > div > div.editor__inspector__select__advanced.js-inspector__select__container > div > ul > li:nth-child(7) > a"
        );
      case "q":
        element = document.querySelector("#sidebar-collapse-button");
        if (element) {
          element.click();
          return;
        }
        break;
    }
    if (element) {
      element.click();
      // delay 1ms
      setTimeout(() => {
        element.click();
      }, 1);
    }
  }
});
