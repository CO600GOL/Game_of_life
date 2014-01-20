/**
 * Javascript grid library that provides an editable grid, on a provided canvas.
 * This library requires JQuery to be installed.
 * Output is in the form of a string:
 *     "-" : denotes a dead cell
 *     "*" : denotes a living cell
 *     "\n" : denotes the next row
 */

function CanvasGrid(selectorString, xCells, yCells) {
    /**
     * This class represents an editable grid that can be used to input a pattern
     * to the Game of Life engine.
     */
    console.log("Creating CanvasGrid");
    var canvas = $(selectorString);
    var canvasWidth;
    var canvasHeight;
    var pixels;

    if (!canvas){
        throw "Canvas object could not be found";
    }
    $("#canvas-container").resize(this.setup); // resize on window change

    this.setup = function() {
        /**
         * Sets up the grid on top of the canvas.
         *  - Draw the grid
         *  - Setup the event listener (duck knows how this works in javascript)
         */
        // Resize the canvas taking into consideration the parent container
        resizeCanvas();

        // Draw Grid
        canvas.clearCanvas();
        drawGrid();
    };

    function resizeCanvas(){
        /**
         * This function resizes the Grid canvas, relative to
         * the size of the parent div and the number of pixels required.
         *
         * The parent container requires an id of "canvas-container"
         */
        // Size the canvas relative to the div above
        canvasWidth = $("#canvas-container").innerWidth();
        canvasWidth = canvasWidth - (canvasWidth % xCells);
        canvas[0].width =  canvasWidth + 1;

        // Set the size of the heigth relative to the size of the width
        canvasHeight = Math.floor((canvasWidth / xCells) * yCells);
        canvas[0].height = canvasHeight + 1;

        // Adjust the pixel size of squares, given the new grid size
        pixels = Math.floor(canvasWidth / xCells);
    }

    function drawGrid() {
        /**
         * Draws the grid.
         */
        console.log("Drawing grid");

        // Draw X lines
        for (var i = 0; i <= (xCells + 1); i++){
            var offset = ((pixels * i) + 0.5);
            canvas.drawLine({
                strokeStyle: '#000',
                strokeWidth: 1,
                x1: 0, y1: offset,
                x2: canvasWidth, y2: offset
            });

        }

        // Draw Y lines
        for (var i = 0; i <= (yCells + 1); i++){
           var offset = ((pixels * i) + 0.5);
           canvas.drawLine({
                    strokeStyle: '#000',
                    strokeWidth: 1,
                    x1: offset, y1: 0,
                    x2: offset, y2: canvasHeight
           });
        }
    };
}