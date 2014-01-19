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
    this.canvasSelector = selectorString;
    if (!canvas){
        throw "Canvas object could not be found";
    }
    var xCells = x;
    var yCells = y;
    var canvasWidth = (xCells * (pixels + 1)) + (xCells + 1);
    var canvasHeight = (yCells * (pixels + 1)) + (yCells + 1);

    this.setup = function() {
        /**
         * Sets up the grid on top of the canvas.
         *  - Draw the grid
         *  - Setup the event listener (duck knows how this works in javascript)
         */
         // Draw Canvas
         canvas[0].width =  canvasWidth;
         canvas[0].height = canvasHeight;

         // Draw Grid
         drawGrid();
    };

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
                strokeWidth: 0.5,
                x1: 0, y1: offset,
                x2: canvasWidth, y2: offset
            });

            canvas.drawLine({
                strokeStyle: '#000',
                strokeWidth: 0.5,
                x1: offset, y1: 0,
                x2: offset, y2: canvasHeight
            });
        }
    };
}