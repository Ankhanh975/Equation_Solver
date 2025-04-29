class Equation {
    constructor(expression_str) {
        // Recursively store the equation in a tree structure
        // with plus, minus, multiply, divide, power, and sqrt as nodes
        // Each node will have a value and a list of children nodes

        this.children = [];
        this.operation = null; // +, -, *, /, ^, sqrt

        // Remove all space in expression_str

        this.parseAll(expression_str);
    }
    parseAll(expression_str) {
        let temp = this.one_step_parse(expression_str);
        this.operation = temp[0];
        this.children = temp[1];

        this.children = this.children.map(element => {
            if (Equation.isBasedNode(element)) {
                return element;
            } else {
                return new Equation(element);
            }
        });
    }
    one_step_parse(expression_str) {
        // Parse the expression_str one step and return the operation and children nodes
        // with plus, minus, multiply, divide, power, and sqrt as operations

        // Handle '=' first
        // TODO: parathesis order

        function mark_parathesis_by_level(expression_str) {

            // Mark the parathesis by level
            let temp = [];
            let stack = [];
            let level = 0;
            for (let i = 0; i < expression_str.length; i++) {
                if (expression_str[i] == '(') {
                    level++;
                    stack.push(i);
                } else if (expression_str[i] == ')') {
                    level--;
                    temp.push([stack.pop(), i, level]);
                }
            }
            temp = temp.map(braces_pair => {
                var open = braces_pair[0];
                const close = braces_pair[1];

                if (open >= 4 && expression_str.substring(open - 4, open + 1) == "sqrt(") {
                    open = open - 4;
                }
                return [open, close];
            });
            console.log("called to mark_parathesis_by_level", expression_str);
            console.log("temp", temp);

            return temp;
        }
        function string_slice_ignoring_region(s, symbol, bounds) {
            let allFound = [];
            for (let i = 0; i < s.length; i++) {
                const char = s[i];
                if (char == symbol) {
                    if (bounds.some(bound => i >= bound[0] && i <= bound[1])) {
                        continue;
                    } else {
                        allFound.push(i);

                    }
                }
            }
            let temp = [];
            // Slice the string at allFound coordinate
            allFound.unshift(0);
            allFound.push(expression_str.length);
            for (let i = 1; i < allFound.length; i++) {
                if (i === 1) {
                    temp.push(expression_str.substring(allFound[i - 1], allFound[i]));
                } else {
                    temp.push(expression_str.substring(allFound[i - 1] + 1, allFound[i]));
                }
            }
            console.log("called to string_slice_ignoring_region", s, symbol, bounds);
            console.log("temp", temp);
            return temp;
        }

        function string_includes_ignoring_region(s, symbol, bounds) {
            for (let i = 0; i < s.length; i++) {
                const char = s[i];
                if (char == symbol) {
                    let is_in_region = false;
                    for (let j = 0; j < bounds.length; j++) {
                        const bound = bounds[j];
                        if (i >= bound[0] && i <= bound[1]) {
                            is_in_region = true;
                            break;
                        }
                    }
                    if (!is_in_region) {
                        return true;
                    }
                }
            }
            console.log("called to string_includes_ignoring_region", s, symbol, bounds);

            return false;
        }
        expression_str = expression_str.replaceAll(' ', '');
        if (expression_str[0] == "(" && expression_str[expression_str.length - 1] == ")") {
            expression_str = expression_str.substring(1, expression_str.length - 1);
        }
        let operation = undefined;
        let bounds = mark_parathesis_by_level(expression_str);
        let parts = [];

        if (Equation.isBasedNode(expression_str)) {
            return expression_str;
        }

        if (expression_str.includes('=')) {
            operation = '=';
            parts = expression_str.split('=');
            return [operation, parts];
        }
        console.log("bounds", bounds);


        const successed = ['+', '-', '*', '/', '^'].some((match, index) => {
            if (string_includes_ignoring_region(expression_str, match, bounds)) {
                operation = match;
                parts = string_slice_ignoring_region(expression_str, match, bounds);
                return true;
            }
        });
        if (!successed) {
            // Handle 'sqrt' next 
            if (expression_str.startsWith('sqrt')) {
                operation = 'sqrt';
                parts = [expression_str.slice(5, -1)]; // Remove 'sqrt(' and ')'
                return [operation, parts];
            }
        }
        return [operation, parts];

    }
    static isBasedNode(s) {
        // If s is a number or x

        function isNumber(n) {
            return !isNaN(n);
        }
        if (s instanceof Equation) {
            return false;
        } else if (s instanceof String || typeof (s) === 'string') {
            if (s == 'x' || isNumber(s)) {
                return true;
            } else {
                return false;
            }
        }
    }
}

function main() {
    var s3 = "sqrt(x+1) + sqrt(x) = 2";
    // var s3 = "x^3+x^2-2*x+1";
    var expression3 = new Equation(s3);
    console.log(expression3.children);
}
main();