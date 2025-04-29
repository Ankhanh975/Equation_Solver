class Equation {
    constructor(expression_str) {
        // Recursively store the equation in a tree structure
        // with plus, minus, multiply, divide, power, and sqrt as nodes
        // Each node will have a value and a list of children nodes

        this.children = [];
        this.operation = null; // +, -, *, /, ^, sqrt

        // Remove all space in expression_str
        expression_str = expression_str.replaceAll(' ', '');
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
                return first + operation + next;
            });
            return temp;
        }
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
        function zip(a, b) {
            // zip([1,2,3], ["a","b","c"])
            // [[1, "a"], [2, "b"], [3, "c"]]
            return a.map((k, i) => [k, b[i]]);
        }

        if (Equation.get_depth(a) === 0 && Equation.get_depth(b) === 0) {
            if (a == b) {
                return true;
            }
        } else if (Equation.get_depth(a) === Equation.get_depth(b)) {

            let condition1 = false;
            let condition2 = false;

            if (a.operation == b.operation) {
                condition1 = true;
            }
            let temp = zip(a.children, b.children);


            condition2 = temp.every(childs => Equation.is_equal(childs[0], childs[1]));
            return condition1 && condition2;

        } else {
            return false;
        }
    }
    static is_simplified(e) {
        // (1) if not contains numerial expressions
        // (2) match for a+a, a*a, a-a or a/a
        function is_simplified_1(e) {
            function contains_unsolve_variable(e) {
                if (Equation.isBasedNode(e) && e == 'x') {
                    return true;
                } else if (!Equation.isBasedNode(e)) {
                    let temp = e.children.some(child => contains_unsolve_variable(child));
                    return temp;
                } else {
                    return false;
                }
            }
            if (Equation.get_depth(e) == 0) {
                return true;
            } else {

                if (contains_unsolve_variable(e)) {
                    let temp = e.children.every(child => is_simplified_1(child));
                    return temp;
                } else {
                    return false;
                }
            }
        }

        function is_simplified_2(e) {
            function is_equal(array, func) {
                // Check if any elements are equal to each others
                // check all permutations of the array

                if (array.length == 0) {
                    return true;
                } else {
                    let temp = array.some((element, index) => {
                        let temp2 = array.some((element2, index2) => {
                            if (index == index2) {
                                return false;
                            } else {
                                return func(element, element2);
                            }
                        });
                        return temp2;
                    });
                    return temp;
                }
            }
            if (Equation.get_depth(e) == 0) {
                return true;
            } else {
                if (["*", "/", "+", "-"].includes(e.operation)) {
                    if (is_equal(e.children, Equation.is_equal)) {
                        return false;
                    }
                }
                return !e.children.some(e => !is_simplified_2(e));
            }
        }
        return is_simplified_1(e) && is_simplified_2(e);
    }
}

class Solver {
    static one_step_BFS(e) {
        // One step Breath First Search over all levels.
        // TODO
        return [Equation];
    }
    static is_immediately_solvable(e) {
        // Check if the equation is solved or not
        if (Equation.get_depth(e) === 1) {
            return true;
        }
        return false;
    }
    static solve(equation) {
        // Solve the equation and return the solution
        // The equation is in the form of Equation class

        if (equation.operation == '=') {
            let left = equation.children[0];
            let right = equation.children[1];
            if (Equation.is_simplified(left) && Equation.is_simplified(right)) {
                if (Equation.is_equal(left, right)) {
                    return "All real numbers are solutions";
                } else {
                    return "No solution";
                }
            } else {
                // Solve the equation recursively
                let left_solution = Solver.solve(left);
                let right_solution = Solver.solve(right);
                return [left_solution, right_solution];
            }
        } else if (equation.operation == 'sqrt') {
            let child = equation.children[0];
            if (Equation.is_simplified(child)) {
                return Solver.solve(child);
            } else {
                return undefined;
            }
        } else if (equation.operation == '+') {
            // Handle addition
            let temp = equation.children.map(child => Solver.solve(child));
            return temp.reduce((first, next) => first + next);
        } else if (equation.operation == '-') {
            // Handle subtraction
            let temp = equation.children.map(child => Solver.solve(child));
            return temp.reduce((first, next) => first - next);
        } else if (equation.operation == '*') {
            // Handle multiplication
            let temp = equation.children.map(child => Solver.solve(child));
            return temp.reduce((first, next) => first * next);
        } else if (equation.operation == '/') {
            // Handle division
            let temp = equation.children.map(child => Solver.solve(child));
            return temp.reduce((first, next) => first / next);
        } else if (equation.operation == '^') {
            // Handle power
            let base = Solver.solve(equation.children[0]);
            let exponent = Solver.solve(equation.children[1]);
            return Math.pow(base, exponent);
        }
    }

    static linear_equation(a, b) {

        // Solve the linear equation ax + b = 0
        // Return x = -b/a
        if (a == 0) {
            return undefined;
        } else {
            return -b / a;
        }
    }

