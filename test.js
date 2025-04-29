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
allFound = [7];
let temp = [];

var expression_str = "(sqrt(x)+sqrt(x+1))+1";
var temp2 = mark_parathesis_by_level(expression_str);
allFound = string_includes_ignoring_region(expression_str, "+", temp2)

console.log(allFound);

allFound.unshift(0);
allFound.push(expression_str.length);
for (let i = 1; i < allFound.length; i++) {
    if (i === 1) {
        temp.push(expression_str.substring(allFound[i - 1], allFound[i]));
    } else {
        temp.push(expression_str.substring(allFound[i - 1] + 1, allFound[i]));
    }
}
console.log("temp", temp);