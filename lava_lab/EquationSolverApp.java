import java.util.*;
import java.util.stream.Collectors;

// Abstract syntax tree for expressions
abstract class Expression {
    public abstract double evaluate(double x);

    public abstract int complexity();
}

class Constant extends Expression {
    private final double value;

    public Constant(double value) {
        this.value = value;
    }

    public double getValue() {
        return value;
    }

    @Override
    public double evaluate(double x) {
        return value;
    }

    @Override
    public int complexity() {
        return 1;
    }

    @Override
    public String toString() {
        return Double.toString(value);
    }
}

class Variable extends Expression {
    @Override
    public double evaluate(double x) {
        return x;
    }

    @Override
    public int complexity() {
        return 1;
    }

    @Override
    public String toString() {
        return "x";
    }
}

class UnaryOperation extends Expression {
    public enum Op {
        NEG
    }

    final Op op;
    final Expression expr;

    public UnaryOperation(Op op, Expression expr) {
        this.op = op;
        this.expr = expr;
    }

    @Override
    public double evaluate(double x) {
        return op == Op.NEG ? -expr.evaluate(x) : 0;
    }

    @Override
    public int complexity() {
        return 1 + expr.complexity();
    }

    @Override
    public String toString() {
        return "(" + op + " " + expr + ")";
    }
}

class BinaryOperation extends Expression {
    public enum Op {
        ADD, SUB, MUL, DIV, POW
    }

    final Op op;
    final Expression left, right;

    public BinaryOperation(Op op, Expression left, Expression right) {
        this.op = op;
        this.left = left;
        this.right = right;
    }

    public Op getOp() {
        return op;
    }

    public Expression getLeft() {
        return left;
    }

    public Expression getRight() {
        return right;
    }

    @Override
    public double evaluate(double x) {
        double a = left.evaluate(x), b = right.evaluate(x);
        switch (op) {
            case ADD:
                return a + b;
            case SUB:
                return a - b;
            case MUL:
                return a * b;
            case DIV:
                return a / b;
            case POW:
                return Math.pow(a, b);
        }
        throw new IllegalStateException();
    }

    @Override
    public int complexity() {
        return 1 + left.complexity() + right.complexity();
    }

    @Override
    public String toString() {
        return "(" + left + " " + op + " " + right + ")";
    }
}

class Equation {
    private final Expression left, right;

    public Equation(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }

    public Expression getLeft() {
        return left;
    }

    public Expression getRight() {
        return right;
    }

    @Override
    public String toString() {
        return left + " = " + right;
    }
}

class RecursiveEquationSolver {
    public List<Double> solve(Equation eq) {
        if (eq.getRight().complexity() > eq.getLeft().complexity())
            eq = new Equation(eq.getRight(), eq.getLeft());
        return solveRec(eq).stream().distinct().collect(Collectors.toList());
    }

    private List<Double> solveRec(Equation eq) {
        eq = simplifyEquation(eq);
        Optional<Double> lin = tryLinear(eq);
        if (lin.isPresent())
            return List.of(lin.get());
        if (eq.getLeft() instanceof Variable && eq.getRight() instanceof Constant)
            return List.of(((Constant) eq.getRight()).getValue());
        Expression L = eq.getLeft(), R = eq.getRight();
        List<Equation> next = new ArrayList<>();
        if (L instanceof BinaryOperation) {
            BinaryOperation bin = (BinaryOperation) L;
            Expression A = bin.getLeft(), B = bin.getRight();
            switch (bin.getOp()) {
                case ADD:
                    next.add(new Equation(A, new BinaryOperation(BinaryOperation.Op.SUB, R, B)));
                    break;
                case SUB:
                    next.add(new Equation(A, new BinaryOperation(BinaryOperation.Op.ADD, R, B)));
                    break;
                case MUL:
                    next.add(new Equation(A, new Constant(0)));
                    next.add(new Equation(B, new BinaryOperation(BinaryOperation.Op.DIV, R, A)));
                    break;
                case DIV:
                    next.add(new Equation(A, new BinaryOperation(BinaryOperation.Op.MUL, B, R)));
                    break;
                case POW:
                    if (B instanceof Constant) {
                        double n = ((Constant) B).getValue();
                        Expression root = new BinaryOperation(BinaryOperation.Op.POW, R, new Constant(1.0 / n));
                        next.add(new Equation(A, root));
                        if (isEven(n))
                            next.add(new Equation(A, new UnaryOperation(UnaryOperation.Op.NEG, root)));
                    }
                    break;
            }
        } else {
            return solveRec(new Equation(eq.getRight(), eq.getLeft()));
        }
        return next.stream().flatMap(e -> solveRec(e).stream()).collect(Collectors.toList());
    }

