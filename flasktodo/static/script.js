const listItems = document.querySelectorAll("li")

for (let listItem of listItems) {
  listItem.addEventListener("mouseover", () => {
    const button = event.target.lastElementChild
    if (button) {
      button.style.display = "inline";
    }
  });
  listItem.addEventListener("mouseleave", () => {
    const button = event.target.lastElementChild
    if (button) {
      button.style.display = "none";
    }
  });
}
