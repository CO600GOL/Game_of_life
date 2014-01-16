/**
 * Javascript grid library that provides an editable grid, on a provided canvas.
 * This library requires JQuery to be installed.
 * Output is in the form of a string:
 *     "-" : denotes a dead cell
 *     "*" : denotes a living cell
 *     "\n" : denotes the next row
 */

function Grid(gridId, x, y) {
    /**
     * This class represents an editable grid that can be used to input a pattern
     * to the Game of Life engine.
     */
    var canvas = $(gridId);
    var xCells = x;
    var yCells = y;

    this.setup = function() {
        /**
         *
         */

    };
};