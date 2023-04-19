// containers
const container = document.getElementById("gridContainer");
const clearBtn = document.getElementById("clearBtn");

// default values
let gridSize = 28;
let penColor = "#000000";

// toggle variables
let isMouseDown = false;

// check if mouse button is pressed
document.addEventListener("mousedown", () => (isMouseDown = true));
document.addEventListener("mouseup", () => (isMouseDown = false));

// create grid with x rows and x cols
function createGrid(amount) {
  container.style.setProperty("--grid-rows", amount);
  container.style.setProperty("--grid-cols", amount);

  for (i = 0; i < amount * amount; i++) {
    let cell = document.createElement("div");
    container.appendChild(cell).className = "grid-item";
  }
}

createGrid(gridSize);
sketchFunctionality();

// clear button
clearBtn.addEventListener("click", () => {
  container.textContent = "";
  createGrid(gridSize, gridSize);
  sketchFunctionality();
});

// main function
function sketchFunctionality() {
  const gridBoxes = document.querySelectorAll(".grid-item");

  // drawing on mouseover
  gridBoxes.forEach((gridBox) => {
    gridBox.addEventListener("mouseover", (e) => {
      if (!isMouseDown) {
        return;
      } else {
        e.target.style.backgroundColor = penColor;
      }
    });

    // drawing on mouse click
    gridBox.addEventListener("click", (e) => {
      e.target.style.backgroundColor = penColor;
    });
  });
}
