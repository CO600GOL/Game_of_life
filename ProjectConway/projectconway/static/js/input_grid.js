/**
 * Javascript grid library that provides an editable grid, on a provided canvas.
 * This library requires JQuery to be installed.
 * Output is in the form of a string:
 *     "-" : denotes a dead cell
 *     "*" : denotes a living cell
 *     "\n" : denotes the next row
 */

function CanvasGrid(selectorString, x, y, pixels) {
    /**
     * This class represents an editable grid that can be used to input a pattern
     * to the Game of Life engine.
     */
    console.log("Creating CanvasGrid");
    var canvas = $(selectorString);
    var xCells = x;
    var yCells = y;
    var canvasWidth = (xCells * (pixels + 1)) + (xCells + 1);
    var canvasHeight = (yCells * (pixels + 1)) + (yCells + 1);

    if (!canvas){
        throw "Canvas object could not be found";
    }

    this.setup = function() {
        /**
         * Sets up the grid on top of the canvas.
         *  - Draw the grid
         *  - Setup the event listener (duck knows how this works in javascript)
         */
        resizeCanvas();
        $(window).resize(resizeCanvas); // resize on window change

        // Draw Grid
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
        var xSize = $("#canvas-container").innerWidth();
        canvas[0].width =  xSize;
        //Set the size of the heigth relative to the size of the width
        var ySize = Math.floor((xSize / xCells) * yCells);
        canvas[0].height = ySize;
    }

    function drawGrid() {
        /**
         * Draws the grid.
         */
        console.log("Drawing grid");

        // Draw X lines
        var noOfLines = xCells + 1;

        for (var i = 0; i <= noOfLines; i++){
            var offset = ((pixels * i) + 0.5);
            canvas.drawLine({
                strokeStyle: '#000',
                strokeWidth: 1,
                x1: 0, y1: offset,
                x2: canvasWidth, y2: offset
            });

            canvas.drawLine({
                strokeStyle: '#000',
                strokeWidth: 1,
                x1: offset, y1: 0,
                x2: offset, y2: canvasHeight
            });
        }
    };
}