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
    // Global variables
    var canvas = $(selectorString);
    var canvasWidth;
    var canvasHeight;
    var pixels;
    var grid;

    if (!canvas){
        throw "Canvas object could not be found";
    }


    // Class Methods
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
        drawCells();
    };

    this.getGridPattern = function() {
        /**
         * This method returns the grid pattern in the form of a string.
         * Rows - "\n"
         * Alive Cells - "*"
         * Dead Cells - "-"
         */
        var patternString = "";
        for (var i = 0; i < grid.length; i++) {
            for (var j = 0; j < grid[i].length; j++) {
                patternString += grid[j][i] ? "*": "-";
            }
            if (i < (grid.length - 1)){
                patternString += "\n";
            }
        }

        return patternString;
    }

    this.setGridPattern = function(patternString) {
        /**
         * This method translates a string into a grid pattern, printing
         * it back on screen.
         * Rows - "\n"
         * Living Cells - "*"
         * Dead Cells - "-"
         */
        patternString = patternString.split("\n")
        for (var i = 0; i < patternString.length; i++) {
            for (var j = 0; j < patternString[i].length; j++) {
                if(patternString[j][i] == "*") {
                    grid[i][j] = true;
                }
            }
        }

        drawCells();
    }


    // Class Construction
    window.addEventListener("resize", this.setup, false)// resize on window change
    canvas.click(handleMouseClick);
    buildGrid();


    // Private functions
    function buildGrid() {
        /**
         * This function will build the grid variable
         * a 2-dimensional array of bools, representing dead or living cells.
         */
        grid = new Array(xCells); // columns

        for (var i = 0; i < xCells; i++) {
            grid[i] = new Array(yCells); // rows

            for (var j = 0; j < yCells; j++) {
                grid[i][j] = false;
            }
        }

    }

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
        for (var i = 0; i < (xCells + 1); i++){
            var lineColour =  (i == 0 || i == xCells)? "#000" : "#777";
            var offset = ((pixels * i) + 0.5);
            canvas.drawLine({
                strokeStyle: lineColour,
                strokeWidth: 1,
                x1: 0, y1: offset,
                x2: canvasWidth, y2: offset
            });

        }

        // Draw Y lines
        for (var i = 0; i < (yCells + 1); i++){
            var lineColour =  (i == 0 || i == yCells)? "#000" : "#777";
            var offset = ((pixels * i) + 0.5);
            canvas.drawLine({
                strokeStyle: lineColour,
                strokeWidth: 1,
                x1: offset, y1: 0,
                x2: offset, y2: canvasHeight
            });
        }
    };

    function handleMouseClick(e) {
        /**
         * Deals with mouse events.
         * Finds which cells as been clicked and toggles that cell's state.
         */
        var x = Math.floor(e.offsetX / pixels);
        var y = Math.floor(e.offsetY / pixels);

        toggleCell(x, y);
    }

    function toggleCell(x, y) {
        /**
         * This function toggles a cell's state and
         * paints the result on the grid.
         */
        var state = !grid[x][y];
        grid[x][y] = state;

        drawCell(x, y, state);
    }

    function drawCells() {
        /**
         * Draw all the cells, given the states in the grid array
         */
        for (var i = 0; i < xCells; i++) {
            for (var j = 0; j < yCells; j++) {
                drawCell(i, j, grid[i][j]);
            }
        }
    }

    function drawCell(x, y, state) {
        /**
         * Function that draws a given cell on the grid with a given state
         */
        var colour;
        colour = state ? "#000": "#FFF";

        $('canvas').drawRect({
            fillStyle: colour,
            x: (pixels * x) + 1, y: (pixels * y) + 1,
            width: pixels - 1,
            height: pixels - 1,
            fromCenter: false
        });
    }
}