    private Equation simplifyEquation(Equation eq) {
        return new Equation(simplifyExpression(eq.getLeft()), simplifyExpression(eq.getRight()));
    }

    private Expression simplifyExpression(Expression e) {
        if (e instanceof BinaryOperation) {
            BinaryOperation bin = (BinaryOperation) e;
            Expression L = simplifyExpression(bin.getLeft());
            Expression R = simplifyExpression(bin.getRight());
            if (L instanceof Constant && R instanceof Constant) {
                double a = ((Constant) L).getValue(), b = ((Constant) R).getValue();
                switch (bin.getOp()) {
                    case ADD:
                        return new Constant(a + b);
                    case SUB:
                        return new Constant(a - b);
                    case MUL:
                        return new Constant(a * b);
                    case DIV:
                        return new Constant(a / b);
                    case POW:
                        return new Constant(Math.pow(a, b));
                }
            }
            return new BinaryOperation(bin.getOp(), L, R);
        }
        if (e instanceof UnaryOperation) {
            UnaryOperation u = (UnaryOperation) e;
            Expression c = simplifyExpression(u.expr);
            if (c instanceof Constant && u.op == UnaryOperation.Op.NEG)
                return new Constant(-((Constant) c).getValue());
            return new UnaryOperation(u.op, c);
        }
        return e;
    }

    private Optional<Double> tryLinear(Equation eq) {
        double[] L = extractLinear(eq.getLeft());
        double[] R = extractLinear(eq.getRight());
        if (L == null || R == null)
            return Optional.empty();
        double a = L[0], b = L[1], c = R[0], d = R[1];
        if (Math.abs(a - c) < 1e-9)
            return Optional.empty();
        return Optional.of((d - b) / (a - c));
    }

    private double[] extractLinear(Expression e) {
        if (e instanceof Constant)
            return new double[] { 0, ((Constant) e).getValue() };
        if (e instanceof Variable)
            return new double[] { 1, 0 };
        if (e instanceof UnaryOperation) {
            double[] c = extractLinear(((UnaryOperation) e).expr);
            return c == null ? null : new double[] { -c[0], -c[1] };
        }
        if (e instanceof BinaryOperation) {
            BinaryOperation bin = (BinaryOperation) e;
            double[] L = extractLinear(bin.getLeft()), R = extractLinear(bin.getRight());
            if ((L == null || R == null)) {
                if (bin.getOp() == BinaryOperation.Op.MUL) {
                    if (bin.getLeft() instanceof Constant) {
                        double k = ((Constant) bin.getLeft()).getValue();
                        double[] cr = extractLinear(bin.getRight());
                        return cr == null ? null : new double[] { k * cr[0], k * cr[1] };
                    }
                    if (bin.getRight() instanceof Constant) {
                        double k = ((Constant) bin.getRight()).getValue();
                        double[] cl = extractLinear(bin.getLeft());
                        return cl == null ? null : new double[] { k * cl[0], k * cl[1] };
                    }
                } else if (bin.getOp() == BinaryOperation.Op.DIV && bin.getRight() instanceof Constant) {
                    double k = ((Constant) bin.getRight()).getValue();
                    double[] cl = extractLinear(bin.getLeft());
                    return cl == null ? null : new double[] { cl[0] / k, cl[1] / k };
                }
                return null;
            }
            switch (bin.getOp()) {
                case ADD:
                    return new double[] { L[0] + R[0], L[1] + R[1] };
                case SUB:
                    return new double[] { L[0] - R[0], L[1] - R[1] };
                default:
                    return null;
            }
        }
        return null;
    }

    private boolean isEven(double n) {
        return Math.abs(n - Math.round(n)) < 1e-9 && (((long) Math.round(n)) % 2 == 0);
    }
}

class EquationParser {
    private enum TokenType {
        NUMBER, VARIABLE, PLUS, MINUS, MUL, DIV, POW, LPAREN, RPAREN, EQ, FUNC, END
    }

    private static class Token {
        TokenType type;
        String text;
        double value;
    }

    private static class Tokenizer {
        private final String input;
        private int pos;

        Tokenizer(String input) {
            this.input = input.replaceAll("\\s+", "");
        }

