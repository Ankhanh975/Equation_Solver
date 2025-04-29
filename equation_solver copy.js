class Equation {


    constructor(expression) {
        // Recursively store the equation in a tree structure
        // with plus, minus, multiply, divide, power, and sqrt as nodes
        // Each node will have a value and a list of children nodes

        this.children = [];
        this.operation_list = ['*', '/', '+', '-', '^'];
        this.operation = null; // +, -, *, /, ^, sqrt

        // Remove all space in expression
        expression = expression.replaceAll(' ', '');
        this.parseAll(expression);
    }
    parseAll(expression) {
        // TODO: parathesis order
        let temp = this.one_step_parse(expression);
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
    one_step_parse(expression) {
        // Parse the expression one step and return the operation and children nodes
        // with plus, minus, multiply, divide, power, and sqrt as operations

        // Handle '=' first
        let parts = [];

        if (expression.includes('=')) {
            this.operation = '=';
            parts = expression.split('=');
            return [this.operation, parts];
        }

        // Handle 'sqrt' next 
        if (expression.startsWith('sqrt')) {
            this.operation = 'sqrt';
            parts = [expression.slice(5, -1)]; // Remove 'sqrt(' and ')'
            return [this.operation, parts];
        } else {
            this.operation_list.forEach(operation => {
                if (expression.includes(operation)) {
                    this.operation = operation;
                    parts = expression.split(operation);
                }
            });
            return [this.operation, parts];
        }


        throw new Error("Invalid expression");
    }
    print() {
        let operation = this.operation;
        let temp = this.children.map(child => {
            if (Equation.isBasedNode(child)) {
                return child;
            } else {
                return child.print();
            }
        });
        if (operation == "sqrt") {
            return operation + "(" + temp[0] + ")";
        } else {
            temp = temp.reduce((first, next) => {
                return first + operation + next
            });
            return temp
        }
    }
    static isBasedNode(s) {
        // If s is a number or x

        function isNumber(n) {
            return !isNaN(n);
        }
        if (s instanceof Equation) {
            return false;
        }
        if (s == 'x' || isNumber(s)) {
            return true;
        } else {
            return false;
        }
    }

    static one_step_BFS(e) {
        // One setp Breath First Search
        return [Equation];
    }
    static get_depth(e) {
        // The depth of the tree is the maximum depth of any node in the tree
        // e.children is a list of children nodes

        function getMaxOfArray(numArray) {
            return Math.max.apply(null, numArray);
        }
        if (Equation.isBasedNode(e)) {
            return 0;
        } else {
            let temp = e.children.map(child => Equation.get_depth(child));
            return getMaxOfArray(temp) + 1;
        }
    }
    static is_equal(a, b) {
        // Assume that a and b are simplified
        if (Equation.get_depth(a) === 0 && Equation.get_depth(b) === 0) {
            if (a == b) {
                return true;
            }
        } else {
            let condition1 = false;
            let condition2 = false;

            if (a.operation == b.operation) {
                condition1 = true;
            let condition3 = false;
            }
            if (a)
                return condition1 && condition2 && condition3
        }
    }
    static is_simplified(e) {
        // (1) If the equation contains numerial expressions, collapse them
        // (2) If the eqation can change a*a*a to a^3 or a+a+a tp 3*a
        // (3) If (a*a)*a or (a+a)+a have depth of 2, transform the structure so that it has depth 1 and length of e.children from 2 to 3.
        // TODO

        return true;
    }
    static simplify(e) {
        // TODO
        if (Equation.get_depth(e) == 0) {
            return;
        } else if (Equation.get_depth(e) == 1) {
            if (this.operation_list.includes(operation)) {

            }
        } else {

        }
    }
}

function equation_solver(s) {
    // TODO
    return;
}

function main() {
    var s = "sqrt(x^2 + x + 1) = 2";
    var expression = new Equation(s);
    console.log(expression.print()); // Print the tree structure
    console.log(Equation.get_depth(expression)); // Print the tree structure
}
main();