    static quadratic_equation(a, b, c) {
        // Solve the quadratic equation ax^2 + bx + c = 0
        // Return x = (-b + sqrt(b^2 - 4ac)) / (2a) or x = (-b - sqrt(b^2 - 4ac)) / (2a)
        if (a == 0) {
            return linear_equation(b, c);
        } else {
            let d = b * b - 4 * a * c;
            if (d < 0) {
                return undefined;
            } else if (d == 0) {
                return -b / (2 * a);
            } else {
                return [(-b + Math.sqrt(d)) / (2 * a), (-b - Math.sqrt(d)) / (2 * a)];
            }
        }

    }

    static cubic_equation(a, b, c, d) {
        // Solve the cubic equation ax^3 + bx^2 + cx + d = 0
        if (a === 0) {
            // If a is 0, reduce to a quadratic equation
            return quadratic_equation(b, c, d);
        }

        // Normalize coefficients
        b /= a;
        c /= a;
        d /= a;

        // Substitute x = y - b/3 to eliminate the quadratic term
        const p = c - (b * b) / 3;
        const q = (2 * b * b * b) / 27 - (b * c) / 3 + d;

        // Calculate the discriminant
        const discriminant = (q * q) / 4 + (p * p * p) / 27;

        if (discriminant > 0) {
            // One real root and two complex roots
            const u = Math.cbrt(-q / 2 + Math.sqrt(discriminant));
            const v = Math.cbrt(-q / 2 - Math.sqrt(discriminant));
            const root = u + v - b / 3;
            return [root]; // Only the real root
        } else if (discriminant === 0) {
            // All roots are real, at least two are equal
            const u = Math.cbrt(-q / 2);
            const root1 = 2 * u - b / 3;
            const root2 = -u - b / 3;
            return [root1, root2]; // Two real roots (one is repeated)
        } else {
            // Three distinct real roots
            const r = Math.sqrt(-(p * p * p) / 27);
            const phi = Math.acos(-q / (2 * r));
            const root1 = 2 * Math.cbrt(r) * Math.cos(phi / 3) - b / 3;
            const root2 = 2 * Math.cbrt(r) * Math.cos((phi + 2 * Math.PI) / 3) - b / 3;
            const root3 = 2 * Math.cbrt(r) * Math.cos((phi + 4 * Math.PI) / 3) - b / 3;
            return [root1, root2, root3];
        }
    }

    static quartic_equation(a, b, c, d, e) {
        // Solve the quartic equation ax^4 + bx^3 + cx^2 + dx + e = 0
        if (a === 0) {
            // If a is 0, reduce to a cubic equation
            return cubic_equation(b, c, d, e);
        }

        // Normalize coefficients
        b /= a;
        c /= a;
        d /= a;
        e /= a;

        // Substitute x = y - b/4 to eliminate the cubic term
        const p = c - (3 * b * b) / 8;
        const q = d - (b * b * b) / 8 + (b * c) / 2;
        const r = e - (3 * b * b * b * b) / 256 + (b * b * c) / 16 - (b * d) / 4;

        if (q === 0) {
            // Special case: biquadratic equation
            const roots = quadratic_equation(1, p, r);
            return roots.map(root => [Math.sqrt(root), -Math.sqrt(root)]).flat().filter(root => !isNaN(root));
        }

        // Solve the resolvent cubic: z^3 + (p/2)z^2 + ((p^2 - 4r)/16)z - q^2/64 = 0
        const cubicRoots = cubic_equation(1, p / 2, (p * p - 4 * r) / 16, -q * q / 64);
        const z = cubicRoots.find(root => root >= 0); // Choose the real, non-negative root

        if (z === undefined) {
            return undefined; // No real roots
        }

        // Solve two quadratic equations
        const sqrtZ = Math.sqrt(z);
        const quadratic1 = quadratic_equation(1, sqrtZ, (p / 2) + z - (q / (2 * sqrtZ)));
        const quadratic2 = quadratic_equation(1, -sqrtZ, (p / 2) + z + (q / (2 * sqrtZ)));

        // Combine all roots
        const roots = [...quadratic1, ...quadratic2].map(root => root - b / 4);
        return roots.filter(root => !isNaN(root));
    }
}



function main() {
    var s1 = "sqrt(x^2 + x + 1 + 1) = 2";
    var s2 = "sqrt(x^2 + x + 2) = 2";

    var s3 = "sqrt(x^2) + 1 + sqrt(x^3) = 2";
    // var s3 = "sqrt(x^3) + 1 + sqrt(x^3)";
    // var s3 = "sqrt(x^2)";
    var expression3 = new Equation(s3);

    console.log(Equation.is_simplified(expression3));

    // console.log(Equation.is_equal(new Equation("sqrt(x^2)"), new Equation("sqrt(x^2)")));
}
main();