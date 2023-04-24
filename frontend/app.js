// containers
const container = document.getElementById("gridContainer");
const clearBtn = document.getElementById("clearBtn");
const computeBtn = document.getElementById("computeBtn");
const resultText = document.getElementById("result");
const form = document.getElementById("form");

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

async function computeData(gridBoxes, limit) {
  let frame = {};
  frame[`label`] = ["?"];

  // Generate pixels array
  let i = 1;
  let j = 1;
  gridBoxes.forEach((pixel) => {
    if (j == 29) {
      i += 1;
      j = 1;
    }
    // If pixel is white
    if (pixel.style.backgroundColor == "") frame[`${i}x${j}`] = [0];
    else frame[`${i}x${j}`] = [255];
    j += 1;
  });

  const payload = { frame, limit };

  try {
    resultText.textContent = "Loading...";
    const response = await fetch("http://localhost:3000/classify", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    const digit = data.digit;
    resultText.textContent = digit;
  } catch (err) {
    resultText.textContent = "ERROR";
  }
}

// computeBtn.addEventListener("click", async () => {
//   const gridBoxes = document.querySelectorAll(".grid-item");
//   await computeData(gridBoxes);
// });

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const gridBoxes = document.querySelectorAll(".grid-item");
  const limit = e.target.limitInput.value;

  await computeData(gridBoxes, limit);
});
