const listItems = document.querySelectorAll("li")

for (let listItem of listItems) {
  listItem.addEventListener("mouseover", () => {

    for (let x = 0; x < event.target.childElementCount; x++){
      button = event.target.children[x]
      button.style.display = "inline";
    }
  });
  listItem.addEventListener("mouseleave", () => {
    for (let x = 0; x < event.target.childElementCount; x++){
      button = event.target.children[x]
      button.style.display = "none";
    }
  });
}
