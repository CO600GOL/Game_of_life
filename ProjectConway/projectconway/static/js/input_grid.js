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
    console.log("executed");
    var canvas = $(selectorString);
    var xCells = x;
    var yCells = y;
    var pixels = pixels;              // number of pixels per cell

    this.setup = function() {
        /**
         * Sets up the grid on top of the canvas.
         *  - Draw the grid
         *  - Setup the event listener (duck knows how this works in javascript)
         */
        // Draw Canvas
        var canvasWidth = (xCells * pixels) + (xCells + 1);
        var canvasHeight = (yCells * pixels) + (yCells + 1);
        canvas.css("width", canvasWidth);
        canvas.css("height", canvasHeight);

        // Draw Grid
        this.drawGrid();
    };

    this.drawGrid = function() {
        /**
         * Draws the grid.
         */
    };
}