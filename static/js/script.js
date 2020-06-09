function setup() {
    let canvas = createCanvas(600, 600);
    // relocating canvas into <div id="canvas-holder"...
    canvas.parent("canvas-holder");
}


function draw() {
    background(200);
    rect(10, 10, 10, 10);
}