        Token next() {
            if (pos >= input.length())
                return make(TokenType.END, "");
            char c = input.charAt(pos);
            if (Character.isDigit(c) || c == '.') {
                int start = pos;
                while (pos < input.length() && (Character.isDigit(input.charAt(pos)) || input.charAt(pos) == '.'))
                    pos++;
                String num = input.substring(start, pos);
                Token t = make(TokenType.NUMBER, num);
                t.value = Double.parseDouble(num);
                return t;
            }
            if (c == 'x') {
                pos++;
                return make(TokenType.VARIABLE, "x");
            }
            if (c == '+') {
                pos++;
                return make(TokenType.PLUS, "+");
            }
            if (c == '-') {
                pos++;
                return make(TokenType.MINUS, "-");
            }
            if (c == '*') {
                pos++;
                return make(TokenType.MUL, "*");
            }
            if (c == '/') {
                pos++;
                return make(TokenType.DIV, "/");
            }
            if (c == '^') {
                pos++;
                return make(TokenType.POW, "^");
            }
            if (c == '(') {
                pos++;
                return make(TokenType.LPAREN, "(");
            }
            if (c == ')') {
                pos++;
                return make(TokenType.RPAREN, ")");
            }
            if (c == '=') {
                pos++;
                return make(TokenType.EQ, "=");
            }
            if (Character.isLetter(c)) {
                int start = pos;
                while (pos < input.length() && Character.isLetter(input.charAt(pos)))
                    pos++;
                String name = input.substring(start, pos);
                return make(TokenType.FUNC, name);
            }
            throw new RuntimeException("Unexpected char: " + c);
        }

        private Token make(TokenType type, String text) {
            Token t = new Token();
            t.type = type;
            t.text = text;
            return t;
        }
    }

    private Tokenizer tokenizer;
    private Token current;

    public Equation parse(String s) {
        tokenizer = new Tokenizer(s);
        current = tokenizer.next();
        Expression left = parseExpression();
        expect(TokenType.EQ);
        Expression right = parseExpression();
        expect(TokenType.END);
        return new Equation(left, right);
    }

    private void expect(TokenType type) {
        if (current.type != type)
            throw new RuntimeException("Expected " + type + ", got " + current.type);
        current = tokenizer.next();
    }

    private Expression parseExpression() {
        Expression expr = parseTerm();
        while (current.type == TokenType.PLUS || current.type == TokenType.MINUS) {
            TokenType op = current.type;
            current = tokenizer.next();
            Expression rhs = parseTerm();
            expr = new BinaryOperation(op == TokenType.PLUS ? BinaryOperation.Op.ADD : BinaryOperation.Op.SUB, expr,
                    rhs);
        }
        return expr;
    }

    private Expression parseTerm() {
        Expression expr = parseFactor();
        while (current.type == TokenType.MUL || current.type == TokenType.DIV) {
            TokenType op = current.type;
            current = tokenizer.next();
            Expression rhs = parseFactor();
            expr = new BinaryOperation(op == TokenType.MUL ? BinaryOperation.Op.MUL : BinaryOperation.Op.DIV, expr,
                    rhs);
        }
        return expr;
    }

    private Expression parseFactor() {
        Expression expr = parseUnary();
        if (current.type == TokenType.POW) {
            current = tokenizer.next();
            Expression exponent = parseUnary();
            expr = new BinaryOperation(BinaryOperation.Op.POW, expr, exponent);
        }
        return expr;
    }

    private Expression parseUnary() {
        if (current.type == TokenType.PLUS) {
            current = tokenizer.next();
            return parseUnary();
        }
        if (current.type == TokenType.MINUS) {
            current = tokenizer.next();
            return new UnaryOperation(UnaryOperation.Op.NEG, parseUnary());
        }
        return parsePrimary();
    }

    private Expression parsePrimary() {
        if (current.type == TokenType.NUMBER) {
            double v = current.value;
            current = tokenizer.next();
            return new Constant(v);
        }
        if (current.type == TokenType.VARIABLE) {
            current = tokenizer.next();
            return new Variable();
        }
        if (current.type == TokenType.FUNC) {
            String name = current.text;
            current = tokenizer.next();
            expect(TokenType.LPAREN);
            Expression arg = parseExpression();
            expect(TokenType.RPAREN);
            if ("sqrt".equals(name)) {
                return new BinaryOperation(BinaryOperation.Op.POW, arg, new Constant(0.5));
            }
            throw new RuntimeException("Unknown function: " + name);
        }
        if (current.type == TokenType.LPAREN) {
            current = tokenizer.next();
            Expression expr = parseExpression();
            expect(TokenType.RPAREN);
            return expr;
        }
        throw new RuntimeException("Unexpected token: " + current.type);
    }
}

public class EquationSolverApp {
    public static void main(String[] args) {
        List<String> tests = List.of(
                // "sqrt(x+3)=5",
                "2*x+3=7",
                "x^2=9",
                "(x-1)^3=8",
                "(x+1)/(x-2)=3",
                "(x+2)*(x-3)^2=0");
        EquationParser parser = new EquationParser();
        RecursiveEquationSolver solver = new RecursiveEquationSolver();
        for (String s : tests) {
            Equation eq = parser.parse(s);
            List<Double> roots = solver.solve(eq);
            System.out.println("Equation: " + eq + "  ->  Roots: " + roots);
        }
    }
}
